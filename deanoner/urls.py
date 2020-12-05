from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns =[
    path("admin/", admin.site.urls),
    path("", mainapp.main, name="main"),
    path("social_inst/", mainapp.social_inst, name="social_inst"),
    path("social_ok/", mainapp.social_ok, name="social_ok"),
    path("social_vk/", mainapp.social_vk, name="social_vk"),
    path("social_vk/result_vk/", mainapp.result_vk, name="result_vk"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)