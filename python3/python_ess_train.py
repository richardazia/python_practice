import art

mammal_art = art.text2art("Mammal dictionary")
print(mammal_art)

mammals = {"land": "cat", "sea": "dolphin", "tree": "bear", }

print(mammals.get('land'))
print(mammals.get('mountains', "goat"))
print(mammals)
print(len(mammals))
print(mammals.values())

alphabet = {"a": "airport", "b": "badger", "c": "chameleon"}

if "f" not in alphabet:
    alphabet["f"] = []
alphabet['f'].append('fox')
alphabet['f'].append('ferret')

alphabet['l'] = ["lemming"]

print(alphabet)

string_split = 'Today is cloudy. The sun is not shining'

string_dot = string_split.split('.')

nothing_passed = string_split.split(" ")

print(string_dot)  # ['Today is cloudy', ' The sun is not shining']
print(nothing_passed)  # ['Today', 'is', 'cloudy.', 'The', 'sun', 'is', 'not', 'shining']

#  Dictionary comprehension
#  remember, use (), not {}.
alphabet_words_list = [('a', 'airport'), ('b', 'badger'), ('c', 'chameleon')]
print(alphabet_words_list)
alphabet_words = {item[0]: item[1] for item in alphabet_words_list}
print(alphabet_words)
alphabet_words = {key: value for key, value in alphabet_words_list}
print(alphabet_words)

# print(alphabet_words_list.items())
print(list(alphabet_words.items()))

key_name = [{'letter': key, 'name': value} for key, value in alphabet_words.items()]

print(key_name)