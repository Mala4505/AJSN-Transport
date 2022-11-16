from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('login/', include('login.urls')),
    path('user/', include('user.urls')),
    path('administration/', include('administration.urls')),
    path('test/', TemplateView.as_view(template_name='index.html')),

    # path('administration/', include('administration.urls')),
]

urlpatterns += staticfiles_urlpatterns()