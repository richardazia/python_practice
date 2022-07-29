
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"
i = 0

# Write a for loop that prints out each character in the above "word" variable
print("For ever and ever")
for char in word:
    print(char)

# Write a while loop that does the same thing!
word_length = int(len(word))

print("While we're at it")
while (i < word_length):
    print(word[i])
    i += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
print("Part 2 - while loop")
num = 100
while num <= 140:
    if num % 2 == 0:
        print(num)
        num += 1
    else:
        num += 1

# Write a for loop that does the same thing (with range())
# for num in range(-10, 10, 2):
#     print(num)
print("The For Loop")
for num in range(100, 140, 2):
    print(num)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
print("Part 3")
print("I dare you to write sillygoose after the prompt.")

want_to_hear = input("sillygoose: ")

while want_to_hear != "sillygoose":
    want_to_hear = input("I really want you to write 'sillygoose'. Do it now and this will be over.")

print("I know I am, but what are you...")