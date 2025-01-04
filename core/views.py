from django.shortcuts import render


def index(request):
    return render(request=request, template_name='core/index.html')


def commands(request):
    return render(request=request, template_name='core/commands.html')


def privacy(request):
    return render(request=request, template_name='core/privacy.html')


def terms(request):
    return render(request=request, template_name='core/terms.html')