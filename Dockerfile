FROM ubuntu:14.04

RUN apt-get update -y && \
    apt-get install \
    nano

ADD classes_play.py classes_play.py