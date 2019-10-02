def reverse(s):
    words = s.split(' ')
    list_words = []
    for word in words:
        list_words.insert(0,word)
    final = ' '.join(list_words)
    print(final)

reverse('i love programming a lot')
