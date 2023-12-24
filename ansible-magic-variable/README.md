# Ansible Special Variables: Magic and Facts Tutorial by DevOps TechPark

## Overview

Ansible utilizes special variables to provide insights into the systems being managed and the execution environment. This tutorial explores two types of special variables:

#### 1. Magic Variables:

    Reflect internal state and system information managed by Ansible.
    Cannot be directly set by users; Ansible overrides them.
    Examples: ansible_hostname, ansible_distribution, playbook_dir, ansible_check_mode
    ### Some more common magic variables in Ansible include:
    - ###### ansible_host: Contains the name of the host currently being worked on.
    - ###### ansible_hostname: Represents the hostname of the target machine.
    - ###### ansible_distribution: Stores the distribution name (like Ubuntu, CentOS, etc.).
    - ###### ansible_distribution_version: Contains the version of the distribution.
    - ###### ansible_facts: Provides a dictionary containing all the gathered facts about the target system.
    - ###### ansible_play_batch: Lists all the hosts in the current play run.
    - ###### ansible_play_hosts: Lists all the hosts in the current play.


    
#### 2. Facts Variables:

    Contain host-specific information, available only if gathered (gather_facts: true).
    Provide details such as IP addresses, disk information, network interfaces, etc.
    Examples: ansible_hostname, ansible_default_ipv4.address

[![asciicast](https://asciinema.org/a/628701.svg)](https://asciinema.org/a/628701)
## Sample Playbook
File: special-variable.yaml
https://asciinema.org/a/628701
```
---
# Ansible Magic and Fact Variable Example
- name: Print Hostname and IP Address
  hosts: all
  gather_facts: true
  tasks:
    - name: Display Ansible Internal (Magic) Variables
      debug:
        msg: "Playbook Dir: {{ playbook_dir }}, Ansible Check Mode: {{ ansible_check_mode }}"

    - name: Display Hostname and IP (Facts Variables)
      debug:
        msg: "Hostname: {{ ansible_hostname }}, IP Address: {{ ansible_default_ipv4.address }}"
```
Use code with caution. Learn more
## Explanation

Task 1:

Demonstrates usage of magic variables.
Outputs playbook directory (playbook_dir) and Ansible's check mode status (ansible_check_mode).
Task 2:

Demonstrates usage of facts variables.
Displays hostname (ansible_hostname) and default IPv4 address (ansible_default_ipv4.address) of the target host.
## Running the Playbook

Bash
`ansible-playbook -i hosts special-variable.yaml`

## Conclusion

Understanding special variables empowers playbook creators to access critical information and create more dynamic and adaptable playbooks.

In Ansible, magic variables are predefined variables that hold information about the system, playbook, or other aspects of the execution environment. These variables are automatically populated by Ansible and can be accessed within playbooks or roles. They provide useful information that can be utilized during the execution of tasks.


