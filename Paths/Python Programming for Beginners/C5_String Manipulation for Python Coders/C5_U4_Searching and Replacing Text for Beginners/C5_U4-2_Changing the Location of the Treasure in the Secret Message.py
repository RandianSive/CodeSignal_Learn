# Given secret message
secret_msg = "The diamond is in the piano. The ruby is in the clock."

secret_msg = secret_msg.replace('piano','sofa')

# Finding the treasure based on substrings. 
diamond_index = secret_msg.find('diamond')
print(f"Diamond location: {diamond_index}")