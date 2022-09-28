contador = 0
suma = 0
maximo = 0
minimo = 0
primerNumero = True
while True:
  try:
    numero = input("Ingrese un numero: ")
    if (numero == "salir"):
     break 
    else:
        contador = contador + 1
        suma = suma + int(numero)
        promedio = suma / contador
        if (primerNumero):
          minimo = int(numero)
          maximo = int(numero)
          primerNumero = False
        else:
          if (int(numero) > maximo): maximo = int(numero)
          if (int(numero) < minimo): minimo = int(numero)
  except:
        print("Error, debe ingresar un valor numerico")
        contador = contador - 1
        continue
print("contador:", contador)
print("sumatoria:", suma)
print("promedio:", promedio)
print("Maximo:", maximo)
print("Minimo:", minimo)