def babi_converter(hiragana: str) -> str:
    """
    Insert "ba, bi, bu, be, bo" into a sentence
    """
    result = ''
    length = len(hiragana) - 1

    for idx, letter in enumerate(hiragana):
        next_letter = hiragana[idx+1:idx+2]

        if (next_letter in 'ぁぃぅぇぉゃゅょ') & (idx < length):
            pass
        elif letter in 'あかがさざただなはばぱまやらわゎ':
            result += (letter + 'ば')
        elif letter in 'いきぎしじちぢにひびぴみり':
            result += (letter + 'び')
        elif letter in 'うゔくぐすずつづぬふぶぷむゆるん':
            result += (letter + 'ぶ')
        elif letter in 'えけげせぜてでねへべぺめれ':
            result += (letter + 'べ')
        elif letter in 'おこごそぞとどのほぼぽもろを':
            result += (letter + 'ぼ')
        elif letter in 'ぁゃ':
            result += (hiragana[idx-1:idx] + letter + 'ば')
        elif letter in 'ぃ':
            result += (hiragana[idx-1:idx] + letter + 'び')
        elif letter in 'ぅゅ':
            result += (hiragana[idx-1:idx] + letter + 'ぶ')
        elif letter in 'ぇ':
            result += (hiragana[idx-1:idx] + letter + 'べ')
        elif letter in 'ぉょ':
            result += (hiragana[idx-1:idx] + letter + 'ぼ')
        elif (letter in 'ー〜') & (idx < length):
            result += (letter + result[-1])
        else:
            result += letter
    return result
