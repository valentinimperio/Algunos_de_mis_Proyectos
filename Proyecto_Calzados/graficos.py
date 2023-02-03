#######################################################################

# Proyecto Final - Inove Escuela de Código
# Tema Elegido: Python Analytics

# Alumno: Valentín Imperio.
# Versión: 1.0
# Profesores: Johana Rangel y Julián Salinas.
# Curso: Programador Python.
# Fecha de Entrega: 28/01/2023

# ARCHIVO BONUS: GRAFICOS.PY

#######################################################################

#### Librerías utilizadas ###

import matplotlib.pyplot as plt
import numpy as np
from main import read_db, ventas_pais, calzado_pais, ventas_genero_pais

# GRAFICOS DEL PROYECTO #

# Gráfico para Ventas por país

def grafico_ventas(countries, country, price):
    dict = ventas_pais(countries, country, price)

    def func(pct, allvals):
        absolute = int(np.round(pct/100.*np.sum(allvals)))
        return "{:.1f}%\n({:d} $)".format(pct, absolute)

    X = list(dict.values())
    Y = dict.keys()

    # Creo mi paleta de colores: 
    colors = ["#7FFFD4","#13EAC9","#04D8B2","#008080"]
    fig = plt.figure() 
    fig.suptitle("Ventas de calzado por país", fontsize = 16, weight = "bold")
    ax = fig.add_subplot()
    ax.pie(X, labels=Y, colors = colors,  autopct=lambda pct: func(pct, X), wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'})
    ax.set_title("En Dólares [$]", fontsize = 12)
    ax.axis("equal")
    plt.show()

# Gráfico para N° de calzado por país

def grafico_calzado(countries, country, size):
    dict = calzado_pais(countries, country, size)

    X = list(dict.keys())
    Y = [float(x) for x in list(dict.values())]
   
    fig = plt.figure() 
    ax = fig.add_subplot()
    ax.bar(X,Y, color="tab:purple", label="Países")
    ax.set_title("Tamaño de calzado más vendido en cada país ", fontsize = 10, weight = "bold")
    ax.set_ylabel(" Tamaño (N° de calzado) ")
    ax.set_xlabel(" Países ")
    ax.legend()
    plt.xticks(X)
    plt.ylim(top=10)
    plt.show() 

# Gráfico para cantidad de ventas por genero elegido para cada país

def grafico_genero_pais(countries, gender_target, country, gender):

    dict = ventas_genero_pais(countries, gender_target, country, gender)

    def func(pct, allvals):
        absolute = int(np.round(pct/100.*np.sum(allvals)))
        return "{:.1f}%\n({:d} u)".format(pct, absolute)

    X = list(dict.values())
    Y = dict.keys()

    # Creo mi paleta de colores: 
    colors = ["#0343DF","#069AF3","#7BC8F6","#000080"]
    fig = plt.figure() 
    fig.suptitle("Ventas de calzado para el genero "+gender_target+" por país", fontsize = 16, weight = "bold")
    ax = fig.add_subplot()
    _, _, autotexts = ax.pie(X, labels=Y, colors = colors,  autopct=lambda pct: func(pct, X), wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'})
    for ins in autotexts:
        ins.set_color('white')
    ax.set_title("En pares [u]", fontsize = 12)
    ax.axis("equal")
    plt.show()


####### Bloque principal del programa #######

if __name__ == "__main__":

    data = read_db()
    country = data[0]
    gender = data[1]
    size = data[2]
    price = data[3]
    countries = ["Canada","Germany","United States", "United Kingdom"]
    gender_target = "Male" # Las opciones a analizar son: "Female", "Male" y "Unix"
    
    grafico_ventas(countries, country, price)
    
    grafico_calzado(countries, country, size)

    grafico_genero_pais(countries, gender_target, country, gender)

    print("Termine! Que buen programa soy ^^")