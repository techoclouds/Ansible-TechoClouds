# Part 1: Introduction to Ansible Roles

## Chapter 1: What Are Ansible Roles?

### 1.1 Overview of Ansible Roles
- **Definition**: Ansible roles are a way to organize playbooks into reusable components. Roles allow you to break down complex tasks into smaller, manageable pieces, making your playbooks more modular and reusable.
- **Use Cases**: Common scenarios where roles are beneficial include managing configurations across multiple servers or environments.
- **Benefits**:
  - Reusability: Roles can be reused across different playbooks and projects.
  - Organization: They help keep playbooks clean and organized by separating concerns.
  - Collaboration: Roles can be shared among team members or the broader community via Ansible Galaxy.

### 1.2 Basic Structure of a Role
- **Directory Layout**: The standard directory structure of an Ansible role includes:
  - `tasks/`: Contains the main list of tasks to be executed by the role.
  - `handlers/`: Contains handlers that can be used by this role or others.
  - `defaults/`: Default variables for the role.
  - `vars/`: Other variables for the role.
  - `files/`: Contains static files to be used by the role.
  - `templates/`: Contains Jinja2 templates to be used by the role.
  - `meta/`: Defines the role’s metadata, including dependencies.
  - `tests/`: Contains tests for the role (optional).
  - `README.md`: Documentation for the role.

### 1.3 Example Role Structure
- A visual example of a simple role structure:
  ```
  my_role/
  ├── defaults/
  │   └── main.yml
  ├── files/
  ├── handlers/
  │   └── main.yml
  ├── meta/
  │   └── main.yml
  ├── tasks/
  │   └── main.yml
  ├── templates/
  ├── tests/
  │   ├── inventory
  │   └── test.yml
  ├── vars/
  │   └── main.yml
  └── README.md
  ```

---

## Chapter 2: Creating Your First Role

### 2.1 Step-by-Step Guide to Creating a Simple Role

#### Step 1: Set Up the Project Directory
```bash
mkdir ansible-roles-tutorial
cd ansible-roles-tutorial
```

#### Step 2: Create a Basic Role
- Use the `ansible-galaxy init` command to create a new role:
```bash
ansible-galaxy init my_role
```
- This command will generate the basic directory structure for the role.

#### Step 3: Define Tasks for the Role
- Navigate to the `tasks/` directory and open `main.yml` to define tasks:
```bash
cd my_role/tasks
nano main.yml
```
- Add a simple task to install and start Nginx:
```yaml
---
- name: Install Nginx
  apt:
    name: nginx
    state: present
    update_cache: yes

- name: Start Nginx service
  service:
    name: nginx
    state: started
```

### 2.2 Running a Playbook with Your Role

#### Step 4: Create a Playbook to Use the Role
- Go back to the project root and create a new playbook:
```bash
cd ../../
touch site.yml
nano site.yml
```
- Add the following content to `site.yml`:
```yaml
---
- hosts: localhost
  become: yes
  roles:
    - my_role
```

#### Step 5: Run the Playbook
- Execute the playbook to apply the role:
```bash
ansible-playbook site.yml
```

#### Step 6: Verify the Role Execution
- After running the playbook, check if Nginx is installed and running:
```bash
systemctl status nginx
```

### 2.3 Hands-On: Modifying the Role
- **Exercise**: Modify the `my_role` role to include additional tasks, such as configuring the Nginx welcome page by creating a template and copying it to the appropriate directory.

