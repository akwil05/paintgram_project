from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User
from django.conf.urls import url



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysite.urls')),
    # path('api/', include('api.urls')),

     #if 'company' если внутри скобой пропишем название класса, чтобы потом его функции через / добавлять
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
