These examples cover a range of Ansible features, showcasing how you can structure playbooks, use variables, conditionally execute tasks, and use handlers. Understanding these concepts will help you create more complex and versatile Ansible playbooks.

# Playbook 1 (playbook1.yaml):
yaml
```
- hosts: localhost
  tasks:
    - name: ping
      ping:
    - name: install vim
      package:
        state: present
```
##### Description:

This playbook targets the localhost.
The tasks include a simple ping check and the installation of the vim package.

# Playbook 2 (playbook2.yaml):

```
---
- hosts: localhost
  gather_facts: False
  tasks:
    - name: ping
      ping:
    - name: install vim
      package:
        state: present
```
##### Description:

Similar to Playbook 1, but with gather_facts set to False.
###### Use Cases and Benefits:

If you don't need facts about the target host (e.g., hardware details, IP addresses), setting gather_facts: False can speed up playbook execution.
# Playbook 3 (playbook3.yaml):

```
---
- hosts: localhost
  gather_facts: False
  tasks:
    - name: ping
      ping:
    - name: install vim
      package:
        state: present
    - name: create a file
      copy:
        content: Hello From TechoClouds
        dest: ~/TechoClouds-hello.txt
```
##### Description:

Adds a task to create a file with specified content.
Demonstrates the ability to perform multiple tasks.

# Playbook 4 (playbook4.yaml):

```
---
- hosts: localhost
  gather_facts: False
  vars:
    data: "Hello From TechoClouds Family"

  tasks:
    - name: ping
      ping:
    - name: install vim
      package:
        state: present
    - name: create a file
      copy:
        content: "{{ data }}"
        dest: ~/TechoClouds-hello.txt
    - name: cat file
      shell: |
        cat ~/TechoClouds-hello.txt
      register: file_content
    - name: "Print the file content to a console"
      debug:
         msg: "{{ file_content.stdout }}"
```
##### Description:

Introduces variable (data) and uses it to create a file.
Registers the output of the cat command in a variable.
###### Use Cases:

Demonstrates variable usage.
Shows how to capture and use the sttout output of a task.
# Playbook 5 (playbook5.yaml):

```
---
- hosts: localhost
  gather_facts: False
  vars:
    data: "Hello From TechoClouds Family"

  tasks:
    - name: ping
      ping:
    - name: install vim
      package:
        state: present
    - name: create a file
      copy:
        content: "{{ data }}"
        dest: ~/TechoClouds-hello.txt
    - name: cat file
      shell: |
        cat ~/TechoClouds-hello.txt
      changed_when: false
      register: file_content
    - name: "Print the file content to a console"
      debug:
         msg: "{{ file_content.stdout }}"
```
##### Description:

Similar to Playbook 4 but with changed_when: false in the cat task.
Demonstrates controlling when a task is considered "changed."
# Playbook 6 (playbook6.yaml):

```
---
- hosts: localhost
  gather_facts: False
  vars:
    data: "Hello From TechoClouds Super Family"

  tasks:
    - name: ping
      ping:
    - name: install vim
      package:
        state: present
    - name: create a file
      copy:
        content: "{{ data }}"
        dest: ~/TechoClouds-hello.txt
      notify: handlers_test
    - name: 
      shell: |
        cat ~/TechoClouds-hello.txt
      register: file_content
      
  handlers:
    - name: handlers_test
      debug:
        msg: "{{ file_content.stdout }}"
```
##### Description:

Introduces a handler (handlers_test) to print the file content.
Demonstrates the use of handlers to perform additional actions when specific tasks trigger changes.
# Playbook 7 (playbook7.yaml):
yaml
```
---
- hosts: localhost
  vars:
    data: "Hello From TechoClouds Supper Family"

  tasks:
    - name: ping
      ping:
    - name: install vim
      package:
        state: present
    - name: create a file
      copy:
        content: "{{ data }}"
        dest: ~/TechoClouds-hello.txt
      when: ansible_distribution_version == '20.04x'
      notify: handlers_test
    - name: 
      shell: |
        cat ~/TechoClouds-hello.txt
      register: file_content
      
  handlers:
    - name: handlers_test
      debug:
        msg: "{{ file_content.stdout }}"
```
##### Description:

Introduces a conditional task (create a file) based on the Ubuntu version.

Demonstrates how to conditionally execute tasks based on specific criteria.

Useful for scenarios where tasks need to adapt to different conditions or target hosts with different characteristics.
