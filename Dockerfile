FROM python:3.13

WORKDIR  /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 5001

RUN useradd app
USER app


ENV FLASK_APP=hello.py


CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]