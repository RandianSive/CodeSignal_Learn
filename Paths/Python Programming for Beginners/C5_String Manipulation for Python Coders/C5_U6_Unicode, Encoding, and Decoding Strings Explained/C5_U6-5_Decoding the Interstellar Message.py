# Encoded Chinese message, encoding is unknown
chinese_message = b'\xff\xfe*Yzz-N\x84v\xee\x95\x19P!\x00'

# TODO: Find out the encoding, trying to decode the input message with different encodings
# Decode the message and assign the value to a variable "decoded_message"
# TODO: Print out the decoded message

decoded_message = chinese_message.decode('utf-16')

print(decoded_message)

# Hint: you should get a string "太空中的问候!" as a result