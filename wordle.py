from english_words import english_words_lower_alpha_set

set = english_words_lower_alpha_set
for word in list(set):
    if len(word) < 5 or len(word) > 5:
        set.remove(word)

print("This is a tool to filter out letters for the web game 'Wordle,' found here: https://www.powerlanguage.co.uk/wordle/")
print("Using this tool is most certainly cheating!\n")
while(True):
    filter_list = input("Enter letters to filter out separated by commas (e.g. [a,b,c,d]):\n").split(",")
    for letter in filter_list:
        if(letter.isalpha()):
            for word in list(set):
                if letter in word:
                    set.remove(word)
        
    filter_list = input("Enter KNOWN letters with KNOWN spaces with '?' acting as placeholder for UNKNOWN letters (e.g. '?pp??' for what is likely 'apple'):\n")
    for index, letter in enumerate(filter_list):
        if(letter.isalpha()):
            for word in list(set):
                if word[index] != letter:
                    set.remove(word)

    filter_list = input("Enter KNOWN letters with UNKNOWN spaces separated by commas (e.g. 'a,l,e'):\n").split(",")
    for letter in filter_list:
        if(letter.isalpha()):
            for word in list(set):
                if letter not in word:
                    set.remove(word)

    print("Remaining words:\n")
    print(sorted(set))