class Persona(object):


    def __init__(self):
#Creamos el super de la clase Persona para poder heredar los metodos de la misma
        super(Persona, self).__init__()

#Creamos los set y get respectivos para las variables 
    def AgregarNombre(self, nombre):
        self.nombre = nombre

    def AgregarApellido(self, apellido):
        self.apellido = apellido

    def AgregarPais(self, pais):
        self.pais = pais


    def ObtenerNombre(self):
        return self.nombre

    def ObtenerApellido(self):
        return self.apellido

    def ObtenerPais(self):
        return self.pais


#Creamos la clase estudiante creando el get y set de la variable codigo
class Estudiante(Persona):


    def __init__(self):
#Declaramos el super 
        super(Estudiante, self).__init__()


    def AgregarCodigo(self, codigo):
        self.codigo = codigo


    def ObtenerCodigo(self):
        return self.codigo


#Creamos la clase estudiante presencial
class EstPresencial(Estudiante):

#Declaramos el super y creamos los get y set de las variables a usar 
    def __init__(self):
        super(EstPresencial, self).__init__()
      

    def AgregarNumeroCreditos(self, m):
        self.num_creditos = m

    def AgregarCiclo(self, ciclo):
        self.ciclo = ciclo.upper()

    def ObtenerNumeroCreditos(self):
        return self.num_creditos

    def ObtenerCiclo(self):
        return self.ciclo
#Creamos el metodo para presentar toda la informacion 
    def PresentarInformacion(self):
        cadena = ("\nInformacion:\n\tNombres Completos: %s %s\n\tCodigo: %s\n\tProcedencia: pais-%s capital-%s\n\tCiclo: %s\n\tNúmero Créditos: %s\n"%(self.ObtenerNombre(), self.ObtenerApellido(), self.ObtenerCodigo(), self.ObtenerPais().ObtenerNombrePais(), self.ObtenerPais().ObtenerCapital(), self.ObtenerCiclo(), self.ObtenerNumeroCreditos()                 ))
        return cadena


#Creamos la clase de el estudainte a distancia con sus respectivos get y set
class EstDistancia(Estudiante):


    def __init__(self):
        super(EstDistancia, self).__init__()


    def AgregarNumeroMaterias(self, m):
        self.num_materias = m

    def AgregarModulo(self, modulo):
        self.modulo = modulo.upper()

    def ObtenerNumeroMaterias(self):
        return self.num_materias

    def ObtenerModulo(self):
        return self.modulo
#Creamos el metodo para presentar la informacion
    def PresentarInformacion(self):
        cadena = ("\nInformacion:\n\tNombres Completos: %s %s\n\tCodigo: %s\n\tProcedencia: pais-%s capital-%s\n\tModulo: %s\n\tNúmero de Materias: %s\n"%(self.ObtenerNombre(), self.ObtenerApellido(), self.ObtenerCodigo(), self.ObtenerPais().ObtenerNombrePais(), self.ObtenerPais().ObtenerCapital(), self.ObtenerModulo(), self.ObtenerNumeroMaterias()))
        return cadena

      
#Creamos la clase pais para agregarle a la cadena la prosedencia
class Pais(object):
#creamos los get y set de las respectivas variables

    def __init__(self, nombre, capital):
        self.nombre = nombre
        self.capital = capital


    def AgregarNombrePais(self,nombre):
        self.nombre=nombre

    def AgregarCapital(self,capital):
        self.capital=capital


    def ObtenerNombrePais(self):
        return  self.nombre

    def ObtenerCapital(self):
        return  self.capital