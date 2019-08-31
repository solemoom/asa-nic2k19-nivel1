FROM python
RUN apt-get update
RUN mkdir /nivel1
WORKDIR /nivel1
COPY . /nivel1
RUN pip install --no-cache-dir -r nivel1_app/requirements.txt
CMD ["python", "nivel1_app/nivel1.py"]
