FROM ubuntu:latest
ENV http_proxy=http://138.85.224.137:8080
ENV https_proxy=https://138.85.224.137:8080
ADD server.py /
volume ["templates"]
RUN apt-get update && apt-get install python
RUN apt-get install python-pip 
RUN pip install flask
ADD index.html /templates/
CMD ["python","server.py"]
