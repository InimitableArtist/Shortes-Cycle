# -*- coding: utf-8 -*-
from collections import deque
import sys

def procitajFile(fileName):
    with open(fileName, "r") as f:
        next(f)
        matrica = f.read().splitlines()
    f.close()
    matricaSusjedstva = [i.replace(" ", "") for i in matrica]
    return matricaSusjedstva

def procitajGraf(matricaSusjedstva):
    graf = dict()
    for i in range(len(matricaSusjedstva)):
        trenutni = []
        for j in range(len(matricaSusjedstva)):
            if (matricaSusjedstva[i][j] == "1"):
                trenutni.append(j + 1)
            graf[i + 1] = trenutni
    return graf

def struk(graf):

    minCiklus = sys.maxsize
    n = len(graf.keys())

    for i in range(n):

        udaljenosti = [sys.maxsize for i in range(n)]
        rod = [-1 for i in range(n)]

        udaljenosti[i] = 0


        q = deque()
        q.append(i + 1)


        while q:

            trenutniVrh = q.popleft()


            for v in graf[trenutniVrh]:

                
                if udaljenosti[v - 1] == sys.maxsize:
                    udaljenosti[v - 1] = 1 + udaljenosti[trenutniVrh - 1]

                    rod[v - 1] = trenutniVrh

                    q.append(v)

                elif rod[trenutniVrh - 1] != v and rod[v - 1] != trenutniVrh - 1:

                    minCiklus = min(minCiklus, udaljenosti[trenutniVrh - 1] + udaljenosti[v - 1] + 1)

        if minCiklus == sys.maxsize:
            return -1
        else:
            return minCiklus
        
def main():
    matricaSusjedstva = procitajFile("graf.txt")
    graf = procitajGraf(matricaSusjedstva)
    
    s = struk(graf)
    
    if s != - 1:
        print("Struk grafa je: ", s)
    else:
        print("Graf nema ciklusa. ")
    
    
if __name__ == "__main__":
    main()    
