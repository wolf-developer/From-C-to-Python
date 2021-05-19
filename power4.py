from abc import ABC, abstractmethod
import random as rand
import time
from bitarray import bitarray
from threading import Thread

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = 0
    def run(self):
        print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return
    
class StopWatch:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0

    def start(self):
        self.start_time = time.time()
        return self.start_time

    def stop(self):
        self.stop_time = time.time()
        return self.stop_time

    def get_elapsed_time(self):
        return (self.stop_time - self.start_time)
        
class PositionS(ABC):
    def __init__(self):
        self._eval = 0.0
        self._nbCoups1 = 0
        self._nbCoups0 = 0
        
    @property
    
    def Eval(self):
        return self._eval

    def Eval(self, value):
        self._eval = value
    
    def NbCoups1(self):
        return self._nbCoups1

    def NbCoups1(self, value):
        self._nbCoups1 = value
    
    def NbCoups2(self):
        return self._nbCoups2

    def NbCoups2(self, value):
        self._nbCoups2 = value
    
    @abstractmethod
    def EffectuerCoup(self, i, j):
        raise NotImplementedError()
    
    def Clone():
        raise NotImplementedError()
    
    def Affiche(self):
        raise NotImplementedError()
    
class JoueurS(ABC):
    @abstractmethod
    def Jouer(p, asj1):
        raise NotImplementedError()
        
    def NouvellePartie(self):
        raise NotImplementedError()
        
    def Des():
        raise NotImplementedError()
        
class JH(JoueurS):
    def Jouer(p, asj1):
        if(asj1 == True):
            pass
        else:
            pass

class PartieS():
    r = 0.0
    def __init__(self, j1, j0, pInitiale):
        self.pCourante = pInitiale.Clone()
        self.j1 = j1
        self.j0 = j0
            
    #def PartieS(j1, j0, pInitiale):
    #    self.j1 = j1
    #    self.j0 = j0
    #    self.pCourante = pInitiale #.Clone()
        
    def NouveauMatch(self, pInitiale):
        self.pCourante = pInitiale.Clone()
        
    def Commencer(self, affichage = True):
        self.j1.NouvellePartie()
        self.j0.NouvellePartie()
        
        condition = True
        while condition:
            if (affichage == True):
                self.pCourante.Affiche() 
                print("\n")
            
            
            res1 = -1
            res0 = -1
            q = self.pCourante.Clone()
            taskThread1 = ThreadWithReturnValue(target=self.j1.Jouer, args=(q, True))
            taskThread1.start()
            
            r = self.pCourante.Clone()
            taskThread0 = ThreadWithReturnValue(target=self.j0.Jouer, args=(r, False))
            taskThread0.start()
            
            res1 = taskThread1.join()
            res0 = taskThread0.join()
            
            self.pCourante.EffectuerCoup(res1, res0)

            rep1 = self.j1.Jouer(self.pCourante.Clone(), True)
            rep0 = self.j0.Jouer(self.pCourante.Clone(), False)
            self.pCourante.EffectuerCoup(rep1, rep0)

            j1.Des()
            j0.Des()
            
            condition = self.pCourante.NbCoups1 > 0 and self.pCourante.NbCoups0 > 0
#            
        
        r = self.pCourante.Eval
        if (affichage):
            self.pCourante.Affiche()
            re = 0
            if (r > 0):
                re = 1 
            if (r < 0): 
                re = -1
            
            if(re == 1):
                print("j1 " + str(self.j1) + " a gagné " + str(self.r) + ".")
            elif(re == -1):
                print("j0 " + str(self.j0) + " a gagné " + str(-self.r) + ".")
            elif(re == 0):
                print("Partie nulle.")

