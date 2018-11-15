#importo modelado
from paquete_academico.modelado import *
#Creo el objeto de la clase EstDistancia
est1 = EstDistancia()    				
p = Pais("Ecuador", "Quito")		

#llamo a los metodos mediante el objeto
est1.AgregarNombre("Jose")					
est1.AgregarApellido("Diaz")
est1.AgregarCodigo("11012")
est1.AgregarNumeroMaterias(5)
est1.AgregarModulo("Noveno")

est1.AgregarPais(p)			
# Imprimimos el metodo de presentar infomracion
print(est1.PresentarInformacion())