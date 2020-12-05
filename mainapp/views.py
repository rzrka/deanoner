from django.shortcuts import render
from django.conf import settings

from .models import  Vk_Category
def main(request):
    title = "главная"
    blocks = [
        {
            'name': 'Search in social network Vkontakte',
            'discription' : 'More information',
            'button_name' : 'Перейти',
            'url':'/social_vk/',
        },
        {
            'name': 'Search in social network Instagramm',
            'discription' : 'More information',
            'button_name' : 'Перейти',
            'url':'/social_inst/',
        },
        {
            'name': 'Search in social network Odnoklassniki',
            'discription' : 'More information',
            'button_name' : 'Перейти',
            'url':'/social_ok/',
        },
    ]
    content = {"title": title, "blocks": blocks}
    return render(request, "mainapp/index.html", content)


def social_inst(request):
    return render(request, "mainapp/social_inst.html")


def social_ok(request):
    return render(request, "mainapp/social_ok.html")

def social_vk(request):
    return render(request, "mainapp/social_vk.html")

def result_vk(request):
    title = "главная"

    users = Vk_Category.objects.all()

    content = {"title":title, 'users':users, 'media_url': settings.MEDIA_URL}
    return render(request, "mainapp/result_vk.html", content)