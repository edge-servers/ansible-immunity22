import os
import sys
from celery.schedules import crontab
from datetime import timedelta

TESTING = 'test' in sys.argv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ immunity22_secret_key }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '{{ inventory_hostname }}',
{% for host in immunity22_allowed_hosts %}
    '{{ host }}',
{% endfor %}
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.gis',
    # all-auth
    'django.contrib.sites',
    # overrides allauth templates
    # must precede allauth
    'immunity_users.accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_extensions',
    # immunity22 modules
    'immunity_users',
    'immunity_controller.pki',
    'immunity_controller.config',
    'immunity_controller.geo',
    'immunity_controller.connection',
{% if immunity22_controller_subnet_division %}
    'immunity_controller.subnet_division',
{% endif %}
{% if immunity22_monitoring %}
    'immunity_monitoring.monitoring',
    'immunity_monitoring.device',
    'immunity_monitoring.check',
    'nested_admin',
{% endif %}
    'immunity_notifications',
    'flat_json_widget',
{% if immunity22_network_topology %}
    'immunity_network_topology',
{% endif %}
{% if immunity22_firmware_upgrader %}
    'immunity_firmware_upgrader',
{% endif %}
    'immunity_ipam',
{% if immunity22_radius %}
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'immunity_radius',
{% endif %}
    # immunity22 admin theme
    # (must be loaded here)
    'immunity_utils.admin_theme',
    {% if immunity22_usage_metric_collection is not false %}
    'immunity_utils.metric_collection',
    {% endif %}
    'admin_auto_filters',
    # admin
    'django.contrib.admin',
    'django.forms',
    # other dependencies
    'sortedm2m',
    'reversion',
    'leaflet',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework.authtoken',
    'django_filters',
{% if immunity22_firmware_upgrader or immunity22_radius %}
    'private_storage',
{% endif %}
    'drf_yasg',
    'channels',
    'pipeline',
    'import_export',
{% for app in immunity22_extra_django_apps %}
    '{{ app }}',
{% endfor %}
{% if immunity22_sentry.get('dsn') %}
    'raven.contrib.django.raven_compat',
{% endif %}
{% if immunity22_email_backend == "djcelery_email.backends.CeleryEmailBackend"%}
    'djcelery_email',
{% endif %}
]

EXTENDED_APPS = [
    'django_x509',
    'django_loci',
]

{% if immunity22_firmware_upgrader or immunity22_radius %}
PRIVATE_STORAGE_ROOT = os.path.join(BASE_DIR, 'private')
{% endif %}

{% if immunity22_firmware_upgrader %}
OPENWISP_FIRMWARE_UPGRADER_MAX_FILE_SIZE = {{ immunity22_firmware_upgrader_max_file_size }}
{% endif %}

AUTH_USER_MODEL = 'immunity_users.User'
SITE_ID = 1
LOGIN_REDIRECT_URL = 'admin:index'
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'email_confirmation_success'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'email_confirmation_success'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'immunity_utils.staticfiles.DependencyFinder',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    {% if immunity22_internationalization %}
    'django.middleware.locale.LocaleMiddleware',
    {% endif %}
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    {% if immunity22_radius %}
    'sesame.middleware.AuthenticationMiddleware',
    {% endif %}
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    {% if immunity22_users_user_password_expiration or immunity22_users_staff_user_password_expiration %}
    'immunity_users.middleware.PasswordExpirationMiddleware',
    {% endif %}
    'pipeline.middleware.MinifyHTMLMiddleware'
]

AUTHENTICATION_BACKENDS = [
    'immunity_users.backends.UsersAuthenticationBackend',
]

{% if immunity22_radius %}
OPENWISP_RADIUS_FREERADIUS_ALLOWED_HOSTS = {{ immunity22_radius_allowed_hosts }}
REST_AUTH = {
    'SESSION_LOGIN': False,
    'PASSWORD_RESET_SERIALIZER': 'immunity_radius.api.serializers.PasswordResetSerializer',
    'REGISTER_SERIALIZER': 'immunity_radius.api.serializers.RegisterSerializer',
}

# dj-rest-auth 3.0 changed the configuration settings.
# The below settings are kept for backward compatability with dj-rest-auth < 3.0
#
# Backward compatible settings begins
REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 'immunity_radius.api.serializers.PasswordResetSerializer',
}
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'immunity_radius.api.serializers.RegisterSerializer',
}
# Backward compatible settings ends

