print ( "INGRESE SU EDAD EN AÑOS")
edad = int (input ())
if edad < 0:
    print ("Edad no válida")
elif edad < 18:
    print ("Eres menor de edad")
elif edad < 65:
    print ("Eres adulto") 