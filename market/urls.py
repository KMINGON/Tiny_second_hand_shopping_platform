"""
URL configuration for market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),                   # 메인 홈 화면
    path('accounts/', include('accounts.urls')),      # 회원 기능
    path('products/', include('products.urls')),      # 상품 기능
    path('chat/', include('chat.urls', namespace='chat')),  # 채팅 기능
    path('reports/', include('reports.urls')),        # 신고 기능
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)