# SMS settings
OPENWISP_RADIUS_SMS_TOKEN_MAX_IP_DAILY = {{ immunity22_radius_sms_token_max_ip_daily }}
{% if immunity22_radius_unverify_inactive_users %}
OPENWISP_RADIUS_UNVERIFY_INACTIVE_USERS = {{ immunity22_radius_unverify_inactive_users }}
{% endif %}
{% if immunity22_radius_delete_inactive_users %}
OPENWISP_RADIUS_DELETE_INACTIVE_USERS = {{ immunity22_radius_delete_inactive_users }}
{% endif %}
SENDSMS_BACKEND = '{{ immunity22_radius_sms_backend }}'

# django-sesame configuration for magic sign-in links.
# Refer https://github.com/aaugustin/django-sesame#django-sesame.
AUTHENTICATION_BACKENDS += [
    'sesame.backends.ModelBackend',
]
SESAME_MAX_AGE = {{ immunity22_django_sesame_max_age }}
{% endif %}

ROOT_URLCONF = 'immunity22.urls'
OPENWISP_USERS_AUTH_API = {{ immunity22_users_auth_api }}
{% if immunity22_users_user_password_expiration %}
OPENWISP_USERS_USER_PASSWORD_EXPIRATION = {{ immunity22_users_user_password_expiration }}
{% endif %}
{% if immunity22_users_staff_user_password_expiration %}
OPENWISP_USERS_STAFF_USER_PASSWORD_EXPIRATION = {{ immunity22_users_staff_user_password_expiration }}
{% endif %}


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('{{ immunity22_redis_host }}', {{ immunity22_redis_port }})],
            'group_expiry': {{ immunity22_daphne_websocket_timeout }},
        },
    },
}
ASGI_APPLICATION = 'immunity22.routing.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    'immunity_utils.loaders.DependencyLoader'
                ]),
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'immunity_utils.admin_theme.context_processor.menu_items',
                'immunity_utils.admin_theme.context_processor.admin_theme_settings',
                'immunity_notifications.context_processors.notification_api_settings',
            ],
        },
    },
]

# Run celery in eager mode using in-memory broker while running tests
if not TESTING:
    CELERY_TASK_ACKS_LATE = {{ immunity22_celery_task_acks_late }}
    CELERY_BROKER_URL = '{{ immunity22_celery_broker_url }}'
else:
    CELERY_TASK_ALWAYS_EAGER = True
    CELERY_TASK_EAGER_PROPAGATES = True
    CELERY_BROKER_URL = 'memory://'

# Workaround for stalled migrate command
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'max_retries': {{ immunity22_celery_broker_max_tries }},
}

