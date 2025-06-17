from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy
from users import views


auth_urls = [
    path(
        'auth/registration/',
        views.register, name='registration',
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dictionary.urls', namespace='dictionary')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
] + auth_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)