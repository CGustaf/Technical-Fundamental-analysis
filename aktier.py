

#Programmets klass Aktier
class Aktier:

    def __init__(self, symbol, pe_tal, ps_tal, skulder, tillgangar, pris_idag, pris_1mo, pris_1y, mo_hog, mo_lag):
        self.__symbol = symbol
        self.__pe_tal = pe_tal
        self.__ps_tal = ps_tal
        self.__skulder = skulder
        self.__tillgangar = tillgangar
        self.__pris_idag = pris_idag
        self.__pris_1mo = pris_1mo
        self.__pris_1y = pris_1y
        self.__mo_hog = mo_hog
        self.__mo_lag = mo_lag

    #Metoden tar in atributen och returnar ett objekt med ovanstående.
    def __str__ (self):
        objekt = self.__symbol+" "+str(self.__pe_tal)+" "+str(self.__ps_tal)+" "+str(self.__skulder)+" "+str(self.__tillgangar)+" "+str(self.__pris_idag)+" "+str(self.__pris_1mo)+" "+str(self.__pris_1y)+" "+str(self.__mo_hog)+" "+str(self.__mo_lag)
        return objekt

    #Metoden gör att man kan komma åt attributets symbol
    def ge_symbol(self):
        return str(self.__symbol)

    #Metoden gör att man kan komma åt attributets pe tal
    def ge_pe_tal(self):
        return str(self.__pe_tal)

    #Metoden gör att man kan komma åt attributets ps tal
    def ge_ps_tal(self):
        return str(self.__ps_tal)

    #Metoden gör att man kan komma åt attributets skulder
    def ge_skulder(self):
        return str(self.__skulder)

    #Metoden gör att man kan komma åt attributets tillgångar
    def ge_tillgangar(self):
        return str(self.__tillgangar)

    #Metoden gör att man kan komma åt attributets dagspris
    def ge_pris_idag(self):
        return str(self.__pris_idag)

    #Metoden gör att man kan komma åt attributets pris för en månad sedan
    def ge_pris_1mo(self):
        return str(self.__pris_1mo)

    #Metoden gör att man kan komma åt attributet pris för ett år sedan
    def ge_pris_1y(self):
        return str(self.__pris_1y)

    #Metoden gör att man kan komma åt attributets högsta kurs denna månad
    def ge_mo_hog(self):
        return str(self.__mo_hog)

    #Metoden gör att man kan komma åt attributets lägsta kurs den här månaden
    def ge_mo_lag(self):
        return str(self.__mo_lag)

    #Metoden tar fram attributets utveckling under ett år
    def utveckling_1y(self):
        return ((self.__pris_idag - self.__pris_1y)/self.__pris_1y)
    
    #Metoden tar fram attributets utveckling under en månad
    def utveckling_1mo(self):
        return ((self.__pris_idag - self.__pris_1mo)/self.__pris_1mo)

    #Metoden tar fram attributets soliditet
    def soliditet(self):
        return ((self.__tillgangar - self.__skulder)/self.__tillgangar)

