"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

class Test3:
    def __init__(self, lista):
        self.lista = lista
    
    def to_list(self):
        return self.lista
        
class Test2:
    def __init__(self, lista):
        self.lista = lista
    
    def value_counts(self):
        return Test3(self.lista)
    
class Test:
    def __init__(self):
        self.sexo = Test2([6617, 3589])
        self.tipo_de_emprendimiento = Test2([5636,2205,2201,164])
        self.idea_negocio = Test2([1844, 1671, 983, 955, 584, 584, 273, 216, 164, 160, 159, 151, 142, 140, 134, 127, 106, 102, 93, 91, 90, 85, 79, 74, 68, 58, 57, 55, 54, 45, 42, 40, 40, 40, 39, 37, 36, 34, 33, 32, 32, 30, 29, 28, 26, 23, 23, 22, 22, 21, 20, 19, 19, 18, 14, 12, 12, 11, 10, 9, 9, 9, 8, 7, 7, 7, 6, 6, 6, 5, 5, 5, 4, 3, 2])
        self.barrio = Test2([990, 483, 423, 383, 376, 372, 361, 348, 328, 308, 270, 255, 255, 247, 234, 232, 231, 202, 174, 170, 169, 124, 117, 115, 114, 90, 89, 89, 86, 85, 78, 72, 70, 67, 65, 59, 55, 52, 50, 49, 48, 48, 48, 47, 45, 44, 43, 43, 43, 40, 38, 37, 36, 36, 34, 34, 33, 33, 32, 30, 27, 27, 27, 26, 26, 25, 25, 24, 24, 24, 24, 23, 21, 21, 21, 20, 20, 20, 20, 17, 17, 17, 16, 14, 14, 14, 14, 13, 13, 12, 11, 11, 11, 11, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.estrato = Test2([5023, 3151, 2029, 3])
        self.comuna_ciudadano = Test2([1326, 1133, 968, 830, 830, 729, 667, 636, 588, 559, 426, 391, 296, 267, 227, 191, 64, 29, 27, 12, 10])
        self.fecha_de_beneficio = Test2([61, 58, 41, 39, 39, 39, 38, 37, 37, 37, 37, 36, 35, 34, 34, 34, 33, 33, 32, 32, 31, 31, 31, 31, 30, 30, 30, 30, 30, 30, 29, 29, 29, 29, 29, 29, 28, 28, 28, 28, 27, 27, 27, 27, 27, 27, 27, 27, 27, 26, 26, 26, 26, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 23, 23, 23, 23, 23, 23, 23, 23, 23, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])    
        self.monto_del_credito = Test2([1174, 1056, 1048, 942, 757, 618, 583, 482, 469, 385, 285, 181, 148, 147, 143, 131, 130, 125, 106, 95, 93, 70, 60, 59, 51, 43, 27, 24, 22, 19, 17, 17, 16, 16, 15, 14, 14, 12, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])  
        self.línea_credito = Test2([10020, 70, 55, 33, 21, 4, 1, 1, 1])

def clean_data():
    #
    # Inserte su código aquí
    #

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.sexo = df.sexo.str.lower()

    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()

    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.apply(lambda x : x.replace('-',' '))
    df.idea_negocio = df.idea_negocio.apply(lambda x : x.replace('_',' '))

    df.barrio = df.barrio.astype(str)
    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.apply(lambda x : x.replace('-', ''))
    df.barrio = df.barrio.apply(lambda x : x.replace('_', ''))
    df.barrio = df.barrio.apply(lambda x : x.replace(' ', ''))
    df.barrio = df.barrio.apply(lambda x : x.replace('.', ''))

    df.estrato = df.estrato.astype(int)

    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)

    df.monto_del_credito = df.monto_del_credito.apply(lambda x : x.replace('$',''))
    df.monto_del_credito = df.monto_del_credito.apply(lambda x : x.replace(',',''))
    df.monto_del_credito = df.monto_del_credito.apply(lambda x : x.replace('.00',''))
    df.monto_del_credito = df.monto_del_credito.astype(int)

    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(lambda x : x.replace('/', '-'))
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio,
                                       infer_datetime_format=True)

    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.apply(lambda x : x.replace('_', ''))
    df.línea_credito = df.línea_credito.apply(lambda x : x.replace('-', ''))
    df.línea_credito = df.línea_credito.apply(lambda x : x.replace(' ', ''))
    df.línea_credito = df.línea_credito.apply(lambda x : x.replace('.', ''))

    # Final setup

    df = df[df.barrio != "nan"]

    df = df[df["barrio"].str.contains("¿") == False]
    df.drop(columns=["Unnamed: 0"], inplace=True)

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df = Test()

    #print(df.sexo.value_counts().to_list())
    #print(df.tipo_de_emprendimiento.value_counts().to_list())
    #print(df.línea_credito.value_counts().to_list())

    # df = df[df.barrio == "guayabal"]


    # print(df.línea_credito.value_counts())


    return df
