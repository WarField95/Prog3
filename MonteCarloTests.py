import random, math, time

class MonteCarlo():
    def __init__(self, mode = 0, runAmount = 900):
        self.mode = mode
        self.runAmount = runAmount
        self.timeRand = []

    def congruentialGenerator(self, a, b, m):
        rand = m - a

        for i in range(m):
            rand = (a * rand + b) % m

        return rand

    def getRandom(self, min = 0, max = 1000):
        rand = 1

        timeStart = time.clock()

        if self.mode == 0:
            rand = random.randint(min, max)
        elif self.mode == 1:
            rand = self.congruentialGenerator(min, random.randint(min, max), max)

        self.timeRand.append(float(time.clock() - timeStart))

        return rand

    # Function to check if a random point is inside the circle quarter
    def checkIfInside(self):
        x = float(self.getRandom(0, 1000)/1000)
        y = float(self.getRandom(0, 1000)/1000)

        return math.sqrt(2 * (x * y))

    # Recursive monte carlo function
    def getPi_MonteCarlo(self):
        #init variables
        inside = 0
        all = 0
        totalRuns = 0

        # Run 900 times
        while totalRuns < self.runAmount:
            if self.checkIfInside() <= 1:
                inside = inside + 1
            all = all + 1
            totalRuns = totalRuns + 1

        # Return approximated pi (1 / 4 of circle)
        return str((inside / all) * 4)

    def getRandomTotalTime(self):
        totalTime = 0

        for i in range(0, len(self.timeRand)):
            totalTime += self.timeRand[i]

        return totalTime

    def getRandomAvgTime(self):
        avgTime = 0

        amount = 0

        for i in range(0, len(self.timeRand)):
            avgTime += self.timeRand[i]
            amount += 1

        avgTime = avgTime / amount

        return avgTime

    def getRandomMaxTime(self):
        maxTime  = self.timeRand[0]

        for i in range(0, len(self.timeRand)):
            if maxTime < self.timeRand[i]:
                maxTime = self.timeRand[i]

        return maxTime

    def getRandomMinTime(self):
        minTime = self.timeRand[0]

        for i in range(0, len(self.timeRand)):
            if minTime > self.timeRand[i]:
                minTime = self.timeRand[i]

        return minTime

monteCarlo0 = MonteCarlo(0, 900)
monteCarlo1 = MonteCarlo(1, 900)

pi0 = monteCarlo0.getPi_MonteCarlo()
pi1 = monteCarlo1.getPi_MonteCarlo()

print("Pi nach Monte Carlo:")
print("\t" + "Normal:" + "\t\t" + str(pi0))
print("\t" + "Congruentual:" + "\t" + str(pi1))
print("\n")

print("Total Time")
print("\t" + "Normal:" + "\t\t" + str(monteCarlo0.getRandomTotalTime()))
print("\t" + "Congruentual:" + "\t" + str(monteCarlo1.getRandomTotalTime()))
print("\n")

print("Avg Time")
print("\t" + "Normal:" + "\t\t" + str(monteCarlo0.getRandomAvgTime()))
print("\t" + "Congruentual:" + "\t" + str(monteCarlo1.getRandomAvgTime()))
print("\n")

print("Max Time")
print("\t" + "Normal:" + "\t\t" + str(monteCarlo0.getRandomMaxTime()))
print("\t" + "Congruentual:" + "\t" + str(monteCarlo1.getRandomMaxTime()))
print("\n")

print("Min Time")
print("\t" + "Normal:" + "\t\t" + str(monteCarlo0.getRandomMinTime()))
print("\t" + "Congruentual:" + "\t" + str(monteCarlo1.getRandomMinTime()))
print("\n")