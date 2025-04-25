from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Chat
from accounts.models import CustomUser
from django.db.models import Q
from django.db import models
from reports.models import ChatReport
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden

def global_chat_view(request):
    return render(request, 'chat/global.html')



@login_required
def private_chat_view(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)

    # 비활성화된 사용자와의 채팅 불가
    if not target_user.is_active:
        return HttpResponseForbidden("비활성화된 사용자입니다.")

    if request.user == target_user:
        return redirect('/')  # 자기 자신과 채팅 방지

    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            Chat.objects.create(
                sender=request.user,
                receiver=target_user,
                message=message
            )
            return redirect('private_chat', user_id=target_user.id)

    # 숨김 처리되지 않은 채팅만 표시
    chats = Chat.objects.filter(
        (models.Q(sender=request.user, receiver=target_user) |
         models.Q(sender=target_user, receiver=request.user)),
        is_hidden=False
    ).order_by('created_at')

    context = {
        'target_user': target_user,
        'chats': chats,
        'user': request.user
    }

    return render(request, 'chat/private_chat.html', context)

@login_required
def chat_list_view(request):
    user = request.user
    # 숨김 처리되지 않은 채팅만 표시
    chats = Chat.objects.filter(
        (Q(sender=user) | Q(receiver=user)),
        is_hidden=False
    )

    # 활성화된 사용자의 채팅만 표시
    chat_partners = {}
    for chat in chats:
        partner = chat.sender if chat.sender != user else chat.receiver
        if partner and partner.is_active:  # 글로벌 채팅과 비활성화된 사용자 제외
            if partner.id not in chat_partners or chat.created_at > chat_partners[partner.id]['last_message_time']:
                chat_partners[partner.id] = {
                    'user': partner,
                    'last_message': chat.message,
                    'last_message_time': chat.created_at
                }

    # 최신 메시지 순으로 정렬
    sorted_partners = sorted(chat_partners.values(), 
                           key=lambda x: x['last_message_time'], 
                           reverse=True)

    context = {
        'chat_partners': sorted_partners,
        'user': user
    }

    return render(request, 'chat/chat_list.html', context)

@login_required
def global_chat_view(request):
    # 숨김 처리되지 않은 글로벌 채팅만 표시
    chats = Chat.objects.filter(
        receiver__isnull=True,
        is_hidden=False,
        sender__is_active=True  # 활성화된 사용자의 메시지만 표시
    ).order_by('created_at')
    
    return render(request, 'chat/global_chat.html', {
        'user_id': request.user.id,
        'chats': chats,
    })

@login_required
@require_POST
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
            reason=f"[{report_type}] {description}"
        )
        messages.success(request, '신고가 접수되었습니다.')

    return redirect(request.META.get('HTTP_REFERER', '/'))