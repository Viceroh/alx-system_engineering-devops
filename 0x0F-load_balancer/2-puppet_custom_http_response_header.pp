# Add a custom HTTP header with Puppet
exec {'update packages':
    command => 'sudo apt-get update',
    path    => ['/usr/bin', '/bin'],
}
package {'nginx':
    ensure => 'present',
}
exec {'add X-Served-By header':
    command => 'sed -i "/listen \[::\]:80 default_server/a add_header X-Served-By \"$(hostname)\";" /etc/nginx/sites-available/default',
    path    => ['/bin', '/usr/bin'],
    require => Package['nginx'],
}
exec {'restart nginx' :
    command => 'sudo service nginx restart',
    path    => ['/usr/sbin', '/usr/bin'],
}
