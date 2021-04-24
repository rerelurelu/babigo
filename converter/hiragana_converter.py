import os

import requests
from dotenv import load_dotenv
from pykakasi import kakasi


def goo_converter(sentence: str) -> str:
    """
    Convert the inputted sentence into hiragana with goo API.
    """
    load_dotenv('.env')
    APP_ID = os.environ.get('APP_ID')

    headers = {
        'Content-Type': 'application/json',
    }

    # Remove line breaks
    table = str.maketrans('', '', '\n\r\n')
    sentence = sentence.translate(table)

    data = (
        '{"app_id":"' + APP_ID + '",'
        '"request_id":"record003",'
        '"sentence":"' + sentence + '",'
        '"output_type":"hiragana"'
        '}'
    )

    response = requests.post(
        'https://labs.goo.ne.jp/api/hiragana',
        headers=headers,
        data=data.encode("utf-8")
    )

    response = response.json()
    hiragana = ''.join(response["converted"].split())

    return hiragana


def kakasi_converter(sentence: str) -> str:
    """
    Convert the inputted sentence into hiragana with pykakasi.
    """
    global kakasi
    kakasi = kakasi()

    kakasi.setMode('J', 'H')
    kakasi.setMode('K', 'H')

    hiragana_converter = kakasi.getConverter()
    hiragana = hiragana_converter.do(sentence)

    return hiragana
