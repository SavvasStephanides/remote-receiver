import pika
import os

HOST = "localhost"
QUEUE_NAME = "hello"

def wait_for_messages():
    channel = get_channel()

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=receive_message, auto_ack=True)

    print("==========================================")
    print('MESSAGES:')
    print("==========================================")
    channel.start_consuming()

def get_channel():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    return channel

def receive_message(ch, method, properties, body):
        message = body.decode("utf-8")
        display_message(message)

def display_message(message):
    print(" 🚨 " + message)

wait_for_messages()