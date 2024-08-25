
# Custom Lookup Plugins - AWS Example

## Objective:

Learn how to create custom lookup plugins in Ansible to fetch external data dynamically, enhancing the flexibility and power of your automation tasks.

## Topics:

### 1. Introduction to Custom Lookup Plugins:
- **What are Custom Lookup Plugins?**
    - Custom lookup plugins allow you to define custom logic or data sources that can be queried during playbook execution.
    - They are written in Python and are useful when built-in plugins don't meet your specific needs.
- **When to Use Custom Lookup Plugins:**
    - Use custom lookup plugins when you need to fetch data from a non-standard source, transform data in a specific way, or encapsulate complex logic that should be reusable across multiple playbooks.
- **AWS Integration:**
    - Custom lookup plugins can be used to interact with AWS services, such as retrieving information about EC2 instances, S3 buckets, or other AWS resources.

### 2. Writing a Custom Lookup Plugin to Retrieve AWS EC2 Instances:
- **Directory Structure:**
    - Custom lookup plugins must be placed in a directory named `lookup_plugins` within your playbook or role directory.
    - Example: `your_playbook/lookup_plugins/aws_ec2_lookup.py`
- **Plugin Structure:**
    - A custom lookup plugin is a Python class that inherits from `LookupBase` and implements a `run` method.
    - The `run` method interacts with AWS using the `boto3` library to retrieve data.
- **Example Plugin:**
    - A simple plugin that retrieves a list of EC2 instances in a specified region.

### 3. Using the Custom AWS Plugin in a Playbook:
- **Syntax for Using Custom Lookup Plugins:**
    - The custom lookup plugin is invoked using the `lookup` keyword in a playbook, just like built-in plugins.
    - Example: `{{ lookup('aws_ec2_lookup', 'us-west-2') }}`
- **Integration in Playbooks:**
    - Demonstrate how to use the custom plugin to dynamically retrieve and use AWS data during playbook execution.

## Hands-On Exercises:

### Exercise 1: Develop a Custom Lookup Plugin that Retrieves AWS EC2 Instances

**Step 1: Create the Directory Structure for the Plugin**

    ```bash
    mkdir -p lookup_plugins
    ```

**Step 2: Write the Custom Lookup Plugin (`lookup_plugins/aws_ec2_lookup.py`)**

    ```python
    from ansible.plugins.lookup import LookupBase
    import boto3

    class LookupModule(LookupBase):

        def run(self, terms, variables=None, **kwargs):
            region = terms[0]  # AWS region is the first term
            ec2 = boto3.client('ec2', region_name=region)

            # Retrieve the list of instances
            response = ec2.describe_instances()
            instances = []
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    instances.append(instance['InstanceId'])

            return instances
    ```

**Explanation**:
- **boto3**: The AWS SDK for Python, used to interact with AWS services.
- **describe_instances**: A method that retrieves details about EC2 instances in the specified region.
- **instances list**: The plugin returns a list of EC2 instance IDs in the specified region.

**Step 3: Write a Playbook to Use the Custom AWS Plugin (`playbook_aws_ec2_lookup.yml`)**

    ```yaml
    ---
    - hosts: localhost
      tasks:
        - name: Retrieve and display EC2 instances in us-west-2
          debug:
            msg: "{{ lookup('aws_ec2_lookup', 'us-west-2') }}"
    ```

**Explanation**:
- **lookup**: The playbook uses the custom lookup plugin `aws_ec2_lookup` to retrieve and display the list of EC2 instance IDs in the `us-west-2` region.

**Step 4: Run the Playbook**

    ```bash
    ansible-playbook playbook_aws_ec2_lookup.yml
    ```

**Outcome**:
- The playbook will use the custom lookup plugin to fetch the list of EC2 instances in the `us-west-2` region and print their instance IDs.

### Advanced Exercise: Extending the Plugin to Filter Instances by State

**Step 1: Extend the Plugin to Accept Filters**

    ```python
    from ansible.plugins.lookup import LookupBase
    import boto3

    class LookupModule(LookupBase):

        def run(self, terms, variables=None, **kwargs):
            region = terms[0]
            instance_state = kwargs.get('state', 'running')  # Default state is 'running'
            ec2 = boto3.client('ec2', region_name=region)

            response = ec2.describe_instances(
                Filters=[{'Name': 'instance-state-name', 'Values': [instance_state]}]
            )
            instances = []
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    instances.append(instance['InstanceId'])

            return instances
    ```

**Explanation**:
- **state filter**: This extended version allows you to filter instances by their state (e.g., running, stopped).

**Step 2: Write a Playbook to Use the Extended Plugin with a Filter**

    ```yaml
    ---
    - hosts: localhost
      tasks:
        - name: Retrieve and display running EC2 instances in us-west-2
          debug:
            msg: "{{ lookup('aws_ec2_lookup', 'us-west-2', state='running') }}"
    ```

**Outcome**:
- The playbook will retrieve and display only the running EC2 instances in the `us-west-2` region.

