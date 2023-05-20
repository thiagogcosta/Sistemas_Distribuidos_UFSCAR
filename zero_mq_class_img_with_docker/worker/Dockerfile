FROM python:3

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-u", "main.py"]

# buildar a imagem
#docker build -t worker .

# executar o container com os containers visualizando a rede da maquina
#docker run -d --name worker --network host worker

# finalizar a execucao do container
#docker kill worker

# excluir os containers finalizados
#docker rm $(docker ps -a -q)