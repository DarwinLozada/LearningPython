from datetime import datetime


def main2():
    monthsnobi = {"Enero": 31, "Febrero": 28, "Marzo": 31, "Abril": 30, "Mayo": 31, "Junio": 30, "Julio": 31,
                  "Agosto": 31, "Septiembre": 30, "Octubre": 31, "Noviembre": 30, "Diciembre": 31}

    monthssibi = {"Enero": 31, "Febrero": 29, "Marzo": 31, "Abril": 30, "Mayo": 31, "Junio": 30, "Julio": 31,
                  "Agosto": 31, "Septiembre": 30, "Octubre": 31, "Noviembre": 30, "Diciembre": 31}

    actual_date = datetime.now()
    years = actual_date.year - birthdaydt.year
    birthdaydtyear = birthdaydt.year
    days = 0
    months = 0

    while birthdaydtyear != actual_date.year:
        if birthdaydtyear % 4 == 0:
            days += sum(monthssibi.values())
            months += 12
        else:
            days += sum(monthsnobi.values())
            months += 12
        birthdaydtyear += 1
    print(days, months)






def main():
    actual_date = datetime.now()
    difference = actual_date - birthdaydt
    if birthdaydt > actual_date:
        print("Introduce una fecha válida")
    else:
        print("Tiene {} años, {} meses y {} días de vivo".format(int(difference
                                                                     .days / 365), int(difference.days / 30),
                                                                 int(difference.days)))
        print("Tu día de cumpleaños es el {}".format(birthdaydt.strftime("%m/%d")))


birthday = input("Dime tu fecha de nacimiento (formato YYYY-MM-DD) ")
try:
    birthdaydt = datetime.strptime(birthday, "%Y-%m-%d")
    main()
    main2()
except ValueError:
    print("Introduce una fecha válida")
