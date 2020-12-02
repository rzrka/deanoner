from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns =[
    path("admin/", admin.site.urls),
    path("", mainapp.main),
    path("social_inst/", mainapp.social_inst),
    path("social_ok/", mainapp.social_ok),
    path("social_vk/", mainapp.social_vk),
]
