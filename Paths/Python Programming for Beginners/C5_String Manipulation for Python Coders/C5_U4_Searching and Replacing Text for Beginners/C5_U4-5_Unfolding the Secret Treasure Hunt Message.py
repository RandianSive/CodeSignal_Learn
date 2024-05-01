# Given a secret message
msg = "X marks the 10th tree to the left, 20 steps forward will lead you to a stone. Look under it!"

# TODO: Use the appropriate string method to find the position of 'X in the string
print(f"\"X\" is located at the position of {msg.find('X')} in the message")

# TODO: Count how many times '10' and '20' appears in the string
print(f"10 appear {msg.count('10')} time, 20 appear {msg.count('20')} time.")

# TODO: For a confused participant, modify the directions replacing 'left' with 'right'. Print the new message.
new_msg = msg.replace("left","right")
print(new_msg)