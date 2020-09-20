import numpy as np
import pandas as pd
from typing import List


def open_txt(filename: str) -> (List[float], List[float], List[float], List[float]):  # todo: make function
    """pass"""
    with open(filename, 'r') as f:
        x = list(map(float, f.readline().rstrip().split()))
        y = list(map(float, f.readline().rstrip().split()))
        x_error = list(map(float, f.readline().rstrip().split()))
        y_error = list(map(float, f.readline().rstrip().split()))
    return x, y, x_error, y_error


def open_xls(filename: str) -> List[List[float]]:  # todo: make function
    """pass"""
    list_of_lines = []
    table = pd.read_excel(filename)
    for row in table:
        list_of_lines.append(list(map(float, list(table[row])[1::])))
    return list_of_lines


X, Y, x_err, y_err = open_txt('211_2.txt')