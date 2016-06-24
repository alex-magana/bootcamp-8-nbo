def words(statement):

    word_list = statement.split()

    count_store = {}

    for word in word_list:
        if word.isdigit():
            word = int(word)
        if count_store.has_key(word):
            count_store[word] = count_store[word] + 1
        else:
            count_store[word] = 1

    return count_store

dict_word = words("olly olly in come free")
for i, j in dict_word.items():
	print i, ": ", j