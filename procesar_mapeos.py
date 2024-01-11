import pandas as pd

import biesoc
import enturb
import medamb
import riedes


def main():
    csv_file_path = 'data/mapeo_hermosillo_datos.csv'
    df = pd.read_csv(csv_file_path)
    resultados = df.sort_values(by=['category_name', 'activity_title'])
    resultados = resultados.iloc[:, 0:12]

    for index, row in df.iterrows():
        if row['activity_id'] == 0:
            resultados.at[index, 'puntuacion'] = None
        # ------------------------------
        # Entorno urbano
        # ------------------------------
        elif row['activity_id'] == 122:  # OA1 Edificios publicos, tiendas y lugares para la comunidad
            resultados.at[index, 'puntuacion'] = enturb.oa1(row)
        elif row['activity_id'] == 124:  # OA2 Paradas de transporte publico
            resultados.at[index, 'puntuacion'] = enturb.oa2(row)
        elif row['activity_id'] == 125:  # OA3 POTENCIAL Paradas de transporte publico
            resultados.at[index, 'puntuacion'] = None
        elif row['activity_id'] == 120:  # OA4 Ciclovías y calles para ciclistas existentes
            resultados.at[index, 'puntuacion'] = enturb.oa4(row)
        elif row['activity_id'] == 119:  # OA5 POTENCIAL Ciclovias y biciestacionamientos
            resultados.at[index, 'puntuacion'] = None
        elif row['activity_id'] == 118:  # OA6 Biciestacionamientos
            resultados.at[index, 'puntuacion'] = enturb.oa6(row)
        elif row['activity_id'] == 116:  # OA7 Banquetas y caminos
            resultados.at[index, 'puntuacion'] = enturb.oa7(row)
        elif row['activity_id'] == 121:  # OA8 Cruces peatonales
            resultados.at[index, 'puntuacion'] = enturb.oa8(row)
        elif row['activity_id'] == 117:  # OA9 POTENCIAL Banquetas y cruces
            resultados.at[index, 'puntuacion'] = None
        elif row['activity_id'] == 123:  # OA10 Espacios publicos y areas verdes
            resultados.at[index, 'puntuacion'] = enturb.oa10(row)
        elif row['activity_id'] == 126:  # OA11 Siniestro vial
            resultados.at[index, 'puntuacion'] = enturb.oa11(row)
        # ------------------------------
        # Calidad medioambiental
        # ------------------------------
        elif row['activity_id'] == 113:  # OB1 Punto de separación y recolección de basura
            resultados.at[index, 'puntuacion'] = medamb.ob1(row)
        elif row['activity_id'] == 112:  # OB2 POTENCIAL Punto de recoleccion de basura
            resultados.at[index, 'puntuacion'] = None
        elif row['activity_id'] == 115:  # OB3 Puntos de acumulacion de basura
            resultados.at[index, 'puntuacion'] = medamb.ob3(row)
        elif row['activity_id'] == 109:  # OB4 Contaminacion del aire
            resultados.at[index, 'puntuacion'] = medamb.ob4(row)
        elif row['activity_id'] == 114:  # OB5 Punto publico de agua potable
            resultados.at[index, 'puntuacion'] = medamb.ob5(row)
        elif row['activity_id'] == 111:  # OB6 Fuentes naturales de agua
            resultados.at[index, 'puntuacion'] = medamb.ob6(row)
        elif row['activity_id'] == 110:  # OB7 Drenaje y alcantarillado
            resultados.at[index, 'puntuacion'] = medamb.ob7(row)
        # ------------------------------
        # Bienestar socioeconómico
        # ------------------------------
        elif row['activity_id'] == 104:  # OC1 Actividades de comercio local
            resultados.at[index, 'puntuacion'] = biesoc.oc1(row)
        elif row['activity_id'] == 108:  # OC2 Puntos de internet
            resultados.at[index, 'puntuacion'] = biesoc.oc2(row)
        elif row['activity_id'] == 107:  # OC3 Mercados locales, fruterías, verdulerías
            resultados.at[index, 'puntuacion'] = biesoc.oc3(row)
        elif row['activity_id'] == 103:  # OC4 Actividades culturales
            resultados.at[index, 'puntuacion'] = biesoc.oc4(row)
        elif row['activity_id'] == 105:  # OC5 Actividades de participacion comunitaria
            resultados.at[index, 'puntuacion'] = biesoc.oc5(row)
        elif row['activity_id'] == 106:  # OC6 Actividades deportivas
            resultados.at[index, 'puntuacion'] = biesoc.oc6(row)
        # ------------------------------
        # Riesgo desastres
        # ------------------------------
        elif row['activity_id'] == 128:  # OD6 Espacios de contingencia frente a catastrofes
            resultados.at[index, 'puntuacion'] = None
        elif row['activity_id'] == 132:  # OD1 Riesgo geologico
            resultados.at[index, 'puntuacion'] = riedes.od1(row)
        elif row['activity_id'] == 133:  # OD2 Riesgo hidrometeorologico
            resultados.at[index, 'puntuacion'] = riedes.od2(row)
        elif row['activity_id'] == 129:  # OD3 Riesgo ambiental
            resultados.at[index, 'puntuacion'] = riedes.od3(row)
        elif row['activity_id'] == 130:  # OD4 Riesgo antropogenico
            resultados.at[index, 'puntuacion'] = riedes.od4(row)
        elif row['activity_id'] == 131:  # OD5 Riesgo biologico
            resultados.at[index, 'puntuacion'] = riedes.od5(row)
        # ------------------------------
        # Otra
        # ------------------------------
        elif row['activity_id'] == 127:  # Mapeo libre
            resultados.at[index, 'puntuacion'] = None

    resultados = resultados[resultados['puntuacion'].notna()]
    resultados_file_path = 'data/export/resultados_hermosillo.csv'
    resultados.to_csv(resultados_file_path, index=False)


if __name__ == "__main__":
    main()
