from num2words import num2words  # https://pypi.org/project/num2words/


def number_to_text(number):
    try:

        return num2words(number, lang='ru')
    except ValueError:
        print('неверный ввод:', number)
        return None


