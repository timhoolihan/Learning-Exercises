word = input("Enter a word: ")
reverse = []

for x in (word):
    reverse.append(x)

reverse.reverse()

for y in reverse:
    print(y, end="")