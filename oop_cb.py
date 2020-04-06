#Ora;Perc;AdasDb;Nev
# 0    1     2    3
# 6;0;2;Laci

class Cb:
    def __init__(self, sor):
        s = sor.strip().split(';')
        self.ora  = int(s[0])
        self.perc = int(s[1])
        self.db   = int(s[2])
        self.nev  =     s[3]
        

        
    
    
    
    
    

with open("cb.txt", 'r', encoding='utf-8-sig') as f:
    fejlec = f.readline()
#    matrix = f.readlines()  soronként beolvassa listába
#    matrix = f.read()  egyetlen gigastringként olvassa be a file-t
#    matrix = []    igy is lehet ...
 #   for sor in f:
  #      matrix.append(sor)  
    matrix=[sor.strip().split(';') for sor in f] # de így szebb
print(f' 3.feladat: Bejegyzések száma: {len(matrix)} db')

for sor in matrix:
    if sor[2] == '4':
        print(f' 4. feladat: Volt 4 adást indító sofőr!')
        break
sofor = input(f' 5. feladat: Kérek egy nevet: ')
adas = 0
van = False

for sor in matrix:
    if sor[3] == sofor:
        adas = adas + int(sor[2])
        van = True
if van:
    print(f' {sofor} {adas}x használta a CB rádiót.')
else:
    print(f' Nincs ilyen nevű sofőr!')

def AtszamolPerc(ora, perc):    # ez volt a hatos feladat
    return ora * 60 + perc

cb2fejlec = 'Kezdes;Nev;AdasDb\n'

with open("cb2.txt", 'w', encoding='utf-8') as fout:
    fout.write(cb2fejlec)
#    print(cb2fejlec, file=fout)
    for sor in matrix:
        perc = AtszamolPerc(int(sor[0]), int(sor[1]))
        nev = sor[3]
        darab = sor[2]
        szoveg = f'{perc};{nev};{darab}\n'
        fout.write(szoveg)
    #    print(szoveg)
    
halmaz = set()
for sor in matrix:
    halmaz.add(sor[3])
print(f' 8. feladat: Sofőrök száma: {len(halmaz)} fő')
    
    

