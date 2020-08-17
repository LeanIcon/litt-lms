"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from . import settings
from starter import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from starter.views import signup_view, activate, activation_sent_view, logout_view, home_view, EntSignup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', signup_view, name="signup"),
    # path('accounts/login/', signup_view, name="login"),
    path('accounts/company/', EntSignup, name="company"),
    path('accounts/sent/', activation_sent_view, name="activation_sent"),
    path('accounts/activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('accounts/logout', logout_view, name="logout"), 
    path('accounts/',include('registration.backends.default.urls')), 
    path('', views.home.as_view()), 
    path('home/', home_view, name='home'), 
    path('uploads/', include('adminUpload.urls')),
    path('', views.home.as_view(), name='home'), 
    path('', include('littapi.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
