class Persona:
    nombre = ""
    apellidos = ""
    anyonacimiento = ""
    pais= ""
    descripción = dict()
    def __init__(self):
        self.pais = "Francia"
    def __str__(self):
        return self.apellidos + "" +self.nombre + ","+self.pais    
    def getDescripcion(self,descripcion):
        return self.getNombre ()
        
    def getNombreCompleto (self):
        self.nombre + "" + self.apellidos

    def getEdad(self):
        return 2025 - self.anoynacimiento
   
        