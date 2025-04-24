from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from accounts.models import CustomUser
from .models import UserReport, ChatReport
from chat.models import Chat

@login_required
def report_user_view(request, user_id):
    reported_user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == 'POST':
        reason = request.POST.get('reason')
        if reason:
            # 중복 신고 방지
            if UserReport.objects.filter(reporter=request.user, reported_user=reported_user).exists():
                messages.warning(request, '이미 신고한 사용자입니다.')
            else:
                UserReport.objects.create(
                    reporter=request.user,
                    reported_user=reported_user,
                    reason=reason
                )
                messages.success(request, '신고가 접수되었습니다.')
            return redirect('profile', user_id=user_id)
    
    return render(request, 'reports/report_user.html', {
        'reported_user': reported_user
    })

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
        messages.success(request, '신고가 접수되었습니다.')

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def my_reports_view(request):
    user_reports = UserReport.objects.filter(reporter=request.user).order_by('-reported_at')
    chat_reports = ChatReport.objects.filter(reporter=request.user).order_by('-reported_at')
    
    return render(request, 'reports/my_reports.html', {
        'user_reports': user_reports,
        'chat_reports': chat_reports
    })
