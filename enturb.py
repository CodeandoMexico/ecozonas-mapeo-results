# Dimensión Entorno Urbano

import utils


# ------------------------------------------------------------
# Subcategoría: Usos mixtos (a2)
# Actividad: Edificios públicos, tiendas y lugares para la comunidad (oa1)
# ------------------------------------------------------------
def oa1(mapeo):
    code = 'dim_enturb_2'
    letters = ['c', 'd', 'e']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Paradas de transporte público (a8, a15)
# Actividad: Paradas de transporte público existentes (oa2)
# ------------------------------------------------------------
def oa2(mapeo):
    code = 'dim_enturb_3'
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Ciclabilidad (a10)
# Actividad: Ciclovías y calles para ciclistas existentes (oa4)
# ------------------------------------------------------------
def oa4(mapeo):
    code = 'dim_enturb_5'
    letters = ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    return utils.calculate_score(mapeo, code, letters, utils.remap_gml)


# ------------------------------------------------------------
# Subcategoría: Ciclabilidad (a10)
# Actividad: Biciestacionamientos existentes (oa6)
# ------------------------------------------------------------
def oa6(mapeo):
    code = 'dim_enturb_7'
    letters = ['a', 'b', 'c', 'd']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Caminabilidad (a11, a15)
# Actividad: Banquetas y caminos (oa7)
# Áreas destinadas para que las personas transiten a pie
# ------------------------------------------------------------
def oa7(mapeo):
    code = 'dim_enturb_9'
    letters = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    return utils.calculate_score(mapeo, code, letters, utils.remap_gml)


# ------------------------------------------------------------
# Subcategoría: Caminabilidad (a11)
# Actividad: Cruces peatonales (oa8)
# Lugares en las  calles , avenidas y carreteras donde las personas pueden atravesar de un lado al otro con
#   mayor seguridad
# ------------------------------------------------------------
def oa8(mapeo):
    code = 'dim_enturb_10'
    letters = ['b', 'c', 'd', 'e', 'f']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Espacios públicos y áreas verdes (a12, a15)
# Actividad: Espacios públicos y áreas verdes (oa10)
# Áreas de uso común que están disponibles para todas las personas
# ------------------------------------------------------------
def oa10(mapeo):
    code = 'dim_enturb_12'
    letters = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
    return utils.calculate_score(mapeo, code, letters, utils.remap_nmrb)


# ------------------------------------------------------------
# Subcategoría: Seguridad vial (a14)
# Actividad: Siniestro vial (oa11)
# Evento en el que dos o más vehículos se ven involucrados, lo cual puede resultar en daños materiales, lesiones
#   o fallecimientos.
# ------------------------------------------------------------
def oa11(mapeo):
    code = 'dim_enturb_13'
    letters = ['a', 'b', 'c']
    return utils.calculate_score(mapeo, code, letters, utils.remap_gml)
