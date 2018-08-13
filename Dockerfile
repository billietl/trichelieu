FROM python:3.4-slim
# run via docker run -e TZ="Europe/Paris" -e token="your token here" --name trichelieu trichelieu

add requirements.txt /

run pip install -r /requirements.txt

add trichelieu.py /

cmd python3 /trichelieu.py
