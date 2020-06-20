FROM python:3.8

MAINTAINER 1964645988@qq.com

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY . /app

CMD ["gunicorn", "car:app", "-c", "./gunicorn.conf.py"]