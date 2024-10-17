"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self):
        number_of_letters = len(self.text)
        number_of_words = len(self.text.split())

        return f'Total text length: {number_of_letters}\nTotal number of words: {number_of_words}'

if __name__ == '__main__':
    text = 'Когда вы выполните эти задания, у меня есть кое-что особенное: мини-проект.'

    text_pro = TextProcessor(text)
    text_advanced_pro = AdvancedTextProcessor(text)

    print('TEXT PROCESSOR')
    print(text_pro.text)
    print(text_pro.to_upper())
    print(text_pro.summarize())

    print('ADVANCED TEXT PROCESSOR')
    print(text_advanced_pro.text)
    print(text_advanced_pro.to_upper())
    print(text_advanced_pro.summarize())

