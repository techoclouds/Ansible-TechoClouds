
## Part 5: Using Tags in Ansible

Tags in Ansible allow you to run specific tasks or roles within a playbook, providing a way to control which parts of your playbook get executed. This is particularly useful for testing, debugging, or applying only a subset of changes.

---

### Chapter 9: Introduction to Tags

#### 9.1 What Are Tags?
- **Overview**: Explain that tags are labels you can apply to tasks, roles, and blocks within an Ansible playbook. They give you the flexibility to run specific parts of a playbook by specifying the tags during execution.
- **Use Cases**: Highlight scenarios where tags are beneficial, such as:
  - Running only the tasks related to package installation.
  - Debugging a specific role without running the entire playbook.
  - Performing configuration updates without applying unrelated changes.

### 9.2 Adding Tags to Playbooks
##### Step 1: Create a Simple Playbook
- Start with a simple playbook that installs and configures a web server. Create a new file named `site.yml`:
  ```yaml
  # site.yml
  ---
  - hosts: all
    become: yes

    tasks:
      - name: Install Nginx
        apt:
          name: nginx
          state: present
        tags: install_nginx

      - name: Configure Nginx
        template:
          src: nginx.conf.j2
          dest: /etc/nginx/nginx.conf
        notify:
          - Restart Nginx
        tags: configure_nginx

      - name: Start Nginx
        service:
          name: nginx
          state: started
        tags: start_nginx

    handlers:
      - name: Restart Nginx
        service:
          name: nginx
          state: restarted
        tags: restart_nginx
  ```

##### Step 2: Create the Template for Nginx
- Create a simple Jinja2 template for Nginx configuration:
  ```jinja2
  # nginx.conf.j2
  server {
      listen 80;
      server_name localhost;
      location / {
          root /var/www/html;
          index index.html;
      }
  }
  ```

##### Step 3: Applying Tags in a Playbook
- In this playbook, each task is tagged (`install_nginx`, `configure_nginx`, `start_nginx`, `restart_nginx`). This allows you to control which tasks are executed by specifying tags during the playbook run.

---

### Chapter 10: Running Playbooks with Tags

#### 10.1 Running Specific Tags
- **Overview**: Explain how to execute specific parts of the playbook using the `--tags` option. This is useful for running only the tasks or roles that match a specific tag.

### 10.2 Practical Example: Using Tags in a Playbook
##### Step 1: Run the Playbook with a Specific Tag
- To run only the tasks related to Nginx installation, use the following command:
  ```bash
  ansible-playbook site.yml --tags "install_nginx"
  ```

##### Step 2: Run Multiple Tags
- You can also run multiple tags by separating them with commas:
  ```bash
  ansible-playbook site.yml --tags "install_nginx,configure_nginx"
  ```

##### Step 3: Skip Specific Tags
- The `--skip-tags` option allows you to skip tasks with specific tags. For example, to skip tasks related to starting Nginx:
  ```bash
  ansible-playbook site.yml --skip-tags "start_nginx"
  ```

##### Step 4: Run All Tasks Except Those with a Specific Tag
- If you want to run the entire playbook except for tasks with a specific tag, use the `--skip-tags` option:
  ```bash
  ansible-playbook site.yml --skip-tags "configure_nginx"
  ```

### 10.3 Hands-On Exercise: Applying Tags
- **Exercise**: Extend the playbook to include tasks for installing and configuring a firewall. Apply tags to these tasks and then test the playbook by running only the firewall-related tasks, skipping the web server configuration.

---

### Chapter 11: Advanced Usage of Tags

#### 11.1 Using Tags in Roles
- **Overview**: Explain how tags can be applied to entire roles, making it easier to include or exclude roles during a playbook run.

### 11.2 Practical Example: Tagging Roles and Tasks within Roles

**Scenario**: You have a role named `webserver` that installs and configures Apache, and a role named `dbserver` that sets up MySQL. You want to use tags to selectively run parts of these roles.

