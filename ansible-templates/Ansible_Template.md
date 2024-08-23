# Chapter: Ansible Templates

## 1. Introduction to Templates
- **Overview**: Explain what templates are and why they are useful in Ansible. Templates allow you to generate configuration files dynamically based on variables, making your deployments flexible and customizable.
- **Jinja2**: Ansible uses Jinja2 templating language to allow variable substitution, conditionals, and loops within your templates.

## 2. Setup and Configuration
- **Step 1: Create a Directory for the Tutorial**
    ```bash
    mkdir ansible-templates-tutorial
    cd ansible-templates-tutorial
    ```

- **Step 2: Create an `ansible.cfg` File**
    - This file will configure Ansible to use the local inventory file and disable host key checking.
    ```bash
    touch ansible.cfg
    ```
    - Add the following content to `ansible.cfg`:
    ```ini
    [defaults]
    inventory = hosts
    host_key_checking = False
    ```

- **Step 3: Create a `hosts` File**
    - This file will define the inventory, using `localhost` for testing.
    ```bash
    touch hosts
    ```
    - Add the following content to `hosts`:
    ```ini
    [default]
    localhost ansible_connection=local
    ```

## 3. Basic Template Usage
- **Step 4: Create a Simple Template**
    - Create a directory for your templates and then create a basic template file.
    ```bash
    mkdir templates
    touch templates/my_template.j2
    ```

    - Add the following content to `my_template.j2`:
    ```jinja2
    server_name {{ server_name }};
    listen {{ listen_port }};
    ```

- **Step 5: Create a Playbook to Use the Template**
    - Create a playbook that uses the `template` module to generate a configuration file from the template.
    ```bash
    touch apply_template.yml
    ```

    - Add the following content to `apply_template.yml`:
    ```yaml
    - hosts: default
      vars:
        server_name: localhost
        listen_port: 8080
      tasks:
        - name: Apply Nginx template
          template:
            src: templates/my_template.j2
            dest: /tmp/nginx.conf
    ```

- **Step 6: Run the Playbook**
    - Execute the playbook to generate the configuration file.
    ```bash
    ansible-playbook apply_template.yml
    ```

- **Step 7: Verify the Output**
    - Check the generated configuration file to ensure it was created as expected.
    ```bash
    cat /tmp/nginx.conf
    ```
    - You should see the following output:
    ```bash
    server_name localhost;
    listen 8080;
    ```

## 4. Advanced Template Features
- **Step 8: Add Conditionals in the Template**
    - Update your template to include conditionals.
    ```bash
    nano templates/my_template.j2
    ```

    - Modify it as follows:
    ```jinja2
    server_name {{ server_name }};
    listen {{ listen_port }};
    
    {% if ssl_enabled %}
    listen 443 ssl;
    ssl_certificate {{ ssl_cert }};
    ssl_certificate_key {{ ssl_key }};
    {% endif %}
    ```

- **Step 9: Update the Playbook with Conditional Variables**
    - Modify the playbook to include SSL-related variables.
    ```bash
    nano apply_template.yml
    ```

    - Update the variables in the playbook:
    ```yaml
    - hosts: default
      vars:
        server_name: localhost
        listen_port: 8080
        ssl_enabled: true
        ssl_cert: /etc/ssl/certs/ssl-cert-snakeoil.pem
        ssl_key: /etc/ssl/private/ssl-cert-snakeoil.key
      tasks:
        - name: Apply Nginx template
          template:
            src: templates/my_template.j2
            dest: /tmp/nginx.conf
    ```

- **Step 10: Run the Playbook Again**
    - Execute the playbook to regenerate the configuration file with SSL enabled.
    ```bash
    ansible-playbook apply_template.yml
    ```

    - Verify the output:
    ```bash
    cat /tmp/nginx.conf
    ```
    - You should see the following output:
    ```bash
    server_name localhost;
    listen 8080;
    listen 443 ssl;
    ssl_certificate /etc/ssl/certs/ssl-cert-snakeoil.pem;
    ssl_certificate_key /etc/ssl/private/ssl-cert-snakeoil.key;
    ```

