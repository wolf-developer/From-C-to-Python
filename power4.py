from abc import ABC, abstractmethod

class JoueurHumainP4(JoueurS):
    def NouvellePartie():
        pass

    def Jouer(p, asj1):
        p4 = p;
        k = 0
        condition = True
        while condition:
            ss = ""
            if(asj1 == True):
                ss = "rouges"
            else:
                ss = "bleus"
            
            s = input("Choisissez la colonne pour les " + ss + " :")
            
            k = -10
            if (len(s) == 1):
                k = s[0] - 'a' + 1
            condition = k < 1 or k > PositionP4S.nbCo or p4.cases[0][-1 + k * PositionP4S.nbLi] or p4.cases[1][-1 + k * PositionP4S.nbLi] or p4.cases[2][-1 + k * PositionP4S.nbLi]
            
        k = k-1
        rep = 0
        for i in range(1, k):
            if (p4.cases[0][-1 + i * PositionP4S.nbLi] == False and p4.cases[1][-1 + i * PositionP4S.nbLi] == False and p4.cases[2][-1 + i * PositionP4S.nbLi] == False):
                rep = rep + 1
        return rep

class PositionP4S(PositionS):
    def __init__():
        self.gen = 0
        self.lmin1 = 3
        self.lmin2 = self.lmin1
        self.nbLi = 6
        self.nbCo = 10
        self.nbCases = self.nbLi * self.nbCo
        
        self.cases = None
    
    def PositionP4S():
        
        Eval = 0
        NbCoups0 = nbCo
        NbCoups1 = nbCo
        
    def PositionP4S(p):
        
        Eval = p.Eval
        NbCoups1 = p.NbCoups1
        NbCoups0 = p.NbCoups0
        
#            static Random gen = new Random();
#            public static byte lmin1 = 3;
#            public static byte lmin2 = lmin1;
#            public static byte nbLi = 6;
#            public static byte nbCo = 10;
#            public static int nbCases = nbLi * nbCo;
#
#            public BitArray[] cases;

    def Equals(obj):
        q = obj
        for i in range(0, nbLi -1):
            for j in range(0, nbCo -1):
                if (cases[0][i + j * nbLi] != q.cases[0][i + j * nbLi]):
                    return False
                if (cases[1][i + j * nbLi] != q.cases[1][i + j * nbLi]):
                    return False
                if (cases[2][i + j * nbLi] != q.cases[1][i + j * nbLi]):
                    return False
        return True

    def Clone():
        newObj = PositionP4S(self)
        return newObj
    
    def EffectuerCoup(i, j):
        k1 = -1
        h = -1
        condition = True
        while condition:
            condition2 = True
            while condition2:
                k1 += 1
                condition2 = cases[1][nbLi - 1 + k1 * nbLi] or cases[0][nbLi - 1 + k1 * nbLi] or cases[2][nbLi - 1 + k1 * nbLi]
            h += 1
            condition = (h < i)

        k1 = nbLi - 1 + k1 * nbLi
        ell = 0
        for ell in range(0,  nbLi - 1):
            if (cases[1][k1 - ell] or cases[0][k1 - ell] or cases[2][k1 - ell]):
                break
        k1 = k1 - ell + 1

        k0 = -1
        h = -1
        condition = True
        while condition:
            condition2 = True
            while condition2:
                k0 += 1
                condition2 = cases[1][nbLi - 1 + k0 * nbLi] or cases[0][nbLi - 1 + k0 * nbLi] or cases[2][nbLi - 1 + k0 * nbLi]
            h += 1
            condition = (h < j)
        
        k0 = nbLi - 1 + k0 * nbLi
        for ell in range(0, nbLi - 1):
            if (cases[1][k0 - ell] or cases[0][k0 - ell] or cases[2][k0 - ell]):
                break
        k0 = k0 - ell + 1

        if (k0 == k1):
            cases[2][k0] = True
            val = 0
            if(k0%nbLi == nbLi-1):
                val = 1
            
            NbCoups0 -= val 
            NbCoups1 = NbCoups0
            return

        cases[1][k1] = True 
        cases[0][k0] = True
        
        re = [false,false]
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

                while (a < nbLi and a >= 0 and b < nbCo and (cases[cou][b * nbLi + a] )):
                    nb = nb + 1;
                    a += dx 
                    b += dy
                    
                a = x - dx 
                b = y - dy
                while (a < nbLi and a >= 0 and b >= 0 and ( cases[cou][b * nbLi + a] )):
                    nb = nb + 1;
                    a -= dx
                    b -= dy
                if (nb >= lmin1):
                    re[cou] = True

        if (re[0] and re[1]):
            NbCoups0 = 0
            NbCoups1 = 0
            return

        if (re[0]):
            NbCoups0 = 0
            NbCoups1 = 0
            Eval = -1
            return

        if (re[1]):
            NbCoups0 = 0
            NbCoups1 = 0
            Eval = 1
            return

        if(k0 % nbLi == nbLi - 1):
            NbCoups0 -= 1
        if(k1 % nbLi == nbLi - 1):
            NbCoups0 -= 1
        NbCoups1 = NbCoups0
            
    def Affiche():
        print("\n| ")
        for j in range(0, nbCo - 1):
            #print(" " + (char)(j + 'a') + " ") # need to test
            print("\n")
        for j in range(0, nbCo - 1):
            print("---")
        
        for i in range(nbLi - 1, 0, -1):
            print("| ")
            for j in range(0, nbCo):
                ca = 0;
                if (cases[1][j * nbLi + i]):
                    ca = 1
                if (cases[0][j * nbLi + i]):
                    ca = 2
                if (cases[2][j * nbLi + i]): 
                    ca = 3
                if(ca == 0):
                    print(" . ")
                if(ca == 1):
                    #Console.ForegroundColor = ConsoleColor.Red
                    print(" 1 ")
                    #Console.ForegroundColor = ConsoleColor.Black
                if(case == 2):
                    #Console.ForegroundColor = ConsoleColor.DarkBlue;
                    print(" 0 ")
                    #Console.ForegroundColor = ConsoleColor.Black;
                if(case == 3):
                    print(" * ")
                print("\n")
                
            for j in range(0, nbCo - 1):
                print("---")
                print("-\n")
                
def main():
    j1 = JMCTSS(15, 200);
    j0 = JoueurHumainP4();
    par = PartieS(j1, j0, PositionP4S());
    par.Commencer()

if __name__ == '__main__':
    main()