
### Setting a single variable and using it in a task
This playbook sets a single variable named example_var to a string value. It then uses this variable in a task to display its value.
```
---

- hosts: localhost
  gather_facts: False

  vars:
    # Defining a string variable
    example_var: Hello from TechoClouds 

  tasks:
    - name: Displaying a single variable value
      debug:
        msg: "{{ example_var }}"
...
```
### Using a dictionary variable and accessing its keys
Here, a dictionary variable named `sample_dict` is defined with a key-value pair. The playbook demonstrates accessing the entire dictionary, a specific key using dot notation `(sample_dict.dict_key)`, and the same key using bracket notation (sample_dict['dict_key']).
```
---

- hosts: localhost
  gather_facts: False

  vars:
    # Defining a dictionary variable
    #dict_inline
    #   {dict_key1: Hello from inline dictionary, dict_key2: value2}

    sample_dict:
      dict_key1: Value1
      dict_key2: This is a value2

  tasks:
    - name: Displaying the entire dictionary
      debug:
        msg: "{{ sample_dict }}"

    - name: Accessing dictionary key using dot notation
      debug:
        msg: "{{ sample_dict.dict_key1 }}"

    - name: Accessing dictionary key using bracket notation
      debug:
        msg: "{{ sample_dict['dict_key2'] }}"




...
```

### Using a list variable and accessing its elements
This section focuses on a list variable named datalist, containing multiple elements. It demonstrates displaying the entire list, accessing the first element using dot notation (datalist.0), and accessing the first element using bracket notation (datalist[0]).
```
---

- hosts: localhost
  gather_facts: False

  vars:
    # Defining a list variable
    datalist:
      - element1
      - element2
      - element3
      - element4
    # Defining an inline list variable
    #datalist2:
    #  [ item1, item2, item3, item4 ]


  tasks:
    - name: Displaying inline list
      debug:
        msg: "{{ datalist }}"

    - name: Accessing first item in inline list using dot notation
      debug:
        msg: "{{ datalist.2 }}"

    - name: Accessing first item in inline list using bracket notation
      debug:
        msg: "{{ datalist[0] }}"
...
```
###   Prompts the user for input variables 

The vars_prompt section prompts the user for input variables that will be used in the playbook. In this case, the variable target_user is prompted, representing the username for the target system. The private: False ensures that the entered value is not treated as a secret.

```
---

---

- hosts: localhost
  gather_facts: False

  # User Input: Prompts the user for input
  vars_prompt:
    - name: target_user
      private: False
      prompt: "Enter the username for the target system:"

  # Execution Tasks
  tasks:
    - name: Display User Input
      debug:
        msg: "{{ target_user }}"


...


...

