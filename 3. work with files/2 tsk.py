def write_array(array, file_name):
    """записывает строки из array в файл file_name"""
    file = open("text_from_strings.txt", "w")
    for i in range(len(strings)):
        file.write(strings[i])
        file.write('\n')
    file.close()
    pass

strings = ['this is just the third hw', 'show must go on', 'queen is such a great musical group']
write_array(strings, "text_from_strings.txt")