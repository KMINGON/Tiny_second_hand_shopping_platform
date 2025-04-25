from django.shortcuts import render
from products.models import Product
from django.db.models import Count

# Create your views here.

def index_view(request):
    # 최근 등록된 상품들 (숨김 처리되지 않은 것만)
    recent_products = Product.objects.filter(
        is_hidden=False,
        user__is_active=True  # 활성화된 사용자의 상품만 표시
    ).order_by('-created_at')[:8]
    
    # 통계 정보
    stats = {
        'total_products': Product.objects.filter(
            is_hidden=False,
            user__is_active=True
        ).count(),
    }
    
    context = {
        'recent_products': recent_products,
        'stats': stats,
    }
    
    return render(request, 'core/index.html', context)
