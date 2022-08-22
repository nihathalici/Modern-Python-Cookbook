# Exer-04-Rewriting-an-immutable-string

title = "Recipe 5: Rewriting, and the Immutable String"
# title[8] = ''  # TypeError: 'str' object does not support item assignment
# some_string = some_string.method()
# some_string = some_string[:chop_here]
colon_position = title.index(':')
discard_text, post_colon_text = title[:colon_position], title[colon_position+1:]
print(discard_text)
print(post_colon_text)

###

pre_colon_text, _, post_colon_text = title.partition(':')
print(pre_colon_text)
print(post_colon_text)


post_colon_text = post_colon_text.replace(' ', '_')
post_colon_text = post_colon_text.replace(',', '_')
print(post_colon_text)

from string import whitespace, punctuation

for character in whitespace + punctuation:
    post_colon_text = post_colon_text.replace(character, '_')
print(post_colon_text)

post_colon_text = post_colon_text.lower()
print(post_colon_text)

post_colon_text = post_colon_text.strip('_')
print(post_colon_text)

while '__' in post_colon_text:
    post_colon_text = post_colon_text.replace('__', '_')
print(post_colon_text)

print(id(post_colon_text))
post_colon_text = post_colon_text.replace('_', '-')
print(id(post_colon_text))

print( 'some word'.isnumeric() )
print( '1298'.isnumeric() )