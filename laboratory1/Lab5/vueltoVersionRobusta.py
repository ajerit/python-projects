"""
Prelaboratorio 5

Descripcion:
 Al realizar una compra en efectivo, es necesario dar el vuelto al comprador.
 Para dar el vuelto se dispone de billetes de 10, 5 y 2, asi como monedas de 1.
 Dado el monto de una compra y del pago, se debe calcular el vuelto y entregarlo
 con el numero minimo posible de billetes y monedas. Los montos de compra y de
 pago son redondos (sin centimos). Se desea solicitar al usuario los montos de
 una compra y del pago, y calcular el vuelto, en su desglose optimo.
 
"""

import sys # Para poder utilizar sys.exit();

# CONSTANTES
BLL_ALTO = 10 # Valor del billete de denominacion alta
BLL_MEDIO = 5 # Valor del billete de denominacion media
BLL_BAJO = 2  # Valor del billete de denominacion baja

# VARIABLES
compra = 0    # int // Entrada: monto de la compra
pago = 0      # int // Entrada: monto del pago realizado

cnt_bll_alto = 0   # int // Salida: Cantidad de billetes de denominacion alta
cnt_bll_medio = 0  # int // Salida: Cantidad de billetes de denominacion media
cnt_bll_bajo = 0   # int // Salida: Cantidad de billetes de denominacion baja
cnt_monedas = 0    # int // Salida: Cantidad de monedas


# Verificacion de la Precondicion (version robusta)

while True:
   try: # Try/except explicado en el prelaboratorio.
     compra = int(input("Indique el monto de la compra: "))
     pago = int(input("Indique el monto del pago: "))
     assert( compra > 0 and pago >= compra )
     break
   except:
     print("Se ha equivocado, debe volver a introducir los datos.")
     print("Los valores deben ser positivos y pago mayor o igual que la compra")

# El algoritmo obtiene la mayor cantidad de billetes de alta denominacion
# luego los de media denominacion, y finalmente los de 
# baja denominacion. El resto se devolvera en monedas.

# Calculos

vuelto = pago - compra
cnt_monedas = vuelto

cnt_bll_alto = cnt_monedas // BLL_ALTO
cnt_monedas = cnt_monedas % BLL_ALTO

cnt_bll_medio = cnt_monedas // BLL_MEDIO
cnt_monedas = cnt_monedas % BLL_MEDIO

cnt_bll_bajo = cnt_monedas // BLL_BAJO
cnt_monedas = cnt_monedas % BLL_BAJO

# Verificacion de la Postcondicion
try:
  assert( vuelto == pago - compra and
          vuelto == cnt_bll_alto * BLL_ALTO 
                +   cnt_bll_medio * BLL_MEDIO 
                +   cnt_bll_bajo * BLL_BAJO
                +   cnt_monedas 
          and (0 <= cnt_bll_alto)
          and (0 <= cnt_bll_medio) and (cnt_bll_medio < 2)
          and (0 <= cnt_bll_bajo) and (cnt_bll_bajo <= 2)
          and (0 <= cnt_monedas) and (cnt_monedas < 2) )
except:
  print("Hubo un error en los calculos") # Mensaje para el usuario
  print("No se cumple la postcondicion con los valores ")
  print("vuelto = " + str(vuelto))
  print("pago = " + str(pago))
  print("compra = " + str(compra))
  print("cnt_bll_alto = " + str(cnt_bll_alto))
  print("cnt_bll_medio = " + str(cnt_bll_medio))
  print("cnt_bll_bajo = " + str(cnt_bll_bajo))
  print("cnt_monedas = " + str(cnt_monedas))
  sys.exit() # Abortamos el programa, pues no cumplio la postcondicion..

# Salida 
# cuando todo resulta normal

print("El vuelto es: " + str(vuelto))
print("\nSe debe dar:\n")
print(str(cnt_bll_alto) + " billetes de " + str(BLL_ALTO))
print(str(cnt_bll_medio) + " billetes de " + str(BLL_MEDIO))
print(str(cnt_bll_bajo) + " billetes de " + str(BLL_BAJO))
print("cantidad de monedas: "+ str(cnt_monedas))

