# Dictionary Web App

## Install Dependencies

```bash
#Install nodejs
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -
sudo apt-get install nodejs
## Verify node installation
node -v

#Install Mongodb

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 4B7C549A058F8B6B
## Ubuntu 18.04:
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb.list
## Ubuntu 16.04
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb.list
## Install mongo
sudo apt update
sudo apt install mongodb-org
sudo systemctl enable mongod
sudo systemctl start mongod
``` 
## Install backend:
```bash
unzip backend.zip
rm -r node_modules
npm install
sudo npm install -g nodemon

# Start backend
nodemon server 
```

## Install Web Server
```bash
unzip dictionary-app.zip
npm install
ng serve --host 0.0.0.0 --port 4200
```

## Install Database

```bash
mongoimport --db nextDICT --collection en_nextDICT --mode=merge --file <json_file>
```