CELERY_BEAT_SCHEDULE = {
{% if immunity22_users_user_password_expiration or immunity22_users_staff_user_password_expiration %}
    'password_expiry_email': {
        'task': 'immunity_users.tasks.password_expiration_email',
        'schedule': crontab(**{ {{ cron_password_expiration_email }} }),
    },
{% endif %}
{% if immunity22_notifications_delete_old_notifications %}
    'delete_old_notifications': {
        'task': 'immunity_notifications.tasks.delete_old_notifications',
        'schedule': crontab(**{ {{ cron_delete_old_notifications }} }),
        'args': ({{ immunity22_notifications_delete_old_notifications }},),
    },
{% endif %}
{% if immunity22_monitoring and immunity22_monitoring_periodic_tasks %}
    'run_checks': {
        'task': 'immunity_monitoring.check.tasks.run_checks',
        'schedule': timedelta(minutes=5),
    },
{% endif %}
{% if immunity22_radius and immunity22_radius_periodic_tasks %}
    'deactivate_expired_users': {
        'task': 'immunity_radius.tasks.deactivate_expired_users',
        'schedule': crontab(**{ {{ cron_deactivate_expired_users }} }),
        'args': None,
        'relative': True,
    },
    'delete_old_radiusbatch_users': {
        'task': 'immunity_radius.tasks.delete_old_radiusbatch_users',
        'schedule': crontab(**{ {{ cron_delete_old_radiusbatch_users }} }),
        'args': [{{ immunity22_radius_delete_old_radiusbatch_users }}],
        'relative': True,
    },
    'cleanup_stale_radacct': {
        'task': 'immunity_radius.tasks.cleanup_stale_radacct',
        'schedule': crontab(**{ {{ cron_cleanup_stale_radacct }} }),
        'args': [{{ immunity22_radius_cleanup_stale_radacct }}],
        'relative': True,
    },
    'delete_old_postauth': {
        'task': 'immunity_radius.tasks.delete_old_postauth',
        'schedule': crontab(**{ {{ cron_delete_old_postauth }} }),
        'args': [{{ immunity22_radius_delete_old_postauth }}],
        'relative': True,
    },
    {% if immunity22_radius_delete_old_radacct %}
        'delete_old_radacct': {
            'task': 'immunity_radius.tasks.delete_old_radacct',
            'schedule': crontab(**{ {{ cron_delete_old_radacct }} }),
            'args': [{{ immunity22_radius_delete_old_radacct }}],
            'relative': True,
        },
    {% endif %}
    {% if immunity22_radius_unverify_inactive_users %}
        'unverify_inactive_users': {
            'task': 'immunity_radius.tasks.unverify_inactive_users',
            'schedule': crontab(**{ {{ cron_unverify_inactive_users }} }),
            'relative': True,
        },
    {% endif %}
    {% if immunity22_radius_delete_inactive_users %}
        'delete_inactive_users': {
            'task': 'immunity_radius.tasks.delete_inactive_users',
            'schedule': crontab(**{ {{ cron_delete_inactive_users }} }),
            'relative': True,
        },
    {% endif %}
{% endif %}
{% if immunity22_usage_metric_collection is not false and immunity22_usage_metric_collection_periodic_tasks %}
    'send_usage_metrics': {
        'task': 'immunity_utils.metric_collection.tasks.send_usage_metrics',
        'schedule': timedelta(days=1),
    },
{% endif %}
}

{% if immunity22_celery_task_routes_defaults %}
CELERY_TASK_ROUTES = {
{% if immunity22_celery_network %}
    # network operations, executed in the "network" queue
    'immunity_controller.connection.tasks.*': {'queue': 'network'},
{% endif %}
{% if immunity22_monitoring and immunity22_celery_monitoring %}
    # monitoring checks are executed in a dedicated "monitoring" queue
    'immunity_monitoring.check.tasks.perform_check': {'queue': 'monitoring'},
    'immunity_monitoring.monitoring.tasks.migrate_timeseries_database': {'queue': 'monitoring'},
{% endif %}
{% if immunity22_firmware_upgrader and immunity22_celery_firmware_upgrader %}
    # firmware upgrade operations, executed in the "firmware_upgrader" queue
    'immunity_firmware_upgrader.tasks.upgrade_firmware': {'queue': 'firmware_upgrader'},
    'immunity_firmware_upgrader.tasks.batch_upgrade_operation': {'queue': 'firmware_upgrader'},
{% endif %}
    # all other tasks are routed to the default queue (named "celery")
}
{% endif %}

# FOR DJANGO REDIS

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '{{ immunity22_redis_cache_url }}',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

WSGI_APPLICATION = 'immunity22.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': '{{ immunity22_database.engine }}',
        'NAME': '{{ immunity22_database.name }}',
{% if immunity22_database.user is defined and immunity22_database.user%}
        'USER': '{{ immunity22_database.user }}',
{% endif %}
{% if immunity22_database.password is defined and immunity22_database.password %}
        'PASSWORD': '{{ immunity22_database.password }}',
{% endif %}
{% if immunity22_database.host is defined and immunity22_database.host %}
        'HOST': '{{ immunity22_database.host }}',
{% endif %}
{% if immunity22_database.port is defined and immunity22_database.port %}
        'PORT': '{{ immunity22_database.port }}',
{% endif %}
{% if immunity22_database.options is defined and immunity22_database.options %}
        'OPTIONS': {{ immunity22_database.options|to_nice_json }}
{% endif %}
    }
}

{% if immunity22_spatialite_path %}
SPATIALITE_LIBRARY_PATH = '{{ immunity22_spatialite_path }}'
{% endif %}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    {'NAME': 'immunity_users.password_validation.PasswordReuseValidator'}
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = '{{ immunity22_language_code }}'
TIME_ZONE = '{{ immunity22_time_zone }}'
{% if immunity22_internationalization %}
USE_I18N = True
USE_L10N = True
{% endif %}
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_custom')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

