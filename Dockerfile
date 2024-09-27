FROM python:3.11

WORKDIR /code

COPY src/stdash/main.py /code/
COPY src/stdash/pages /code/pages

# 필요한 패키지 설치

RUN pip install --no-cache-dir --upgrade git+https://github.com/baechu805/stdash@0.1/dash

CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
