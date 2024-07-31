# SSL Setup
1. Download docker-compose:


    curl -LO https://dependencytrack.org/docker-compose.yml


2. change the `API_BASE_URL=http://localhost:8081` to `API_BASE_URL=https://dptrack.yourdomain.com` in docker-compose.yml
3. Install nginx on the host server
4. Copy your certificate and private key into these directories:


        /etc/nginx/ssl/nginx.crt;
        /etc/nginx/ssl/nginx.key;


5. Change the nginx config:

   
        #user  nobody;
        worker_processes  1;
    
        #error_log  logs/error.log;
        #error_log  logs/error.log  notice;
        #error_log  logs/error.log  info;
    
        #pid        logs/nginx.pid;
    
    
        events {
        worker_connections  1024;
        }    
    
    
        http {
        include       mime.types;
        default_type  application/octet-stream;
    
        #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
        #                  '$status $body_bytes_sent "$http_referer" '
        #                  '"$http_user_agent" "$http_x_forwarded_for"';
    
        #access_log  logs/access.log  main;
    
        sendfile        on;
        #tcp_nopush     on;
    
        #keepalive_timeout  0;
        keepalive_timeout  65;
    
        #gzip  on;
    
        server {
            listen       443 ssl;
            server_name  dptrack.yourdomain.com;
            ssl_certificate /etc/nginx/ssl/nginx.crt;
            ssl_certificate_key /etc/nginx/ssl/nginx.key;
            ssl_protocols TLSv1.2 TLSv1.3;
    
            #charset koi8-r;
    
            #access_log  logs/host.access.log  main;
    
            location / {
                proxy_pass http://127.0.0.1:8080;
                proxy_ssl_verify off;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
    
            #error_page  404              /404.html;
    
            # redirect server error pages to the static page /50x.html
            #
            error_page   500 502 503 504  /50x.html;
            location = /50x.html {
                root   html;
            }
        }
            server {
                 listen       8443 ssl;
                 server_name  dptrack.yourdomain.ir;
                 ssl_certificate /etc/nginx/ssl/nginx.crt;
                 ssl_certificate_key /etc/nginx/ssl/nginx.key;
                 ssl_protocols TLSv1.2 TLSv1.3;
    
            #charset koi8-r;
    
            #access_log  logs/host.access.log  main;
    
            location / {
                proxy_pass http://127.0.0.1:8081;
                proxy_ssl_verify off;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;

            }
        }
        }

6. Now nginx forwards your requests to backend api and front-end containers.

## API_BASE_URL Note
if you have changed the API_BASE_URL in your docker-compose.yml, and it did not work, you can get shell from the frontend container, and go to `static/config.json` and change the API_BASE_URL.
