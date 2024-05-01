# Treasure map
treasure_map = "ChesapeakeBayIsland, 5 10N 10 15W. Key: Use 'fairy' to summon the treasure chest."

# TODO: Decode the key message from the treasure_map
# You need to retrieve the part after "Key: " in the `treasure_map`,
# the output should be "Use 'fairy' to summon the treasure chest."
key_message = treasure_map[treasure_map.find("Key:")+5:]
print("Decoded key message: ", key_message)


# TODO: Replace the word 'fairy' with 'dragon', and print the new message
updated_treasure_map = treasure_map.replace('fairy','dragon')
print("Updated treasure map: ", updated_treasure_map)