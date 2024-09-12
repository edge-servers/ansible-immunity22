from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

{% for import in immunity22_websocket_extra_imports %}
{{ import }}
{% endfor %}

routes = []

{% if immunity22_controller_urls %}
from openwisp_controller.routing import get_routes as get_controller_routes

routes.extend(get_controller_routes())
{% endif %}

{% if immunity22_network_topology %}
from openwisp_network_topology.routing import \
    websocket_urlpatterns as network_topology_routes

routes.extend(network_topology_routes)
{% endif %}

{% for extra_routes in immunity22_websocket_extra_routes %}
routes.extend({{ extra_routes }})
{% endfor %}

application = ProtocolTypeRouter(
    {
        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(routes))
        )
    }
)
