from collections import Counter
def popular_words (text, words):
    words_in_text = text.lower().split()
    word_counts = Counter(words_in_text)
    popular_dict_words = {word: word_counts.get(word, 0) for word in words}

    return popular_dict_words


assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')