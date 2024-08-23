
# Part 3: Advanced Role Features

## Chapter 5: Using Dependencies and Meta Files

### 5.1 Understanding Role Dependencies
- **Overview**: Explain the concept of role dependencies. In some scenarios, a role may depend on other roles to be executed first. This is where the `meta` directory comes into play.
- **Use Case**: Describe a scenario where one role depends on another. For example, a `webserver` role might depend on a `common` role that sets up basic server configurations (like installing common packages).

### 5.2 Practical Example: Defining Role Dependencies
#### Step 1: Create the Dependent Roles
- Create two roles: `common` and `webserver`.
  ```bash
  ansible-galaxy init common
  ansible-galaxy init webserver
  ```

#### Step 2: Define Tasks in the `common` Role
- In the `common` role, define tasks to install essential packages.
  ```yaml
  # common/tasks/main.yml
  ---
  - name: Install essential packages
    apt:
      name: "{{ item }}"
      state: present
    loop:
      - curl
      - vim
      - git
  ```

#### Step 3: Add a Dependency in the `webserver` Role
- In the `webserver` role, define a dependency on the `common` role in the `meta/main.yml` file.
  ```yaml
  # webserver/meta/main.yml
  ---
  dependencies:
    - role: common
  ```

#### Step 4: Define Tasks in the `webserver` Role
- Define tasks in the `webserver` role to install and configure Apache.
  ```yaml
  # webserver/tasks/main.yml
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

#### Step 5: Create a Playbook to Run the `webserver` Role
- Create a playbook that applies the `webserver` role.
  ```yaml
  # site.yml
  ---
  - hosts: localhost
    become: yes
    roles:
      - webserver
  ```

#### Step 6: Run the Playbook
- Execute the playbook, which will automatically run the `common` role before the `webserver` role due to the dependency.
  ```bash
  ansible-playbook site.yml
  ```

### 5.3 Hands-On Exercise: Adding More Dependencies
- **Exercise**: Add another role, `firewall`, which configures UFW (Uncomplicated Firewall). Modify the `webserver` role to depend on both the `common` and `firewall` roles. Test the playbook to ensure all roles are executed in the correct order.

---

## Chapter 6: Role Handlers and Notifications

### 6.1 Understanding Handlers and Notifications
- **Overview**: Explain the purpose of handlers in Ansible. Handlers are tasks that are triggered by other tasks using the `notify` directive, usually for actions that need to occur only if there is a change (e.g., restarting a service after a configuration file is modified).

### 6.2 Practical Example: Using Handlers in a Role
#### Step 1: Create a Role with a Handler
- Define a role that includes a handler to restart Apache when its configuration is changed.
  ```bash
  ansible-galaxy init apache_handler
  cd apache_handler
  ```

#### Step 2: Define the Main Tasks
- Add a task to deploy an Apache configuration file using a template.
  ```yaml
  # apache_handler/tasks/main.yml
  ---
  - name: Deploy Apache configuration
    template:
      src: apache.conf.j2
      dest: /etc/apache2/sites-available/000-default.conf
    notify:
      - Restart Apache
  ```

#### Step 3: Define the Handler
- Create a handler to restart the Apache service.
  ```yaml
  # apache_handler/handlers/main.yml
  ---
  - name: Restart Apache
    service:
      name: apache2
      state: restarted
  ```

#### Step 4: Create a Template
- Create a simple template for the Apache configuration.
  ```jinja2
  # apache_handler/templates/apache.conf.j2
  <VirtualHost *:80>
      DocumentRoot /var/www/html
      ErrorLog ${APACHE_LOG_DIR}/error.log
      CustomLog ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
  ```

#### Step 5: Run the Role in a Playbook
- Create a playbook to apply the `apache_handler` role.
  ```yaml
  # site.yml
  ---
  - hosts: localhost
    become: yes
    roles:
      - apache_handler
  ```

#### Step 6: Execute the Playbook
- Run the playbook, which should deploy the Apache configuration and restart Apache if the configuration changes.
  ```bash
  ansible-playbook site.yml
  ```

### 6.3 Hands-On Exercise: Adding Multiple Handlers
- **Exercise**: Extend the `apache_handler` role by adding more handlers, such as reloading Apache when the document root is updated. Test the role by changing the configuration and verifying that the correct handlers are triggered.
