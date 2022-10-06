cadena = "XEDSPAM-Confidence:0.87475"
inicio = cadena.find(":") + 1
final = len(cadena)
numero = float(cadena[inicio:final])
print(numero)
print(type(numero))