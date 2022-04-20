
#P-uppgift
#Gustaf Jakobsson 31-10-21
#Aktietips, ett terminal basserat program som hjälper andvändaren att välja aktier
 
# Programet importerar Yahoo_fin för att kunna nå aktiv börsdata med Yahoos api
# Programet importerar Pandas för at manipulera datastrukturena i Yahoos api
# Programet importerar Tid från Class_Tid för att kunna nå 
# Programer importerar os för att kunna rensa terminalen


import os
import time
import yahoo_fin.stock_info as si
from datetime import date, timedelta
from aktier import Aktier


#Funktionen låter användaren välja fil med aktie och index tickers
def val_fil():
    while True:
        try:
            print("Ange filnamn med aktier och index:")
            fil = input()
            open (fil,"r",encoding= 'utf-8')
            return fil
        except FileNotFoundError:
            print("Ange en giltig fill")


#Funktionen skapar en lista med tickerserna från filen användaren anger
def skapa_aktie_lista(filnamn):
    aktielista = []
    texten = open (filnamn,"r",encoding= 'utf-8')
    aktie_symboler = texten.read().split("\n")
    symboler = aktie_symboler[0].split(sep = " ")
    index = aktie_symboler[1].split(sep = " ")
    for symbol in symboler:
        aktielista.append(symbol)
    return aktielista, index


#Funktionen skapar en lista och appendar all data för varje aktie_ticker i aktielistan genom klassen
def data_aktier(aktielista):
    aktie_data_lista = []
    dagens_datum = str(date.today() + timedelta(days =-1))
    datum_1mo = str(date.today() + timedelta(days =-31))
    datum_1y = str(date.today() + timedelta(days =-366))
    for temp_symbol in aktielista:
        print(f"...loading {temp_symbol}")
        time.sleep(0.2)
        temp_statistik = si.get_stats_valuation(temp_symbol)
        time.sleep(0.2)
        temp_aktie_data = si.get_data(temp_symbol, start_date  = datum_1y, end_date = dagens_datum)
        time.sleep(0.2)
        temp_balansrakning = si.get_balance_sheet(temp_symbol)
        time.sleep(0.2)
        temp_tillgangar = temp_balansrakning.loc["totalAssets"][0]
        temp_skulder = temp_balansrakning.loc["totalLiab"][0]
        temp_pe_tal = temp_statistik.iloc[2,1]
        temp_ps_tal = temp_statistik.iloc[5,1]
        time.sleep(0.2)
        temp_mo_hog = round(temp_aktie_data[datum_1mo:]['high'].max(),2)
        temp_mo_lag = round(temp_aktie_data[datum_1mo:]['low'].min(),2)
        temp_pris_idag = temp_aktie_data.loc[(temp_aktie_data.index[temp_aktie_data.index.get_loc(dagens_datum,method ='nearest')])]['close']
        temp_pris_1mo = temp_aktie_data.loc[(temp_aktie_data.index[temp_aktie_data.index.get_loc(datum_1mo,method ='nearest')])]['close']
        temp_pris_1y = temp_aktie_data.loc[(temp_aktie_data.index[temp_aktie_data.index.get_loc(datum_1y,method ='nearest')])]['close']
        aktie_data_lista.append(Aktier(temp_symbol, temp_pe_tal, temp_ps_tal, temp_skulder, temp_tillgangar, temp_pris_idag, temp_pris_1mo, temp_pris_1y, temp_mo_hog, temp_mo_lag))
    print("Done...")
    time.sleep(1)
    clear()
    return aktie_data_lista


#Funktionen hämtar index tickern från filen användaren anger och apendar datan genom klassen till en lista
def ladda_index(bors_index_lista):
    index_lista = []
    dagens_datum = str(date.today() + timedelta(days =-1))
    datum_1mo = str(date.today() + timedelta(days =-31))
    datum_1y = str(date.today() + timedelta(days =-366))
    for bors_index in bors_index_lista:
        bors_index_data = si.get_data(bors_index, start_date  = datum_1y, end_date = dagens_datum)
        pris_idag = bors_index_data.loc[(bors_index_data.index[bors_index_data.index.get_loc(dagens_datum,method ='nearest')])]['close']
        pris_1mo = bors_index_data.loc[(bors_index_data.index[bors_index_data.index.get_loc(datum_1mo,method ='nearest')])]['close']
        pris_1y = bors_index_data.loc[(bors_index_data.index[bors_index_data.index.get_loc(datum_1y,method ='nearest')])]['close']
        index_lista.append(Aktier(bors_index, "", "", "", "", pris_idag, pris_1mo, pris_1y, "", ""))
    return index_lista


