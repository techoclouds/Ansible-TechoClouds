.3 Loops and Conditionals

Objective: Master advanced looping and conditional execution.

Topics:

    Deep Dive into with_items, with_nested, and with_dict:
        with_items: Loop over a list of items.
        with_nested: Loop over a nested list.
        with_dict: Loop over key-value pairs in a dictionary.

    Using the When Conditional with Tasks and Blocks:
        when: Conditional execution based on variables or facts.

Hands-On Exercises:

Exercise 1: Write a Playbook Using with_nested for Complex Configurations

Step 1: Write the Playbook (playbook_nested.yml)

yaml

---
- hosts: localhost
  tasks:
    - name: Configure multiple users with roles
      user:
        name: "{{ item[0] }}"
        groups: "{{ item[1] }}"
      with_nested:
        - [ 'user1', 'user2' ]
        - [ 'admin', 'developers' ]

Step 2: Run the Playbook

bash

ansible-playbook playbook_nested.yml

Observe how the playbook creates users and assigns them to different groups.
