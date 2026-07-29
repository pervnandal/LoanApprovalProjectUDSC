### Connect with .pem file
```
ssh -i loan-app-key.pem ubuntu@YOUR_PUBLIC_IP
```

### Small exercises

- Exercise-1
```
pwd
```

- Exercise-1
```
ls
```

- Exercise-1
```
ls -a
```

- Exercise-1
```
cat /etc/os-release
```

### Install Docker 

1. Step 1
```
sudo apt install \
ca-certificates \
curl \
gnupg \
lsb-release \
-y
```

2. Step 2
```
sudo install -m 0755 -d /etc/apt/keyrings
```

3. Step 3
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

4. Step 4
```
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

5. Step 5
```
sudo apt update
```

6. Step 6
```
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

6. Step 7 (Expecting error)
```
docker ps
```

6. Step 8
```
sudo usermod -aG docker ubuntu
```

6. Step 9
```
docker ps
```

### Clone the repo and Run Container

1. Step-1
```
cd ~

git clone https://github.com/Monalsingh/loan-approval-ml-UDS2-live.git

cd loan-approval
```

2. Step-2
```
docker build -t loan-approval:v1 .
```

3. Step-3
```
docker run -d \
--name loan-app \
-p 8000:8000 \
-p 8501:8501 \
--restart unless-stopped \
loan-approval:v1
```

4. Step-4
```
docker ps -a
```

5. Step-5
```
docker logs loan-app

or 

docker logs -f <Container-ID>
```

### Test running container

```
curl http://localhost:8000/docs

curl http://localhost:8501
```