- **Step 11: Add Loops in the Template**
    - Modify your template to include a loop for multiple backend servers.
    ```bash
    nano templates/my_template.j2
    ```

    - Update it as follows:
    ```jinja2
    upstream backend {
    {% for server in backend_servers %}
      server {{ server }};
    {% endfor %}
    }
    server_name {{ server_name }};
    listen {{ listen_port }};
    ```

- **Step 12: Update the Playbook with a List of Servers**
    - Modify the playbook to include a list of backend servers.
    ```bash
    nano apply_template.yml
    ```

    - Update the variables:
    ```yaml
    - hosts: default
      vars:
        server_name: localhost
        listen_port: 8080
        backend_servers:
          - 192.168.1.1
          - 192.168.1.2
          - 192.168.1.3
      tasks:
        - name: Apply Nginx template
          template:
            src: templates/my_template.j2
            dest: /tmp/nginx.conf
    ```

- **Step 13: Run the Playbook Again**
    - Execute the playbook to generate a configuration file with a backend server list.
    ```bash
    ansible-playbook apply_template.yml
    ```

    - Verify the output:
    ```bash
    cat /tmp/nginx.conf
    ```
    - You should see the following output:
    ```bash
    upstream backend {
      server 192.168.1.1;
      server 192.168.1.2;
      server 192.168.1.3;
    }
    server_name localhost;
    listen 8080;
    ```

## 5. Real-World Example: Nginx Configuration
- **Scenario**: Generate an Nginx configuration file using a template for a real-world scenario.
- **Step 14: Create the Template for Nginx Config**
    - Create a more complex template for Nginx configuration.
    ```bash
    nano templates/nginx_template.j2
    ```

    - Example content:
    ```jinja2
    upstream backend {
    {% for server in backend_servers %}
      server {{ server }};
    {% endfor %}
    }

    server {
        listen {{ listen_port }};
        server_name {{ server_name }};

        location / {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }

        {% if ssl_enabled %}
        listen 443 ssl;
        ssl_certificate {{ ssl_cert }};
        ssl_certificate_key {{ ssl_key }};
        {% endif %}
    }
    ```

- **Step 15: Update the Playbook for the Nginx Config**
    - Modify your playbook to use the new Nginx template.
    ```bash
    nano apply_template.yml
    ```

    - Example content:
    ```yaml
    - hosts: default
      vars:
        server_name: localhost
        listen_port: 8080
        ssl_enabled: false
        backend_servers:
          - 192.168.1.1
          - 192.168.1.2
          - 192.168.1.3
      tasks:
        - name: Apply Nginx configuration
          template:
            src: templates/nginx_template.j2
            dest: /tmp/nginx.conf
    ```

- **Step 16: Run the Playbook to Deploy Nginx Configuration**
    - Execute the playbook and review the generated Nginx configuration file.
    ```bash
    ansible-playbook apply_template.yml
    ```

    - Verify the output:
    ```bash
    cat /tmp/nginx.conf
    ```

## 6. Error Handling and Debugging
- **Step 17: Debugging Template Issues**
    - Use the `debug` module to print variables or inspect issues in your playbooks.

    - Example:
    ```yaml
    - name: Debug template variables
      debug:
        var: backend_servers
    ```

- **Step 18: Handle Common Errors**
    - Identify and resolve common issues related to missing variables, syntax errors in templates, etc.

## 7. Best Practices
- **Step 19: Organize Templates Efficiently**
    - Tips on how to organize your templates, such as grouping by service or project.

- **Step 20: Create Reusable Templates**
    - Create templates that can be reused across multiple playbooks by making them generic and parameterized.

## 8. Hands-On Exercise
- **Exercise**: Create a custom Apache configuration template and deploy it across multiple servers.

