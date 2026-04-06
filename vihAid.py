import matplotlib.pyplot as plt
import pandas as pd
import os

def Mostrar_Bienvenida():
    print("Bienvenido a ... ")
    print("""
 __      __  _____   _    _                       _____   _____
 \ \    / / |_   _| | |  | |              /\     |_   _| |  __ \     Integrantes:
  \ \  / /    | |   | |__| |  ______     /  \      | |   | |  | |    - CHAVEZ AYALA, GERARDO MANUEL        U202314672
   \ \/ /     | |   |  __  | |______|   / /\ \     | |   | |  | |    - LÉVANO MEJÍA, ANDRÉS FABIAN         U202316606
    \  /     _| |_  | |  | |           / ____ \   _| |_  | |__| |    - SORIA ZAPATA, ANGEL AURELIO         U202316237
     \/     |_____| |_|  |_|          /_/    \_\ |_____| |_____/     - VALDIVIEZO LUNA, JAGGER SEBASTIAN   U202315474
    """)
    input('Presiona Enter para continuar')

def R1_Porc_Hombres_Mujeres_VIH_Castilla_Leon():

    df_hombres=df[df['Sexo'] =='H']
    df_mujeres=df[df['Sexo'] =='M']
    porch=100*df_hombres['Sexo'].count()/df['Sexo'].count()
    porcm=100*df_mujeres['Sexo'].count()/df['Sexo'].count()

    porcentajes=[porch,porcm]
    sexos=["Hombres","Mujeres"]
    colores = ["#746ee5","#A3E4D7"]

    plt.pie(porcentajes,
            labels=sexos,
            autopct="%0.1f %%",
            colors=colores,
            startangle=45)

    plt.legend(title="Sexo:",
               labels=sexos,
               loc="center left",
               bbox_to_anchor=(1, 0, 0.5, 1))

    plt.title("Reporte de Porcentaje de Hombres y Mujeres \nRegistrados con VIH en Castilla y León", fontsize=20)
    plt.axis("equal")
    plt.show()

def R2_Provincia_Mayor_Casos_VIH_1982_a_2022():

    ListProvincias = ['Segovia', 'Valladolid', 'Palencia', 'Burgos', 'Salamanca', 'León', 'Avila', 'Zamora', 'Soria']
    provincia_contador = {}

    for provincia in ListProvincias:
        count = (df['provincia'] == provincia).sum()
        provincia_contador[provincia] = count

    total = sum(provincia_contador.values())
    print('Total:', total)
    print('Provincia con más casos de VIH:', max(provincia_contador, key=provincia_contador.get))

    colores = ["#D1F2EB","#A3E4D7","#76D7C4","#48C9B0","#1ABC9C","#17A589","#148F77","#117864","#0E6251"]

    plt.figure(figsize=(9,5))

    plt.bar(provincia_contador.keys(),
            provincia_contador.values(),
            color=colores)

    plt.title('Reporte de la provincia con más casos de VIH', fontsize=20)
    plt.ylabel('Cantidad de casos', fontsize=15)
    plt.show()

def R3_Tendencia_Casos_VIH_2000_a_2022():

    lista_años = [año for año in range(2000, 2023)]
    año_contador={}

    for año in lista_años:
        count = (df['Año de diagnóstico'] == año).sum()
        año_contador[año] = count

    plt.figure(figsize=(9,5))
    plt.grid()

    plt.plot(año_contador.keys(),
             año_contador.values(),
             'bo-')

    plt.title('Tendencia de casos de VIH', fontsize=20)
    plt.xlabel('Años',fontsize=12)
    plt.ylabel('Número de casos',fontsize=12)
    plt.show()

def R4_Promedio_Edades_Según_Década():

    promedios = df.groupby((df['Año de diagnóstico'] // 10) * 10)['Edad años'].mean().astype(int)

    colores = ["#F2D7D5","#E6B0AA","#D98880","#CD6155","#C0392B"]
    lista = ["1980-1989","1990-1999","2000-2009","2010-2019","2020-2022"]

    plt.figure(figsize=(9,5))
    plt.bar(lista,
            promedios.values,
            color=colores)

    for i, v in enumerate(promedios.values):
      plt.text(i, v + 0.2, str(v), ha='center')

    plt.title('Promedio de edad según década', fontsize=20)
    plt.xlabel("Décadas",fontsize=15)
    plt.show()

def R5_Frecuencia_Vías_De_Transmisión_VIH_1982_a_2022():

    Frecuencia_grupos = df.groupby((df['Código Grupo de riesgo'] // 10) * 10)['Código Grupo de riesgo'].count().astype(int)

    lista = ["Varones \nhomosexuales/\nbisexuales\n\n\n 10" , "Personas que \nse inyectan \ndrogas\n\n\n 20",
             "Personas que \nse inyectan drogas/\nVarones homo/\nbisexuales\n\n 30" , "Receptores de \nhemoderivados\n\n\n\n 40",
             "Receptores de \ntransfusión  \n\n\n\n 50" , "Hijo de madre \na riesgo \n\n\n\n 60",
             "Relaciones \nHeterosexuales \n\n\n\n 70" , "Grupo de riesgo \ndesconocido\n\n\n\n 80"]

    colores = ["#E5E8E8","#CCD1D1","#B2BABB","#99A3A4","#7F8C8D", "#707B7C","#616A6B","#515A5A"]

    plt.figure(figsize=(15,5))

    plt.bar(lista,
            Frecuencia_grupos.values,
            color = colores)

    plt.title("Frecuencia de las principales \nvías de transmisión de VIH entre 1982 y 2022", fontsize=20)
    plt.xlabel("\nCódigo de grupo", fontsize=15)
    plt.ylabel("Frecuencia", fontsize=15)
    plt.show()

def Menu():
    print('Lista de reportes')
    print("""
    1- Reporte de porcentaje de hombres y mujeres registrados con VIH en Castilla y León.
    2- Reporte de la provincia con más casos de VIH entre los años 1982 - 2022.
    3- Reporte de la tendencia de casos de VIH registrados entre los años 2000 - 2022.
    4- Reporte de promedio de edades, según la década, de pacientes de VIH.
    5- Reporte de la frecuencia de las principales vías de transmisión del VIH entre los años 1982 - 2022.
    6- Visualizar Dataframe.
    7- Salir del programa.
    """)

###############################################################################
df = pd.read_csv('/content/drive/MyDrive/poo2/Excel_VIH.csv',delimiter = ';')
###############################################################################

os.system('cls')
Mostrar_Bienvenida()

def main():

 while True:
  os.system('cls')
  Menu()
  reporte = 0
  reporte = int(input("Ingresa el reporte que quieres ver(1-7): "))
  if reporte == 1:
    os.system('cls')
    R1_Porc_Hombres_Mujeres_VIH_Castilla_Leon()
  elif reporte == 2:
    os.system('cls')
    R2_Provincia_Mayor_Casos_VIH_1982_a_2022()
  elif reporte == 3:
    os.system('cls')
    R3_Tendencia_Casos_VIH_2000_a_2022()
  elif reporte == 4:
    os.system('cls')
    R4_Promedio_Edades_Según_Década()
  elif reporte == 5:
    os.system('cls')
    R5_Frecuencia_Vías_De_Transmisión_VIH_1982_a_2022()
  elif reporte == 6:
    os.system('cls')
    print(df)
    input('\nPresione para continuar')
  else:
    os.system('cls')
    print('Adiós!')
    exit()

if __name__ == "__main__":
  main()
