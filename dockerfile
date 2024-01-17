FROM python 
WORKDIR /app
COPY . ./
RUN pip install pyzabbix
CMD python python.py
