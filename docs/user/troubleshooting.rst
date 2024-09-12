Troubleshooting
===============

OpenWISP is deployed using **uWSGI** and also uses **daphne** for
WebSockets and **celery** as a task queue.

All these services are run by **supervisor**.

.. code-block:: shell

    sudo service supervisor start|stop|status

You can view each individual process run by supervisor with the following
command:

.. code-block:: shell

    sudo supervisorctl status

For more information about Supervisord, refer to `Running supervisorctl
<http://supervisord.org/running.html#running-supervisorctl>`__.

The **nginx** web server sits in front of the **uWSGI** application
server. You can control nginx with the following commands:

.. code-block:: shell

    service nginx status start|stop|status

OpenWISP is installed in ``/opt/immunity22`` (unless you changed the
``immunity22_path`` variable in the Ansible playbook configuration). These
are some useful directories to check when experiencing issues.

========================= ==============================
Location                  Description
========================= ==============================
/opt/immunity22            The OpenWISP 2 root directory.
/opt/immunity22/log        Log files
/opt/immunity22/env        Python virtual environment
/opt/immunity22/db.sqlite3 OpenWISP 2 SQLite database
========================= ==============================

All processes are running as the ``www-data`` user.

If you need to copy or edit files, you can switch to the ``www-data`` user
with the following commands:

.. code-block:: shell

    sudo su www-data -s /bin/bash
    cd /opt/immunity22
    source env/bin/activate

SSL Certificate Gotchas
-----------------------

When you access the admin website, you will receive an SSL certificate
warning because the playbook creates a self-signed (untrusted) SSL
certificate. You can get rid of the warning by installing your own trusted
certificate and setting the ``immunity22_ssl_cert`` and
``immunity22_ssl_key`` variables accordingly or by following the
instructions explained in the section :doc:`certbot-ssl`.

If you keep the untrusted certificate, you will also need to disable SSL
verification on devices using :doc:`openwisp-config
</openwrt-config-agent/index>` by setting ``verify_ssl`` to ``0``,
although we advise against using this kind of setup in a production
environment.
