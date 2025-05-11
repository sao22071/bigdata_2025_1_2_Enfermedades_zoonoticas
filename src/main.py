import pandas as pd
from database import DataBase

def main():
    df = pd.DataFrame()
    df = pd.read_csv('src/static/cvs/enfermzoonoticas.csv',encoding='latin1')
    print("*************** impresión de los datos obtenidos ************************")
    print(df)
    print(df.head())
    nombre_tabla = "enfermedades_zoonoticas"
    database.insert_data(df,nombre_tabla)
    #print("*************** Insertar los datos obtenidos en la base datos tabla: {}*********".format(nombre_tabla))


if __name__ == "__main__":
    main()