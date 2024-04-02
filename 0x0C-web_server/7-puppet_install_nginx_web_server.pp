# Install Nginx web server
exec {'update packages':
    command => ' sudo apt-get update',
    path    => ['/usr/bin', '/bin'],
}
package {'nginx':
    ensure => 'present',
}
exec {'fire wall' :
    command => 'sudo ufw allow \'Nginx HTTP\'',
    path    => ['/usr/sbin', '/usr/bin'],
}
file {'/var/www/html/index.nginx-debian.html' :
    ensure  => 'present',
    content => 'Hello World!',
}
file {'/etc/nginx/sites-available/default':
    ensure  => 'present',
    content => @(EOT)
        server {
            listen 80 default_server;
            listen [::]:80 default_server;
            root /var/www/html;
            server_name _;

            location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
            }

            location / {
                index index.html index.nginx-debian.html;
            }
        }
    EOT
}
exec {'restart nginx' :
    command => 'sudo service nginx restart',
    path    => ['/usr/sbin', '/usr/bin'],
}
