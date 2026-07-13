# docker build --tag python-app:0.0 .
#                                   |---> for location of project

FROM python:3.12-slim
# pull image form hub.docker.com 
# there is no url means default url in hub.docker.com

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
# --no-cache-dir means install fresh dont do caching

COPY . .

EXPOSE 5000

# command to run application
CMD ["python", "app.py"]