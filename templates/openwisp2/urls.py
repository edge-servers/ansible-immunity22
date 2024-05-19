from django.urls import include, path, reverse_lazy
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
{% if immunity22_firmware_upgrader %}
# When using S3_REVERSE_PROXY feature of django-private-storage,
# the storage backend reverse the "serve_private_file" URL
# pattern in order to proxy the file with the correct URL.
from openwisp_firmware_upgrader.private_storage.urls import (
    urlpatterns as fw_private_storage_urls,
)
{% endif %}

redirect_view = RedirectView.as_view(url=reverse_lazy('admin:index'))

urlpatterns = [
    path('admin/', admin.site.urls),
{% if immunity22_controller_urls %}
    path('', include('openwisp_controller.urls')),
{% endif %}
    path('api/v1/', include('openwisp_utils.api.urls')),
    path('api/v1/', include('openwisp_users.api.urls')),
{% if immunity22_network_topology %}
    path('', include('openwisp_network_topology.urls')),
{% endif %}
{% if immunity22_firmware_upgrader %}
    path('', include('openwisp_firmware_upgrader.urls')),
    path(
        '',
        include((fw_private_storage_urls, 'firmware'), namespace='firmware'),
    ),
{% endif %}
{% if immunity22_monitoring %}
    path('', include('openwisp_monitoring.urls')),
{% endif %}
{% if immunity22_radius and immunity22_radius_urls %}
    path('', include('openwisp_radius.urls')),
{% endif %}
{% for extra_url in immunity22_extra_urls %}
    {{ extra_url }},
{% endfor %}
    path('', redirect_view, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
