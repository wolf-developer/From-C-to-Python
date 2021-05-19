from abc import ABC, abstractmethod


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

#    @NbCoups2.deleter
#    def NbCoups2(self):
#        del self._nbCoups2
    
    @abstractmethod
    def EffectuerCoup(i, j):
        raise NotImplementedError()
    
    def Clone():
        raise NotImplementedError()
    
    def Affiche():
        raise NotImplementedError()
    
class JoueurS(ABC):
    @abstractmethod
    def Jouer(p, asj1):
        raise NotImplementedError()
        
    def NouvellePartie():
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
    def __init__(self):
        self.pCourante = None
        self.j1 = None
        self.j0 = None
        self.r = 0.0
        
    def PartieS(j1, j0, pInitiale):
        self.j1 = j1
        self.j0 = j0
        self.pCourante = pInitiale #.Clone()
        
    def NouveauMatch(pInitiale):
        self.pCourante = pInitiale #.Clone()
        
    def Commencer(affichage = True):
        self.j1.NouvellePartie()
        self.j0.NouvellePartie()
        
        condition = True
        while condition:
            if (affichage == True):
                pCourante.Affiche() 
                print("\n")

            # Task<int> t1 = Task.Run(() => j1.Jouer(pCourante.Clone(), true));
            # Task<int> t0 = Task.Run(() => j0.Jouer(pCourante.Clone(), false));
            #t1.Wait(); t0.Wait();
            #pCourante.EffectuerCoup(t1.Result, t0.Result);

            #int rep1 = j1.Jouer(pCourante.Clone(), true);
            #int rep0 = j0.Jouer(pCourante.Clone(), false);
            #pCourante.EffectuerCoup(rep1, rep0);

            j1.Des()
            j0.Des()
            
            condition = pCourante.NbCoups1 > 0 and pCourante.NbCoups0 > 0
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
    def __init__(self):
        self.p = None
        self.pere = None
        self.fils = None
        self.cross = 0
        self.win = 0.0
        self.indiceMeilleurFils1 = 0
        self.indiceMeilleurFils0 = 0
        
    def NoeudS(pere, p):
        self.pere = pere
        self.p = p
        self.fils = NoeudS(self.p.NbCoups1, self.p.NbCoups0)
    
    def CalculMeilleurFils(phi, g):
        sM = 0
        sw = 0 
        sc = 0

        i0 = g.Next(p.NbCoups1) 
        indiceMeilleurFils1 = i0
        sw = 0
        sc = 0
            
        for j in range(0, p.NbCoups0 - 1):
            if (fils[i0, j] != null):
                sc += fils[i0, j].cross
                sw += fils[i0, j].win
                    
        sM = phi(sc, sw)

        for i in range(0, p.NbCoups1 - 1):
            sw = 0
            sc = 0
            for j in range(0, p.NbCoups0 - 1):
                if (fils[i, j] != None):
                    sc += fils[i, j].cross 
                    sw += fils[i, j].win
            
                s = phi(sc, sw)
                if (s > sM):
                    sM = s 
                    indiceMeilleurFils1 = i
                    

        j0 = g.Next(p.NbCoups0) 
        indiceMeilleurFils0 = j0;
        sw = 0
        sc = 0
        for i in range(0, p.NbCoups1 - 1):
            if (fils[i, j0] != null):
                sc += fils[i, j0].cross
                sw += - fils[i, j0].win
                
        sM = phi(sc, sw)
        
        for j in range(0, p.NbCoups0 - 1):
            sw = 0
            sc = 0
            for i in range(0, p.NbCoups1 - 1):
                if (fils[i, j] != null):
                    sc += fils[i, j].cross
                    sw +=- fils[i, j].win
            s = phi(sc, sw)
            if (s > sM):
                sM = s
                indiceMeilleurFils0 = j
                
    def MeilleurFils():
        if (fils[indiceMeilleurFils1, indiceMeilleurFils0] != None):
            return fils[indiceMeilleurFils1, indiceMeilleurFils0]
        q = p#.Clone();
        q.EffectuerCoup(indiceMeilleurFils1, indiceMeilleurFils0)
        fils[indiceMeilleurFils1, indiceMeilleurFils0] = NoeudS(this, q)
        return fils[indiceMeilleurFils1, indiceMeilleurFils0]     
                    
    def ToString():
        s = ""
        s = s + "indiceMF1 = " + str(indiceMeilleurFils1) + " indiceMF0 = " + str(indiceMeilleurFils0) + "\n"
        sw = 0
        sc = 0
        for j in range(0, p.NbCoups0 - 1):
            if (fils[indiceMeilleurFils1, j] != None):
                sc = sc + fils[indiceMeilleurFils1, j].cross 
                sw = sw + fils[indiceMeilleurFils1, j].win
            
        note1 = sw / sc
        sw = 0 
        sc = 0
        for i in range(0, p.NbCoups1 - 1):
            if (fils[i,indiceMeilleurFils0] != null):
                sc = sc + fils[i,indiceMeilleurFils0].cross
                sw = sw + fils[i, indiceMeilleurFils0].win
                 
        note0 = sw / sc
        s = s + "note1= " + str(note1) +  "note0= " + str(note0) + "\n"
        s = s + "\n"
        return s
        
        

class JMCTSS(JoueurS):
    def __init__(self):
        self.a = 0
        self.temps = 0
        self.racine = None
        self._iter = 0
        self.gen = None
        self.sw = None
    
        #Random gen = new Random();
        #Stopwatch sw = new Stopwatch();
    def JMCTSS(a, temps):
        self.a = a
        self.temps = temps
    
    def ToString():
        return "JMCTSS[" + str(a) + " - temps= " + str(temps) + "]"
    
    def JeuHasard(p):
        q = p#.Clone();
        while (q.NbCoups1 > 0 and q.NbCoups0>0):
            q.EffectuerCoup(gen.Next(0, q.NbCoups1), gen.Next(0, q.NbCoups0))
        return q.Eval;
    
    def NouvellePartie():
        racine = None
        
    def Jouer(p, asj1):
        # sw.Restart()
        #phi = (C, W) => (a+W) / (a + C)
        racine = NoeudS(None, p)
        _iter = 0
        while (sw.ElapsedMilliseconds < temps):
            no = racine

            condition = True
            while condition:
                no.CalculMeilleurFils(phi,gen)
                no = no.MeilleurFils()
                condition = (no.cross > 0) and (no.fils.Length > 0)

            re = JeuHasard(no.p) # Simulation

            while (no != None): # Rétropropagation
                no.cross = no.cross + 1
                no.win += re
                no = no.pere
            _iter = _iter + 1
            
        racine.CalculMeilleurFils(phi,gen)
        rep = 0
        if(asj1 == true):
            rep = racine.indiceMeilleurFils1
        else:
            rep = racine.indiceMeilleurFils0
            
        return rep
        
    def Des():
        print(str(_iter) + " itérations  ")
        print(str(racine)) # Console.Write(racine);
        
