SSH Project
This project focuses on understanding and implementing SSH (Secure Shell) for secure remote server access. It involves creating an SSH key pair, configuring SSH to use the key pair for authentication, and connecting to a remote server using the key pair. The project also explores using Puppet for managing SSH configurations.
objectives
Understand what a server is and where servers usually live.
Understand what SSH is and how it works.
Know how to create an SSH RSA key pair.
Know how to connect to a remote host using an SSH RSA key pair.
Understand the advantage of using #!/usr/bin/env bash instead of /bin/bash in Bash scripts.
Tasks
0. Use a Private Key
    Write a Bash script that uses SSH to connect to your server using the private key ~/.ssh/school with the user ubuntu. The script should only use SSH single-character flags and should not handle the case of a private key protected by a passphrase.

1. Create an SSH Key Pair
    Write a Bash script that creates an RSA key pair with the name school, a key size of 4096 bits, and a passphrase betty.

2. Client Configuration File
    Configure your local SSH client to use the private key ~/.ssh/school and refuse to authenticate using a password. Share your SSH client configuration in your answer file.

3. Let Me In!
    Add the provided SSH public key to your server so that you can connect using the ubuntu user.

4. Client Configuration File (w/ Puppet)
    Use Puppet to configure your client SSH configuration file to use the private key ~/.ssh/school and refuse to authenticate using a password.

