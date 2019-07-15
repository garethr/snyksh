FROM python:alpine

RUN pip3 install ipython termcolor pysnyk prettyprinter 

COPY snyksh.py /snyksh.py

ENTRYPOINT ["python3", "/snyksh.py"]
