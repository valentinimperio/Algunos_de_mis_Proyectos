#######################################################################

# Proyecto Final - Inove Escuela de Código
# Tema Elegido: Python Analytics

# Alumno: Valentín Imperio.
# Versión: 1.0
# Profesores: Johana Rangel y Julián Salinas.
# Curso: Programador Python.
# Fecha de Entrega: 28/01/2023

# ARCHIVO PRINCIPAL: MAIN.PY

#######################################################################

# DESARROLLO DEL PROYECTO #

#### Librerías utilizadas ###

import numpy as np
import re # Para convertir a float y remover $
import sqlalchemy
from sqlalchemy import Column, Integer, String # Herramientas para crear la tabla.
from sqlalchemy.ext.declarative import declarative_base # Molde para tablas de bases de datos.
from sqlalchemy.orm import sessionmaker # Sirve para poder iniciar la sesión


### Creación del motor (engine) de la base de datos

engine = sqlalchemy.create_engine("sqlite:///ventas_calzados.db")
base = declarative_base()


###### Creación de la Clase Ventas ######
# Para armar la estructura de la tabla dada (visualizador de bases de datos en
# https://extendsclass.com/sqlite-browser.html) con el ORM de SqlAlchemy se
# genera la siguiente clase.

class Ventas(base):
    __tablename__ = "venta"
    id = Column(Integer , primary_key=True)
    date = Column(String,nullable=True)
    product_id = Column(Integer,nullable=True)
    country = Column(String,nullable=True)
    gender = Column(String,nullable=True)
    size = Column(String,nullable=True)
    price = Column(String,nullable=True)
    
    def __repr__(self): # Método informativo
        return f"Producto ID {self.product_id} del país {self.country}, género {self.gender} \
        \n tamaño {self.size}, precio {self.price} en la fecha {self.date}"

####### Funciones #######

# Función READ_DB: Para leer la base de datos ventas_calzado.db y organizar los datos.
def read_db(limit=10):

    # Crear la sesión
    Sesion = sessionmaker(bind=engine)
    sesion = Sesion()

    # Buscar todas las ventas
    query = sesion.query(Ventas)

    # Aplica el limite si está definido
    if limit > 0:
        query1 = query.limit(limit)

    # Leer una venta a la vez e imprime en pantalla
    print("Estos son los primeros 10 datos de la tabla ORIGINAL")
    for venta in query1:
        print(venta) 
    
    nro_filas=query.count()
    print("La tabla ORIGINAL tiene",nro_filas,"filas.") #14967

    # Se eliminan las filas que tengan un valor nulo
    print("\n")
    print("Removiendo filas con valores vacíos...")
    print("\n")

    # Estas son las filas con valores nulos.
    query2 = sesion.query(Ventas).filter(
        (Ventas.date == "") |
        (Ventas.product_id == "") |
        (Ventas.country == "") |
        (Ventas.gender == "") |
        (Ventas.size == "") |
        (Ventas.price == "")
        )
    nro_filas2 = query2.count()
    print("Se eliminaran",nro_filas2,"filas de la tabla por datos faltantes") #120
    print("\n")

    # Se procede a borrar las filas mencionadas.
    sesion.query(Ventas).filter(
        (Ventas.date == "") |
        (Ventas.product_id == "") |
        (Ventas.country == "") |
        (Ventas.gender == "") |
        (Ventas.size == "") |
        (Ventas.price == "")
        ).delete()

    sesion.commit() # Para guardar los cambios.

    # Se vuelve a hacer la consulta para ver la tabla filtrada
    query = sesion.query(Ventas)

    # Aplica el limite si está definido
    if limit > 0:
        query1 = query.limit(limit)

    print("Estos son los primeros 10 datos de la tabla FILTRADA")
    for venta in query1:
        print(venta) 
    nro_filas3 = query.count()
    print("Quedan",nro_filas3,"filas en la tabla.") #14847

    query3 = sesion.query(Ventas)
    country = np.array([])
    gender = np.array([])
    size = np.array([])
    price = np.array([])

    for i in query3:
        country = np.append(country, i.country)
        gender = np.append(gender,i.gender) 
        size = np.append(size,i.size)
        price_str = " ".join(i.price)
        price_i = float(re.sub(r'[^\d\-.]', '', price_str)) # Sacar $ y pasar a float
        price = np.append(price,price_i)

    return country, gender, size, price

# Función PAÍSES ÚNICOS: Para ver en qué países hubo ventas:
def paises_unicos(country):

    paises_unicos = np.unique(country)
    print(paises_unicos)

def ventas_pais(countries, country, price):

    # Crear unas máscaras para obtener los índices del array
    # que corresponden a los paises
    mask_0 = country == countries[0] #"Canada"
    mask_1 = country == countries[1] #"Germany"
    mask_2 = country == countries[2] #"United States"
    mask_3 = country == countries[3] #"United Kingdom"

    # Utilizo las máscaras para acceder a los indices del array price
    # que corresponden a cada pais
    ventas_canada = price[mask_0]
    ventas_germany = price[mask_1]
    ventas_united_states = price[mask_2]
    ventas_united_kingdom = price[mask_3]

    suma_canada = np.sum(ventas_canada)
    suma_germany = np.sum(ventas_germany)
    suma_united_states = np.sum(ventas_united_states)
    suma_united_kingdom = np.sum(ventas_united_kingdom)

    Countries_dict = {}
    Countries_dict.update({ countries[0]: suma_canada, countries[1]: suma_germany, countries[2]: suma_united_states, countries[3]: suma_united_kingdom})

    return(Countries_dict)

