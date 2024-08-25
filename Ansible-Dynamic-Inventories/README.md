### 1.1 Dynamic Inventories

**Objective:** Introduce dynamic inventory scripts to pull in hosts from cloud providers.

**Topics:**

- **Basics of Dynamic Inventories:**
  - Dynamic inventories allow Ansible to query external sources (like cloud providers) to get the list of hosts.
  - Unlike static inventories, dynamic inventories can adjust in real-time to reflect the current state of your infrastructure.
  - We'll explore using the AWS EC2 plugin and creating a custom script for dynamic inventories.

- **Using AWS EC2 Plugin for Dynamic Inventories:**
  - The AWS EC2 plugin allows you to automatically pull instances from your AWS account.
  - **Prerequisites:** AWS CLI configured, IAM user with appropriate permissions, and running EC2 instances.

- **Custom Dynamic Inventory Scripts:**
  - Custom scripts provide flexibility when you need to pull inventory data from non-standard sources, like custom APIs.
  - We'll walk through creating a simple Python script to retrieve inventory data from an API.

**Hands-On Exercises:**

1. **Exercise 1: Setting up Dynamic Inventory with AWS EC2**

**Step 1: Install Required Ansible Collections**

```bash
ansible-galaxy collection install amazon.aws
```

**Step 2: Configure AWS CLI**

```bash
aws configure
```
*Ensure you have your AWS Access Key, Secret Key, and default region set.*

**Step 3: Create the AWS EC2 Inventory File (`aws_ec2.yml`)**

```yaml
plugin: amazon.aws.ec2
regions:
  - us-west-2
filters:
  tag:Name: my-ansible-instance
keyed_groups:
  - key: tags.Name
    prefix: tag
hostnames:
  - tag:Name
```

**Step 4: Write a Playbook to Target the Dynamically Fetched EC2 Instances (`playbook_aws.yml`)**

```yaml
---
- hosts: tag_my-ansible-instance
  tasks:
    - name: Display EC2 Instance Details
      debug:
        var: ansible_facts
```

**Step 5: Run the Playbook**

```bash
ansible-playbook -i aws_ec2.yml playbook_aws.yml
```
*This will dynamically fetch the EC2 instances tagged with "my-ansible-instance" and display their details.*

---

**Exercise 2: Create a Custom Dynamic Inventory Script**

**Step 1: Write a Simple Python Script to Fetch Hosts (`custom_inventory.py`)**

```python
#!/usr/bin/env python

import json
import requests

def get_inventory():
    response = requests.get("https://api.example.com/hosts")
    hosts = response.json()
    inventory = {
        "all": {
            "hosts": [host['hostname'] for host in hosts],
        }
    }
    return inventory

if __name__ == "__main__":
    print(json.dumps(get_inventory()))
```

**Step 2: Make the Script Executable**

```bash
chmod +x custom_inventory.py
```

**Step 3: Integrate the Script with Ansible**

In your `ansible.cfg`, set the `inventory` option to point to `custom_inventory.py`.

```ini
[defaults]
inventory = ./custom_inventory.py
```

**Step 4: Write a Playbook to Use This Custom Inventory (`playbook_custom_inventory.yml`)**

```yaml
---
- hosts: all
  tasks:
    - name: Display Custom Inventory Hosts
      debug:
        msg: "Host {{ inventory_hostname }} is part of the inventory."
```

**Step 5: Run the Playbook**

```bash
ansible-playbook playbook_custom_inventory.yml
```
*This will use the custom inventory script to fetch hosts and display their names.*

---
