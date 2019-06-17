from django.urls import path, include
from django.contrib import admin

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from accounts.urls import router as accounts_router


schema_view = get_schema_view(
    title='Example API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('auth_recaptcha.urls')),
    path('swagger/', schema_view),
    path('', include('posts.urls')),
]
urlpatterns += accounts_router.urls

#
# from django.conf.urls import include, url
# from django.contrib import admin
# from django.views.generic import TemplateView, RedirectView
#
# from rest_framework_swagger.views import get_swagger_view
#
# urlpatterns = [
#     url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
#     url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
#         name='signup'),
#     url(r'^email-verification/$',
#         TemplateView.as_view(template_name="email_verification.html"),
#         name='email-verification'),
#     url(r'^login/$', TemplateView.as_view(template_name="login.html"),
#         name='login'),
#     url(r'^logout/$', TemplateView.as_view(template_name="logout.html"),
#         name='logout'),
#     url(r'^password-reset/$',
#         TemplateView.as_view(template_name="password_reset.html"),
#         name='password-reset'),
#     url(r'^password-reset/confirm/$',
#         TemplateView.as_view(template_name="password_reset_confirm.html"),
#         name='password-reset-confirm'),
#
#     url(r'^user-details/$',
#         TemplateView.as_view(template_name="user_details.html"),
#         name='user-details'),
#     url(r'^password-change/$',
#         TemplateView.as_view(template_name="password_change.html"),
#         name='password-change'),
#
#
#     # this url is used to generate email content
#     url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#         TemplateView.as_view(template_name="password_reset_confirm.html"),
#         name='password_reset_confirm'),
#
#     url(r'^rest-auth/', include('rest_auth.urls')),
#     url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
#     url(r'^account/', include('allauth.urls')),
#     url(r'^admin/', admin.site.urls),
#     url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
#     url(r'^docs/$', get_swagger_view(title='API Docs'), name='api_docs'),
#
# ]
#
