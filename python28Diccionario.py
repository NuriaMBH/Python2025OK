# Los diccionarios en Python son un tipo de estructuras de datos que permite 
# guardar un conjunto no ordenado de pares clave-valor.
# Las claves deben ser únicas, no deben existir elementos con la misma clave. 
# Son mutables.

# Realizar un ejercicio donde guardemos en un diccionario los prefijos telefónicos 
# de diferentes provincias.

print("Diccionario Python")
provincias = dict()
provincias = {
    924 : "Badajoz",
    956 : "Cádiz",
    958 : "Granada",
    959 : "Huelva",
    91 : "Madrid",
    95 : "Málaga",
    968 : "Murcia",
    923 : "Salamanca",
    95 : "Sevilla",
    922 : "Sta. Cruz de Tenerife",
    975 : "Soria",
    96  : "Valencia",
    976 : "Zaragoza",
}
print("Número de provincias:", len(provincias))
