from converter.hiragana_converter import goo_converter, kakasi_converter
from converter.babi_converter import babi_converter


if __name__ == '__main__':
    sentence = input('enter: ')
    hiragana = goo_converter(sentence)
    output = babi_converter(hiragana)

    # goo api converter
    print('<< goo API >>')
    print(f'input -> {sentence}')
    print(f'hira -> {hiragana}')
    print(f'result -> {output}')

    # A line to make it easier to see
    print('-'*40)

    # pykakasi converter
    hiragana = kakasi_converter(sentence)
    output = babi_converter(hiragana)

    print('<< Pykakasi >>')
    print(f'input -> {sentence}')
    print(f'hira -> {hiragana}')
    print(f'result -> {output}')
