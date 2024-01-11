# Bienestar socioeconomico
# Referencias:
# * https://docs.google.com/spreadsheets/d/1owfdwKv25AkBEb5QuA0nNwKj4LoEXVo2/edit#gid=1512333624
# * Gestor de Mapeo

import utils


# ------------------------------------------------------------
# Subcategoría: Recolección y eliminación de residuos (b1, b2, b3)
# Actividad: Punto de separación y recolección de basura (ob1)
# Características de los basureros y contenedores de basura
# ------------------------------------------------------------
def ob1(mapeo):
    code = 'dim_medamb_14'
    letters = ['b', 'c', 'd', 'e', 'f', 'g', 'h']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Recolección y eliminación de residuos (b1, b2, b3)
# Actividad: Puntos de acumulación de basura (ob3)
# Lugares donde los residuos se depositan sin un proceso de separación ni reciclaje y se acumulan los desechos
#   no tratados en un área designada.
# ------------------------------------------------------------
def ob3(mapeo):
    code = 'dim_medamb_16'
    letters = ['b', 'c', 'd', 'e', 'f']
    return utils.calculate_score(mapeo, code, letters, utils.remap_gml)


# ------------------------------------------------------------
# Subcategoría: Calidad del aire (b4)
# Actividad: Contaminacion del aire (ob4)
# Presencia de sustancias dañinas en el aire que respiramos, que pueden implicar riesgo, daño o molestia
# ------------------------------------------------------------
def ob4(mapeo):
    code = 'dim_medamb_18'
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return utils.calculate_score(mapeo, code, letters, utils.remap_gml)


# ------------------------------------------------------------
# Subcategoría: Disponibilidad de agua (b6)
# Actividad: Punto público de agua potable (ob5)
# Instalaciones que proporcionan agua segura y apta para el consumo humano,
# ------------------------------------------------------------
def ob5(mapeo):
    code = 'dim_medamb_19'
    letters = ['c', 'd', 'e', 'f']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Disponibilidad de agua (b6)
# Actividad: Fuentes naturales de agua (ob6)
# Lugares donde el agua se encuentra de manera natural, como ríos, lagos, entre otros
# ------------------------------------------------------------
def ob6(mapeo):
    code = 'dim_medamb_20'
    letters = ['c', 'd', 'e']
    return utils.calculate_score(mapeo, code, letters, utils.remap_gml)


# ------------------------------------------------------------
# Subcategoría: Saneamiento e Higiene (b7)
# Actividad: Drenaje y alcantarillado (ob7)
# Área en la que no existe un sistema de tuberías subterráneas o alcantarillas para la eliminación adecuada de
#   aguas residuales y pluviales.
# ------------------------------------------------------------
def ob7(mapeo):
    code = 'dim_medamb_21'
    letters = ['c', 'd', 'e', 'f', 'g', 'h', 'i']
    return utils.calculate_score(mapeo, code, letters, utils.remap_gml)
