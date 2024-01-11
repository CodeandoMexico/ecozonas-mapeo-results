# Bienestar socioeconomico
# Referencias:
# * https://docs.google.com/spreadsheets/d/1owfdwKv25AkBEb5QuA0nNwKj4LoEXVo2/edit#gid=1512333624
# * Gestor de Mapeo
import pandas as pd

import utils
from statistics import mean


# ------------------------------------------------------------
# Subcategoría: Recolección y eliminación de residuos (b1, b2, b3)
# Actividad: Punto de separación y recolección de basura (ob1)
# Características de los basureros y contenedores de basura
# ------------------------------------------------------------
def ob1(mapeo):
    evaluaciones = []
    code = 'dim_medamb_14'
    if not pd.isna(mapeo[code + 'b']) and mapeo[code + 'b'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_nmrb(mapeo[code + 'b']))
    if not pd.isna(mapeo[code + 'c']) and mapeo[code + 'c'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_nmrb(mapeo[code + 'c']))
    if not pd.isna(mapeo[code + 'd']) and mapeo[code + 'd'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_nmrb(mapeo[code + 'd']))
    if not pd.isna(mapeo[code + 'e']) and mapeo[code + 'e'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_nmrb(mapeo[code + 'e']))
    if not pd.isna(mapeo[code + 'f']) and mapeo[code + 'f'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_nmrb(mapeo[code + 'f']))
    if not pd.isna(mapeo[code + 'g']) and mapeo[code + 'g'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_nmrb(mapeo[code + 'g']))
    if not pd.isna(mapeo[code + 'h']) and mapeo[code + 'h'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_nmrb(mapeo[code + 'h']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0


# ------------------------------------------------------------
# Subcategoría: Recolección y eliminación de residuos (b1, b2, b3)
# Actividad: Puntos de acumulación de basura (ob3)
# Lugares donde los residuos se depositan sin un proceso de separación ni reciclaje y se acumulan los desechos
#   no tratados en un área designada.
# ------------------------------------------------------------
def ob3(mapeo):
    evaluaciones = []
    code = 'dim_medamb_16'
    if not pd.isna(mapeo[code + 'b']) and mapeo[code + 'b'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'b']))
    if not pd.isna(mapeo[code + 'c']) and mapeo[code + 'c'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'c']))
    if not pd.isna(mapeo[code + 'd']) and mapeo[code + 'd'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'd']))
    if not pd.isna(mapeo[code + 'e']) and mapeo[code + 'e'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'e']))
    if not pd.isna(mapeo[code + 'f']) and mapeo[code + 'f'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'f']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0


# ------------------------------------------------------------
# Subcategoría: Calidad del aire (b4)
# Actividad: Contaminacion del aire (ob4)
# Presencia de sustancias dañinas en el aire que respiramos, que pueden implicar riesgo, daño o molestia
# ------------------------------------------------------------
def ob4(mapeo):
    evaluaciones = []
    code = 'dim_medamb_18'
    if not pd.isna(mapeo[code + 'a']) and mapeo[code + 'a'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'a']))
    if not pd.isna(mapeo[code + 'b']) and mapeo[code + 'b'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'b']))
    if not pd.isna(mapeo[code + 'c']) and mapeo[code + 'c'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'c']))
    if not pd.isna(mapeo[code + 'd']) and mapeo[code + 'd'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'd']))
    if not pd.isna(mapeo[code + 'e']) and mapeo[code + 'e'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'e']))
    if not pd.isna(mapeo[code + 'f']) and mapeo[code + 'f'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'f']))
    if not pd.isna(mapeo[code + 'g']) and mapeo[code + 'g'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'g']))
    if not pd.isna(mapeo[code + 'h']) and mapeo[code + 'h'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'h']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0


# ------------------------------------------------------------
# Subcategoría: Disponibilidad de agua (b6)
# Actividad: Punto público de agua potable (ob5)
# Instalaciones que proporcionan agua segura y apta para el consumo humano,
# ------------------------------------------------------------
def ob5(mapeo):
    evaluaciones = []
    code = 'dim_medamb_19'
    if not pd.isna(mapeo[code + 'c']) and mapeo[code + 'c'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'c']))
    if not pd.isna(mapeo[code + 'd']) and mapeo[code + 'd'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'd']))
    if not pd.isna(mapeo[code + 'e']) and mapeo[code + 'e'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'e']))
    if not pd.isna(mapeo[code + 'f']) and mapeo[code + 'f'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_mrb(mapeo[code + 'f']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0


# ------------------------------------------------------------
# Subcategoría: Disponibilidad de agua (b6)
# Actividad: Fuentes naturales de agua (ob6)
# Lugares donde el agua se encuentra de manera natural, como ríos, lagos, entre otros
# ------------------------------------------------------------
def ob6(mapeo):
    evaluaciones = []
    code = 'dim_medamb_20'
    if not pd.isna(mapeo[code + 'c']) and mapeo[code + 'c'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'c']))
    if not pd.isna(mapeo[code + 'd']) and mapeo[code + 'd'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'd']))
    if not pd.isna(mapeo[code + 'e']) and mapeo[code + 'e'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'e']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0


# ------------------------------------------------------------
# Subcategoría: Saneamiento e Higiene (b7)
# Actividad: Drenaje y alcantarillado (ob7)
# Área en la que no existe un sistema de tuberías subterráneas o alcantarillas para la eliminación adecuada de
#   aguas residuales y pluviales.
# ------------------------------------------------------------
def ob7(mapeo):
    evaluaciones = []
    code = 'dim_medamb_21'
    if not pd.isna(mapeo[code + 'c']) and mapeo[code + 'c'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'c']))
    if not pd.isna(mapeo[code + 'd']) and mapeo[code + 'd'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'd']))
    if not pd.isna(mapeo[code + 'e']) and mapeo[code + 'e'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'e']))
    if not pd.isna(mapeo[code + 'f']) and mapeo[code + 'f'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'f']))
    if not pd.isna(mapeo[code + 'g']) and mapeo[code + 'g'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'g']))
    if not pd.isna(mapeo[code + 'h']) and mapeo[code + 'h'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'h']))
    if not pd.isna(mapeo[code + 'i']) and mapeo[code + 'i'] != utils.Constants.NINGUNO.value:
        evaluaciones.append(utils.remap_gml(mapeo[code + 'i']))
    if len(evaluaciones) > 0:
        return mean(evaluaciones)
    return 0
