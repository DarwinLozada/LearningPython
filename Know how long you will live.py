import datetime


def ask_yes_not_or_sometimes(message, years_to_take):
    return_years_to_take = None
    print(message)
    response = input("Yes/No/Sometimes ")
    if response == "Yes":
        return_years_to_take = years_to_take
    elif response == "Sometimes":
        return_years_to_take = years_to_take / 2
    elif response == "No":
        return_years_to_take = 0
    return return_years_to_take


AVERAGE_LIFESPAN = 80
SMOKER = 12
DRINKER = 10
SEDENTARY = 10
STRESS = 6
years_lost = 0

birth_date = input("Tell me your birth date. (dd/mm/yyyy) ")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")

user_smoker = "Do you smoke? "
years_smoke = ask_yes_not_or_sometimes(user_smoker, SMOKER)
years_lost += years_smoke

user_drinker = "Do you drink? "
years_drinker = ask_yes_not_or_sometimes(user_drinker, DRINKER)
years_lost += years_drinker

user_sedentary = "Are you sedentary? "
years_sedentary = ask_yes_not_or_sometimes(user_sedentary, SEDENTARY)
years_lost += years_sedentary

user_stress = "Are you stressed all day? "
years_stress = ask_yes_not_or_sometimes(user_stress, STRESS)
years_lost += years_stress

lifespan = AVERAGE_LIFESPAN - years_lost
death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("Death date: {}, you have {} days of life".format(death_day.strftime("%d/%m/%y"), days_to_death.days))