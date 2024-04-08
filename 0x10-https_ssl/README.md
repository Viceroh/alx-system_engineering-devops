HTTPS SSL Project
This repository contains the project files for the HTTPS SSL course, part of the System Engineering Foundations curriculum at Holberton School. The project focuses on securing web traffic using HTTPS and SSL, with a particular emphasis on configuring HAProxy for SSL termination and enforcing HTTPS traffic.

Project Overview
The project is divided into three main tasks:

World Wide Web: Configure domain zones and subdomains, and write a Bash script to display information about subdomains.
HAProxy SSL Termination: Create a certificate using Certbot and configure HAProxy to accept encrypted traffic for the www subdomain.
No Loophole in Website Traffic: Configure HAProxy to automatically redirect HTTP traffic to HTTPS.
Configuration
Domain Configuration: Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Add other subdomains as needed.
HAProxy Configuration: Configure HAProxy for SSL termination and HTTP to HTTPS redirection. Refer to the provided configuration files (1-haproxy_ssl_termination and 100-redirect_http_to_https) for examples.
