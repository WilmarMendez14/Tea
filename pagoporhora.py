# Tendencias e Innovacion en Tecnologia Agricola (TEA)

horas = input("horas trabajadas?")
valorPorHora = input("valor por hora?")

#se utiliza la conversion de tipo a int
# si no se hace la conversion existiera error porque trata de multiplicar strings
total=int(horas)*float(valorPorHora)
print("usted ha recibido:")
print(total)