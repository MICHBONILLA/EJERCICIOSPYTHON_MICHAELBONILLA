# Se declara la variable nombre del estudiante
nomestud= (input (" Ingrese nombre del estudiante "))
# Se declara la variable califpro
califpro= int(input(" ingrese la calificación promedio de las actividades realizadas en clase"))
# Se declara la variable acticlas para multiplicar la calificacion promedio de actividades por el 30%
acticlas= califpro * 0.30
califprofin= int(input(" ingrese la calificación del proyecto final"))  
proyectfinal= califprofin * 0.50
califproevpar= int(input(" ingrese la calificación promedio de las evaluaciones parcialesl"))
evaparcial= califproevpar* 0.20
notafinal= int (acticlas+ proyectfinal+ evaparcial)
print (" La nota final de algoritmia de estudiante ", nomestud, " es: ", notafinal)
       