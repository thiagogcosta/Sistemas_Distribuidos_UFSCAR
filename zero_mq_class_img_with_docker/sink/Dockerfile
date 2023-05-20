FROM python:3

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5556

CMD [ "python3", "-u", "main.py"]


# buildar a imagem
#docker build -t sink .

# executar o container com os containers visualizando a rede da maquina
#docker run -d --name sink_container --network host sink

# finalizar a execucao do container
#docker kill sink_container

# excluir os containers finalizados
#docker rm $(docker ps -a -q)