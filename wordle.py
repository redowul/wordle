set = []
with open('words.txt') as file:
    for line in file:
        set.append(line.rstrip())

print("This is a tool to filter out letters for the web game 'Wordle,' found here: https://www.powerlanguage.co.uk/wordle/")
print("Using this tool is most certainly cheating!\n")
while(True):
    filter_list = input("Enter letters to filter out separated by commas (e.g. [a,b,c,d]):\n").lower().split(",")
    for letter in filter_list:
        if(letter.isalpha()):
            for word in list(set):
                if letter in word:
                    set.remove(word)
        
    filter_list = input("Enter KNOWN letters with CORRECT placement with '?' acting as a placeholder for UNKNOWN letters separated by commas (e.g. '?,p,p,?,?' for what is likely 'apple'):\n").lower().split(",")
    for index, letter in enumerate(filter_list):
        if(letter.isalpha()):
            for word in list(set):
                if word[index] != letter:
                    set.remove(word)

    filter_list = input("Enter KNOWN letters with INCORRECT placement with '?' acting as a placeholder for UNKNOWN letters separated by commas (e.g. 'a,l,e'):\n").lower().split(",")
    for index, letter in enumerate(filter_list):
        if(letter.isalpha()):
            for word in list(set):
                if letter not in word or word[index] == letter:
                    set.remove(word)

    print("Remaining words:\n")
    print(sorted(set))
