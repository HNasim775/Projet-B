#!/bin/bash

# Donner les permissions d'exécution au script

chmod +x "$0"

sudo apt-get update -y
sudo mkdir /etc/nginx/ssl

mkdir /etc/nginx/ssl

# Installation des packages nécessaires pour SSL
sudo apt-get install openssl libssl-dev -y

# Installation de Nginx
sudo apt-get install nginx -y

# Téléchargement et installation de OpenSSL
sudo wget https://www.openssl.org/source/openssl-1.1.1k.tar.gz
sudo tar -xzvf openssl-1.1.1k.tar.gz
cd openssl-1.1.1k
sudo ./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib no-shared zlib-dynamic
make
sudo make install

# Export du chemin de la bibliothèque
echo 'export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64' | sudo tee /etc/profile.d/openssl.sh
source /etc/profile.d/openssl.sh

# Création des clés SSL
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt \
 -subj "/C=France/ST=Rhône/L=Lyon/O=ITSGroupLyon/OU=DevOps/CN=Lyon3/EmailAdresse=DevOpsPoject@gmail.com"

sudo chmod 600 /etc/ssl/private/nginx-selfsigned.key
sudo chmod 644 /etc/ssl/certs/nginx-selfsigned.crt

sudo ls -l /etc/ssl/private/nginx-selfsigned.key
sudo ls -l /etc/ssl/certs/nginx-selfsigned.crt

# Création du fichier de configuration SSL
sudo tee /etc/nginx/conf.d/ssl.conf > /dev/null <<EOF
server {
    listen 443 http2 ssl;
    server_name nginx;

    ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
    ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
    ssl_dhparam /etc/ssl/certs/dhparam.pem;
}

server {
    listen 80;
    server_name nginx;
    return 301 https://\$host\$request_uri;
}
EOF

# Renforcement de la clé avec Diffie-Hellman
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048

# Configuration du load balancer
sudo tee /etc/nginx/conf.d/load_balancer.conf > /dev/null <<EOF
upstream backend {
    server localhost:5000;
}

server {
    listen 80;

    location / {
        proxy_redirect off;
        proxy_pass http://localhost:5000;
    }
}
EOF

# Redémarrage de Nginx
sudo systemctl restart nginx

# Vérification de l'état de Nginx apès son installation
if sudo systemctl is-active nginx >/dev/null; then
    echo "Nginx est installé et en cours d'exécution."
else
    echo "L'installation de Nginx a échoué ou n'est pas en cours d'exécution."
    systemctl status nginx.service
    journalctl -xeu nginx.service
fi

sudo nginx -t
sudo systemctl restart nginx
