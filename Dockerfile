FROM python:3.7
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

RUN pip install Flask gunicorn
RUN pip install flask-cors
RUN pip install requests
RUN pip install pytz
RUN pip install line-bot-sdk

RUN pip install --upgrade google-cloud-storage

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app

