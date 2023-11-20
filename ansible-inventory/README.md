# Ansible Course By TechoClouds
## Step no. 1
- Introduced basic structure.
- Added a single ubuntu-vm1 host.

This initial Step establishes a simple Ansible inventory structure with a single Ubuntu host (ubuntu-vm1). It serves as a starting point to build upon for subsequent configurations.

###### Hosts File Content 

```
[all]
ubuntu-vm1
```
##### Purpose
Use this Step to understand how to create a basic Ansible inventory file and define hosts within different groups.




## Step no. 2
- Disabled host key checking.

Disabling host key checking removes the prompt that verifies SSH connections, allowing for smoother automation without user interaction.
###### Hosts File Content 
```
[defaults]
inventory = hosts
host_key_checking = False
[all]
centos-vm1
```
##### Purpose
Demonstrate the impact of disabling host key checking and understand its relevance in automated Ansible operations.
## Step no. 3
- Expanded host groups: CentOS and Ubuntu with multiple hosts under each

This revision showcases the ability to organize hosts into distinct groups for different operating systems (CentOS and Ubuntu).
###### Hosts File Content 
```
[centos]
centos-vm1
centos-vm2

[ubuntu]
ubuntu-vm1
ubuntu-vm2
```
##### Purpose
Understand how grouping hosts based on their operating systems facilitates targeted configuration management using Ansible playbooks.


## Step no. 4
- Assigned ansible_user=root for CentOS hosts.


Setting ansible_user=root for CentOS hosts ensures Ansible connects using the root user.

###### Hosts File Content 
```
[centos]
centos-vm1
centos-vm2
[ubuntu]
ubuntu-vm1 ansible_user=root
ubuntu-vm2 ansible_user=root
```
##### Purpose

Understand how to specify different user privileges for various hosts in the inventory.




## Step no. 5
- Assigned ansible_become=true and ansible_become_pass=password for Ubuntu hosts.
Define privilege escalation settings (ansible_become) for Ubuntu hosts.
###### Hosts File Content 
```
[defaults]
inventory = hosts
host_key_checking = False
[centos]
centos-vm1 ansible_user=root
centos-vm2 ansible_user=root
centos-vm3 ansible_user=root

[ubuntu]
ubuntu-vm1 ansible_become=true ansible_become_pass=password
ubuntu-vm2 ansible_become=true ansible_become_pass=password
ubuntu-vm3 ansible_become=true ansible_become_pass=password
```
##### Purpose





mplement privilege escalation within Ansible for specific hosts.




## Step no. 6
- SSH port and user configurations 
Illustrate how different SSH port and user configurations can be applied to different hosts.
```
[centos]
centos-vm1 ansible_user=root ansible_port=2222
##following is another way of defining port
#centos-vm1:2222 ansible_user=root

centos-vm2 ansible_user=root
centos-vm3 ansible_user=root
[ubuntu]
ubuntu-vm1 ansible_become=true ansible_become_pass=password
ubuntu-vm2 ansible_become=true ansible_become_pass=password
ubuntu-vm3 ansible_become=true ansible_become_pass=password
```
##### Purpose
Showcase customized SSH configurations for specific hosts within the Ansible inventory.
Demonstrate the flexibility to customize SSH connection parameters for specific hosts within the Ansible inventory.

## Step no. 7
- Restructured host and group definitions using shorthand notation.

- 

`centos-vm1 ansible_user=root ansible_port=2222`: This line represents a single CentOS host with specific connection details (user and port).

`centos[2:3] ansible_user=root`: This line is a range notation indicating CentOS hosts from centos-vm2 to centos-vm3 with the same ansible_user but without specifying the port (default port is assumed).


`ubuntu[1:3] ansible_become=true ansible_become_pass=password`: It defines three Ubuntu hosts (ubuntu-vm1, ubuntu-vm2, and ubuntu-vm3) with privilege escalation settings (`ansible_become=true for sudo/root access`)
```
[defaults]
inventory = hosts
host_key_checking = False
[control]
ubuntu-c ansible_connection=local


[centos]
centos-vm1 ansible_user=root ansible_port=2222
centos[2:3] ansible_user=root

[ubuntu]
ubuntu[1:3] ansible_become=true ansible_become_pass=password

```
##### Purpose


## Step no. 8

- User varibale in hosts file

- 

`ansible_user=root`: Defines a variable within the centos and ubuntu group, setting the `ansible_user` as `root` for all hosts within this group.
```

ubuntu-c ansible_connection=local

[centos]
centos-vm1 ansible_port=2222
centos[2:3]


[centos:vars]
ansible_user=root

[ubuntu]
ubuntu[1:3]

[ubuntu:vars]
ansible_become=true
ansible_become_pass=password


```
##### Purpose
