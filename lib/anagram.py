class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))
    
    def match(self, words):
        return [word for word in words if ''.join(sorted(word)) == self.sorted_word]
