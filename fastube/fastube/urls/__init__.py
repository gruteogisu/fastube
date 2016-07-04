from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^', include("users.urls", namespace="users")),
    url(r'^posts/', include("posts.urls", namespace="posts")),

    url(r'^api/', include("fastube.urls.api", namespace="api")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
