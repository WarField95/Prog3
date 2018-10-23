import random



class VokabelTrainer(object):
    #Konstruktor
    def __init__(self):
        #self.attribut=start_value
        self.d={"house":"Haus", "Cat":"katze", "Nose":"Nase"}

        self.number_questions=5

        self.wrongs = 0
        self.rights = 0
        self.runs = 0



    def hinzufuegen(self):

        input_newger=input("Pls add new german word here").lower()
        input_neweng=input("Pls add new english word here").lower()

        self.d[input_newger]=input_neweng


    def trainieren(self, number_questions, wrongs, rights, runs):

        for i in range(number_questions):
            key1 = random.choice(list(self.d.keys()))
            value1 = self.d.get(self, key1)
            print(value1)
            print(key1)
            input_voc=input("Pls write vocab for {} here: ".format(value1))

            if input_voc.lower() == value1.lower():
                print("right")
                rights = rights+1
            else:
                print("wrong")
                wrongs = wrongs+1

        return rights, wrongs



    def zuruecksetzen(self, number_questions, rights, wrongs, runs):

        self.rights=0
        self.wrongs=0
        self.runs=0

        self.trainieren(number_questions, wrongs, rights, runs)



    def ergebnisAufgabe(self, wrongs, rights):


        print("Wrong answers: " + wrongs + "\n Right answers: " + rights)


    def printDict(self):
        for keys, values in self.d.items():
            print(keys, end=" : ")
            print(values)


    # input_choice=int(input("Pls choose what to do: \n"
    #                    "1 to add a pair of vocabs \n"
    #                    "2 to set back your stuff \n"
    #                    "3 to train your voc knowledge"))

    # while input_choice != 5:
    #
    #     if input_choice == 1:
    #         hinzufuegen()
    #     elif input_choice == 2:
    #         zuruecksetzen(rights, wrongs, runs)
    #     elif input_choice == 3:
    #         trainieren(d, number_questions, wrongs, rights, runs)


test = VokabelTrainer()
test.trainieren(1,0,0,1)
test.ergebnisAufgabe(wrongs, rights)
#test.hinzufuegen()
#test.printDict()