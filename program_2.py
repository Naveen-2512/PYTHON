#file = open("input.txt","r")
# text = input("Enter text : ")
#text = file.read()
#file.close()

text = input("Enter text : ")
text = text.lower()

# to remove punctuations

punctuation = ",.!?;:"
for p in punctuation:
    text = text.replace(p,"")

words = text.split()

print("Total words : " , len(words))

# palindromes
print("\nPalindromes words:")

Found = False
for word in words:
    reverse = word[::-1]
    if len(word)>1 and word == reverse:
        print(word)
        Found = True

if Found == False:
    print("No palindrome found")

# Word frequency
print("\nWord frequency")

for i in range(len(words)):
    count = 0

    already_checked = False
    for j in range(i):
        if words[i] == words[j]:
            already_checked = True
            break

        
    if already_checked == False:
        for word in words:
            if words[i] == word:
                count += 1

        print(words[i], ":" , count)