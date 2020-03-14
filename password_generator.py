"""
Copyright(c) 2020 Tatsuro Watanabe
https://github.com/ktpcschool/password_generator
"""

import string
import secrets


def password_generator(lowercase, uppercase, numbers, symbol, number_of_characters):
    """
    パスワードを作成
    :param lowercase: 小文字を含めるならTrue
    :param uppercase: 大文字を含めるならTrue
    :param numbers: 数字を含めるならTrue
    :param symbol: 記号を含めるならTrue
    :param number_of_characters: 文字数
    :return: パスワード
    """

    chars = ''

    if lowercase:   # 小文字が含まれている場合
        chars += string.ascii_lowercase

    if uppercase:   # 大文字が含まれている場合
        chars += string.ascii_uppercase

    if numbers:     # 数字が含まれている場合
        chars += string.digits

    if symbol:      # 記号が含まれている場合
        chars += '/*+.,!?#$%&~|^@;:()[]{}'

    return ''.join(secrets.choice(chars) for n in range(number_of_characters))


def main():
    lowercase = True
    uppercase = True
    numbers = True
    symbol = False
    number_of_characters = 8
    passwords = [password_generator(lowercase,
                                    uppercase,
                                    numbers,
                                    symbol,
                                    number_of_characters) for n in range(5)]
    print(passwords)


if __name__ == '__main__':
    main()
