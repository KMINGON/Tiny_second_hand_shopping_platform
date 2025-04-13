from django.shortcuts import render

def global_chat_view(request):
    return render(request, 'chat/global.html')

def private_chat_view(request, user_id):
    return render(request, 'chat/private.html', {'user_id': user_id})
