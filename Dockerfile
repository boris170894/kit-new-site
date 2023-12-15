FROM python:3.10

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ${APP_HOME}
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . ${APP_HOME}

# running migrations
RUN python manage.py migrate

RUN apt-get update && apt-get install -y entr

# gunicorn
# CMD ["gunicorn", "--config", "gunicorn-cfg.py", "config.wsgi"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
CMD ["bash", "-c", "find . -name '*.py' | entr -nr python manage.py runserver 0.0.0.0:8080 --insecure"]
