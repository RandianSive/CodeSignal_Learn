# A French astronaut sends you a space journal entry encoded in "latin-1".
# Use your Python decoding capabilities to read it!

journal_entry = "Cher journal, aujourd'hui nous avons vu une nébuleuse magnifique!".encode('latin-1')
# TODO: Decipher the encoded journal using the appropriate method and print the decoded journal

decode_journal = journal_entry.decode('latin-1')

print(decode_journal)