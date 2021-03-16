import sys
sys.path.append('../')

import pytest
import pandas as pd

from converter.babi_converter import babi_converter


test_data = pd.read_csv('tests/test_data/test_data.csv')


def test_babi_converter() -> None:
    data = [[sentence[1], sentence[2]] for sentence in test_data.itertuples()]

    assert babi_converter(data[0][0]) == data[0][1]
    assert babi_converter(data[2][0]) == data[2][1]
    assert babi_converter(data[3][0]) == data[3][1]
    assert babi_converter(data[4][0]) == data[4][1]
    assert babi_converter(data[5][0]) == data[5][1]
    assert babi_converter(data[6][0]) == data[6][1]
    assert babi_converter(data[7][0]) == data[7][1]
    assert babi_converter(data[8][0]) == data[8][1]
    assert babi_converter(data[9][0]) == data[9][1]
    assert babi_converter(data[10][0]) == data[10][1]
