# Dimensión Entorno Urbano

import utils
from statistics import mean


# ------------------------------------------------------------
# Categoría: Urban form / Forma Urbana
# Subcategoría: Mixed uses (a2)
# Availability of facilities and basic servicies within a walking distance that avoid the need for long and
#   motorized trips, according to 15-minute city principles, and ensuring the fullfillment of basic needs such as food,
#   schools and medical care (pharmacyes and healthcare services), carecenters, and public spaces and green areas
# ------------------------------------------------------------
def oa1(df):
    return mean([
        utils.remap_mrb(df["dim_enturb_2c"]),
        utils.remap_mrb(df["dim_enturb_2d"]),
        utils.remap_mrb(df["dim_enturb_2e"])
    ])
