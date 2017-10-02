
This is being tested on Ubuntu 16.04.3

Two environment variables need to be set correctly prior to the run for the username and password of the Ubuntu server:

```
export ANSIBLE_SSH_USERNAME=ubuntu
export ANSIBLE_SSH_PASSWORD=ubuntu
```
You will need to update thelicaense key prior to the playbook run. The tyk dashboard site configuration can be found in:

```yaml
➜  tyk-ansible more inventory/group_vars/tyk_dashboard/vars.yml
tyk_dashboard_config:
  admin_secret: "12345"
  host_config:
    hostname: "{{ ansible_default_ipv4['address'] }}"
    override_hostname: "{{ inventory_hostname }}"
    portal_root_path: /portal
  license_key: XXXXX
  license_owner: Company
  listen_port: 3000
  mongo_url: mongodb://127.0.0.1/tyk_analytics
  redis_host: localhost
  redis_port: 6379
  tyk_api_config:
    Host: http://localhost
    Port: "8080"

tyk_dashboard_organization:
  owner_name: Default Org
  owner_slug: default
  cname_enabled: true
  cname: ""

tyk_dashboard_user_account:
  first_name: Sample
  last_name: User
  email_address: suser@company.net
  org_id: "{{ exisiting_organisation_id if exisiting_organisation else organisation['json']['Meta'] }}"
  password: password

tyk_dashboard_user_password:
  new_password: password
```

The IP address of the Ubuntu server will also need to be updated.  It can be found:

```shell
➜  tyk-ansible more inventory/inventory.txt
ubuntu ansible_host=172.16.124.173


[tyk_dashboard]
ubuntu

[mongo]
ubuntu

[redis]
ubuntu
```
