FROM python:3.8
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
ADD fact.py /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD streamlit run fact.py
