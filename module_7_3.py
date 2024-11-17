class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding = 'utf-8') as file:
                words = []
                for name in file:
                    name = name.lower()
                    string_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for i in string_punctuation:
                        name = name.replace(i, '' if i != ' - ' else ' ')
                    words.extend(name.split())
                all_words[file_name] = words
        return all_words

    def find(self, word: str):
        word = word.lower()
        find_word = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                find_word[file_name] = words.index(word) + 1
        return find_word

    def count(self, word):
        word = word.lower()
        count_word = {}
        for file_name, words in self.get_all_words().items():
            count_word[file_name] = words.count(word)
        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))







