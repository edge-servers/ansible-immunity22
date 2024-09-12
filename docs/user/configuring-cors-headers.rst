Configuring CORS Headers
========================

While integrating OpenWISP with external services, you can run into issues
related to `CORS (Cross-Origin Resource Sharing)
<https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS>`__. This role
allows users to configure the CORS headers with the help of
`django-cors-headers
<https://github.com/adamchainz/django-cors-headers>`__ package. Here's a
short summary of how to do this:

**Step 1**: :ref:`Install ansible <ansible_install>`

**Step 2**: :ref:`Install this role <ansible_install_role>`

**Step 3**: :ref:`Create inventory file <ansible_create_inventory_file>`

**Step 4**: Create a playbook file with following contents:

.. code-block:: yaml

    - hosts: immunity22
      become: "{{ become | default('yes') }}"
      roles:
        - openwisp.immunity22
      vars:
        # Cross-Origin Resource Sharing (CORS) settings
        immunity22_django_cors:
          enabled: true
          allowed_origins_list:
            - https://frontend.openwisp.org
            - https://logs.openwisp.org

**Note:** to learn about the supported fields of the
``immunity22_django_cors`` variable, look for the word
*"immunity22_django_cors"* in the :doc:`role-variables` section of this
document.

**Step 5**: :ref:`Run the playbook <ansible_run_playbook>`

When the playbook is done running, if you got no errors you can login at
https://immunity22.mydomain.com/admin, with the following credentials:

.. code-block:: text

    username: admin
    password: admin

The ansible-immunity22 only provides abstraction (variables) for handful of
settings available in `django-cors-headers
<https://github.com/adamchainz/django-cors-headers>`__ module. Use the
``immunity22_extra_django_settings_instructions`` or
``immunity22_extra_django_settings`` variable to configure additional
setting of ``django-cors-headers`` as shown in the following example:

.. code-block:: yaml

    - hosts: immunity22
      become: "{{ become | default('yes') }}"
      roles:
        - openwisp.immunity22
      vars:
        immunity22_django_cors:
          enabled: true
          allowed_origins_list:
            - https://frontend.openwisp.org
            - https://logs.openwisp.org
          replace_https_referer: true
        # Configuring additional settings for django-cors-headers
        immunity22_extra_django_settings_instructions:
          - |
            CORS_ALLOW_CREDENTIALS = True
            CORS_ALLOW_ALL_ORIGINS = True
