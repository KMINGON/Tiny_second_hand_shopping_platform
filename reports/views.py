from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from accounts.models import CustomUser
from .models import UserReport, ChatReport, ProductReport
from chat.models import Chat
from products.models import Product

@login_required
@require_POST
def report_user_view(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)

    if request.user == target_user:
        messages.error(request, "자기 자신은 신고할 수 없습니다.")
        return redirect('/')

    if UserReport.objects.filter(reporter=request.user, reported_user=target_user).exists():
        messages.warning(request, "이미 신고한 사용자입니다.")
    else:
        reason = request.POST.get('reason', '')
        UserReport.objects.create(reporter=request.user, reported_user=target_user, reason=reason)
        auto_block_user(target_user)  # ✅ 자동 제재 호출
        messages.success(request, "신고가 접수되었습니다.")

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def report_chat_view(request, message_id):
    message = get_object_or_404(Chat, id=message_id)
    report_type = request.POST.get('report_type')
    description = request.POST.get('description', '')

    # 중복 신고 방지
    if ChatReport.objects.filter(reporter=request.user, message=message).exists():
        messages.warning(request, '이미 신고한 메시지입니다.')
    else:
        ChatReport.objects.create(
            reporter=request.user,
            message=message,
            reason=f"[{report_type}] {description}"  # 신고 유형과 사유를 합쳐서 저장
        )
        auto_blind_message(message)  # ✅ 자동 블라인드 호출
        messages.success(request, '신고가 접수되었습니다.')

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def my_reports_view(request):
    user_reports = UserReport.objects.filter(reporter=request.user).order_by('-reported_at')
    chat_reports = ChatReport.objects.filter(reporter=request.user).order_by('-reported_at')
    product_reports = ProductReport.objects.filter(reporter=request.user).order_by('-reported_at')
    
    return render(request, 'reports/my_reports.html', {
        'user_reports': user_reports,
        'chat_reports': chat_reports,
        'product_reports': product_reports
    })

@login_required
@require_POST
def report_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    report_type = request.POST.get('report_type')
    description = request.POST.get('description', '')

    # 중복 신고 방지
    if ProductReport.objects.filter(reporter=request.user, reported_product=product).exists():
        messages.warning(request, '이미 신고한 상품입니다.')
    else:
        ProductReport.objects.create(
            reporter=request.user,
            reported_product=product,
            reason=f"[{report_type}] {description}"
        )
        auto_hide_product(product)  # ✅ 자동 숨김 호출
        messages.success(request, '신고가 접수되었습니다.')

    return redirect('products:product_detail', id=product.id)

# 사용자 제재
def auto_block_user(user, threshold=2):
    report_count = UserReport.objects.filter(reported_user=user).count()
    if report_count >= threshold and user.is_active:
        user.is_active = False
        user.save()

# 상품 숨김
def auto_hide_product(product, threshold=2):
    report_count = ProductReport.objects.filter(reported_product=product).count()
    if report_count >= threshold and not product.is_hidden:
        product.is_hidden = True
        product.save()

# 채팅 메시지 블라인드
def auto_blind_message(message, threshold=2):
    report_count = ChatReport.objects.filter(message=message).count()
    if report_count >= threshold and not message.is_hidden:
        message.is_hidden = True
        message.save()

