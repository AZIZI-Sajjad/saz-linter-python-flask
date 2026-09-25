#!/bin/bash
sudo apt update
sudo apt install -y docker.io

curl -L -o /home/ubuntu/docker-compose.yml https://raw.githubusercontent.com/Loise/linter-python-flask/refs/heads/main/docker-compose.yml

DOCKER_CONFIG=/home/ubuntu/.docker
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.39.4/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose

chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
sudo usermod -aG docker ubuntu
newgrp docker

git init 
git pull https://github.com/docker/awesome-compose.git
cd react-express-mysql

sudo -u ubuntu docker compose -f /home/ubuntu/docker-compose.yml up -d
