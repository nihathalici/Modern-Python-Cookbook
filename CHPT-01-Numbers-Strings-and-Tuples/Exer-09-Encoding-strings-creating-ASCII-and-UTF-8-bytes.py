# Exer-09-Encoding-strings-creating-ASCII-and-UTF-8-bytes

with open('some_file.txt', 'w', encoding='utf-8') as output:
    print( 'You drew \U0001F000', file=output)
with open('some_file.txt', 'r', encoding='utf-8') as input:
    text = input.read()

string_bytes = 'You drew \U0001F000'.encode('utf-8')
print(string_bytes)

'You drew \U0001F000'.encode('ascii')  # UnicodeEncodeError: 'ascii' codec can't encode character 