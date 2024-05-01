# During your communications with astronaut friends from Japan and Spain, you received two encoded messages.

# Message from Japanese astronaut: コスモからの挨拶！ (Greetings from Cosmos!)
message_jp = "コスモからの挨拶！".encode('utf-16') 
decoded_message_jp = message_jp.decode('utf-16')
print("Decoded message (Japanese): ", decoded_message_jp)

# Message from Spanish astronaut: ¡Saludos desde el cosmos! (Greetings from Cosmos!)
message_es = "¡Saludos desde el cosmos!".encode('utf-8')
decoded_message_es = message_es.decode('utf-8')
print("Decoded message (Spanish): ", decoded_message_es)