rank_dict = {'Python': 1, 'Java': 2, 'JavaScript': 3}



invalid_key = 'C#'

print(rank_dict.get(invalid_key,"The key doesn't exist!"))

#print(rank_dict[invalid_key])    # This will trigger KeyError exception