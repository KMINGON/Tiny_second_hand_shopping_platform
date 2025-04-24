from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Chat
from accounts.models import CustomUser
from django.db.models import Q
from django.db import models

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
    latest_chats = {}
    for chat in chats.order_by('-created_at'):
        other = chat.receiver if chat.sender == user else chat.sender
        if other.id not in latest_chats:
            latest_chats[other.id] = {
                'user': other,
                'last_message': chat.message,
                'timestamp': chat.created_at
            }

    context = {
        'chat_partners': latest_chats.values()
    }
    return render(request, 'chat/chat_list.html', context)