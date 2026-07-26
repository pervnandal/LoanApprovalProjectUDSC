(.venv) C:\Monal\Work\AllLight\Krish-sir\KNB2-DataScience\Practical-live\level-5\25-07-2026>docker build -t loan-approval-app .
[+] Building 131.0s (11/11) FINISHED                                                   docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                   0.0s
 => => transferring dockerfile: 401B                                                                   0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                    3.2s
 => [internal] load .dockerignore                                                                      0.0s
 => => transferring context: 164B                                                                      0.0s
 => [1/6] FROM docker.io/library/python:3.11-slim@sha256:db3ff2e1800a8581e2c48a27c3995339d47bdf046da2  0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:db3ff2e1800a8581e2c48a27c3995339d47bdf046da2  0.0s
 => [internal] load build context                                                                      0.5s
 => => transferring context: 8.39MB                                                                    0.4s
 => CACHED [2/6] WORKDIR /app                                                                          0.0s
 => [3/6] COPY requirements.txt .                                                                      0.0s
 => [4/6] RUN pip install     --no-cache-dir     -r requirements.txt                                 106.2s
 => [5/6] COPY . .                                                                                     0.2s 
 => [6/6] RUN chmod +x start.sh                                                                        0.2s 
 => exporting to image                                                                                20.4s 
 => => exporting layers                                                                               15.4s 
 => => exporting manifest sha256:8f90bcfad2f83fd1a15474957fa4fedfeffdfaf6510b48163afee54d787edc8c      0.0s 
 => => exporting config sha256:64d6c6bfc470f33937871c96d1fedc7f9299de3ee490a38759b29966636290c6        0.0s 
 => => exporting attestation manifest sha256:2a9a278dd87abe7ffeaa1dfb8115dffe5b8ec60642c68c6bf4b1e181  0.0s
 => => exporting manifest list sha256:3599ad4e8cd74290ef7ec6bda715e8636d58196e2e1f2db5aaa7afff20076f4  0.0s
 => => naming to docker.io/library/loan-approval-app:latest                                            0.0s
 => => unpacking to docker.io/library/loan-approval-app:latest                                         4.9s