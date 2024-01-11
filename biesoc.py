# Bienestar socioeconomico
# Referencias:
# * https://docs.google.com/spreadsheets/d/1owfdwKv25AkBEb5QuA0nNwKj4LoEXVo2/edit#gid=1512333624
# * Gestor de Mapeo
import pandas as pd

import utils
from statistics import mean


# ------------------------------------------------------------
# Subcategoría: Empleo y emprendimiento (c1)
# Actividad: Actividades de comercio local
# Actividades de comercio y servicios realizados por individuos o pequeñas empresas que buscan generar ingresos y crear
#   empleo en el barrio
# ------------------------------------------------------------
def oc1(mapeo):
    evaluaciones = []
    code = 'dim_biensoc_22'
    if not pd.isna(mapeo[code + 'c']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'c']))
    if not pd.isna(mapeo[code + 'd']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'd']))
    if not pd.isna(mapeo[code + 'e']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'e']))
    if not pd.isna(mapeo[code + 'f']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'f']))
    if not pd.isna(mapeo[code + 'g']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'g']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0


# ------------------------------------------------------------
# Subcategoría: Sistemas alimentarios (c8)
# Actividad: Mercados locales, fruterías, verdulerías (oc3)
# ------------------------------------------------------------
def oc3(mapeo):
    evaluaciones = []
    code = 'dim_biensoc_24'
    if not pd.isna(mapeo[code + 'c']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'c']))
    if not pd.isna(mapeo[code + 'd']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'd']))
    if not pd.isna(mapeo[code + 'e']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'e']))
    if not pd.isna(mapeo[code + 'f']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'f']))
    if not pd.isna(mapeo[code + 'g']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'g']))
    if not pd.isna(mapeo[code + 'h']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'h']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0


# ------------------------------------------------------------
# Subcategoría: Digitalización (c4)
# Actividad: Puntos de internet (oc2)
# ------------------------------------------------------------
def oc2(mapeo):
    evaluaciones = []
    code = 'dim_biensoc_23'
    if not pd.isna(mapeo[code + 'c']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'c']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0


# ------------------------------------------------------------
# Subcategoría: Cultura e identidad (c9)
# Actividad: Actividades culturales (oc4)
# Expresiones y eventos que celebran y promueven la cultura e identidad de una comunidad
# ------------------------------------------------------------
def oc4(mapeo):
    evaluaciones = []
    code = 'dim_biensoc_25'
    if not pd.isna(mapeo[code + 'c']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'c']))
    if not pd.isna(mapeo[code + 'd']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'd']))
    if not pd.isna(mapeo[code + 'e']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'e']))
    if not pd.isna(mapeo[code + 'f']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'f']))
    if not pd.isna(mapeo[code + 'g']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'g']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0


# ------------------------------------------------------------
# Subcategoría: Participación de la comunidad (c10)
# Actividad: Actividades de participación comunitaria (oc5)
# Actividades y acciones en las que las personas se involucran activamente para abordar temas o desafíos locales de
#   su comunidad
# ------------------------------------------------------------
def oc5(mapeo):
    evaluaciones = []
    code = 'dim_biensoc_26'
    if not pd.isna(mapeo[code + 'c']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'c']))
    if not pd.isna(mapeo[code + 'd']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'd']))
    if not pd.isna(mapeo[code + 'e']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'e']))
    if not pd.isna(mapeo[code + 'f']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'f']))
    if not pd.isna(mapeo[code + 'g']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'g']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0


# ------------------------------------------------------------
# Subcategoría: Cultura e identidad (c9)
# Actividad: Actividades desportivas (oc6)
# ------------------------------------------------------------
def oc6(mapeo):
    evaluaciones = []
    code = 'dim_biensoc_27'
    if not pd.isna(mapeo[code + 'c']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'c']))
    if not pd.isna(mapeo[code + 'd']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'd']))
    if not pd.isna(mapeo[code + 'e']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'e']))
    if not pd.isna(mapeo[code + 'f']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'f']))
    if not pd.isna(mapeo[code + 'g']):
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'g']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0
