FROM python:3.11

WORKDIR /code

COPY src/stdash/main.py /code/

# 필요한 패키지 설치

RUN pip install --no-cache-dir --upgrade git+https://github.com/baechu805/stdash@0.1/dash

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
