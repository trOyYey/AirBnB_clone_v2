#!/usr/bin/env bash
# static deployment for webservers

apt-get -y update
apt-get -y install nginx
#creating folder if it doesn't exist
mkdir -p /data/web_static /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

#echoing test text inside index.html
echo "<h1>hello spody</h1>" > /data/web_static/releases/test/index.html

#creating symbolic link between test and current
ln -sf /data/web_static/releases/test/ /data/web_static/current

name=$(hostname)
echo "Hello World!" | sudo tee /var/www/html/index.html
echo "Ceci n'est pas une page" | sudo tee /var/www/html/error_404.html

#owner previlages
chown -R ubuntu:ubuntu /data

echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

	add_header X-Served-By $name always;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;
        server_name troy-yey.tech;
	error_page 404 /error_404.html;

	location = /error_404.html {
		root /var/www/html;
		internal;
	}
	location /hbnb_static/ {
	alias /data/web_static/current/;
	}

	location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
}" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
