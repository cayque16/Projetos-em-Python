import os
import mysql.connector as mysql
import redis
import json
from bottle import Bottle, request

class Sender(Bottle):
    def __init__(self):
        super().__init__()

        db_host = os.getenv('DB_HOST','db')
        db_user = os.getenv('DB_USER', 'root')
        db_name = os.getenv('DB_NAME', 'sender')
        db_password = os.getenv('MYSQL_ROOT_PASSWORD')
        db_port = os.getenv('DB_PORT', '3306')

        self.conn = mysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            port=db_port
        )

        redis_host = os.getenv('REDIS_HOST', 'queue')
        self.fila = redis.StrictRedis(host=redis_host, port=6379, db=0)

        self.route('/', method='POST', callback=self.send)

    def register_message(self, assunto, mensagem):
        SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'

        cur = self.conn.cursor()
        cur.execute(SQL, (assunto, mensagem))
        self.conn.commit()
        cur.close()

        msg = {'assunto': assunto, 'mensagem': mensagem}
        self.fila.rpush('sender', json.dumps(msg))
        print('Mensagem registrada!')

    def send(self):
        assunto = request.forms.get('assunto')
        mensagem = request.forms.get('mensagem')
        self.register_message(assunto, mensagem)
        return 'Mensagem enfileirada! Assunto: {} Mensagem {}'.format(assunto, mensagem)

if __name__ == '__main__':
    sender = Sender()
    sender.run(host='0.0.0.0', port=8080, debug=True)