phrase = str(input("Dime una frase"))
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

for i in phrase:
    for j in vowels:
        if i == j:
            phrase = phrase.replace(i, "0")

print(phrase)
