import os
import pika
import socket
from django.conf import settings
import datetime
import json
import uuid


class RabbitService:
    def __init__(self) -> None:
        self._user = settings.BROKER_USER
        self._pass = settings.BROKER_PASS
        self._host = settings.BROKER_HOST
        self._port = settings.BROKER_PORT
        self._vhost = settings.BROKER_VHOST
        self.connection = None
        self.channel = None

    def create_connection(self):
        credentials = pika.PlainCredentials(
            self._user,
            self._pass
        )
        parameters = pika.ConnectionParameters(
            self._host,
            self._port,
            self._vhost,
            credentials
        )
        self.connection = pika.BlockingConnection(parameters)

    def connect_channel(self):
        if self.connection is None:
            self.create_connection()
        self.channel = self.connection.channel()

    def create_message(self, task, args):
        message = {
            'id': str(uuid.uuid4()),
            'task': task,
            'args': args,
            'kwargs': {},
            'retries': 0,
            'eta': str(datetime.datetime.now())
        }
        return message

    def publish_message(self, channel, queue, message):
        if self.connection is None:
            self.create_connection()
        if self.channel is None:
            self.connect_channel()
        hrds = {
            'lang': 'py',
            'task': 'propostas.tasks.add',
            'argsrepr': repr(message['args']),
            'kwargsrepr': repr(message['kwargs']),
            'origin': '@'.join([str(os.getpid()), str(socket.gethostname())])
        }
        properties = pika.BasicProperties(
            content_type='application/json',
            headers=hrds,
            content_encoding='utf-8',
            correlation_id=message['id']
        )
        channel.basic_publish(
            exchange='',
            routing_key=queue,
            body=json.dumps(message),
            properties=properties
        )

    def close_connection(self, connection):
        self.connection.close()
        self.connection = None
        self.channel = None
