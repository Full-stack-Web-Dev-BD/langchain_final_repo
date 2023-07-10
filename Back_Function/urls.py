"""Back_Function URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # define a route for home
    path('', views.home, name='home'),
    path('pdf_upload/', views.upload, name='index'),
    path('old/', views.oldUpload, name='old'),
    path('webhook/', views.webhook, name='webhook'),
    path('api/chatting/', views.chatting, name='chatting'),
    path('api/chatting_tuned/', views.chatting_tuned, name='chatting'),
    path('chatting_tuned/', views.chatting_tunedView, name='chatting'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)