def imprimirCalificación(Calificación):
        if(Puntuación >= 0.9 and Puntuación <= 1.0):
                Calificación = "Sobresaliente"
        elif (Puntuación >= 0.8 and Puntuación < 0.9):
                Calificación = "Notable"
        elif (Puntuación >= 0.7 and Puntuación < 0.8):
                Calificación=  "Bien"
        elif (Puntuación >= 0.6 and Puntuación < 0.7):
                Calificación = "Suficiente"
        elif (Puntuación >= 0 and Puntuación < 0.6):
                Calificación= "Insuficiente"
        else:
                Calificación = "No definido"
        return Calificación
        
try:
        Puntuación = float(input("Ingrese la calificación (0.01 - 1.00): "))
        Calificación = imprimirCalificación(Puntuación)
        print("La calificación de su puntuación es:", Calificación)
except:
        print("Error, calificación solo acepta números")