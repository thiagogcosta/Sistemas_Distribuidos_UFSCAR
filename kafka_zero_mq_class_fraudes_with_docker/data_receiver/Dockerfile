FROM python:3

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5555

CMD [ "python3", "-u", "main.py"]

# buildar a imagem
#docker build -t data_receiver .

# executar o container com os containers visualizando a rede da maquina
#docker run -d --name data_receiver --network host data_receiver

# finalizar a execucao do container
#docker kill data_receiver

# excluir os containers finalizados
#docker rm $(docker ps -a -q)