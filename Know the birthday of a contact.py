from datetime import *


def age_contact(birthyear):
    birthyear_days = birthyear * 365
    delta_birth = timedelta(days=birthyear_days)
    today = date.today()
    age = today - delta_birth
    age_year = int(age.year)
    print("La edad del contacto es {}".format(age_year))