{% if immunity22_context %}
NETJSONCONFIG_CONTEXT = {{ immunity22_context|to_nice_json }}
{% endif %}

# django x509 settings
DJANGO_X509_DEFAULT_CERT_VALIDITY = {{ immunity22_default_cert_validity }}
DJANGO_X509_DEFAULT_CA_VALIDITY = {{ immunity22_default_ca_validity }}

{% if immunity22_leaflet_config %}
LEAFLET_CONFIG = {{ immunity22_leaflet_config|to_nice_json }}
{% else %}
LEAFLET_CONFIG = {}
{% endif %}
# always disable RESET_VIEW button
LEAFLET_CONFIG['RESET_VIEW'] = False

# Set default email
DEFAULT_FROM_EMAIL = '{{ immunity22_default_from_email }}'
EMAIL_BACKEND = '{{ immunity22_email_backend }}'
EMAIL_TIMEOUT = {{ immunity22_email_timeout }}
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
        'verbose': {
            'format': '[%(levelname)s %(asctime)s] module: %(module)s, process: %(process)d, thread: %(thread)d\n%(message)s\n'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'main_log': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/immunity22.log'),
            'maxBytes': 15728640,
            'backupCount': 3,
            'formatter': 'verbose'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
{% if immunity22_sentry.get('dsn') %}
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'filters': ['require_debug_false']
        },
{% endif %}
    },
    'root': {
        'level': 'INFO',
        'handlers': [
            'main_log',
            'console',
            'mail_admins',
{% if immunity22_sentry.get('dsn') %}
            'sentry'
{% endif %}
        ]
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['main_log'],
            'propagate': False,
        }
    }
}

# HTML minification with django pipeline
PIPELINE = {'PIPELINE_ENABLED': True}
# static files minification and invalidation with django-compress-staticfiles
STATICFILES_STORAGE = 'immunity_utils.storage.CompressStaticFilesStorage'
# GZIP compression is handled by nginx
BROTLI_STATIC_COMPRESSION = False
GZIP_STATIC_COMPRESSION = False

{% if immunity22_sentry.get('dsn') %}
RAVEN_CONFIG = {{ immunity22_sentry|to_nice_json }}
{% endif %}

{% if immunity22_monitoring %}
TIMESERIES_DATABASE = {
    'BACKEND': '{{ immunity22_timeseries_database.backend }}',
    'USER': '{{ immunity22_timeseries_database.user }}',
    'PASSWORD': '{{ immunity22_timeseries_database.password }}',
    'NAME': '{{ immunity22_timeseries_database.name }}',
    'HOST': '{{ immunity22_timeseries_database.host }}',
    'PORT': '{{ immunity22_timeseries_database.port }}',
}
OPENWISP_MONITORING_DEFAULT_RETENTION_POLICY = '{{ immunity22_monitoring_default_retention_policy }}'
{% endif %}

{% for setting, value in immunity22_extra_django_settings.items() %}
{{ setting }} = {% if value is string %}'{{ value }}'{% else %}{{ value }}{% endif %}

{% endfor %}

{% for instruction in immunity22_extra_django_settings_instructions %}
{{ instruction }}

{% endfor %}

{% if immunity22_django_cors.enabled %}
# CORS configuration
INSTALLED_APPS.append('corsheaders')
MIDDLEWARE.insert(MIDDLEWARE.index('django.middleware.common.CommonMiddleware'), 'corsheaders.middleware.CorsMiddleware')
{% if immunity22_django_cors.get('replace_https_referer', False) %}
MIDDLEWARE.insert(MIDDLEWARE.index('django.middleware.csrf.CsrfViewMiddleware') + 1, 'corsheaders.middleware.CorsPostCsrfMiddleware')
CORS_REPLACE_HTTPS_REFERER = {{ immunity22_django_cors.get('replace_https_referer', False) }}
{% endif %}
CORS_ALLOWED_ORIGINS = {{ immunity22_django_cors.get('allowed_origins_list', []) }}
{% endif %}

TEST_RUNNER = 'immunity_utils.metric_collection.tests.runner.MockRequestPostRunner'
