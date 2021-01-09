def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep( body.count('.') )
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(queue='hello', on_message_callback=callback)