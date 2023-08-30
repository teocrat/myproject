import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info("Index page accessed")
    return HttpResponse("Hello, world.")


def main(request):
    logger.info("Main page accessed")
    return render(request,'main.html')

def about(request):
    logger.info("About page accessed")
    return render(request, 'about_me.html')

