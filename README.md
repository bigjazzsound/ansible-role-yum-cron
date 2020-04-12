ansible-role-yum-cron
=========

A role to manage the yum-cron service.

Requirements
------------

None

Role Variables
--------------

```
yum_cron_service_enabled: true
yum_cron_service_state: started
```

Manage the state of the yum-cron service.

```
yum_cron_conf:
  commands:
    update_cmd: "default"
    update_messages: "yes"
    download_updates: "yes"
    apply_updates: "no"
    random_sleep: "360"
  emitters:
    system_name: "None"
    emit_via: "stdio"
    output_width: "80"
  email:
    email_from: "root@localhost"
    email_to: "root"
    email_host: "localhost"
  groups:
    group_list: "None"
    group_package_types: "mandatory, default"
  base:
    debuglevel: "-2"
    skip_broken: "False"
    mdpolicy: "group:main"
    assumeyes: "False"

yum_cron_conf_custom: {}
```

A dictionary representation of the yum-cron.conf file. **The default values are the same as when you install the yum-cron package.** You can use your own configuration by setting `yum_cron_conf` or modify the default configuration by adding any override values to the `yum_cron_conf_custom` dictionary.

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: all
  roles:
     - role: ansible-role-yum-cron
```

License
-------

BSD

Author Information
------------------

[Github](https://github.com/bigjazzsound)  
[Email](craigjamesfielder@gmail.com)  
