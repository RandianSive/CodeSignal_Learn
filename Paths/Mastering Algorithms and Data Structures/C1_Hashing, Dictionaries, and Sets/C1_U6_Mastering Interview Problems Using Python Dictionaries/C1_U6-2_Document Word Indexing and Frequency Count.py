def keyword_index(docs):


    # implement this
    
    result_index = {}
    
    for index_doc,doc in enumerate(docs):
        for index_word,word in enumerate(doc.split()):
           #如果沒有該字的目錄，就創造一個
           #Output :{'Hello': {0: 1}, 'world': {0: 1}, 'of': {1: 1}, 'python': {1: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}
            if word not in result_index:
                result_index[word] = {index_doc:1}
           #如果有該字的目錄，但還沒有該文件的子目錄，就創造一個
            elif index_doc not in result_index[word]:
                result_index[word][index_doc] = 1
            #如果有該字的目錄和該文件的子目錄，計數器+1
            else:
                result_index[word][index_doc] += 1
        return result_index

docs = ["Hello world", "world of python", "python is a snake"]
print(keyword_index(docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}