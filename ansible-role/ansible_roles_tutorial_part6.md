
# Part 6: Ansible Galaxy and Community Roles

## Chapter 12: Introduction to Ansible Galaxy

### 12.1 What is Ansible Galaxy?
- **Overview**: Ansible Galaxy is a community hub for finding, sharing, and downloading Ansible roles. It allows you to leverage the work of others and contribute your roles to the community.
- **Key Features**:
  - **Role Discovery**: Search and find roles developed by the community.
  - **Role Installation**: Install roles directly from Galaxy into your projects.
  - **Role Sharing**: Publish your roles to the community.

### 12.2 Setting Up Ansible Galaxy
- **Step 1: Install Ansible Galaxy CLI**
  - Ensure you have Ansible installed, as the Galaxy CLI is included with Ansible.
  - Verify the installation:
    ```bash
    ansible-galaxy --version
    ```

- **Step 2: Configure Ansible Galaxy**
  - You can customize the behavior of the Galaxy CLI by configuring the `ansible.cfg` file:
    ```ini
    [galaxy]
    server_list = ansible_galaxy

    [galaxy_server.ansible_galaxy]
    url=https://galaxy.ansible.com/
    ```

---

## Chapter 13: Finding and Installing Roles

### 13.1 Searching for Roles
- **Step 1: Search for Roles Using the Galaxy CLI**
  - Use the search command to find roles related to a specific technology or service:
    ```bash
    ansible-galaxy search nginx
    ```
  - The output will display a list of roles with their names, authors, and descriptions.