#Funktionen för programets huvudmeny
def huvud_meny(aktie_data_lista, index_data_lista):
    while True:
        try:
            analys_alternativ = int(input('''
Vilken analys vill du göra?
1. Fundamental analys 
2. Teknisk analys 
3. Jämför betavärden 
4. Avsluta
        '''))
            if analys_alternativ == 1:
                fundamental_analys(aktie_data_lista)
            elif analys_alternativ == 2:
                teknisk_analys(aktie_data_lista, index_data_lista)
            elif analys_alternativ == 3:
                beta_värde_jämför(aktie_data_lista, index_data_lista)
            elif analys_alternativ == 4:
                clear()
                return
            else:
                raise ValueError
        except ValueError:
            print("Var god ange ett av alternativen")


#Funktionen låter användaren välja vilken aktie de ska analysera
def val_aktie(aktie_data_lista):
    while True:
        print("Vilken aktie vill du analysera?")
        for i, aktie_objekt in enumerate(aktie_data_lista, start = 1):
            print(i, aktie_objekt.ge_symbol())
        try:
            svar = int(input()) - 1
            if svar in range((len(aktie_data_lista))):
                clear()
                return svar
            else:
                raise ValueError
        except ValueError:
            print("Ange ett av alternativen")


#Funktionen räknar ut aktiens pe tal, ps tal och soliditet
def fundamental_analys(aktie_data_lista):
    temp_fun_aktie = aktie_data_lista[val_aktie(aktie_data_lista)]
    temp_pe_tal = str(temp_fun_aktie.ge_pe_tal())
    temp_ps_tal = str(temp_fun_aktie.ge_ps_tal())
    temp_soliditet = str(temp_fun_aktie.soliditet())
    print(f"{temp_fun_aktie.ge_symbol()}\nPE_tal: {temp_pe_tal}\nPS_tal: {temp_ps_tal}\nSoliditet: {temp_soliditet}") 


#Funktionen tar fram aktiens utveckling under en månad, beta värde, högsta/lägsta kurs under en månad
def teknisk_analys(aktie_data_lista, index_data_lista):
    index = index_data_lista[0]
    temp_tek_aktie = aktie_data_lista[val_aktie(aktie_data_lista)]
    temp_utveckling_1mo = str(temp_tek_aktie.utveckling_1mo())
    beta_varde = str(temp_tek_aktie.utveckling_1y()/index.utveckling_1y())
    temp_monads_hog = str(temp_tek_aktie.ge_mo_hog())
    temp_monads_lag = str(temp_tek_aktie.ge_mo_lag())
    print(f"{temp_tek_aktie.ge_symbol()}\nBeta: {beta_varde}\nUtveckling en månad: {temp_utveckling_1mo}\nHögsta kurs 30 dagar: {temp_monads_hog}\nLägsta kurs 30 dagar: {temp_monads_lag}")


#Funktionen tar in listand med aktiedata och index och räknar 
def beta_värde_jämför(aktie_data_lista, index_data_lista):
    clear()
    beta_vardes_bibolotek = {}
    index = index_data_lista[0]
    for aktier in aktie_data_lista:
        aktie_namn = aktier.ge_symbol()
        beta_varde = aktier.utveckling_1y()/index.utveckling_1y()
        beta_vardes_bibolotek[aktie_namn] = str(round(beta_varde, 2))
    print("Aktie Ticker : Betavärde\n")
    beta_stat_sorterad = sorted(beta_vardes_bibolotek.items(), key = lambda x: x[1], reverse = True)
    for aktie, beta in beta_stat_sorterad:
        print(aktie, ' : ', beta)


#Funktionen rensar terminalen mellan utskrifter
def clear():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


#Funktionens main, programet börjar med att välja aktiefil, sedan hämtas all aktie och index data och sist tillkalas huvudmenyn
def main():
    fil_aktier = val_fil()
    lista_aktie_symboler = skapa_aktie_lista(fil_aktier)
    aktie_data_lista = data_aktier(lista_aktie_symboler[0])
    index_data_lista = ladda_index(lista_aktie_symboler[1])
    huvud_meny(aktie_data_lista, index_data_lista)
main()
