import logging

class GetraenkeAutomat():
    def __init__(self):
        self.zustandList = (
            "Anfang",
            "Auswahl",
            "FalscheMuenze"
        );
        self.zustand = self.zustandList[0]

    def __eingabeBefehle(self):
        """ Diese Funktion gibt eine Liste der möglichen Befehle im Zustand "Eingabe" zurück
            @return list
        """

        return (
            "50Cent",
            "1Cent",
            "2Cent",
            "5Cent",
            "10Cent",
            "20Cent",
            "1Euro",
            "2Euro",
            "beenden"
        )

    def __auswahlBefehle(self):
        """ Diese Funktion gibt eine Liste der möglichen Befehle im Zustand "Auswahl" zurück
            @return list
        """

        return (
            "Limonade",
            "Mineralwasser",
            "beenden"
        )

    def __falscheMuenzeBefehle(self):
        """ Diese Funktion gibt eine Liste der möglichen Befehle im Zustand "FalscheMuenze" zurück
            @return list
        """

        return self.__auswahlBefehle()

    def eingabe(self, befehl):
        """ Diese Funktion verarbeitet einen Befehl im Zustand "Eingabe"
            @arg befehl Eingabebefehl als String
            @return Boolean

            >>> [ eingabe(befehl) for befehl in self.__eingabeBefehle() ]
            [True, False, False, False, False, False, False, False, True]
        """

        print("Eingabe speichern")
        logging.debug("Eingabe: " + befehl)

        self.zustand = self.zustandList[0]

        befehle = self.__eingabeBefehle()

        for i in range(0, len(befehle)):
            if befehle[i] == befehl:
                if befehl == befehle[0]: #50Cent
                    self.zustand = self.zustandList[1]
                    logging.debug('Zustandsaenderung: ' + self.zustandList[0] + " -> " + self.zustandList[1])
                    return True
                if befehl == befehle[len(befehle) - 1]: #beenden
                    return True

        self.zustand = self.zustandList[2]
        logging.debug('Zustandsaenderung: ' + self.zustandList[0] + " -> " + self.zustandList[2])
        return False

    def auswahl(self, befehl):
        """ Diese Funktion verarbeitet einen Befehl im Zustand "Auswahl"
            @arg befehl Eingabebefehl als String
            @return Boolean
        """

        logging.debug("Ausgabe: " + befehl)

        if self.zustand != self.zustandList[1]:
            print("Aktueller Zustand '" + self.zustand + "' akzeptiert keine Auswahl")
            logging.debug('Zustandsaenderung: ' + self.zustand + " -> " + self.zustandList[0])
            self.zustand = self.zustandList[0]
            return False

        """
            >>> [ auswahl(befehl) for befehl in self.__auswahlBefehle() ]
            [True, True, True]
        """

        befehle = self.__auswahlBefehle()

        for i in range(0, len(befehle)):
            if befehle[i] == befehl:
                if befehl != befehle[len(befehle) - 1]: #beenden
                    print("Bitte " + befehle[i] + " entnehmen")

                self.zustand = self.zustandList[0]
                logging.debug('Zustandsaenderung: ' + self.zustandList[1] + " -> " + self.zustandList[0])
                return True

        logging.warning('Befehl ist nicht gueltig')

        print("Befehl '" + befehl + "' existiert nicht")
        return False;

    def zustandsAusgabe(self):
        """ Diese Funktion gibt den aktuellen Zustand und eine Liste möglicher Befehle aus
            @return self.zustand

            >>> zustandsAusgabe()
            self.zustand
        """

        print(self.zustand)
        logging.debug("Zustand: " + self.zustand)

        if self.zustand == self.zustandList[0]:
            print(str(self.__eingabeBefehle()))
        elif self.zustand == self.zustandList[1]:
            print(str(self.__auswahlBefehle()))
        elif self.zustand == self.zustandList[2]:
            print(str(self.__falscheMuenzeBefehle()))
        else:
            logging.warning("Zustand '" + self.zustand + "' existiert nicht");

        return self.zustand
