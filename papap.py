sanas = "si"
while sanas == "si" or sanas == "s":
 #1
 def oper():
     Vv= (vu1 + vu2 + vu3) * 0.10 + vu4
     return Vv
 print("1. valor de comicion 10% de 3 ventas + sueldo total")
 vu1 = float(input("Venta 1: "))
 vu2 = float(input("Venta 2: "))
 vu3 = float(input("Venta 3: "))
 vu4 = float(input("sueldo: "))
 oper()
 nn = oper()
 print(f"1. Resultado: {nn}")
 print()
 #2
 def venta():
     ds = V-(0.15*V)
     return ds
 print("2. venta de un producto con descuento del 15%")
 V= float(input("Valor compra: "))
 venta()
 ss = venta()
 print(f"2. pago {ss}")
 print()
 #3
 def Estudiante():
     prom = round((cal1 + cal2 +cal3)/3)
     return prom
 print("3. Estudiante quiere saber cuales son sus calificaciones de un examen")
 cal1 = float(input("Digite la calificacion 1: "))
 cal2 = float(input("Digite la calificacion 2: "))
 cal3 = float(input("Digite la calificacion 3: "))
 Estudiante()
 hh = Estudiante()
 print(f"3. Calificacion {hh}")
 print()
 #4
 def Porcento():
     cal ="Todos", M + H ,"Mujeres", (M * 100)/(H+M),"Hombres", (H*100)/(M+H)
     return cal
 print("4. Porcentaje de hombres y mujeres en un curso")
 H = float(input("Numero de estudiantes Hombre: "))
 M = float(input("Numero de estudiantes Mujeres: "))
 Porcento()
 bb = Porcento()
 print(f"4. Pocentaje {bb}")
 sanas = input("¿otra vez?:")