ep = "si"
while ep == "si" or ep == "s":
  Ed = float(input("Indique su edad: "))
  bn = float(input("Sueldo base: "))
  sm = input("tiene esposa: ")
  nh = input("tiene hijos: ")
  ju = float(input("dias trabajdos: "))
  print()

# 1. Bono pencionario
  if Ed >= 55:
    bon= bn * 0.05
    d = bon + bn
    estado = (f"1. Aprobado. la edad es= {Ed} El valor del bono= {bon :,.0f} saldo total= {d :,.0f}")
  else:
    estado = (f"1. Negado. La edad es= {Ed}")
  print(estado)
  print()
#2. Viaje is o no
  if sm in "si":
   est = "si"
  else:
   est = "no"

  if nh in "si":
    es = "si"
  else:
    es = "no"
  p = est and es

  print(f"2. beneficio de viaje= {p}")
  print()
    
# 3. Sueldo si o no
  if bn >= 1000000 and bn <= 1500000:
   rel = bn * 0.02
   men = bn + rel
   col = (f"si y comicion {rel :,.0f} sueldo {men :,.0f}")
  else:
   col = ("no")
  if bn >= 1500001 and bn <= 2000000:
   yuo = bn * 0.05
   como =bn + yuo
   mal = (f"si y comicion {yuo :,.0f} sueldo {como :,.0f}")
  else:
   mal = ("no")
  
  print(f"3. Comicion del 2% {col}")
  print(f"   Comicion del 5% {mal}")
  print()
# total plata

#4.  Bono de alimentos
  if bn > 1000000:
    gb = "No"
  else:
    gb = "Si"
    
  if ju  >= 20:
    dg = "si"
  else:
    dg = "no"
    
  hak = dg and gb
  print(f"4. se le entrega bono de alimento= {hak}")

 #lolo 3
  ep = input("Desea realizarlo otra vez: ")
