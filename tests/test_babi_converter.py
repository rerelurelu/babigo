import sys
sys.path.append('../')

import pytest
import pandas as pd

from converter.babi_converter import babi_converter


test_data = pd.read_csv('tests/test_data/test_data.csv')
length = len(test_data)


def test_babi_converter() -> None:
    for data in test_data.itertuples():
        assert babi_converter(data[2]) == data[3]
