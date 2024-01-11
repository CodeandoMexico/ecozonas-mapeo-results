# Bienestar socioeconomico
# Referencias:
# * https://docs.google.com/spreadsheets/d/1owfdwKv25AkBEb5QuA0nNwKj4LoEXVo2/edit#gid=1512333624
# * Gestor de Mapeo

import utils


# ------------------------------------------------------------
# Subcategoría: Empleo y emprendimiento (c1)
# Actividad: Actividades de comercio local
# Actividades de comercio y servicios realizados por individuos o pequeñas empresas que buscan generar ingresos y crear
#   empleo en el barrio
# ------------------------------------------------------------
def oc1(mapeo):
    code = 'dim_biensoc_22'
    letters = ['c', 'd', 'e', 'f', 'g']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Sistemas alimentarios (c8)
# Actividad: Mercados locales, fruterías, verdulerías (oc3)
# ------------------------------------------------------------
def oc3(mapeo):
    code = 'dim_biensoc_24'
    letters = ['c', 'd', 'e', 'f', 'g', 'h']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Digitalización (c4)
# Actividad: Puntos de internet (oc2)
# ------------------------------------------------------------
def oc2(mapeo):
    code = 'dim_biensoc_23'
    letters = ['c']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Cultura e identidad (c9)
# Actividad: Actividades culturales (oc4)
# Expresiones y eventos que celebran y promueven la cultura e identidad de una comunidad
# ------------------------------------------------------------
def oc4(mapeo):
    code = 'dim_biensoc_25'
    letters = ['c', 'd', 'e', 'f', 'g']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Participación de la comunidad (c10)
# Actividad: Actividades de participación comunitaria (oc5)
# Actividades y acciones en las que las personas se involucran activamente para abordar temas o desafíos locales de
#   su comunidad
# ------------------------------------------------------------
def oc5(mapeo):
    code = 'dim_biensoc_26'
    letters = ['c', 'd', 'e', 'f', 'g']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Cultura e identidad (c9)
# Actividad: Actividades desportivas (oc6)
# ------------------------------------------------------------
def oc6(mapeo):
    code = 'dim_biensoc_27'
    letters = ['c', 'd', 'e', 'f', 'g']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)
