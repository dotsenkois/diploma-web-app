#!/bin/bash
# git clone https://github.com/dotsenkois/diploma-web-app.git
cp -f ./env ./backend/Salary_counter/.env
docker-compose build
docker-compose up