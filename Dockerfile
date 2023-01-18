FROM Abishnoi/Chatbot-python:latest

RUN  git clone https://github.com/Abishnoi69/Chatbot -b main  /root/Chatbot
RUN  mkdir  /root/Chatbot/bin/
WORKDIR /root/Chatbot/

COPY   ./config.py* /root/Chatbot
RUN pip3 install -r requirements.txt

CMD python3 chatbot.py
