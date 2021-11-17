import re
haslo = input("Wprowadź hasło: ")
#if not sprawdza najpierw czy warunek niespełniony. Próbowałem zrobić samym ifem, ale w niektórych próbach wpisania błędnego hasła wyświetlał się komunikat, że hasło spełnia wymagania
if not re.search(r'[a-z]', haslo):
    print("Hasło nie spełnia wymagań!")
elif not re.search(r'[A-Z]', haslo):
    print("Hasło nie spełnia wymagań!")
elif not re.search(r'\d', haslo):
    print("Hasło nie spełnia wymagań!")
elif not re.search(r'[$#@]', haslo):
    print("Hasło nie spełnia wymagań!")
elif not len(haslo)>6 and len(haslo)<16:
    print("Hasło nie spełnia wymagań!")
else:
    print("Hasło spełnia wymagania")
