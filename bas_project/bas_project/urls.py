from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy


auth_urls = [
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('dictionary:home'),
        ),
        name='registration',
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dictionary.urls', namespace='dictionary')),
    path('auth/', include('django.contrib.auth.urls')),
] + auth_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
