from class30coche import Coche

class deportivo:
    color = "Amarillo"
    
    def turbo(self):
            print ("activando turbo")
    marca = ""
    modelo = ""
    velocidad = 0
    estado = False
    turbo = True

    def acelerar(self):
        if (self.estado == False):
            print("El cohe no esta arrancando. Debe arrancar antes")
        else:
            self.velocidad += 20
        print ("Velocidad actual " + str(self.velocidad))
