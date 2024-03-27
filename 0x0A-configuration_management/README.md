Configuration Management with Puppet
This repository contains Puppet manifests for various tasks related to configuration management. These tasks include creating files, installing packages, and executing commands.

Project Structure
0x0A-configuration_management/
0-create_a_file.pp: Puppet manifest to create a file in /tmp.
1-install_a_package.pp: Puppet manifest to install the Flask package.
2-execute_a_command.pp: Puppet manifest to execute a command to kill a process.
Installation
To use these Puppet manifests, ensure you have Puppet and puppet-lint installed on your Ubuntu 20.04 LTS system. If not installed, follow the instructions below:

Installing Puppet
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades $ apt-get install -y ruby-augeas $ apt-get install -y ruby-shadow $ apt-get install -y puppet

Installing puppet-lint
$ gem install puppet-lint
