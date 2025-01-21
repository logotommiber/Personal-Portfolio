from django.shortcuts import render


def index(request):
    return render(request, 'iPortfolio/index.html')


def details(request):
    return render(request, 'iPortfolio/portfolio-details.html')


def service(request):
    return render(request, 'iPortfolio/service-details.html')
