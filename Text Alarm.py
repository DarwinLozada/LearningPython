from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1


def write_file_and_screen(text, file_name):
    with open(file_name, "a+") as file_text:
        file_text.write("{}{}".format(text, "\n"))
        print(text)


def week_date_to_day(day):
    days_list = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday",
                 6: "Sunday"}
    day_weekday_user = day.weekday()
    if day_weekday_user == days_list.keys():
        week_day_of_the_day = days_list.get(day_weekday_user)
        return week_day_of_the_day


def main():
    today = datetime.date.today()
    current_time = datetime.datetime.now()
    is_night = False
    today_week_day = today.weekday()
    now_hour = datetime.datetime.now().time().hour
    current_hour = datetime.time(hour=now_hour)

    want_alarm = input("Do you want to set a alarm? Yes/No ")
    if want_alarm == "Yes":

        # Aquí preguntamos si desea una alarma para una fecha específica.

        specific_date = input("Do you want an alarm in a specific date? Yes/No ")
        if specific_date == "Yes":
            date_user = input("Tell me the date. (dd/mm/yyyy) ")
            date_format = datetime.datetime.strptime(date_user, "%d/%m/%Y")
            if datetime.date.today() == date_format.date():
                write_file_and_screen("ALARM. It's {}".format(date_format), "Specific alarm.txt")

        elif specific_date == "No":
            # Aquí preguntamos si desea una alarma normal, haciendo que elija el día y la hora.

            normal_alarm = input("Do you want a normal alarm? Yes/No ")
            if normal_alarm == "Yes":
                hour_alarm = int(input("Hour of the alarm? 0/23 "))
                user_hour_alarm = datetime.time(hour=hour_alarm)
                days_of_alarm_input = ""
                days_of_alarm_list = []
                print("Write ""End"" to end the loop ")
                while not days_of_alarm_input == "End":
                    days_of_alarm_input = input("Tell me the days that you want to set the alarm 0 to 6, 0 is "
                                                "Monday ""and 6 is Sunday ")
                    if not days_of_alarm_input == "End":
                        days_of_alarm_list.append(days_of_alarm_input)
                if days_of_alarm_input == "End":
                    for i in days_of_alarm_list:
                        if today_week_day == int(i):
                            if user_hour_alarm == current_hour:
                                write_file_and_screen("ALARM. It's {}".format(current_hour), "Weekdays "
                                                                                             "alarm.txt")
    # Se imprime la hora actual y se le va sumando una más, además de que si indica si es de día
    # o de noche

    while True:

        sleep(5)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True

        elif (DAY_STARTS < current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if light_changed:
            if is_night:
                write_file_and_screen("It's night", "hours.txt")
            else:
                write_file_and_screen("It's day", "hours.txt")

        write_file_and_screen("The hour is {}".format(current_time), "horas.txt")
        sleep(3)


if __name__ == "__main__":
    main()
