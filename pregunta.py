"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    #
    # Inserte su código aquí
    #

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.sexo = df.sexo.str.lower()

    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()

    df.idea_negocio = df.idea_negocio.str.lower()

    df.barrio = df.barrio.str.lower()

    df.estrato = df.estrato.astype(int)

    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)

    df.monto_del_credito = df.monto_del_credito.apply(lambda x : x.replace('$',''))
    df.monto_del_credito = df.monto_del_credito.apply(lambda x : x.replace(',',''))
    df.monto_del_credito = df.monto_del_credito.apply(lambda x : x.replace('.00',''))
    df.monto_del_credito = df.monto_del_credito.astype(int)

    df.línea_credito = df.línea_credito.str.lower()

    return df