class NoeudS:
    def __init__(self, pere, p):
        self.p = p
        self.pere = pere
        self.fils = None
        self.cross = 0
        self.win = 0.0
        self.indiceMeilleurFils1 = 0
        self.indiceMeilleurFils0 = 0
        if(p != None):
            self.fils = [[None] * self.p.NbCoups1] * self.p.NbCoups0
            #self.fils = NoeudS()[self.p.NbCoups1, self.p.NbCoups0)]
    
    def CalculMeilleurFils(self):
        sM = 0
        sw = 0 
        sc = 0

        i0 = rand.randrange(0, self.p.NbCoups1)
        
        self.indiceMeilleurFils1 = i0
        sw = 0
        sc = 0
            
        for j in range(0, self.p.NbCoups0 - 1):
            if (self.fils[i0, j] != None):
                sc += self.fils[i0, j].cross
                sw += self.fils[i0, j].win
                    
        sM = GetPhi(sc, sw)

        for i in range(0, self.p.NbCoups1 - 1):
            sw = 0
            sc = 0
            for j in range(0, self.p.NbCoups0 - 1):
                if (self.fils[i, j] != None):
                    sc += self.fils[i, j].cross 
                    sw += self.fils[i, j].win
            
                s = GetPhi(sc, sw)
                if (s > sM):
                    sM = s 
                    self.indiceMeilleurFils1 = i
                    

        j0 = rand.randrange(0, self.p.NbCoups1)
        self.indiceMeilleurFils0 = j0;
        sw = 0
        sc = 0
        for i in range(0, self.p.NbCoups1 - 1):
            if (fils[i, j0] != None):
                sc += self.fils[i, j0].cross
                sw += - self.fils[i, j0].win
                
        sM = GetPhi(sc, sw)
        
        for j in range(0, self.p.NbCoups0 - 1):
            sw = 0
            sc = 0
            for i in range(0, self.p.NbCoups1 - 1):
                if (self.fils[i, j] != None):
                    sc += self.fils[i, j].cross
                    sw +=- self.fils[i, j].win
            s = GetPhi(sc, sw)
            if (s > sM):
                sM = s
                self.indiceMeilleurFils0 = j
                
    def MeilleurFils(self):
        if (self.fils[self.indiceMeilleurFils1, self.indiceMeilleurFils0] != None):
            return self.fils[self.indiceMeilleurFils1, self.indiceMeilleurFils0]
        q = p.Clone();
        q.EffectuerCoup(self.indiceMeilleurFils1, self.indiceMeilleurFils0)
        self.fils[self.indiceMeilleurFils1, self.indiceMeilleurFils0] = NoeudS(this, q)
        return self.fils[self.indiceMeilleurFils1, self.indiceMeilleurFils0]     
                    
    def ToString(self):
        s = ""
        s = s + "indiceMF1 = " + str(indiceMeilleurFils1) + " indiceMF0 = " + str(indiceMeilleurFils0) + "\n"
        sw = 0
        sc = 0
        for j in range(0, p.NbCoups0 - 1):
            if (self.fils[indiceMeilleurFils1, j] != None):
                sc = sc + self.fils[indiceMeilleurFils1, j].cross 
                sw = sw + self.fils[indiceMeilleurFils1, j].win
            
        note1 = sw / sc
        sw = 0 
        sc = 0
        for i in range(0, p.NbCoups1 - 1):
            if (self.fils[i,indiceMeilleurFils0] != null):
                sc = sc + self.fils[i,indiceMeilleurFils0].cross
                sw = sw + self.fils[i, indiceMeilleurFils0].win
                 
        note0 = sw / sc
        s = s + "note1= " + str(note1) +  "note0= " + str(note0) + "\n"
        s = s + "\n"
        return s
        
        

class JMCTSS(JoueurS):
    _iter = 0
    
    def __init__(self, a, temps):
        self.a = a
        self.temps = temps
        self.sw = StopWatch()
        self.racine = None
    
    def ToString(self):
        return "JMCTSS[" + str(self.a) + " - temps= " + str(self.temps) + "]"
    
    def JeuHasard(p):
        q = p.Clone();
        
        while (q.NbCoups1 > 0 and q.NbCoups0>0):
            q.EffectuerCoup(rand.randrange(0, q.NbCoups1), rand.randrange(0, p.NbCoups0))
        return q.Eval;
    
    def NouvellePartie(self):
        self.racine = None
    
    def GetPhi(self, C, W):
        return (self.a +W) / (self.a + C)
    
    def Jouer(self, p, asj1):
        self.sw.start()
        # sw.Restart()
        
        self.racine = NoeudS(None, p)
        _iter = 0
        
        #self.sw.stop()
        elapsed = self.sw.get_elapsed_time()
        timelimit = self.temps
        while (self.sw.get_elapsed_time() < self.temps):
            no = self.racine

            condition = True
            while condition:
                no.CalculMeilleurFils()
                no = no.MeilleurFils()
                condition = (no.cross > 0) and (no.fils.Length > 0)

            re = JeuHasard(no.p) # Simulation

            while (no != None): # Rétropropagation
                no.cross = no.cross + 1
                no.win += re
                no = no.pere
            _iter = _iter + 1
            
        self.racine.CalculMeilleurFils()
        rep = 0
        if(asj1 == true):
            rep = self.racine.indiceMeilleurFils1
        else:
            rep = self.racine.indiceMeilleurFils0
        
        res = rep
        return rep
        
    def Des():
        print(str(_iter) + " itérations  ")
        print(str(self.racine)) # Console.Write(racine);

