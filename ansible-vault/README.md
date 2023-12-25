# Ansible Vault Tutorial 
#####  This tutorial demonstrates the use of Ansible Vault for securely managing sensitive data within Ansible playbooks.

## Purpose
Ansible Vault provides a way to encrypt sensitive information, such as passwords or API keys, within Ansible playbooks. This ensures that confidential data remains secure, even when stored in version control or shared among team members.

## Steps

#### Encrypt Sensitive Data:

```ansible-vault encrypt password.yaml```
Sets a vault password to encrypt password.yaml.
Stores sensitive variables like passwords, API keys, etc.
#### Execute the Playbook:

```ansible-playbook playbook.yaml --ask-vault-pass```
Prompts for the vault password to decrypt password.yaml during execution.
Utilizes decrypted variables within the playbook.
## Sample Code

password.yaml:

```
---
password: SecurePASS
```
playbook.yaml
```
---
- name: Playbook using Vault
  hosts: all
  tasks:
    - name: Include Vaulted Variables
      include_vars:
        file: password.yaml
    - name: Print Password
      debug:
        var: password
```
[![asciicast](https://asciinema.org/a/628772.svg)](https://asciinema.org/a/628772)


#### Decrypt Sensitive Data:
Decrypt Encrypted Data
To decrypt encrypted data using Ansible Vault:
```
ansible-vault decrypt password.yaml
```
This command decrypts the password.yaml file, making its contents readable. You'll be prompted to enter the vault password used during encryption.



## Additional Information

Vault Best Practices:
Securely store vault passwords (password files, integration with password managers).
Avoid plaintext storage or sharing.
Managing Multiple Vaults:
Use multiple vaults or passwords for different access levels and security in large projects.
Refer to the Ansible Vault documentation: https://docs.ansible.com/ansible/latest/user_guide/vault.html
## Further Insights

Alternative Vault Password Handling:
Use `ansible-playbook playbook.yaml --vault-password-file=vault_password.txt` for password files.

