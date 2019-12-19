import datetime

fecha_hoy = datetime.datetime.today()
dia_cumpleanos = int(input("¿Qué día cumples? "))
mes_cumpleanos = int(input("¿Qué mes cumples? "))
ano_estamos = int(input("¿Qué año es tu próximo cumpleaños? "))

fecha_cumpleanos = datetime.datetime(day=dia_cumpleanos, month=mes_cumpleanos, year=ano_estamos)

resta_dias_cumple = fecha_cumpleanos - fecha_hoy

dia_semana_cumple = fecha_cumpleanos.weekday()
week_day_cumple = ""

if dia_semana_cumple == 0:
    week_day_cumple = "Lunes"
elif dia_semana_cumple == 1:
    week_day_cumple = "Martes"
elif dia_semana_cumple == 2:
    week_day_cumple = "Miércoles"
elif dia_semana_cumple == 3:
    week_day_cumple = "Jueves"
elif dia_semana_cumple == 4:
    week_day_cumple = "Viernes"
elif dia_semana_cumple == 5:
    week_day_cumple = "Sábado"
elif dia_semana_cumple == 6:
    week_day_cumple = "Domingo"

print("Faltan {} días para tu cumple, un {}".format(resta_dias_cumple.days, week_day_cumple))


