class WordCount:
    def get_text(self, filename) -> list:
        with open(f'{filename}.txt', 'r', encoding='utf8') as f:
            text = f.read()

        symbols = ['.', ',', ':', '?', '!', '`', '...']
        text.replace('\n', ' ')
        for s in symbols:
            text.replace(s, '')
        text = text.lower()

        return text.split()
        

    def unique_word(self, text: dict) -> list:
        words = [word for word, count in text.items() if count == 1]
        return words
   

    def main(self):
        text = self.get_text('file')
        print(f'Кол-во слов в тексте: {len(text)}')

        text_dict = dict()
        for word in text:
            text_dict[word] = text.count(word)

        words = self.unique_word(text_dict)
        print(f'Кол-во уникальных слов: {len(words)}')
        print('Все уникальные слова: ')
        for word in words: print(word.center(100))


def start():
    wd = WordCount()
    wd.main()


if __name__ == '__main__':
    start()
