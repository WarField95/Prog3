#import getraenkeAutomat
import Prog3.Aufgabe7.getraenkeAutomat as getraenkeAutomat
import doctest
import unittest

doctest.testmod()

class automatTest(unittest.TestCase):
    def setUp(self):
        self.__getraenkeAutomat = getraenkeAutomat.GetraenkeAutomat()

    def testEingabe(self):
        eingabe = self.__getraenkeAutomat.eingabe("50Cent")
        zustand = self.__getraenkeAutomat.zustandsAusgabe()

        self.assertEqual(eingabe, True)
        self.assertEqual(zustand, "Auswahl")
        return

    def testAusgabe(self):
        eingabe = self.__getraenkeAutomat.eingabe("50Cent")
        auswahl = self.__getraenkeAutomat.auswahl("Mineralwasser")
        zustand = self.__getraenkeAutomat.zustandsAusgabe()

        self.assertEqual(eingabe, True)
        self.assertEqual(auswahl, True)
        self.assertEqual(zustand, "Anfang")
        return

    def testZustandsAusgabe(self):
        zustand = self.__getraenkeAutomat.zustandsAusgabe()

        self.assertEqual(zustand, "Anfang")
        return

suite = unittest.TestLoader().loadTestsFromTestCase(automatTest)
unittest.TextTestRunner(verbosity=1).run(suite)

# Instanz erzeugen
g = getraenkeAutomat.GetraenkeAutomat()

g.zustandsAusgabe()

g.eingabe('50Cent')

g.zustandsAusgabe()
# Getränk wählen
g.auswahl('Limonade')
