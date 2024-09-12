Role Variables
==============

This role has many variables values that can be changed to best suit your
needs.

Below are listed all the variables you can customize (you may also want to
take a look at `the default values of these variables
<https://github.com/openwisp/ansible-immunity22/blob/master/defaults/main.yml>`__).

.. code-block:: yaml

    - hosts: yourhost
      roles:
      # you can add other roles here
        - openwisp.immunity22
      vars:
        # Enable the modules you want to use
        immunity22_network_topology: false
        immunity22_firmware_upgrader: false
        immunity22_monitoring: true
        # you may replace the values of these variables with any value or URL
        # supported by pip (the python package installer)
        # use these to install forks, branches or development versions
        # WARNING: only do this if you know what you are doing; disruption
        # of service is very likely to occur if these variables are changed
        # without careful analysis and testing
        immunity22_controller_version: "openwisp-controller~=1.0.0"
        immunity22_network_topology_version: "openwisp-network-topology~=1.0.0"
        immunity22_firmware_upgrader_version: "openwisp-firmware-upgrader~=1.0.0"
        immunity22_monitoring_version: "openwisp-monitoring~=1.0.0"
        immunity22_radius_version: "openwisp-radius~=1.0.0"
        immunity22_django_version: "django~=3.2.13"
        # Setting this to true will enable subnet division feature of
        # openwisp-controller. Refer openwisp-controller documentation
        # for more information. https://github.com/openwisp/openwisp-controller#subnet-division-app
        # By default, it is set to false.
        immunity22_controller_subnet_division: true
        # when immunity22_radius_urls is set to false, the radius module
        # is setup but it's urls are not added, which means API and social
        # views cannot be used, this is helpful if you have an external
        # radius instance.
        immunity22_radius_urls: "{{ immunity22_radius }}"
        immunity22_path: /opt/immunity22
        # It is recommended that you change the value of this variable if you intend to use
        # OpenWISP2 in production, as a misconfiguration may result in emails not being sent
        immunity22_default_from_email: "immunity22@yourhostname.com"
        # Email backend used by Django for sending emails. By default, the role
        # uses "CeleryEmailBackend" from django-celery-email.
        # (https://github.com/pmclanahan/django-celery-email)
        immunity22_email_backend: "djcelery_email.backends.CeleryEmailBackend"
        # Email timeout in seconds used by Django for blocking operations
        # like connection attempts. For more info read the Django documentation,
        # https://docs.djangoproject.com/en/4.2/ref/settings/#email-timeout.
        # Defaults to 10 seconds.
        immunity22_email_timeout: 5
        # edit database settings only if you are not using sqlite
        # eg, for deploying with PostgreSQL (recommended for production usage)
        # you will need the PostGIS spatial extension, find more info at:
        # https://docs.djangoproject.com/en/4.1/ref/contrib/gis/tutorial/
        immunity22_database:
            engine: django.contrib.gis.db.backends.postgis
            name: "{{ DB_NAME }}"
            user: "{{ DB_USER }}"
            host: "{{ DB_HOST }}"
            password: "{{ DB_PASSWORD }}"
            port: 5432
        # SPATIALITE_LIBRARY_PATH django setting
        # The role will attempt determining the right mod-spatialite path automatically
        # But you can use this variable to customize the path or fix future arising issues
        immunity22_spatialite_path: "mod_spatialite.so"
        # customize other django settings:
        immunity22_language_code: en-gb
        immunity22_time_zone: UTC
        # openwisp-controller context
        immunity22_context: {}
        # additional allowed hosts
        immunity22_allowed_hosts:
            - myadditionalhost.openwisp.org
        # geographic map settings
        immunity22_leaflet_config:
            DEFAULT_CENTER: [42.06775, 12.62011]
            DEFAULT_ZOOM: 6
        # enable/disable geocoding check
        immunity22_geocoding_check: true
        # specify path to a valid SSL certificate and key
        # (a self-signed SSL cert will be generated if omitted)
        immunity22_ssl_cert: "/etc/nginx/ssl/server.crt"
        immunity22_ssl_key: "/etc/nginx/ssl/server.key"
        # customize the self-signed SSL certificate info if needed
        immunity22_ssl_country: "US"
        immunity22_ssl_state: "California"
        immunity22_ssl_locality: "San Francisco"
        immunity22_ssl_organization: "IT dep."
        # the following setting controls which ip address range
        # is allowed to access the controller via unencrypted HTTP
        # (this feature is disabled by default)
        immunity22_http_allowed_ip: "10.8.0.0/16"
        # additional python packages that will be installed with pip
        immunity22_extra_python_packages:
            - bpython
            - django-owm-legacy
        # additional django apps that will be added to settings.INSTALLED_APPS
        # (if the app needs to be installed, the name its python package
        # must be also added to the immunity22_extra_python_packages var)
        immunity22_extra_django_apps:
            - owm_legacy
        # additional django settings example
        immunity22_extra_django_settings:
            CSRF_COOKIE_AGE: 2620800.0
        # in case you need to add python instructions to the django settings file
        immunity22_extra_django_settings_instructions:
            - TEMPLATES[0]['OPTIONS']['loaders'].insert(0, 'apptemplates.Loader')
        # extra URL settings for django
        immunity22_extra_urls:
          - "path(r'', include('my_custom_app.urls'))"
        # allows to specify imports that are used in the websocket routes, e.g.:
        immunity22_websocket_extra_imports:
          - from my_custom_app.websockets.routing import get_routes as get_custom_app_routes
        # allows to specify extra websocket routes, e.g.:
        immunity22_websocket_extra_routes:
          # Callable that returns a list of routes
          - get_custom_app_routes()
          # List of routes
          - "[path('ws/custom-app/', consumer.CustomAppConsumer.as_asgi())]"
        # controller URL are enabled by default
        # but can be disabled in multi-VM installations if needed
        immunity22_controller_urls: true
        # The default retention policy that applies to the timeseries data
        # https://github.com/openwisp/openwisp-monitoring#openwisp-monitoring-default-retention-policy
        immunity22_monitoring_default_retention_policy: "26280h0m0s" # 3 years
        # whether NGINX should be installed
        immunity22_nginx_install: true
        # spdy protocol support (disabled by default)
        immunity22_nginx_spdy: false
        # HTTP2 protocol support (disabled by default)
        immunity22_nginx_http2: false
        # ipv6 must be enabled explicitly to avoid errors
        immunity22_nginx_ipv6: false
        # nginx client_max_body_size setting
        immunity22_nginx_client_max_body_size: 10M
        # list of upstream servers for OpenWISP
        immunity22_nginx_openwisp_server:
          - "localhost:8000"
        # dictionary containing more nginx settings for
        # the 443 section of the immunity22 nginx configuration
        # IMPORTANT: 1. you can add more nginx settings in this dictionary
        #            2. here we list the default values used
        immunity22_nginx_ssl_config:
            gzip: "on"
            gzip_comp_level: "6"
            gzip_proxied: "any"
            gzip_min_length: "1000"
            gzip_types:
                - "text/plain"
                - "text/html"
                - "image/svg+xml"
                - "application/json"
                - "application/javascript"
                - "text/xml"
                - "text/css"
                - "application/xml"
                - "application/x-font-ttf"
                - "font/opentype"
        # nginx error log configuration
        immunity22_nginx_access_log: "{{ immunity22_path }}/log/nginx.access.log"
        immunity22_nginx_error_log: "{{ immunity22_path }}/log/nginx.error.log error"
        # nginx Content Security Policy header, customize if needed
        immunity22_nginx_csp: >
          CUSTOM_NGINX_SECURITY_POLICY
        # uwsgi gid, omitted by default
        immunity22_uwsgi_gid: null
        # number of uWSGI process to spawn. Default value is 1.
        immunity22_uwsgi_processes: 1
        # number of threads each uWSGI process will have. Default value is 1.
        immunity22_uwsgi_threads: 2
        # value of the listen queue of uWSGI
        immunity22_uwsgi_listen: 100
        # socket on which uwsgi should listen. Defaults to UNIX socket
        # at "{{ immunity22_path }}/uwsgi.sock"
        immunity22_uwsgi_socket: 127.0.0.1:8000
        # extra uwsgi configuration parameters that cannot be
        # configured using dedicated ansible variables
        immunity22_uwsgi_extra_conf: |
          single-interpreter=True
          log-4xx=True
          log-5xx=True
          disable-logging=True
          auto-procname=True
        # whether daphne should be installed
        # must be enabled for serving websocket requests
        immunity22_daphne_install: true
        # number of daphne process to spawn. Default value is 1
        immunity22_daphne_processes: 2
        # maximum time to allow a websocket to be connected (in seconds)
        immunity22_daphne_websocket_timeout: 1800
        # the following setting controls which ip address range
        # is allowed to access the immunity22 admin web interface
        # (by default any IP is allowed)
        immunity22_admin_allowed_network: null
        # install ntp client (enabled by default)
        immunity22_install_ntp: true
        # if you have any custom supervisor service, you can
        # configure it to restart along with other supervisor services
        immunity22_extra_supervisor_restart:
            - name: my_custom_service
              when: my_custom_service_enabled
        # Disable usage metric collection. It is enabled by default.
        # Read more about it at
        # https://openwisp.io/docs/user/usage-metric-collection.html
        immunity22_usage_metric_collection: false
        # enable sentry example
        immunity22_sentry:
            dsn: "https://7d2e3cd61acc32eca1fb2a390f7b55e1:bf82aab5ddn4422688e34a486c7426e3@getsentry.com:443/12345"
        immunity22_default_cert_validity: 1825
        immunity22_default_ca_validity: 3650
        # the following options for redis allow to configure an external redis instance if needed
        immunity22_redis_install: true
        immunity22_redis_host: localhost
        immunity22_redis_port: 6379
        immunity22_redis_cache_url: "redis://{{ immunity22_redis_host }}:{{ immunity22_redis_port }}/1"
        # the following options are required to configure influxdb which is used in openwisp-monitoring
        immunity22_influxdb_install: true
        immunity22_timeseries_database:
            backend: "openwisp_monitoring.db.backends.influxdb"
            user: "openwisp"
            password: "openwisp"
            name: "immunity22"
            host: "localhost"
            port: 8086
        # celery concurrency for the default queue, by default the number of CPUs is used
        # celery concurrency for the default queue, by default it is set to 1
        # Setting it to "null" will make concurrency equal to number of CPUs if autoscaling is not used
        immunity22_celery_concurrency: null
        # alternative to the previous option, the celery autoscale option can be set if needed
        # for more info, consult the documentation of celery regarding "autoscaling"
        # by default it is set to "null" (no autoscaling)
        immunity22_celery_autoscale: 4,1
        # prefetch multiplier for the default queue,
        # the default value is calculated automatically by celery
        immunity22_celery_prefetch_multiplier: null
        # celery queuing mode for the default queue,
        # leaving the default will work for most cases
        immunity22_celery_optimization: default
        # whether the dedicated celerybeat worker is enabled which is
        # responsible for triggering periodic tasks
        # must be turned on unless there's another server running celerybeat
        immunity22_celerybeat: true
        # whether the dedicated worker for the celery "network" queue is enabled
        # must be turned on unless there's another server running a worker for this queue
        immunity22_celery_network: true
        # concurrency option for the "network" queue (a worker is dedicated solely to network operations)
        # the default is 1. Setting it to "null" will make concurrency equal to number of CPUs if autoscaling is not used.
        immunity22_celery_network_concurrency: null
        # alternative to the previous option, the celery autoscale option can be set if needed
        # for more info, consult the documentation of celery regarding "autoscaling"
        # by default it is set to "null" (no autoscaling)
        immunity22_celery_network_autoscale: 8,4
        # prefetch multiplier for the "network" queue,
        # the default is 1, which mean no prefetching,
        # because the network tasks are long running and is better
        # to distribute the tasks to multiple processes
        immunity22_celery_network_prefetch_multiplier: 1
        # celery queuing mode for the "network" queue,
        # fair mode is used in this case, which means
        # tasks will be equally distributed among workers
        immunity22_celery_network_optimization: fair
        # whether the dedicated worker for the celery "firmware_upgrader" queue is enabled
        # must be turned on unless there's another server running a worker for this queue
        immunity22_celery_firmware_upgrader: true
        # concurrency option for the "firmware_upgrader" queue (a worker is dedicated solely to firmware upgrade operations)
        # the default is 1. Setting it to "null" will make concurrency equal to number of CPUs if autoscaling is not used
        immunity22_celery_firmware_upgrader_concurrency: null
        # alternative to the previous option, the celery autoscale option can be set if needed
        # for more info, consult the documentation of celery regarding "autoscaling"
        # by default it is set to "null" (no autoscaling)
        immunity22_celery_firmware_upgrader_autoscale: 8,4
        # prefetch multiplier for the "firmware_upgrader" queue,
        # the default is 1, which mean no prefetching,
        # because the firmware upgrade tasks are long running and is better
        # to distribute the tasks to multiple processes
        immunity22_celery_firmware_upgrader_prefetch_multiplier: 1
        # celery queuing mode for the "firmware_upgrader" queue,
        # fair mode is used in this case, which means
        # tasks will be equally distributed among workers
        immunity22_celery_firmware_upgrader_optimization: fair
        # whether the dedicated worker for the celery "monitoring" queue is enabled
        # must be turned on unless there's another server running a worker for this queue
        immunity22_celery_monitoring: true
        # concurrency option for the "monitoring" queue (a worker is dedicated solely to monitoring operations)
        # the default is 2. Setting it to "null" will make concurrency equal to number of CPUs
        # if autoscaling is not used.
        immunity22_celery_monitoring_concurrency: null
        # alternative to the previous option, the celery autoscale option can be set if needed
        # for more info, consult the documentation of celery regarding "autoscaling"
        # by default it is set to "null" (no autoscaling)
        immunity22_celery_monitoring_autoscale: 4,8
        # prefetch multiplier for the "monitoring" queue,
        # the default is 1, which mean no prefetching,
        # because the monitoring tasks can be long running and is better
        # to distribute the tasks to multiple processes
        immunity22_celery_monitoring_prefetch_multiplier: 1
        # celery queuing mode for the "monitoring" queue,
        # fair mode is used in this case, which means
        # tasks will be equally distributed among workers
        immunity22_celery_monitoring_optimization: fair
        # whether the default celery task routes should be written to the settings.py file
        # turn this off if you're defining custom task routing rules
        immunity22_celery_task_routes_defaults: true
        # celery settings
        immunity22_celery_broker_url: redis://{{ immunity22_redis_host }}:{{ immunity22_redis_port }}/3
        immunity22_celery_task_acks_late: true
        # maximum number of retries by celery before giving up when broker is unreachable
        immunity22_celery_broker_max_tries: 10
        # whether to activate the django logging configuration in celery
        # if set to true, will log all the celery events in the same log stream used by django
        # which will cause log lines to be written to "{{ immunity22_path }}/log/immunity22.log"
        # instead of "{{ immunity22_path }}/log/celery.log" and "{{ immunity22_path }}/log/celerybeat.log"
        immunity22_django_celery_logging: false
        # postfix is installed by default, set to false if you don't need it
        immunity22_postfix_install: true
        # allow overriding default `postfix_smtp_sasl_auth_enable` variable
        postfix_smtp_sasl_auth_enable_override: true
        # allow overriding postfix_smtpd_relay_restrictions
        postfix_smtpd_relay_restrictions_override: permit_mynetworks
        # allows overriding the default duration for keeping notifications
        immunity22_notifications_delete_old_notifications: 10
        # Expiration time limit (in seconds) of magic sign-in links.
        # Magic sign-in links are used only when OpenWISP RADIUS is enabled.
        immunity22_django_sesame_max_age: 1800 # 30 minutes
        # Maximum file size(in bytes) allowed to be uploaded as firmware image.
        # It overrides "immunity22_nginx_client_max_body_size" setting
        # and updates nginx configuration accordingly.
        immunity22_firmware_upgrader_max_file_size: 41943040 # 40MB
        # to add multi-language support
        immunity22_internationalization: true
        immunity22_users_auth_api: true
        # Allows setting OPENWISP_USERS_USER_PASSWORD_EXPIRATION setting.
        # Read https://github.com/openwisp/openwisp-users#openwisp_users_user_password_expiration
        immunity22_users_user_password_expiration: 30
          # Allows setting OPENWISP_USERS_STAFF_USER_PASSWORD_EXPIRATION setting.
        # Read https://github.com/openwisp/openwisp-users#openwisp_users_staff_user_password_expiration
        immunity22_users_staff_user_password_expiration: 30
        # used for SMS verification, the default is a dummy SMS backend
        # which prints to standard output and hence does nothing
        # one of the available providers from django-sendsms can be
        # used or alternatively, you can write a backend class for your
        # favorite SMS API gateway
        immunity22_radius_sms_backend: "sendsms.backends.console.SmsBackend"
        immunity22_radius_sms_token_max_ip_daily: 25
        immunity22_radius_delete_old_radiusbatch_users: 365
        immunity22_radius_cleanup_stale_radacct: 1
        immunity22_radius_delete_old_postauth: 365
        # days for which the radius accounting sessions (radacct) are retained,
        # 0 means sessions are kept forever.
        # we highly suggest to set this number according
        # to the privacy regulation of your jurisdiction
        immunity22_radius_delete_old_radacct: 365
        # days after which inactive users will flagged as unverified
        # Read https://openwisp.io/docs/dev/radius/user/settings.html#openwisp-radius-unverify-inactive-users
        immunity22_radius_unverify_inactive_users: 540
        # days after which inactive users will be deleted
        # Read Read https://openwisp.io/docs/dev/radius/user/settings.html#openwisp-radius-delete-inactive-users
        immunity22_radius_delete_inactive_users: 540
        immunity22_radius_allowed_hosts: ["127.0.0.1"]
        # allow disabling celery beat tasks if needed
        immunity22_monitoring_periodic_tasks: true
        immunity22_radius_periodic_tasks: true
        immunity22_usage_metric_collection_periodic_tasks: true
        # this role provides a default configuration of freeradius
        # if you manage freeradius on a different machine or you need different configurations
        # you can disable this default behavior
        immunity22_freeradius_install: true
        # Set an account to expire T seconds after first login.
        # This variable sets the value of T.
        freeradius_expire_attr_after_seconds: 86400
        freeradius_dir: /etc/freeradius/3.0
        freeradius_mods_available_dir: "{{ freeradius_dir }}/mods-available"
        freeradius_mods_enabled_dir: "{{ freeradius_dir }}/mods-enabled"
        freeradius_sites_available_dir: "{{ freeradius_dir }}/sites-available"
        freeradius_sites_enabled_dir: "{{ freeradius_dir }}/sites-enabled"
        freeradius_rest:
            url: "https://{{ inventory_hostname }}/api/v1/freeradius"
        freeradius_safe_characters: "+@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_: /"
        # Sets the source path of the template that contains freeradius site configuration.
        # Defaults to "templates/freeradius/openwisp_site.j2" shipped in the role.
        freeradius_openwisp_site_template_src: custom_freeradius_site.j2
        # Whether to deploy the default openwisp_site for FreeRADIUS.
        # Defaults to true.
        freeradius_deploy_openwisp_site: false
        # FreeRADIUS listen address for the openwisp_site.
        # Defaults to "*", i.e. listen on all interfaces.
        freeradius_openwisp_site_listen_ipaddr: "10.8.0.1"
        # A list of dict that includes organization's name, UUID, RADIUS token,
        # TLS configuration, and ports for authentication, accounting, and inner tunnel.
        # This list of dict is used to generate FreeRADIUS sites that support
        # WPA Enterprise (EAP-TTLS-PAP) authentication.
        # Defaults to an empty list.
        freeradius_eap_orgs:
            # The name should not contain spaces or special characters
          - name: openwisp
            # UUID of the organization can be retrieved from the OpenWISP admin
            uuid: 00000000-0000-0000-0000-000000000000
            # Radius token of the organization can be retrieved from the OpenWISP admin
            radius_token: secret-radius-token
            # Port used by the authentication service for this FreeRADIUS site
            auth_port: 1832
            # Port used by the accounting service for this FreeRADIUS site
            acct_port: 1833
            # Port used by the authentication service of inner tunnel for this FreeRADIUS site
            inner_tunnel_auth_port: 18330
            # CA certificate for the FreeRADIUS site
            ca: /etc/freeradius/certs/ca.crt
            # TLS certificate for the FreeRADIUS site
            cert: /etc/freeradius/certs/cert.pem
            # TLS private key for the FreeRADIUS site
            private_key: /etc/freeradius/certs/key.pem
            # Diffie-Hellman key for the FreeRADIUS site
            dh: /etc/freeradius/certs/dh
            # Extra instructions for the "tls-config" section of the EAP module
            # for the FreeRADIUS site
            tls_config_extra: |
              private_key_password = whatever
              ecdh_curve = "prime256v1"
        # Sets the source path of the template that contains freeradius site configuration
        # for WPA Enterprise (EAP-TTLS-PAP) authentication.
        # Defaults to "templates/freeradius/eap/openwisp_site.j2" shipped in the role.
        freeradius_eap_openwisp_site_template_src: custom_eap_openwisp_site.j2
        # Sets the source path of the template that contains freeradius inner tunnel
        # configuration for WPA Enterprise (EAP-TTLS-PAP) authentication.
        # Defaults to "templates/freeradius/eap/inner_tunnel.j2" shipped in the role.
        freeradius_eap_inner_tunnel_template_src: custom_eap_inner_tunnel.j2
        # Sets the source path of the template that contains freeradius EAP configuration
        # for WPA Enterprise (EAP-TTLS-PAP) authentication.
        # Defaults to "templates/freeradius/eap/eap.j2" shipped in the role.
        freeradius_eap_template_src: custom_eap.j2
        cron_delete_old_notifications: "'hour': 0, 'minute': 0"
        cron_deactivate_expired_users: "'hour': 0, 'minute': 5"
        cron_delete_old_radiusbatch_users: "'hour': 0, 'minute': 10"
        cron_cleanup_stale_radacct: "'hour': 0, 'minute': 20"
        cron_delete_old_postauth: "'hour': 0, 'minute': 30"
        cron_delete_old_radacct: "'hour': 1, 'minute': 30"
        cron_password_expiration_email: "'hour': 1, 'minute': 0"
        cron_unverify_inactive_users: "'hour': 1, 'minute': 45"
        cron_delete_inactive_users: "'hour': 1, 'minute': 55"
        # cross-origin resource sharing (CORS) settings
        # https://pypi.org/project/django-cors-headers/
        immunity22_django_cors:
          # Setting this to "true" will install the django-cors-headers package
          # and configure the Django middleware setting to support CORS.
          # By default, it is set to false.
          enabled: true
          # Configures "CORS_ALLOWED_ORIGINS" setting of the django-cors-headers
          # package. A list of origins that are authorized to make cross-site
          # HTTP requests. Read https://github.com/adamchainz/django-cors-headers#cors_allowed_origins-sequencestr
          # for detail. By default, it is set to an empty list.
          allowed_origins_list: ["https://log.openwisp.org"]
          # Configures "CORS_REPLACE_HTTPS_REFERER" setting of the django-cors-headers
          # package. Read https://github.com/adamchainz/django-cors-headers#cors_replace_https_referer-bool
          # for detail. Setting this to "true" will also configure the
          # Django middleware setting to add "CorsPostCsrfMiddleware".
          # By default, it is set to false.
          replace_https_referer: true

.. note::

    The default settings for controlling the number of processes and
    threads in uWSGI and Daphne are set conservatively. Users are
    encouraged to adjust these settings to match the scale of their
    project. The same applies to the concurrency and auto-scaling settings
    for Celery workers.
