import datetime

fecha_hoy = datetime.date.today()
dia_usuario = int(input("¿Qué día? "))
mes_usuario = int(input("¿Qué mes? "))
ano_usuario = int(input("¿Qué año? "))

fecha_usuario = datetime.date(day=dia_usuario, month=mes_usuario, year=ano_usuario)
fecha_es_menor = True
diferencia_fechas = fecha_hoy - fecha_usuario

if fecha_hoy <= fecha_usuario:
    print("Introduce una fecha anterior a hoy")
    fecha_comprobacion = False

if fecha_es_menor:
    print("Hay una diferencia de {} horas".format(diferencia_fechas.days * 24))