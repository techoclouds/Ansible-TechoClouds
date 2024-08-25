
# Part 2: Structuring and Organizing Roles

## Chapter 3: Role Directory Structure

### 3.1 Understanding the Role Directory Structure
- **Overview**: Explain the purpose of each directory and file in an Ansible role. This helps ensure that students understand where to place different components of their role and how to organize their work.
  - **tasks/**: Contains the main tasks to be executed by the role.
  - **handlers/**: Contains handlers that are triggered by tasks.
  - **defaults/**: Stores default variables for the role.
  - **vars/**: Stores other variables, typically higher precedence than defaults.
  - **files/**: Holds static files that can be copied to managed hosts.
  - **templates/**: Holds Jinja2 templates for generating dynamic files.
  - **meta/**: Contains metadata about the role, including dependencies.
  - **tests/**: Contains tests for the role (optional).
  - **README.md**: Documentation for the role, explaining its purpose and usage.

### 3.2 Practical Example: Building a Multi-Task Role
#### Step 1: Create a New Role
- Set up a new role using the `ansible-galaxy init` command.
  ```bash
  ansible-galaxy init apache_role
  cd apache_role
  ```

#### Step 2: Define Tasks in the `tasks/` Directory
- Open `tasks/main.yml` and define tasks to install and configure Apache.
  ```yaml
  ---
  - name: Install Apache
    apt:
      name: apache2
      state: present
      update_cache: yes

  - name: Ensure Apache is started
    service:
      name: apache2
      state: started
  ```

#### Step 3: Add a Handler in the `handlers/` Directory
- Create a handler to restart Apache when the configuration changes.
  ```yaml
  ---
  # handlers/main.yml
  - name: Restart Apache
    service:
      name: apache2
      state: restarted
  ```

#### Step 4: Set Default Variables in `defaults/` Directory
- Define default variables for the role in `defaults/main.yml`.
  ```yaml
  ---
  apache_port: 80
  ```

#### Step 5: Use a Template in the `templates/` Directory
- Create an Apache configuration template (`templates/apache.conf.j2`).
  ```jinja2
  <VirtualHost *:{{ apache_port }}>
      DocumentRoot /var/www/html
      ErrorLog ${APACHE_LOG_DIR}/error.log
      CustomLog ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
  ```
- Modify the task to use the template.
  ```yaml
  ---
  - name: Deploy Apache configuration
    template:
      src: apache.conf.j2
      dest: /etc/apache2/sites-available/000-default.conf
    notify:
      - Restart Apache
  ```

#### Step 6: Add Metadata in the `meta/` Directory
- Define metadata for the role in `meta/main.yml`, such as dependencies.
  ```yaml
  ---
  dependencies: []
  ```

#### Step 7: Write Documentation in `README.md`
- Document the role's purpose, variables, and usage in `README.md`.




## Chapter 4: Using Variables in Roles

### 4.1 Variable Precedence in Roles
- **Overview**: Explain how variable precedence works in Ansible, especially within roles. Clarify the differences between variables defined in `defaults/`, `vars/`, playbooks, and inventory files.

### 4.2 Defining and Using Default Variables
#### Step 1: Set Default Variables in `defaults/`
- Describe how to set default variables that can be overridden by higher precedence variables.
  ```yaml
  ---
  apache_port: 8080
  document_root: /var/www/html
  ```

### 4.3 Overriding Variables in Playbooks
#### Step 2: Override Variables in a Playbook
- Show how to override default variables when applying the role in a playbook.
  ```yaml
  ---
  - hosts: localhost
    become: yes
    vars:
      apache_port: 8080
    roles:
      - apache_role
  ```

### 4.4 Using Variables from Inventory Files
#### Step 3: Use Variables from Inventory Files
- Demonstrate how to set variables in inventory files that can override role defaults.

### 4.5 Hands-On: Working with Variables
#### 3.4 Practical Example: Overriding Variables from Inventory Files

**Scenario**: You want to override the default `apache_port` variable defined in the `defaults/main.yml` file of the `apache_role` using an inventory file. This is useful when you want different servers in your infrastructure to use different port configurations without modifying the role itself.

##### 1. Define the Default Variable in the Role

Ensure that the `defaults/main.yml` file in your role defines the `apache_port` variable:

```yaml
# apache_role/defaults/main.yml
---
apache_port: 80
```

This sets the default port to `80`.

##### 2. Create an Inventory File with Variable Overrides

Now, create an inventory file that defines host-specific variables to override the default port.

```ini
# inventory.ini
[webservers]
server1 ansible_host=127.0.0.1 apache_port=8080
server2 ansible_host=192.168.1.2 apache_port=9090
```

In this example:
- `server1` will use port `8080`.
- `server2` will use port `9090`.

##### 3. Update the Playbook to Use the Inventory File

Modify your playbook to use the inventory file:

```yaml
# site.yml
---
- hosts: webservers
  become: yes
  roles:
    - apache_role
```

When you run this playbook, it will apply the `apache_role` to the hosts defined in the `inventory.ini` file.

##### 4. Modify the Template to Use the Variable

Ensure that the Apache configuration template uses the `apache_port` variable:

```jinja2
# apache_role/templates/apache.conf.j2
<VirtualHost *:{{ apache_port }}>
    DocumentRoot /var/www/html
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

##### 5. Run the Playbook

Execute the playbook with the inventory file:

```bash
ansible-playbook -i inventory.ini site.yml
```

##### 6. Verify the Configuration

After the playbook runs, verify that the correct port is set in the Apache configuration for each server:

- For `server1`:
  ```bash
  cat /etc/apache2/sites-available/000-default.conf
  ```

  You should see:
  ```text
  <VirtualHost *:8080>
      DocumentRoot /var/www/html
      ...
  </VirtualHost>
  ```

- For `server2`:
  ```bash
  cat /etc/apache2/sites-available/000-default.conf
  ```

  You should see:
  ```text
  <VirtualHost *:9090>
      DocumentRoot /var/www/html
      ...
  </VirtualHost>
  ```

### Hands-On Exercise: Expanding the Example

- **Exercise**: Extend this example by adding more variables like `server_admin` and `document_root` to the inventory file and modify the `apache_role` to use these variables. Test the playbook to ensure the role correctly applies these settings based on the inventory.
