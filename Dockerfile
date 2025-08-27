FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
COPY css/styles.css /usr/share/nginx/html/styles.css
