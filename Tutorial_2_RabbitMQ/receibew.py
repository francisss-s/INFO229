#!/usr/bin/env python
import pika
import sys
import wikipedia

wikipedia.set_lang("es")

def wiki(n):
    return wikipedia.summary(n)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]

channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key='wikipedia')

print(' [*] Waiting for logs. To exit press CTRL+C')



def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key,wiki(body)))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()