class JoueurHumainP4(JoueurS):
    def NouvellePartie(self):
        pass

    def Jouer(self, p, asj1):
        p4 = p;
        k = 0
        condition = True
        
        abcd = 'abcdefghijklmnopqrstuvwxyz'
        
        while condition:
            ss = ""
            if(asj1 == True):
                ss = "rouges"
            else:
                ss = "bleus"
            
            s = input("Choisissez la colonne pour les " + ss + " :")
            
            k = -10
            if (len(s) == 1):
                res1 = abcd.find(s[0])
                if(res1 >= 0):
                    k = res1 + 1
                    #k = s[0] - 'a' + 1
            condition = k < 1 or k > PositionP4S.nbCo or p4.cases[0][-1 + k * PositionP4S.nbLi] or p4.cases[1][-1 + k * PositionP4S.nbLi] or p4.cases[2][-1 + k * PositionP4S.nbLi]
            
        k = k-1
        rep = 0
        for i in range(1, k):
            if (p4.cases[0][-1 + i * PositionP4S.nbLi] == False and p4.cases[1][-1 + i * PositionP4S.nbLi] == False and p4.cases[2][-1 + i * PositionP4S.nbLi] == False):
                rep = rep + 1
        return rep



class PositionP4S(PositionS):
    def __init__(self, p):
        self.lmin1 = 3
        self.lmin2 = self.lmin1
        self.nbLi = 6
        self.nbCo = 10
        self.nbCases = self.nbLi * self.nbCo
        if(p == None):
             self.Eval = 0
             self.NbCoups0 = self.nbCo
             self.NbCoups1 = self.nbCo
             self.cases = [bitarray(self.nbCases),bitarray(self.nbCases),bitarray(self.nbCases)]
             
        else:
             self.Eval = p.Eval
             self.NbCoups0 = p.NbCoups0
             self.NbCoups1 = p.NbCoups1
             self.cases = [bitarray(self.nbCases),bitarray(self.nbCases),bitarray(self.nbCases)]

    def Equals(self, obj):
        q = obj
        nbLi = self.nbLi
        nbCo = self.nbCo
        for i in range(0, nbLi -1):
            for j in range(0, nbCo -1):
                if (self.cases[0][i + j * nbLi] != q.cases[0][i + j * nbLi]):
                    return False
                if (self.cases[1][i + j * nbLi] != q.cases[1][i + j * nbLi]):
                    return False
                if (self.cases[2][i + j * nbLi] != q.cases[1][i + j * nbLi]):
                    return False
        return True

    def Clone(self):
        newObj = PositionP4S(self)
        return newObj
    
    def EffectuerCoup(self, i, j):
        k1 = -1
        h = -1
        nbLi = self.nbLi
        nbCo = self.nbCo
        
        condition = True
        while condition:
            condition2 = True
            while condition2:
                k1 += 1
                condition2 = self.cases[1][nbLi - 1 + k1 * nbLi] or self.cases[0][nbLi - 1 + k1 * nbLi] or self.cases[2][nbLi - 1 + k1 * nbLi]
            h += 1
            if(h < i):
                condition = True
            else:
                condition = False

        k1 = nbLi - 1 + k1 * nbLi
        ell = 0
        for ell in range(0,  nbLi - 1):
            if (self.cases[1][k1 - ell] or self.cases[0][k1 - ell] or self.cases[2][k1 - ell]):
                break
        k1 = k1 - ell + 1

        k0 = -1
        h = -1
        condition = True
        while condition:
            condition2 = True
            while condition2:
                k0 += 1
                condition2 = self.cases[1][nbLi - 1 + k0 * nbLi] or self.cases[0][nbLi - 1 + k0 * nbLi] or self.cases[2][nbLi - 1 + k0 * nbLi]
            h += 1
            condition = (h < j)
        
        k0 = nbLi - 1 + k0 * nbLi
        for ell in range(0, nbLi - 1):
            if (self.cases[1][k0 - ell] or self.cases[0][k0 - ell] or self.cases[2][k0 - ell]):
                break
        k0 = k0 - ell + 1

        if (k0 == k1):
            self.cases[2][k0] = True
            val = 0
            if(k0%nbLi == nbLi-1):
                val = 1
            
            self.NbCoups0 -= val 
            self.NbCoups1 = self.NbCoups0
            return

        self.cases[1][k1] = True 
        self.cases[0][k0] = True
        
        re = [False,False]
        kt = [k0, k1]

        for cou in range(0,1):
            x = kt[cou] % nbLi
            y = kt[cou] / nbLi

            for dx in range(-1,1): # && !re[cou];
                if(re[cou] == False):
                    break
                for dy in range(0, 1): # && !re[cou];
                    if (re[cou] == False):
                        break    
                    if (dx == 0 and dy == 0):
                        continue
                    if (dx == -1 and dy == 0):
                        continue
                    
                    nb = 1
                    a = x + dx
                    b = y + dy

                while (a < nbLi and a >= 0 and b < nbCo and (self.cases[cou][b * nbLi + a] )):
                    nb = nb + 1;
                    a += dx 
                    b += dy
                    
                a = x - dx 
                b = y - dy
                while (a < nbLi and a >= 0 and b >= 0 and ( self.cases[cou][b * nbLi + a] )):
                    nb = nb + 1;
                    a -= dx
                    b -= dy
                if (nb >= lmin1):
                    re[cou] = True

        if (re[0] and re[1]):
            self.NbCoups0 = 0
            self.NbCoups1 = 0
            return

        if (re[0]):
            self.NbCoups0 = 0
            self.NbCoups1 = 0
            Eval = -1
            return

        if (re[1]):
            self.NbCoups0 = 0
            self.NbCoups1 = 0
            Eval = 1
            return

        if(k0 % nbLi == nbLi - 1):
            self.NbCoups0 -= 1
        if(k1 % nbLi == nbLi - 1):
            self.NbCoups0 -= 1
        self.NbCoups1 = self.NbCoups0
            
    def Affiche(self):
        print("\n| ")
        nbCo = self.nbCo
        nbLi = self.nbLi
        for j in range(0, nbCo - 1):
            #print(" " + (char)(j + 'a') + " ") # need to test
            print("\n")
        for j in range(0, nbCo - 1):
            print("---")
        
        for i in range(nbLi - 1, 0, -1):
            print("| ")
            for j in range(0, nbCo):
                ca = 0;
                if (self.cases[1][j * nbLi + i]):
                    ca = 1
                if (self.cases[0][j * nbLi + i]):
                    ca = 2
                if (self.cases[2][j * nbLi + i]): 
                    ca = 3
                if(ca == 0):
                    print(" . ")
                if(ca == 1):
                    #Console.ForegroundColor = ConsoleColor.Red
                    print(" 1 ")
                    #Console.ForegroundColor = ConsoleColor.Black
                if(ca == 2):
                    #Console.ForegroundColor = ConsoleColor.DarkBlue;
                    print(" 0 ")
                    #Console.ForegroundColor = ConsoleColor.Black;
                if(ca == 3):
                    print(" * ")
                print("\n")
                
            for j in range(0, nbCo - 1):
                print("---")
                print("-\n")
                
def main():
    j1 = JMCTSS(15, 200)
    j0 = JoueurHumainP4()
    po4S = PositionP4S(None)
    par = PartieS(j1, j0, po4S)
    par.Commencer()

if __name__ == '__main__':
    main()