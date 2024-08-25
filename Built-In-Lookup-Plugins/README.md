# Built-In Lookup Plugins

## Objective:
Gain a deep understanding of built-in lookup plugins in Ansible, exploring how to use them effectively in playbooks to query and manipulate data dynamically.

## Topics:

### 1. Introduction to Lookup Plugins:
- **What are Lookup Plugins?**
    - Lookup plugins in Ansible allow you to query external data sources or manipulate data dynamically within your playbooks. These plugins return values that can be used directly in tasks or stored in variables for further use.
- **Common Use Cases**:
    - Fetching data from files, environment variables, or other resources during playbook execution.
    - Dynamically setting variables based on external data.

### 2. Overview of Common Built-In Lookup Plugins:
- **`file`**:
    - Reads the content of a file and returns it as a string.
- **`env`**:
    - Retrieves the value of an environment variable.
- **`pipe`**:
    - Executes a shell command and returns its output.
- **`template`**:
    - Renders a template using Jinja2 and returns the result.
- **`dict`**:
    - Returns a list of key-value pairs from a dictionary.
- **`first_found`**:
    - Returns the content of the first file found in a list of files.
- **`password`**:
    - Generates a random password or retrieves a stored one.

## Hands-On Exercises:

### Exercise 1: Using the `file` Lookup Plugin to Read File Content

**Step 1: Prepare a Text File (`files/sample.txt`)**

    ```bash
    echo "Hello, this is a sample file content." > files/sample.txt
    ```

**Step 2: Write a Playbook to Use the `file` Lookup Plugin (`playbook_file_lookup.yml`)**

    ```yaml
    ---
    - hosts: localhost
      tasks:
        - name: Read content from a file using the file lookup plugin
          debug:
            msg: "{{ lookup('file', 'files/sample.txt') }}"
    ```

**Step 3: Run the Playbook**

    ```bash
    ansible-playbook playbook_file_lookup.yml
    ```

### Exercise 2: Using the `env` Lookup Plugin to Retrieve Environment Variables

**Step 1: Set an Environment Variable**

    ```bash
    export MY_VAR="This is an environment variable"
    ```

**Step 2: Write a Playbook to Use the `env` Lookup Plugin (`playbook_env_lookup.yml`)**

    ```yaml
    ---
    - hosts: localhost
      tasks:
        - name: Retrieve an environment variable using the env lookup plugin
          debug:
            msg: "{{ lookup('env', 'MY_VAR') }}"
    ```

**Step 3: Run the Playbook**

    ```bash
    ansible-playbook playbook_env_lookup.yml
    ```

### Exercise 3: Using the `pipe` Lookup Plugin to Execute Shell Commands

**Step 1: Write a Playbook to Use the `pipe` Lookup Plugin (`playbook_pipe_lookup.yml`)**

    ```yaml
    ---
    - hosts: localhost
      tasks:
        - name: Execute a shell command using the pipe lookup plugin
          debug:
            msg: "{{ lookup('pipe', 'date') }}"
    ```

**Step 2: Run the Playbook**

    ```bash
    ansible-playbook playbook_pipe_lookup.yml
    ```

### Exercise 4: Using the `template` Lookup Plugin to Render Templates

**Step 1: Create a Jinja2 Template (`templates/sample_template.j2`)**

    ```bash
    mkdir -p templates
    echo "Hello, {{ ansible_user }}!" > templates/sample_template.j2
    ```

**Step 2: Write a Playbook to Use the `template` Lookup Plugin (`playbook_template_lookup.yml`)**

    ```yaml
    ---
    - hosts: localhost
      tasks:
        - name: Render a template using the template lookup plugin
          debug:
            msg: "{{ lookup('template', 'templates/sample_template.j2') }}"
    ```

**Step 3: Run the Playbook**

    ```bash
    ansible-playbook playbook_template_lookup.yml
    ```

### Exercise 5: Using the `first_found` Lookup Plugin to Find and Read Files

**Step 1: Prepare Multiple Files**

    ```bash
    mkdir -p files
    echo "This is the first file." > files/file1.txt
    echo "This is the second file." > files/file2.txt
    ```

**Step 2: Write a Playbook to Use the `first_found` Lookup Plugin (`playbook_first_found.yml`)**

    ```yaml
    ---
    - hosts: localhost
      tasks:
        - name: Use the first_found lookup plugin to read the first available file
          debug:
            msg: "{{ lookup('first_found', item) }}"
          loop:
            - files/file3.txt
            - files/file2.txt
            - files/file1.txt
    ```

**Step 3: Run the Playbook**

    ```bash
    ansible-playbook playbook_first_found.yml
    ```
