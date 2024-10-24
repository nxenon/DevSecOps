Steps to use HTTPS:
1. Update [docker-compose.override.https.yml](#docker-composeoverridehttpsyml)
2. Update [nginx_TLS.conf](#nginxtlsconf)
3. Copy your certificate and private key in django-DefectDojo/nginx/ssl directory
4. Add **volumes** for cert and private key in [docker-compose.yml](#docker-composeyml)
5. Add **TRUSTED** in [nginx.crt](#nginxcrt)
   1. `-----BEGIN CERTIFICATE-----` --> `-----BEGIN TRUSTED CERTIFICATE-----`
   2. `-----END CERTIFICATE-----` --> `-----END TRUSTED CERTIFICATE-----`

## docker-compose.override.https.yml

    ---
    services:
      nginx:
        environment:
          USE_TLS: 'true'
          GENERATE_TLS_CERTIFICATE: 'false'
        ports:
          - target: 443
            published: ${DD_TLS_PORT:-443}
            protocol: tcp
            mode: host
      uwsgi:
        environment:
          DD_SESSION_COOKIE_SECURE: 'True'
          DD_CSRF_COOKIE_SECURE: 'True'


## nginx_TLS.conf

    worker_processes 1;
    error_log /var/log/nginx/error.log warn;
    pid /var/run/defectdojo/nginx.pid;
    events {
        worker_connections    32;
    }
    
    http {
      include /etc/nginx/mime.types;
      default_type application/octet-stream;
      log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';
      access_log /var/log/nginx/access.log main;
      client_max_body_size 800m;
      sendfile on;
      keepalive_timeout 65;
      upstream uwsgi_server {
        include /run/defectdojo/uwsgi_server;
      }
      server {
          listen 80;
          location / {
              return 301 https://$host:443$request_uri;
          }
      }
      # Disable metrics auth for localhost (for nginx prometheus exporter)
      geo $metrics_auth_bypass {
        127.0.0.1/32 "off";
        default "Metrics";
      }
      server {
        server_tokens off;
        listen 443 ssl;
        server_name defectdojo.domain.com;
        ssl_certificate /etc/nginx/ssl/nginx.crt;
        ssl_certificate_key /etc/nginx/ssl/nginx.key;
        ssl_session_cache builtin:1000 shared:SSL:10m;
        # ciphers from https://ssl-config.mozilla.org/#server=nginx&version=1.17.7&config=intermediate&openssl=1.1.1d&guideline=5.4
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256;
        ssl_prefer_server_ciphers off;
    
        gzip on;
        gzip_types      application/atom+xml  application/geo+json  application/javascript  application/x-javascript  application/json  application/ld+json  application/manifest+json  application/rdf+xml  application/rss+xml  application/xhtml+xml  application/xml  font/eot  font/otf  font/ttf  image/svg+xml  text/css  text/javascript text/plain  text/xml;
        gzip_proxied    any;
        gzip_min_length 1000;
    
        location = /50x.html {
            root                    /usr/share/nginx/html;
        }
        location /static/ {
          alias /usr/share/nginx/html/static/;
        }
        location / {
          include /run/defectdojo/uwsgi_pass;
          include /etc/nginx/wsgi_params;
          uwsgi_read_timeout 1800;
    
          # an HTTP header important enough to have its own Wikipedia entry:
          #   http://en.wikipedia.org/wiki/X-Forwarded-For
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    
          # enable this if and only if you use HTTPS, this helps to
          # set the proper protocol for doing redirects:
          proxy_set_header X-Forwarded-Proto $scheme;
    
          # pass the Host: header from the client right along so redirects
          # can be set properly within the Rack application
          proxy_set_header Host $host;
    
          # we don't want nginx trying to do something clever with
          # redirects, we set the Host: header above already.
          proxy_redirect off;
        }
        location /django_metrics {
          # do no edit the following lines, instead set the environment
          # variables METRICS_HTTP_AUTH_USER and METRICS_HTTP_AUTH_PASSWORD
          #auth_basic $metrics_auth_bypass;
          #auth_basic_user_file /etc/nginx/.htpasswd;
          include /run/defectdojo/uwsgi_pass;
          include /etc/nginx/wsgi_params;
          uwsgi_read_timeout 1800;
    
          # an HTTP header important enough to have its own Wikipedia entry:
          #   http://en.wikipedia.org/wiki/X-Forwarded-For
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    
          # enable this if and only if you use HTTPS, this helps to
          # set the proper protocol for doing redirects:
          proxy_set_header X-Forwarded-Proto $scheme;
    
          # pass the Host: header from the client right along so redirects
          # can be set properly within the Rack application
          proxy_set_header Host $host;
    
          # we don't want nginx trying to do something clever with
          # redirects, we set the Host: header above already.
          proxy_redirect off;
        }
        location /nginx_status {
          # do no edit the following lines, instead set the environment
          # variables METRICS_HTTP_AUTH_USER and METRICS_HTTP_AUTH_PASSWORD
          #auth_basic $metrics_auth_bypass;
          #auth_basic_user_file /etc/nginx/.htpasswd;
          #stub_status  on;
          access_log   off;
    
          # an HTTP header important enough to have its own Wikipedia entry:
          #   http://en.wikipedia.org/wiki/X-Forwarded-For
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    
          # enable this if and only if you use HTTPS, this helps to
          # set the proper protocol for doing redirects:
          proxy_set_header X-Forwarded-Proto $scheme;
    
          # pass the Host: header from the client right along so redirects
          # can be set properly within the Rack application
          proxy_set_header Host $host;
    
          # we don't want nginx trying to do something clever with
          # redirects, we set the Host: header above already.
          proxy_redirect off;
        }
        # Used by Kubernetes liveness and readiness checks
        location = /nginx_health {
          return 200 "Born to be alive!\n";
          access_log off;
        }
        location = /uwsgi_health {
          limit_except GET { deny all; }
          rewrite /.+ /login?force_login_form&next=/ break;
          include /run/defectdojo/uwsgi_pass;
          include /etc/nginx/wsgi_params;
          access_log off;
        }
        error_page 500 502 503 504 /50x.html;
      }
    }

## docker-compose.yml

    ---
    services:
      nginx:
        build:
          context: ./
          dockerfile: "Dockerfile.nginx-${DEFECT_DOJO_OS:-debian}"
        image: "defectdojo/defectdojo-nginx:${NGINX_VERSION:-latest}"
        profiles:
          - mysql-rabbitmq
          - mysql-redis
          - postgres-rabbitmq
          - postgres-redis
        depends_on:
          - uwsgi
        environment:
          NGINX_METRICS_ENABLED: "${NGINX_METRICS_ENABLED:-false}"
        volumes:
          - defectdojo_media:/usr/share/nginx/html/media
          - /home/USER/django-DefectDojo/nginx/ssl:/etc/nginx/ssl
          - /home/USER/django-DefectDojo/nginx/ssl:/etc/nginx/ssl
          ...

## nginx.crt

    -----BEGIN TRUSTED CERTIFICATE-----
    ...
    -----END TRUSTED CERTIFICATE-----
