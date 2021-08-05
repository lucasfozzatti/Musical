FROM python:3

RUN git clone https://github.com/NicoBeast98/TaTeTI.git

WORKDIR /practica_final_python

RUN pip install -r requirements.txt

CMD ["python3", "./test_musical.py"]