from algemene_functies import mijn_functie_2 

def aanbieding_1(smaak, prijs, korting):
    prijs_korting=prijs*(1-korting)
    uitvoer=f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_korting} euro."
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten,procent):
    bedragen=[220,430,125,160,205,90,345]
    inkomsten=sum(bedragen)
    btw=inkomsten*(1-procent)
    uitvoer=f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {btw} euro btw betaald dient te worden."
    return uitvoer
print(inkomsten_totaal(inkomsten,0.09)) 

def laag_en_hoog(mijn_lijst):
    mijn_lijst=(220,430,125,160,205,90,345)
    hoogste=max(mijn_lijst)
    laagste=min(mijn_lijst)
    return hoogste, laagste
print(laag_en_hoog)

def gemiddelde(mijn_lijst):
    mijn_lijst=(220,430,125,160,205,90,345)
    gemiddelde = statistics.mean(mijn_lijst)
    uitvoer=f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    return uitvoer
print(gemiddelde)

def meervoudig(invoer_lijst):
    invoer_lijst=[10,5,3,2,1,2,9]
    laag_en_hoog(meervoudig)
    return meervoudig

def combinatie(invoer_lijst_2):
    meervoudig(invoer_lijst_2)
    return combinatie
mijn_functie_2(combinatie)
korte_lijst=combinatie
print(korte_lijst)