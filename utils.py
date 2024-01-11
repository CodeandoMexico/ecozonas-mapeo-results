from enum import Enum
import pandas as pd
from statistics import mean


class Constants(Enum):
    MALO = "MALO"
    REGULAR = "REGULAR"
    BUENO = "BUENO"
    NINGUNO = "NINGUNO"
    NO_HAY = "NO_HAY"
    GRAVE = "GRAVE"
    MODERADO = "MODERADO"
    LEVE = "LEVE"
    X1 = "1"
    X2_5 = "2_5"
    X5_N = "5_N"


class RemapException(Exception):
    def __init__(self, message):
        super().__init__(message)


def remap(value, x_min, x_max, y_min, y_max):
    return ((value - x_min) / (x_max - x_min)) * (y_max - y_min) + y_min


def remap_nmrb(s):
    if s == Constants.NO_HAY.value:
        return 0
    if s == Constants.MALO.value:
        return 33
    elif s == Constants.REGULAR.value:
        return 66
    elif s == Constants.BUENO.value:
        return 100
    raise RemapException("No existe la opción " + s)


def remap_gml(s):
    if s == Constants.GRAVE.value:
        return 0
    if s == Constants.MODERADO.value:
        return 33
    elif s == Constants.LEVE.value:
        return 66
    raise RemapException("No existe la opción " + s)


def remap_veces(v, s):
    if v == Constants.X1.value and s == Constants.NINGUNO.value:
        return 66
    elif v == Constants.X1.value and s == Constants.LEVE.value:
        return 66
    elif v == Constants.X1.value and s == Constants.MODERADO.value:
        return 33
    elif v == Constants.X1.value and s == Constants.GRAVE.value:
        return 33
    elif v == Constants.X2_5.value and s == Constants.NINGUNO.value:
        return 66
    elif v == Constants.X2_5.value and s == Constants.LEVE.value:
        return 33
    elif v == Constants.X2_5.value and s == Constants.MODERADO.value:
        return 33
    elif v == Constants.X2_5.value and s == Constants.GRAVE.value:
        return 0
    elif v == Constants.X5_N.value and s == Constants.NINGUNO.value:
        return 33
    elif v == Constants.X5_N.value and s == Constants.LEVE.value:
        return 33
    elif v == Constants.X5_N.value and s == Constants.MODERADO.value:
        return 0
    elif v == Constants.X5_N.value and s == Constants.GRAVE.value:
        return 0
    return None


def procesable(row, column):
    return not pd.isna(row[column]) and row[column] != Constants.NINGUNO.value


def calculate_score(mapeo, code, letters, remap_function):
    evaluaciones = []
    for letter in letters:
        if procesable(mapeo, code + letter):
            evaluaciones.append(remap_function(mapeo[code + letter]))
    if len(evaluaciones) > 0:
        return int(round(mean(evaluaciones)))
    return None


def calculate_score_riesgo(mapeo, code_veces, code, letters):
    evaluaciones = []
    v = mapeo[code_veces]
    for letter in letters:
        if procesable(mapeo, code + letter):
            c = mapeo[code + letter]
            evaluaciones.append(remap_veces(v, c))
    if len(evaluaciones) > 0:
        return int(round(mean(evaluaciones)))
    return None
