def letter_count(file_name):
    all_words = open(file_name).read()
    count = 0

    for ch in all_words:
        if(ch.isalpha()):
            count += 1
    
    print(count)

def count_possible_sentences(file_name):
    all_words = open(file_name).read().split()
    count = 0

    for s in all_words:
        if(s[len(s) - 1] in "!?."):
            count += 1

    print(count)

def find_last_capitalised(file_name):
    all_words = open(file_name).read().split()   
    for s in reversed(all_words):
        if(s[0].isupper()):
            print(s)
            break


letter_count("words.txt")
count_possible_sentences("words.txt")
find_last_capitalised("words.txt")