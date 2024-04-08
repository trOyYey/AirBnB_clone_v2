# puppet to script to update install start create and test server

exec {'update apt':
  provider => shell,
  command  => 'sudo apt-get update',
}

-> exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
}

-> exec {'start nginx':
  provider => shell,
  command  => 'sudo service nginx start',
}

-> exec {'create folders':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
}

-> exec {'create release':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
}

-> exec {'add test content':
  provider => shell,
  command  => 'echo "<h1>hello spody<h1>" > /data/web_static/releases/test/index.html',
}

-> exec {'symbolic link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
}

-> file {'ownership for data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

-> exec {'add current path':
  provider => shell,
  command  => 'sed -i "61i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default',
}

-> exec {'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
