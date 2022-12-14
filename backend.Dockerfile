FROM dotsenkois/my-ubuntu:0.0.1

WORKDIR /usr/src/app

COPY ./backend/ ./
# COPY entrypoint.sh .
# RUN apt-get update
# RUN apt-get install python3-pip locales git -y && apt-get clean
# RUN echo "ru_RU.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
# ENV LC_ALL=ru_RU.UTF-8
# RUN git clone https://github.com/dotsenkois/diploma-web-app.git && mv diploma-web-app/* /usr/src/app
RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt

ENTRYPOINT ["bash", "entrypoint.sh"]