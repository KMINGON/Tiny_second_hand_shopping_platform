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

    chats = Chat.objects.filter(
        (models.Q(sender=request.user, receiver=target_user) |
         models.Q(sender=target_user, receiver=request.user))
    )

    return render(request, 'chat/private_chat.html', {
        'target_user': target_user,
        'chats': chats
    })

