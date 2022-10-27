FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY docker/frontend/nginx.conf /etc/nginx/conf.d
COPY ./frontend/static/ /static/
