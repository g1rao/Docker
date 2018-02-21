FROM ubuntu:latest
ENV http_proxy=http://138.85.224.137:8080
ENV https_proxy=https://138.85.224.137:8080
RUN apt-get update && apt-get install python
COPY a.png .
COPY b.png .
COPY c.jpg .
ADD httpserver.py /
CMD ["python", "httpserver.py"]





