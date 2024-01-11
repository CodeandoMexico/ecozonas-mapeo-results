# Dimensión Riesgo Desastres
# Referencias:
# * https://docs.google.com/spreadsheets/d/1owfdwKv25AkBEb5QuA0nNwKj4LoEXVo2/edit#gid=1512333624
# * Gestor de Mapeo

import utils


# ------------------------------------------------------------
# Subcategoría: Riesgo geologico (d2)
# Actividad: Riesgo geologico (od1)
# Eventos originados de procesos internos de la tierra
# ------------------------------------------------------------
def od1(mapeo):
    code_veces = 'dim_riesdes_28b'
    code = 'dim_riesdes_28'
    letters = ['c', 'd', 'e', 'f', 'g']
    return utils.calculate_score_riesgo(mapeo, code_veces, code, letters)


# ------------------------------------------------------------
# Subcategoría: Riesgo hidrometeorológico (d3)
# Actividad: Riesgo hidrometeorológico (od2)
# Relacionados con el agua subterránea y la interacción entre el agua y el suelo
# ------------------------------------------------------------
def od2(mapeo):
    code_veces = 'dim_riesdes_29b'
    code = 'dim_riesdes_29'
    letters = ['c', 'd', 'e', 'f', 'g']
    return utils.calculate_score_riesgo(mapeo, code_veces, code, letters)


# ------------------------------------------------------------
# Subcategoría: Riesgo ambiental (d1)
# Actividad: Riesgo ambiental (od3)
# Peligros associados a daños en el entorno natural, incluyendo los ecosistemas, la biodiversidad y los
#   recursos naturales, así como en la salud y el bienestar de las personas
# ------------------------------------------------------------
def od3(mapeo):
    code_veces = 'dim_riesdes_30b'
    code = 'dim_riesdes_30'
    letters = ['c', 'd', 'e', 'f', 'g']
    return utils.calculate_score_riesgo(mapeo, code_veces, code, letters)


# ------------------------------------------------------------
# Subcategoría: Riesgos antropogénicos (d5)
# Actividad: Riesgos antropogénicos (od4)
# Riesgos asociados a la contaminación causada por actividades humanas (agua, suelo, aire)
# ------------------------------------------------------------
def od4(mapeo):
    code_veces = 'dim_riesdes_31b'
    code = 'dim_riesdes_31'
    letters = ['c', 'd', 'e', 'f', 'g']
    return utils.calculate_score_riesgo(mapeo, code_veces, code, letters)


# ------------------------------------------------------------
# Subcategoría: Riesgos biologicos (d4)
# Actividad: Riesgos biologicos (od5)
# Se refieren a las amenazas derivadas de organismos vivos (bacterias, virus, hongos, etc.) y otros seres vivos que
#   pueden causar enfermedades o daños a los seres humanos, animales o plantas
# ------------------------------------------------------------
def od5(mapeo):
    code_veces = 'dim_riesdes_32b'
    code = 'dim_riesdes_32'
    letters = ['c', 'd', 'e', 'f', 'g']
    return utils.calculate_score_riesgo(mapeo, code_veces, code, letters)
