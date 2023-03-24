#Using Puppet, install flask from pip3.

exec { 'flask installation':
    command => 'pip3 install -Iv flask==2.1.0',
    path => '/usr/bin/',
}
