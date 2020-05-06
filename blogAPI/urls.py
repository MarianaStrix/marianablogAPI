from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from accounts.urls import router as accounts_router
from blogAPI.settings.env import env

schema_view = get_schema_view(
    title='Example API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('auth_recaptcha.urls')),
    path('', include('posts.urls')),
]
urlpatterns += accounts_router.urls

if env('ENVIRONMENT') != 'production':
    urlpatterns += [
        path('swagger/', schema_view),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
