#!/usr/bin/env python
import pika
import sys

DEFA = "python"

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

if len(sys.argv) < 2:
    print("Error, igreso de argumentos invalidos, pruebe con wikipedia o youtube y lo que decea buscar")
    connection.close()
else:
    severity = sys.argv[1]
    message = ' '.join(sys.argv[2:]) or DEFA
    channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
    print(" [x] Sent %r:%r" % (severity, message))
    connection.close()