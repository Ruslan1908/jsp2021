import re

def sprawdz(pesel):
                #Sprawdzanie re
                if ( re.match('[0-9]{11}$',pesel)):
                        pass
                else:
                        return 0
                # Sprawdzenie sumy 
                l=int(pesel[10])
                suma =((l*int(pesel[0]))+(3*int(pesel[l]))+(7*int(pesel[2]))+(9*int(pesel[3]))+((l*int(pesel[4])))+(3*int(pesel[5]))+(7*int(pesel[6]))+(9*int(pesel[7]))+(l*int(pesel[8]))+(3*int(pesel[9])))
                kon=10-(suma %10)
                if kon== 10:
                        kon= 0
                else:
                        kon=kon
 
                #kon i sprawdzenie zgodnostci z tym
                if ((kon== 10)or(kon== 0)):
                        return 0
                else:
                        return 1
 
 
def index():
        pobranie=input('Podaj PESEL: ')
        p=int(pobranie[9]) %2
        r=int(pobranie[0:2])
        m=pobranie[2:4]
        d=pobranie[4:6]
        if (sprawdz(pobranie)):
                #sprawdza plec 
                if p ==1:
                        plec = "Mezczyzna"
                else:
                        plec = "Kobieta"
                #sprawdza rok urodzenia
                if r<99 and r>10:
                        pr=1900
                else:
                        pr=2000
                #sprawdza miesiac
                if m =='01':
                        mies="Stycznia"
                elif m =='02':
                        mies="Lutego"
                elif m =='03':
                        mies="Marca"
                elif m =='04':
                        mies="Kwietnia"
                elif m =='05':
                        mies="Maja"
                elif m =='06':
                        mies="Czerwca"
                elif m =='07':
                        mies="Lipca"
                elif m =='08':
                        mies="Siperpnia"
                elif m =='09':
                        mies="Wrzesnia"
                elif m =='10':
                        mies="Pazdzierniaka"
                elif m =='11':
                        mies="Listopada"
                elif m =='12':
                        mies="Grudnia"
                else:
                    #wyświetlanie na ekranie
                        print ("Zly PESEL !")
                        print ("Data urodzenia: %s %s %d %d")
                        print ("Plec: %s"% plec)
        else:
                print ("Zly PESEL !")
 
        print ("Twoja data urodzenia to: ",pr+r ,m ,d)
        print ("Twoja plec to: " ,plec)
 
index()