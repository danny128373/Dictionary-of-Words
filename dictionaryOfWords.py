"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()
word_definitions['agitate'] = 'make (someone) troubled or nervous'
word_definitions['onomatopoeia'] = 'the formation of a word from a sound associated with what is named'

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions['fascism'] = 'a form of far-right, authoritarian ultranationalism characterized by dictatorial power, forcible suppression of opposition, as well as strong regimentation of society and of the economy'
word_definitions['social darwism'] = 'the theory that individuals, groups, and peoples are subject to the same Darwinian laws of natural selection as plants and animals'
"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions['fascism'])
print(word_definitions['agitate'])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for key, value in word_definitions.items():
    print(f"The definition of {key} is {value}")
