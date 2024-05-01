# File and folder names
file_name = 'mission_clues.txt'
folder_name = 'Top_Secret'

# Using a raw string for the file path
raw_file_path = r"C:\User\Cosmo"  # TODO: replace this comment with a raw string representing some random file path.

# Preparing the guidance message with escaped characters
# TODO: replace this comment with code to create the guidance message by applying string formatting and special characters.
# Use `file_name`, `folder_name`, and `raw_file_path` in your message.
# Feel free to use special characters and multiple lines in your message
guidance_message = f"File path:\n\t{raw_file_path}\\{folder_name}\\{file_name}"

# Printing the message
print(guidance_message)