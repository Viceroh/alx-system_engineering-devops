MySQL Project: Primary-Replica Setup and Backup
This project focuses on setting up a MySQL primary-replica infrastructure and implementing a robust backup strategy for MySQL databases.

Project Overview
The project involves several key tasks:

Installing MySQL 5.7: MySQL 5.7.x is installed on two servers, web-01 and web-02.
Database Administration: A MySQL user is created for accessing the database, and a database with a table is set up for replication purposes.
Setting Up Replication: A primary-replica setup is configured to ensure data redundancy and load distribution.
Database Backup: A Bash script is written to generate a MySQL dump and compress it into a tar.gz archive for backup purposes.
Tasks
0. Install MySQL
Install MySQL 5.7.x on both web-01 and web-02 servers. Ensure the MySQL version is 5.7.x by running mysql --version.

1. Create MySQL User
Create a MySQL user named holberton_user with the host name set to localhost and the password projectcorrection280hbtn. This user should have permission to check the primary/replica status of your databases.

2. Set Up Database and Table
Create a database named tyrell_corp and a table named nexus6 within it. Add at least one entry to the table. Ensure holberton_user has SELECT permissions on the table.

3. Create Replica User
On the primary MySQL server (web-01), create a new user named replica_user with the host name set to % and assign appropriate permissions for replication.

4. Set Up Primary-Replica Infrastructure
Configure the primary-replica infrastructure using MySQL. The primary must be hosted on web-01, and the replica on web-02. Set up replication for the tyrell_corp database.

5. MySQL Backup
Write a Bash script that generates a MySQL dump of all databases, compresses it into a tar.gz archive, and names the archive according to the format day-month-year.tar.gz.
