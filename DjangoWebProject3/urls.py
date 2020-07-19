"""
Definition of urls for DjangoWebProject3.
"""


from django.urls import path,include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('',include('app.urls')),
    ]
