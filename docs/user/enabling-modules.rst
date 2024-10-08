Enabling OpenWISP Modules
=========================

.. contents:: **Table of Contents**:
    :depth: 3
    :local:

Enabling the Monitoring Module
------------------------------

The :doc:`Monitoring module </monitoring/index>` is enabled by default, it
can be disabled by setting ``immunity22_monitoring`` to ``false``.

Enabling the Firmware Upgrader Module
-------------------------------------

It is encouraged that you read the :doc:`quick-start guide of
openwisp-firmware-upgrader </firmware-upgrader/user/quickstart>` before
going ahead.

To enable the :doc:`Firmware Upgrader </firmware-upgrader/index>` module
you need to set ``immunity22_firmware_upgrader`` to ``true`` in your
``playbook.yml`` file. Here's a short summary of how to do this:

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
        immunity22_firmware_upgrader: true

**Step 5**: :ref:`Run the playbook <ansible_run_playbook>`

When the playbook is done running, if you got no errors you can login at
https://immunity22.mydomain.com/admin with the following credentials:

.. code-block:: text

    username: admin
    password: admin

You can configure :doc:`openwisp-firmware-upgrader specific settings
</firmware-upgrader/user/settings>` using the
``immunity22_extra_django_settings`` or
``immunity22_extra_django_settings_instructions``.

E.g:

.. code-block:: yaml

    - hosts: immunity22
      become: "{{ become | default('yes') }}"
      roles:
        - openwisp.immunity22
      vars:
        immunity22_firmware_upgrader: true
        immunity22_extra_django_settings_instructions:
          - |
            OPENWISP_CUSTOM_OPENWRT_IMAGES = (
                ('my-custom-image-squashfs-sysupgrade.bin', {
                    'label': 'My Custom Image',
                    'boards': ('MyCustomImage',)
                }),
            )

Refer the :doc:`role-variables` section of the documentation for a
complete list of available role variables.

Enabling the Network Topology Module
------------------------------------

To enable the :doc:`Network Topology module </network-topology/index>` you
need to set ``immunity22_network_topology`` to ``true`` in your
``playbook.yml`` file. Here's a short summary of how to do this:

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
        immunity22_network_topology: true

**Step 5**: :ref:`Run the playbook <ansible_run_playbook>`

When the playbook is done running, if you got no errors you can login at
https://immunity22.mydomain.com/admin with the following credentials:

.. code-block:: text

    username: admin
    password: admin

.. _ansible_enabling_radius_module:

Enabling the RADIUS Module
--------------------------

To enable the :doc:`RADIUS module </radius/index>` you need to set
``immunity22_radius`` to ``true`` in your ``playbook.yml`` file. Here's a
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
        immunity22_radius: true
        immunity22_freeradius_install: true
        # set to false when you don't want to register openwisp-radius
        # API endpoints.
        immunity22_radius_urls: true

.. note::

    ``immunity22_freeradius_install`` option provides a basic configuration
    of freeradius for OpenIWSP, it sets up the :ref:`radius user token
    mechanism <radius_user_token>` if you want to use another mechanism or
    manage your freeradius separately, please disable this option by
    setting it to ``false``.

**Step 5**: :ref:`Run the playbook <ansible_run_playbook>`

When the playbook is done running, if you got no errors you can login at:

.. code-block::

    https://immunity22.mydomain.com/admin
    username: admin
    password: admin

**Note:** for more information regarding radius configuration options,
look for the word “radius” in the :doc:`role-variables` section of this
document.
