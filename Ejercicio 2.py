carrera=(input("¿El corredor ha acabado la carrera?"))
if carrera == "si":
    print("Ha acabado la carrera")
else:
    while carrera == "no":
     carrera=(input("¿El corredor ha acabado la carrera?"))
     hora=(input("Ingrese la hora por el que pasa el corredor"))
     km=(input("Ingrese el punto kilometrico por el que pasa el corredor"))
     corredor={hora:hora,km:km}
    print("El corredor a las ",corredor[hora],"estaba en el km",corredor[km])
