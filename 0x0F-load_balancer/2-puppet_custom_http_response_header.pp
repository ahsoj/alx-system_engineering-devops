# Automation: creates a custom HTTP header response with Puppet.
exec { 'command':
  command  => 'sudo apt -y update;
  sudo apt -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}
