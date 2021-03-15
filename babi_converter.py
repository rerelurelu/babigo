def babi_converter(hiragana: str) -> str:
    """
    Insert "ba, bi, bu, be, bo" into a sentence
    """
    result = ''
    length = len(hiragana) - 1

    for idx, letter in enumerate(hiragana):
        next_letter = hiragana[idx+1:idx+2]

        if (next_letter in 'ゃゅょ') & (idx < length):
            pass
        elif letter in 'あかがさざただなはばぱまやらわゎ':
            result += (letter + 'ば')
        elif letter in 'いきぎしじちぢにひびぴみり':
            result += (letter + 'び')
        elif letter in 'うくぐすずつづぬふぶぷむゆるん':
            result += (letter + 'ぶ')
        elif letter in 'えけげせぜてでねへべぺめれ':
            result += (letter + 'べ')
        elif letter in 'おこごそぞとどのほぼぽもろを':
            result += (letter + 'ぼ')
        elif letter in 'ゃ':
            result += (hiragana[idx-1:idx] + letter + 'ば')
        elif letter in 'ゅ':
            result += (hiragana[idx-1:idx] + letter + 'ぶ')
        elif letter in 'ょ':
            result += (hiragana[idx-1:idx] + letter + 'ぼ')
        elif letter in 'ー':
            result += (letter + result[-1])
        else:
            result += letter
    return result
