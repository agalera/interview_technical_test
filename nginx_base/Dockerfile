FROM nginx:latest
MAINTAINER Alberto Galera "agalera@globalstudio.es"
COPY nginx.conf /etc/nginx/nginx.conf
COPY test_0.conf /etc/nginx/sites-enabled/test_0.conf

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
