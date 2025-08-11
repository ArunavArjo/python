def match_words(words):
    count = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count+=1
            lst.append(word)
    print("List words which first and last charecter are same ",lst)
    return count

count = match_words(['tnt','dvd','yap','clap'])
print("The number of words are",count)