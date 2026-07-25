"""
URL configuration for config project.

The `urlpatterns` list routes URLs to accounts_views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function accounts_views
    1. Add an import:  from my_app import accounts_views
    2. Add a URL to urlpatterns:  path('', accounts_views.home, name='home')
Class-based accounts_views
    1. Add an import:  from other_app.accounts_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('coins/', include('coins.urls')),
    path('attendance/', include('attendance.urls')),
    path('news/', include('news.urls')),
    path('normativ/', include('normativ.urls')),
    path('schedule/', include('schedule.urls')),
]
