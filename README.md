### Overview

This playbook builds out a single server installation of tyk.  It is intended to be used to deploy tyk for development and testing purposes or as a starting point for a production multi server playbook.

### OS support

This is being tested on Ubuntu 16.04.3

### Server credentials

Two environment variables need to be set correctly prior to the run for the username and password of the Ubuntu server:

```
export ANSIBLE_SSH_USERNAME=ubuntu
export ANSIBLE_SSH_PASSWORD=ubuntu
```

### License key
You will need to update the licaense key prior to the playbook run. The tyk dashboard site configuration can be found in

```
inventory/tyk_dashboard/vars.yml
```

### Server IP address

The IP address of the Ubuntu server will also need to be updated if it cannot be found in DNS.  It can be found:

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

### Users

Two users are built, one super-admin and one admin in the default organization.  The configuration for these users is in:

```
inventory/tyk_dashboard
```
