def read_file_as_words():
    f = open('speech.txt', 'r', encoding="utf-8")
    list_of_words = f.readlines()
    return list_of_words


def clean_up(list_of_words):
    list_of_cleaned_words, words = [], []
    for i in range(len(list_of_words)):
        list_of_words[i] = list_of_words[i][:-1]
    for i in list_of_words:
        if i == "":
            list_of_words.remove("")
    for string in list_of_words:
        s = ""
        for e in string:
            if e == " ":
                s += e
            elif e.isalnum():
                s += e
        words.append(s)
    for i in words:
        i = i.split(" ")
        list_of_cleaned_words.extend(i)
    return list_of_cleaned_words


def count_words(cleaned_words):
    count_num = {}
    for item in cleaned_words:
        if item in count_num:
            count_num[item] += 1
        else:
            count_num[item] = 1
    return count_num


def sort_by_count_word(wordcount):
    list_of_sorted_wordcount = sorted(wordcount.items(), key=lambda q: q[1], reverse=True)
    return list_of_sorted_wordcount


def write_out(sort_by_count_word):
    f=open("problem3.txt","w")
    y = 0
    while y < 20:
        f.write(f"{y+1}) {sort_by_count_word[y][0]}---{sort_by_count_word[y][1]}\n")
        y += 1


words = read_file_as_words()
cleaned_words = clean_up(words)
wordcount = count_words(cleaned_words)
sorted_wordcount = sort_by_count_word(wordcount)
write_out(sorted_wordcount)