# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:28:11 2022

@author: Marco
"""

import pandas as pd

df = pd.read_csv('Contratos2020.csv', delimiter = ';')
df.columns = df.columns.str.replace(' ','_')

columnas_analizar = [df.Título_del_expediente,df.Título_del_contrato,df.Descripción_del_contrato]

df_actualizado = pd.DataFrame()

filas_elim = []
elim =[]

p_eli = ("agua","medicina","desalsove","fiscal","redaccion","barra","perimetral","docencia",
         "pavimentacion","cine","luz","facturacion","redactora","laton","prendas","tuberia",
         "music","energia","electrica","concreto","adoquin","barra","refrigerador","red fria",
         "quimic","imagen","revista","calle","comida","extintor","soldadura","diesel","alta","tension",
         "femenina","arbol","extinguidor","tuerca","acero","alumbrado","baja","masculina","refosteración",
         "odontologia","montacargas","combustible","conferencia","tension","limpieza",
         "bachillerato","violencia","madera","publico","camino","camion","garrafon","voltaje",
         "reloj","caja","publicos","licenciatura","trabe","pintura","playa","vial",
         "evento","diplomado","electricidad","iluminacion","jardin","acondicionado",
         "restaurante","congreso","credito","asfalto","manguera","barredora","ventilador",
         "ferreas","ferroviario","alimento","banqueta","botonera","pluma","calentaador","ventilacion",
         "ropa","pintura","drenaje","techumbre","llanta","reactivo","playera","hidraulic",
         "alcantarillado","drenaje","aceite","guion","pozo","asigna","potable","electricidad",
         "tanque","boquilla","hidraulico","radiolucion","pluvial","electrico","saneamiento",
         "pared","clinico","clinicos","farmaceutico","farmaceuticos","radiologico","radiologic",
         "radiologi","vehiculo","vehiculos","vehicular","medicina","revista","revistas","diesel",
         "gasolina","automotor","automotriz","automoviles","autotransporte","gas","luninarias",
         "alumbrado","vialidad","vialidades","pavimento","cofee break","bebidas","concreto","pluvial",
         "saneamiento","alcantarillado","quimico","quimica","camioneta","camionetas","maquinaria","camion",
         "comida","salon","radiodiagnostico","extintor","medicos","medico","medicos,","medico,","medicos.","medico.")

p_ok = ("conectividad","internet","movil","torre","refacciones","materiales","accesorios","consumibles",
        "antenas","comunicaciones","telecomunicaciones","radiocomunicaciones","fibra","optica",
        "cableado","estructurado","redes","telefonia","satelital","satelitales","satelite","fija",
        "convencional","radiolocalizacion","voz","datos","conmutador","antena","comunciacion/telecomunicacion",
        "conectividad","seguridad","infraestructura","comunicaciones/telecomunicaciones",
        "satelital+internet","internet+internet","internet+seguridad","convencional+internet","fija+internet",
        "movil+internet","satelital+internet","telefonia+radiocomunicacion","torre","mpls")


def normalize(s):
    s = str(s)
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("à", "a"),
        ("è", "e"),
        ("ì", "i"),
        ("ò", "o"),
        ("ù", "ù")
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    
    s = s.lower()
    return s


def comparar_ok():
    global df
    global df_actualizado
    global filas_elim
    global elim 
    print("Se está buscando coincidencias de palabras deseadas.")
    for columna in range (len(columnas_analizar)):
        print("Procesando la columna", columna)
        for fila in range (len(df.RFC )):
            titulo = normalize(columnas_analizar[columna][fila])
            titulo = titulo.split(" ")
            coincidencia = False
            for palabras in titulo:
                for palabra in p_ok:
                    if palabras == palabra:
                        coincidencia = True
            if coincidencia!=True:
                filas_elim.append(fila)

def comparar_elim():
    global df
    global df_actualizado
    global filas_elim
    global elim 
    print("Se está buscando coincidencias de palabras no deseadas.")
    for columna in range (len(columnas_analizar)):
        print("Procesando la columna", columna)
        for fila in range (len(df.RFC )):
            titulo = normalize(columnas_analizar[columna][fila])
            titulo = titulo.split(" ")
            for palabras in titulo:
                for palabra in p_eli:
                    if palabras == palabra:
                        filas_elim.append(fila)
    

                      
    #print("\nSe encontraron",coincidencia,"palabras que coinciden.")

                        
comparar_ok()
comparar_elim()

elim = list(set(filas_elim))
df_actualizado = df.drop(elim)
df_actualizado.columns = df_actualizado.columns.str.replace('_',' ')

print("Se eliminaron",len(elim),"filas.")
df_actualizado.to_csv("Actualizado.csv",index = False)