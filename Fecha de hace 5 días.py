import datetime

fecha_hoy = datetime.datetime.now()
fecha_hace_cinco_dias = fecha_hoy - datetime.timedelta(days=5)

dia_hace_5_dias = fecha_hace_cinco_dias.weekday()
dia_now = fecha_hoy.weekday()
week_day_5 = ""
week_day_now = ""

if dia_now == 0:
    week_day_now = "Lunes"
elif dia_now == 1:
    week_day_now = "Martes"
elif dia_now == 2:
    week_day_now = "Miércoles"
elif dia_now == 3:
    week_day_now = "Jueves"
elif dia_now == 4:
    week_day_now = "Viernes"
elif dia_now == 5:
    week_day_now = "Sábado"
elif dia_now == 6:
    week_day_now = "Domingo"


if dia_hace_5_dias == 0:
    week_day_5 = "Lunes"
elif dia_hace_5_dias == 1:
    week_day_5 = "Martes"
elif dia_hace_5_dias == 2:
    week_day_5 = "Miércoles"
elif dia_hace_5_dias == 3:
    week_day_5 = "Jueves"
elif dia_hace_5_dias == 4:
    week_day_5 = "Viernes"
elif dia_hace_5_dias == 5:
    week_day_5 = "Sábado"
elif dia_hace_5_dias == 6:
    week_day_5 = "Domingo"

print("Hoy es {}, {}".format(week_day_now, fecha_hoy.strftime("%d del %m de %Y")))
print("Hace 5 días fue {}, {}".format(week_day_5, fecha_hace_cinco_dias.strftime("%d del %m de %Y")))
