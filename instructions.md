1. python -m venv .venv
# uv venv --python 3.14.3

2. Activate
```
Macos / linux : source .venv/bin/activate
Windows : .venv\Scripts\activate.bat
```

3. python -m pip install -r requirements.txt

4. pip freeze > req.txt

5. Create model + eval + Classloader + api + streamlit+app

6. Dockerfile

7. Create Image 
```
"docker images" : shows docker images
"docker ps -a" : to show container status
"docker build -t loan-approval-app ." : to build docker image

"docker run -d -p 8501:8501 -p 8000:8000 loan-approval-app" : -d -> background (optional)

"docker rmi <image-id>"
"docker rmi 335ac43a1699"

"docker rm <container-id>"

"docker stop <container-id>"

"docker logs -f <container-id>"
```

8. Test Docker container locally