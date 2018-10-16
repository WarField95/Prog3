
"""
a=[15, 5]
b=[35, 27]
c=[27, 27]
d=[8, 43]
e=[21, 2]

städte =[a,b,c,d,e]

def rundreise(städte):
    ersteStadt = städte.pop[0]
    if städte.length >1:
        for each städte as stadt:
            zweiteListe=copy(städte)
            nächsteStadt = zweiteListe.pop[stadt]

            teilweg=rundreise(zweiteListe)
    else return distance

def distance (ersteStadt, teilweg):
    return ersteStadt-teilweg

"""


import doctest
from itertools import permutations

def distance(city1,city2):
    ##returns distance between two cities in coordinates system
    return ((city1[0]-city2[0])**2+(city1[1]-city2[1])**2)**0.5

def distance_total(cities):
    ##returns distance passing through all cities in order
    return sum([distance(city, cities[index+1])for index, city in enumerate(cities[:-1])])

def travellingSalesman(cities, start=None):
    ##Searches for shortest route by brute force
    if start is None:
        start=cities[0]
    return min([perm for perm in permutations(cities) if perm[0]==start], key=distance_total)

def travelingSalesman_Optimized(cities, start=None):
    ##Always goes to the neares city
    if start is None:
        start=cities[0]
    must_visit=cities
    path=[start]
    must_visit.remove(start)
    while must_visit:
        nearest=min(must_visit,key=lambda x: distance(path[-1], x))
        path.append(nearest)
        ##waypoints.append(path)
        must_visit.remove(nearest)
    return path, ##waypoints


def main():    ##waypoints for array to save removed cities/paths
    ##doctest.testmod()
    cities=[[0,0],[1,5.7],[2,3],[3,9],[0.5,14],[7,2]]

    print(""""minimum distance going around all cities:"""
    .format(
    tuple(cities),  ##tupels are always unchangeable
    cities[0],
    distance_total(travellingSalesman(cities))),
    distance_total(travelingSalesman_Optimized(cities)))
    ##print(waypoints)

if __name__=="__main__":
    main()






