


def main():
    # Otvaramo datoteku Marko4.txt za pisanje
    file = open("Marko4.txt", "w")
    # Stvaramo praznu listu
    a = []
    # Unosimo n (treba nam za for loop)
    n = int(input("Koliko brojeva: "))
    # Unosimo brojeve po redu.
    for i in range(n):
        # Pitamo za unos brojeva po redu po (i + 1) znaci 1, 2, 3, 4...
        b = input("Unesi {0}. broj: ".format(i + 1))
        # Ubacujemo taj broj u listu pomocu append
        a.append(b)
    # Stvaramo praznu listu
    c = []
    # Petljamo po elementima iz liste a
    for x in a:
        # Stavljamo u listu brojeve sa \n karakterom (ENTER)
        c.append(x + "\n")
    # Zapisujemo nasu listu u Marko4.txt
    file.writelines(c)
    # Zatvaramo Marko4.txt
    file.close()

    # Otvaramo drugi file ali ovaj put za citanje
    file2 = open("Marko4.txt", "r")
    # Unosimo brojeve u listu d
    d = file2.readlines()
    # Otvaramo loop za brojeve n
    for i in range(n):
        # Pomocu metode rstrip() skidamo \n sa kraja broja
        d[i] = d[i].rstrip()
        # Te pretvaramo d[i] u int (cijeli broj)
        d[i] = int(d[i])


    # a) prosjek najvećeg i najmanjeg broja

    # Dobivamo najmanji broj iz liste d funkcijom min
    najmanji_broj = min(d)
    # Dobivamo najveci broj iz liste d funkcijom max
    najveci_broj = max(d)
    # Prosjek dobijemo tako da zbrojimo najmanji i najveci broj te podijelimo sa 2
    prosjek = ( najmanji_broj + najveci_broj ) / 2
    # Ispisujemo prosjek
    print("Prosjek najveceg i najmanjeg broja: ", prosjek)


    # b) brojeve poredane od većeg prema manjem
    
    # Kopiramo listu d u listu e zbog sigurnosnih razloga
    e = d
    # Otvaramo loop do n-1 (zato sto liste pocinju od 0)
    for i in range(n - 1): 
        # Svaki loop krecemo od drugih brojeva po redu
        for j in range(i + 1, n):
            # Ako je broj i manji od trenutnog broja
           if(e[i] < e[j]): 
                # Stavljamo broj i u privremenu varijablu
                tmp = e[i] 
                # Mijenjamo broj i s trenutnim brojem
                e[i] = e[j] 
                # Te samo prosli najveci broj stavljamo na mjesto trenutnog broja
                e[j] = tmp
    # Ispisujemo sortiranu listu
    print("Sortirana lista: ", e)


    # c) samo brojeve djeljive s 5

    # Stvaramo novu listu gdje cemo spremiti brojeve djeljive s 5
    f = []
    # Petljamo kroz listu d
    for x in d:
        # Ako je trenutni broj djeljiv s 5
        if(x % 5 == 0):
            # Stavljamo u listu trenutni broj
            f.append(x)
    # Ispisujemo brojeve
    print("Brojevi djeljivi s 5: ", f)


    # d) prosjek brojeva većih od 5

    # Stvaramo varijablu gdje spremamo koliko ima brojeva vecih od 5
    koliko_brojeva = 0
    # Stvaramo varijablu gdje cemo spremati zbroj koji nam je potreban za prosjek
    zbroj = 0
    # Petljamo kroz brojeve
    for x in d:
        # Ako je broj veci od 5
        if(x > 5):
            # Povecavamo varijablu za 1
            koliko_brojeva += 1
            # Zbrajamo brojeve u varijablu zbroj
            zbroj += x
    # Racunamo prosjek
    prosjek2 = zbroj / koliko_brojeva
    # Ispisujemo prosjek
    print("Prosjek brojeva vecih od 5: ", prosjek2)


    # e) broj neparnih brojeva

    # Stvaramo varijablu gdje spremamo broj neparnih brojeva
    broj_neparnih = 0
    # Petljamo kroz brojeve
    for x in d:
        # Ako broj NIJE djeljiv s 2 onda je neparan
        if(x % 2 != 0):
            # Povecavamo varijablu
            broj_neparnih += 1
    # Ispisujemo
    print("Broj neparnih brojeva: ", broj_neparnih)

    return

if(__name__ == "__main__"):
    main()
