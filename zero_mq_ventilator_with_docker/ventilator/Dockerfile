FROM python:3

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5555

CMD [ "python3", "-u", "main.py"]

# buildar a imagem
#docker build -t ventilator .

# executar o container com os containers visualizando a rede da maquina
#docker run -d --name ventilator --network host ventilator

# finalizar a execucao do container
#docker kill ventilator

# excluir os containers finalizados
#docker rm $(docker ps -a -q)