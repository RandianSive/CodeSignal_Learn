# Interplanetary communication: Sending congratulations to all astronauts in their native language!
str_en = "Congratulations for successful Mars exploration!"
str_de = "Herzlichen Glückwunsch zur erfolgreichen Mars-Erkundung!"
str_fr = "Félicitations pour l'exploration réussie de Mars!"

# Encoding the strings to byte sequences (in UTF-16 format)
b_en = str_en.encode('utf-16')
b_de = str_de.encode('utf-16')
b_fr = str_fr.encode('utf-16')

# Now, let's pretend we received these byte sequences and decode them back to the original message.
# We use the '.decode()' method and specify 'utf-16' as the decoding format to match the encoding format.

print("Decoded English: ", b_en.decode('utf-16')) # should print: Congratulations for successful Mars exploration!
print("Decoded German: ", b_de.decode('utf-16')) # should print: Herzlichen Glückwunsch zur erfolgreichen Mars-Erkundung!
print("Decoded French: ", b_fr.decode('utf-16')) # should print: Félicitations pour l'exploration réussie de Mars!

# TODO: change UTF-8 encoding/decoding to UTF-16