# fix bulk request error to 0 error

exec { 'file limit':
  provider => shell,
  onlyif   => 'test -e /etc/default/nginx',
  command  => 'sed -i "5s/[0-9]\+/$( ulimit -n )/" /etc/default/nginx; service nginx restart',
}
