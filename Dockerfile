FROM python:3.8
COPY . /vinted_bot
RUN pip3 install -r /vinted_bot/requirements.txt
CMD ["python", "/vinted_bot/main.py"]
