from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Chat
from accounts.models import CustomUser
from django.db.models import Q
from django.db import models
from reports.models import ChatReport
from django.contrib import messages
from django.views.decorators.http import require_POST

def global_chat_view(request):
    return render(request, 'chat/global.html')



@login_required
def private_chat_view(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)

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

    # 이전 채팅 내역 불러오기
    chats = Chat.objects.filter(
        (models.Q(sender=request.user, receiver=target_user) |
         models.Q(sender=target_user, receiver=request.user))
    ).order_by('created_at')  # 시간순 정렬

    context = {
        'target_user': target_user,
        'chats': chats,
        'user': request.user  # 현재 사용자 정보도 전달
    }

    return render(request, 'chat/private_chat.html', context)

@login_required
def chat_list_view(request):
    user = request.user
    # 내가 주고받은 모든 채팅
    chats = Chat.objects.filter(Q(sender=user) | Q(receiver=user))

    # 상대방 ID 기준 마지막 메시지 시간 기준 정렬
    chat_partners = {}
    for chat in chats:
        partner = chat.sender if chat.sender != user else chat.receiver
        if partner:  # 글로벌 채팅의 경우 partner가 None일 수 있음
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
    chats = Chat.objects.filter(receiver__isnull=True).order_by('created_at')  # 전체 채팅만
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