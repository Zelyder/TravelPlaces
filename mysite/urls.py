"""mysite URL Configuration

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
from django.urls import include, re_path
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from ugc.views import index, about, events, page, login, directions_city, feedback, LikeDislike, Page, VotesView, PostLikeAPIToggle, PostLikeToggle
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('login/', login, name='login'),
    path('directions_city/', directions_city, name='directions_city'),
    path('feedback/', feedback, name='feedback'),
    re_path(r'^page/(?P<page_id>\d+)/like/$',PostLikeAPIToggle.as_view(),name='like'),
    
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('page/<int:page_id>/', page, name='page'),
    prefix_default_language=False
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)