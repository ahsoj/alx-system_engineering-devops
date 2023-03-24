# Using Puppet, install flask from pip3.

exec { 'flask':
    command => 'pip3 install -Iv flask==2.1.0',
}