- **Step 2: Search for Roles on the Galaxy Website**
  - Visit [Ansible Galaxy](https://galaxy.ansible.com) and use the search bar to find roles. You can filter by popularity, quality, and other criteria.

### 13.2 Installing Roles
- **Step 1: Install a Role Using the Galaxy CLI**
  - Install a role directly into your project using the CLI:
    ```bash
    ansible-galaxy install geerlingguy.nginx
    ```
  - This command downloads the role into the `roles/` directory of your project.

- **Step 2: Installing Roles via Requirements File**
  - Create a `requirements.yml` file to specify roles to install:
    ```yaml
    # requirements.yml
    - src: geerlingguy.nginx
    - src: git+https://github.com/yourusername/yourrole.git
      version: master
    ```
  - Install all roles listed in the file:
    ```bash
    ansible-galaxy install -r requirements.yml
    ```

---

## Chapter 14: Using Community Roles in Your Playbooks

### 14.1 Incorporating Downloaded Roles
- **Step 1: Add the Role to Your Playbook**
  - Use the downloaded role in your playbook:
    ```yaml
    # site.yml
    ---
    - hosts: all
      become: yes
      roles:
        - geerlingguy.nginx
    ```

- **Step 2: Override Role Variables**
  - Customize the role by overriding its default variables:
    ```yaml
    # site.yml
    ---
    - hosts: all
      become: yes
      roles:
        - role: geerlingguy.nginx
          vars:
            nginx_vhosts:
              - server_name: "example.com"
                root: "/var/www/html"
    ```

### 14.2 Hands-On Exercise: Using a Community Role
- **Exercise**: Search for a role to set up MySQL, install it via the Galaxy CLI, and create a playbook that uses the role. Customize the role by overriding variables to set the MySQL root password and create a database.

---

## Chapter 15: Sharing Your Roles with the Community

### 15.1 Preparing Your Role for Sharing
- **Step 1: Structure and Document Your Role**
  - Ensure your role follows best practices:
    - Use a clear and descriptive name.
    - Include a well-documented `README.md` file.
    - Define default variables in `defaults/main.yml`.
    - Write handlers and tasks with clear names.

- **Step 2: Test Your Role**
  - Before sharing, thoroughly test your role to ensure it works in different environments.

### 15.2 Publishing Roles to Ansible Galaxy
- **Step 1: Create a Galaxy Account**
  - Sign up for an account at [Ansible Galaxy](https://galaxy.ansible.com).

- **Step 2: Link Your GitHub Repository**
  - Connect your Galaxy account to your GitHub account and import your repository. Ensure your repository has a `meta/main.yml` file with metadata about the role.

- **Step 3: Publish the Role**
  - Use the Galaxy CLI to publish your role:
    ```bash
    ansible-galaxy import yourusername yourrole
    ```

- **Step 4: Versioning and Updates**
  - Keep your role updated and versioned. Use semantic versioning to indicate changes.

### 15.3 Hands-On Exercise: Publishing a Role
- **Exercise**: Create a simple role, document it, and publish it to Ansible Galaxy. Once published, verify that others can download and use it.

---

## Chapter 16: Creating a Private Ansible Galaxy Repository

### 16.1 What is a Private Galaxy Repository?
- **Overview**: A private Galaxy repository allows you to host and manage Ansible roles within your organization. This is useful for sharing roles that are specific to your company's infrastructure without exposing them to the public.

### 16.2 Setting Up a Private Galaxy Server
- **Step 1: Deploy a Galaxy Server**
  - Ansible Galaxy can be hosted privately using tools like AWX (the open-source version of Ansible Tower) or custom solutions.
  - You can also use a simple file server or Git repository to host roles. The roles can then be installed using the `ansible-galaxy` command with the `src` parameter pointing to your private server.

- **Step 2: Configure the Private Galaxy Server**
  - Customize your `ansible.cfg` to include the private Galaxy server:
    ```ini
    [galaxy]
    server_list = private_galaxy

    [galaxy_server.private_galaxy]
    url=https://your-private-galaxy-server.com/
    ```

- **Step 3: Install Roles from the Private Repository**
  - Install a role from your private Galaxy server:
    ```bash
    ansible-galaxy install yourcompany.yourrole -s private_galaxy
    ```

### 16.3 Hands-On Exercise: Setting Up a Private Galaxy Repository
- **Exercise**: Set up a private Galaxy server using AWX or a Git repository. Publish a role to the private repository and install it on another machine using the `ansible-galaxy` CLI.

---

## Chapter 17: Pushing Roles to GitHub and Managing `.gitignore`

### 17.1 Pushing Your Ansible Roles to GitHub
- **Step 1: Initialize a Git Repository**
  - Navigate to your role directory and initialize a Git repository:
    ```bash
    git init
    git add .
    git commit -m "Initial commit of my Ansible role"
    ```

- **Step 2: Create a GitHub Repository**
  - Create a new repository on GitHub. You can do this via the GitHub website or the CLI:
    ```bash
    gh repo create yourusername/yourrole --public
    ```

- **Step 3: Push to GitHub**
  - Link your local repository to the GitHub repository and push your changes:
    ```bash
    git remote add origin https://github.com/yourusername/yourrole.git
    git push -u origin master
    ```

### 17.2 Managing `.gitignore` for Ansible Projects
- **Step 1: Create a `.gitignore` File**
  - To avoid pushing unnecessary files to GitHub, create a `.gitignore` file in your project directory:
    ```bash
    touch .gitignore
    ```

- **Step 2: Define Files to Ignore**
  - Add the following typical entries to your `.gitignore` file for an Ansible project:
    ```plaintext
    # Ignore Ansible Galaxy roles
    roles/

    # Ignore temporary files
    *.retry
    *.log
    ```

- **Step 3: Add and Commit `.gitignore`**
  - Add the `.gitignore` file to your repository and commit the changes:
    ```bash
    git add .gitignore
    git commit -m "Add .gitignore to exclude unnecessary files"
    ```

### 17.3 Hands-On Exercise: Managing Git and GitHub for Ansible Roles
- **Exercise**: Create a new role, initialize a Git repository, and push it to GitHub. Ensure that your `.gitignore` file is correctly configured to exclude unnecessary files.
