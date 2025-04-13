from django.shortcuts import render

def report_create_view(request):
    return render(request, 'reports/create.html')
