from django.shortcuts import render


def main(request):
    return render(request, "mainapp/index.html")


def social_inst(request):
    return render(request, "mainapp/social_inst.html")


def social_ok(request):
    return render(request, "mainapp/social_ok.html")

def social_vk(request):
    return render(request, "mainapp/social_vk.html")
