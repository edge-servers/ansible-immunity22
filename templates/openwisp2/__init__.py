from .celery import app as celery_app

__all__ = ['celery_app']
__openwisp_version__ = '24.0.0a'
__openwisp_installation_method__ = (
    '{{ immunity22_installation_method | default("ansible-immunity22") }}'
)
