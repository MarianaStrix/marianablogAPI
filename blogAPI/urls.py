from django.urls import path, include

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from accounts.urls import router as accounts_router


schema_view = get_schema_view(
    title='Example API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('swagger/', schema_view),
    path('', include('posts.urls')),
]
urlpatterns += accounts_router.urls


