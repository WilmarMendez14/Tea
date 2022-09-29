maximo = 0
minimo = 0
primer_numero = True
while True:
    try:
        input_str = input("Ingrese un numero: ")
        if (input_str == "done"):
            break
        else:
            if (primer_numero):
                maximo = int(input_str)
                minimo = int(input_str)
                primer_numero = False
            else:
                if (int(input_str) > maximo): maximo = int(input_str)
                if (int(input_str) < minimo): minimo = int(input_str)
    except:
        print("Valor no es valido")
        continue
    print("Maximo:", maximo)
    print("Minimo:", minimo)
