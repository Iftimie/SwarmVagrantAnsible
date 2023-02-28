# Docker swarm cluster stack setup with Vagrant and Ansible

This repository contains the definitions for a basic docker swarm cluster stack deployed on 2 VMs.

## Setup

Create the virtual machines with the command `vagrant up`. In case it fails, run `vagrant destroy -f` and retry. Perhaps retry without destroying using `vagrant up --provision`.

While still on the host, create the cluster using the following commands
```
export ANSIBLE_HOST_KEY_CHECKING=False 
ansible-playbook -i inventory.ini create_cluster.yml
```

Deploy the app using the following command. Retry the command in case the it fails.
```
ansible-playbook -i inventory.ini deploy.yml
```

Test that it works by running these commands on the host
```
curl 192.168.56.11:9999 --http0.9
curl 192.168.56.10:9999 --http0.9
```