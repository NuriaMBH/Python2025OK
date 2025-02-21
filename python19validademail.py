# Vamos a realizar un programa para validar un Email con Python
# El usuario introducirá un email y le indicaremos si está mal y la razón.

# NO QUIERO BUCLES, TODO CON METODOS

# Que el email contenga @
# Que el email tenga un punto
# @ ni al principio ni al final
# Punto ni al principio ni al final
# Que el email solamente tenga una @
# Que exista un punto después de la @
# El dominio debe ser de 2 a 3 caracteres
# SOLUCION

print("Validacion Email")
print("Introduzca un email")
email = input()
# EMAIL CON @
if (email.count("@") == 0):
    print("Email sin @")
# QUE EXISTA UN PUNTO
elif (email.find(".") == -1):
    print("Email sin punto")
# EMAIL SIN @ AL INICIO NI FINAL
elif (email.startswith("@") == True or email.endswith("@") == True):
    print("@ al inicio o al final del email")
# Punto ni al inicio ni al final
elif (email[0] == "." or email.endswith(".") == True):
    print("Punto al inicio o al final")
# Email con una sola @
elif (email.count("@") > 1):
    print("Existe más de una @")
# Exista un punto despues de @
elif (email.find("@") > email.rfind(".")):
    print("Debe existir un punto despues de la @")
else:
    # Necesitamos recuperar el dominio
    ultimoPunto = email.rfind(".")
    # RECUPERAMOS EL DOMINIO A PARTIR DEL ULTIMO PUNTO EN ADELANTE
    dominio = email[ultimoPunto + 1:]
    # LONGITUD DEL DOMINIO
    longitudDominio = len(dominio)
    # Comprobar la longitud 2-3
    if (longitudDominio >= 2 and longitudDominio <= 3):
        print("Email correcto " + email)
    else:
        print("El email debe tener un dominio de 2 a 3 caracteres")
print("Fin de programa")
