import pandas as pd

import biesoc
import medamb


def main():
    csv_file_path = 'data/mapeo_hermosillo_datos.csv'
    df = pd.read_csv(csv_file_path)
    resultados = df.sort_values(by=['category_name', 'activity_title'])
    resultados = resultados.iloc[:, 0:12]

    for index, row in df.iterrows():
        # ------------------------------
        # Bienestar socioeconómico
        # ------------------------------
        if row['activity_id'] == 104:  # Actividades de comercio local
            resultados.at[index, 'puntuacion'] = biesoc.oc1(row)
        elif row['activity_id'] == 108:  # Puntos de internet
            resultados.at[index, 'puntuacion'] = biesoc.oc2(row)
        elif row['activity_id'] == 107:  # Mercados locales, fruterías, verdulerías
            resultados.at[index, 'puntuacion'] = biesoc.oc3(row)
        elif row['activity_id'] == 103:  # Actividades culturales
            resultados.at[index, 'puntuacion'] = biesoc.oc4(row)
        elif row['activity_id'] == 105:  # Actividades de participacion comunitaria
            resultados.at[index, 'puntuacion'] = biesoc.oc5(row)
        elif row['activity_id'] == 106:  # Actividades deportivas
            resultados.at[index, 'puntuacion'] = biesoc.oc6(row)
        # ------------------------------
        # Calidad medioambiental
        # ------------------------------
        elif row['activity_id'] == 113:  # Punto de separación y recolección de basura
            resultados.at[index, 'puntuacion'] = medamb.ob1(row)
        elif row['activity_id'] == 112:  # POTENCIAL Punto de recoleccion de basura (ob2)
            resultados.at[index, 'puntuacion'] = None
        elif row['activity_id'] == 115:  # Puntos de acumulacion de basura
            resultados.at[index, 'puntuacion'] = medamb.ob3(row)
        elif row['activity_id'] == 109:  # Contaminacion del aire
            resultados.at[index, 'puntuacion'] = medamb.ob4(row)
        elif row['activity_id'] == 114:  # Punto publico de agua potable
            resultados.at[index, 'puntuacion'] = medamb.ob5(row)
        elif row['activity_id'] == 111:  # Fuentes naturales de agua
            resultados.at[index, 'puntuacion'] = medamb.ob6(row)
        elif row['activity_id'] == 110:  # Drenaje y alcantarillado
            resultados.at[index, 'puntuacion'] = medamb.ob7(row)

    resultados = resultados[resultados['puntuacion'].notna()]
    resultados['puntuacion'] = resultados['puntuacion'].apply(lambda x: int(round(x)))
    resultados_file_path = 'data/export/resultados_hermosillo.csv'
    resultados.to_csv(resultados_file_path, index=False)


if __name__ == "__main__":
    main()