##### Step 1: Create the `webserver` Role

1. **Create the Role Structure**:
   - Create the `webserver` role:
     ```bash
     ansible-galaxy init webserver
     cd webserver
     ```

2. **Define Tasks with Tags**:
   - In the `webserver/tasks/main.yml` file, define tasks to install and configure Apache, applying tags to each task:
     ```yaml
     # webserver/tasks/main.yml
     ---
     - name: Install Apache
       apt:
         name: apache2
         state: present
         update_cache: yes
       tags:
         - web
         - install

     - name: Configure Apache
       template:
         src: apache.conf.j2
         dest: /etc/apache2/sites-available/000-default.conf
       notify:
         - Restart Apache
       tags:
         - web
         - configure

     - name: Start Apache service
       service:
         name: apache2
         state: started
       tags:
         - web
         - start
     ```

3. **Create a Simple Template**:
   - Create a basic Jinja2 template for the Apache configuration:
     ```jinja2
     # webserver/templates/apache.conf.j2
     <VirtualHost *:80>
         DocumentRoot /var/www/html
         ErrorLog ${APACHE_LOG_DIR}/error.log
         CustomLog ${APACHE_LOG_DIR}/access.log combined
     </VirtualHost>
     ```

4. **Define a Handler**:
   - Add a handler to restart Apache if the configuration changes:
     ```yaml
     # webserver/handlers/main.yml
     ---
     - name: Restart Apache
       service:
         name: apache2
         state: restarted
       tags:
         - web
         - restart
     ```

---

##### Step 2: Create the `dbserver` Role

1. **Create the Role Structure**:
   - Create the `dbserver` role:
     ```bash
     ansible-galaxy init dbserver
     cd dbserver
     ```

2. **Define Tasks with Tags**:
   - In the `dbserver/tasks/main.yml` file, define tasks to install and configure MySQL, applying tags to each task:
     ```yaml
     # dbserver/tasks/main.yml
     ---
     - name: Install MySQL
       apt:
         name: mysql-server
         state: present
         update_cache: yes
       tags:
         - database
         - install

     - name: Configure MySQL
       copy:
         src: my.cnf
         dest: /etc/mysql/my.cnf
       notify:
         - Restart MySQL
       tags:
         - database
         - configure

     - name: Start MySQL service
       service:
         name: mysql
         state: started
       tags:
         - database
         - start
     ```

3. **Create a MySQL Configuration File**:
   - Add a basic MySQL configuration file:
     ```bash
     echo '[mysqld]
bind-address = 127.0.0.1' > dbserver/files/my.cnf
     ```

4. **Define a Handler**:
   - Add a handler to restart MySQL if the configuration changes:
     ```yaml
     # dbserver/handlers/main.yml
     ---
     - name: Restart MySQL
       service:
         name: mysql
         state: restarted
       tags:
         - database
         - restart
     ```

---

##### Step 3: Create a Playbook with Tagged Roles

1. **Create the Playbook**:
   - Create a playbook that includes both the `webserver` and `dbserver` roles with tags:
     ```yaml
     # site_roles.yml
     ---
     - hosts: all
       become: yes

       roles:
         - role: webserver
           tags: web

         - role: dbserver
           tags: database
     ```

---

##### Step 4: Run the Playbook with Specific Tags

1. **Run Only the Web Server Role**:
   - Execute the playbook, but only run tasks related to the `webserver` role:
     ```bash
     ansible-playbook site_roles.yml --tags "web"
     ```

2. **Run Only Specific Tasks in the Web Server Role**:
   - Run only the tasks tagged as `install` within the `webserver` role:
     ```bash
     ansible-playbook site_roles.yml --tags "install"
     ```

3. **Skip the Database Role**:
   - Execute the playbook and skip all tasks related to the `dbserver` role:
     ```bash
     ansible-playbook site_roles.yml --skip-tags "database"
     ```