# Función CALZADO PAÍS: Para ver qué tamaño fue el más vendido en cada país.
def calzado_pais(countries, country, size):

    # Crear unas máscaras para obtener los índices del array
    # que corresponden a los paises
    mask_0 = country == countries[0] #"Canada"
    mask_1 = country == countries[1] #"Germany"
    mask_2 = country == countries[2] #"United States"
    mask_3 = country == countries[3] #"United Kingdom"

    # Utilizo las máscaras para acceder a los indices del array size
    # que corresponden a cada pais
    tamaño_canada = size[mask_0]
    tamaño_germany = size[mask_1]
    tamaño_united_states = size[mask_2]
    tamaño_united_kingdom = size[mask_3]

    sizes_canada = np.unique(tamaño_canada,return_counts=True)
    sizes_germany = np.unique(tamaño_germany,return_counts=True)
    sizes_united_states = np.unique(tamaño_united_states,return_counts=True)
    sizes_united_kingdom = np.unique(tamaño_united_kingdom,return_counts=True)

    
    mask_mas_vendido_C = sizes_canada[1] == max(sizes_canada[1])
    tamaño_mas_vendido_C = sizes_canada[0][mask_mas_vendido_C]
    tamaño_mas_vendido_C = " ".join(tamaño_mas_vendido_C .tolist()) # Con tolist() se remuev el dtype y con el join se pasa de lista a str
    mask_mas_vendido_G = sizes_germany[1] == max(sizes_germany[1])
    tamaño_mas_vendido_G = sizes_germany[0][mask_mas_vendido_G]
    tamaño_mas_vendido_G = " ".join(tamaño_mas_vendido_G .tolist())
    mask_mas_vendido_USA = sizes_united_states[1] == max(sizes_united_states[1])
    tamaño_mas_vendido_USA = sizes_united_states[0][mask_mas_vendido_USA]
    tamaño_mas_vendido_USA = " ".join(tamaño_mas_vendido_USA .tolist())
    mask_mas_vendido_UK = sizes_united_kingdom[1] == max(sizes_united_kingdom[1])
    tamaño_mas_vendido_UK = sizes_united_kingdom[0][mask_mas_vendido_UK]
    tamaño_mas_vendido_UK = " ".join(tamaño_mas_vendido_UK .tolist())

    Sizes_dict = {}
    Sizes_dict.update({ countries[0]: tamaño_mas_vendido_C, countries[1]: tamaño_mas_vendido_G, countries[2]: tamaño_mas_vendido_USA, countries[3]: tamaño_mas_vendido_UK})

    return(Sizes_dict)

# Función VENTAS GENERO PAÍS: Para ver qué genero compro la mayor cantidad de calzado en cada país.
def ventas_genero_pais(countries, gender_target, country, gender):

    generos_unicos = np.unique(gender) # "Female", "Male" y "Unix"
    
    # Crear unas máscaras para obtener los índices del array
    # que corresponden a los paises
    mask_0 = country == countries[0] #"Canada"
    mask_1 = country == countries[1] #"Germany"
    mask_2 = country == countries[2] #"United States"
    mask_3 = country == countries[3] #"United Kingdom"

    # Utilizo las máscaras para acceder a los indices del array size
    # que corresponden a cada pais
    genero_canada = gender[mask_0] 
    genero_germany = gender[mask_1]
    genero_united_states = gender[mask_2]
    genero_united_kingdom = gender[mask_3]

    gender_canada = np.unique(genero_canada,return_counts=True)
    gender_germany = np.unique(genero_germany,return_counts=True)
    gender_united_states = np.unique(genero_united_states,return_counts=True)
    gender_united_kingdom = np.unique(genero_united_kingdom,return_counts=True)

    
    mask_target_C = gender_canada[0] == gender_target
    genero_target_C = gender_canada[1][mask_target_C]
    genero_target_C = genero_target_C .tolist()[0] # Con tolist() se remuev el dtype y con el [0] se obtiene el unico elemento de la lista.
    mask_target_G = gender_germany[0] == gender_target
    genero_target_G = gender_germany[1][mask_target_G]
    genero_target_G = genero_target_G .tolist()[0]
    mask_target_USA = gender_united_states[0] == gender_target
    genero_target_USA = gender_united_states[1][mask_target_USA]
    genero_target_USA = genero_target_USA .tolist()[0]
    mask_target_UK = gender_united_kingdom[0] == gender_target
    genero_target_UK = gender_united_kingdom[1][mask_target_UK]
    genero_target_UK = genero_target_UK .tolist()[0]

    Target_Genre_dict = {}
    Target_Genre_dict.update({ countries[0]: genero_target_C, countries[1]: genero_target_G, countries[2]: genero_target_USA, countries[3]: genero_target_UK})

    return(Target_Genre_dict)




####### Bloque principal del programa #######

if __name__ == "__main__":

    data = read_db()
    country = data[0]
    gender = data[1]
    size = data[2]
    price = data[3]
    countries = ["Canada","Germany","United States", "United Kingdom"]
    gender_target = "Male" # Las opciones a analizar son: "Female", "Male" y "Unix"
    print("En el siguiente array se muestran los países en los que hubo ventas:")
    paises_unicos(country)

    print("En el siguiente diccionario se muestra el total de ventas por país:")
    print(ventas_pais(countries, country, price))

    print("En el siguiente diccionario se muestra el tamaño de calzado más vendido en cada país:")
    print(calzado_pais(countries, country, size))

    print("En el siguiente diccionario se muestan las ventas para el género "+ gender_target+ " en cada país:")
    print(ventas_genero_pais(countries, gender_target, country, gender))

    print("Termine! Que buen programa soy ^^")
    