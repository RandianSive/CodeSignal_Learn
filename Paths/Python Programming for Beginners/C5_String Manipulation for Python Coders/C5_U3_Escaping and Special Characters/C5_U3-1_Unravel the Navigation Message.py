# Folder and file names
game_name = "Cosmo_Python_Game"
file_name = game_name + ".exe"

# Preparing a direction message to navigate to the game file
direction_message = 'The game {} awaits you!\nTo start the game, follow these steps:\n\t1. Press "Windows + E" to open File Explorer.\n\t2. Navigate through: C:\\Program Files (x86)\\{}\\{}\nLet the fun begin!'.format(game_name, game_name, file_name)

# Print the direction message
print(direction_message)