# Descripcion: Procedimiento que invoca una función que imprime una variable local y otra global y luego intenta imprimir estas variables fuera 
#			   de la función
# Parametros:

globalVar = "Esta es de alcance global"
def miFuncion() -> "void":
  localVar = "Esta es local"
  print("miFuncion - localVar:  " + localVar)
  print("miFuncion - globalVar: " + globalVar)
 
##################################
# Inicio del programa 
##################################
miFuncion()
print("global - globalVar: " + globalVar)
print("global - localVar:  " + localVar)