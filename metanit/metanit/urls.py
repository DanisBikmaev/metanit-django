"""metanit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path, include
from hello import views

product_patterns = [
    #2
    path('', views.product),
    path('new', views.new),
    path('top', views.top),
    path('comment', views.comment),
    path('question', views.question),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/<int:id>', views.person),
    path('access/<int:age>', views.access),
    #3
    path('first_page/', views.first_page),
    path('second_page/', views.second_page),
    path('third_page/', views.third_page),
    
    #2
    path('', views.index, name='home'),
    path('product/<int:id>/', include(product_patterns)),
    
    #1
    re_path(r'^about', views.about, kwargs={'name':'Tom', 'age':23}, name='about'),
    re_path(r'^contact', views.contact, name='contact'),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', views.user),
    re_path(r'^user/(?P<name>\D+)', views.user),
    re_path(r'^user', views.user),
]
