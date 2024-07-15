def word_counter(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return word_count

print(word_counter("example.txt"))