
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
print("Problem 1 - for loop:")
for i in word:
    print(i)
print()
# Write a while loop that does the same thing!
print("Problem 2 - while loop:")
word_length = len(word)
i = 0

while i < word_length:
    print(word[i])
    i += 1
print()

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
print("Problem 3 - while loop:")
count_start = 100
count_end = 140

while count_start < count_end:
    if count_start % 2 == 0:
        print(count_start)
    count_start += 1
print()

# Write a for loop that does the same thing (with range())
print("Problem 4 - for loop range():")
for i in range(100,142, 2):
    print(i)
print()

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
print("Problem 5 - passphrase:")
passphrase = "sillygoose"
answer = ""
while answer != passphrase:
    answer = input("Enter the passphrase: ")
print(f"Passphrase {passphrase} entered successfully. You got it!")