# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 09:39:33 2021

@author: etudiant
"""
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


"""Une petit modification entrain une modification complete """

"""
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(b"abc")
digest.update(b"123")
hash = digest.finalize()
print(hash)

digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(b"abc")
digest.update(b"124")
hash = digest.finalize()
print(hash) """


""" Pour ne pas mettre en peril notre blockchain on va passer
le self.data et le self.privious poue etre hashé les 2


Dans la someClass je vais ajouter le num ds __repr__, il faut
savoir que quand je met des modifications ds __repr__ elles sont prises
en considération après si je modifie """


class someClass:
    string = None
    num = 328965
    def __init__(self, mystring):
        self.string = mystring
    def __repr__(self):
        return self.string + '^^^'+str(self.num)
    
"""Le hash prendra celui du block precedent (qui a le hash du 
hash du precedent et le hash du de la data actuelle )"""   

class Cblock:
    data = None
    previousHash = None
    previousBlock = None
    def __init__(self, data, previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        if previousBlock != None: 
            self.previousHash = previousBlock.computeHash()
    def computeHash(self):
       digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
       digest.update(bytes(str(self.data), 'utf-8'))
       digest.update(bytes(str(self.previousHash), 'utf-8'))
       return digest.finalize()
       
    

 
    
if __name__ == '__main__':
    root = Cblock('I am root', None)
    
    B1 = Cblock('I am child', root)  
    B2 = Cblock(b'I am B1s Brother', root)
    B3 = Cblock(12345, B1)
    B4 = Cblock(someClass('Hi there!'), B3)
    B5 = Cblock('TOP BLOCK!', B4)

    
    
    for b in [B1, B2, B3, B4, B5]:
        if b.previousBlock.computeHash() == b.previousHash:
            print("Succees, hash is good")
        else:
            print("ERROR, hash is not good")
            
    B3.data = 1234
    print(B4.previousBlock.data)
    if B4.previousBlock.computeHash() == B4.previousHash:
            print("Attention, La modification n'a pas été détéctée")
    else:
            print("Modifcation détéctée")
            
    """Je vais changer le num ds la some class à travers B4
    """
    print(B4.data)
    B4.data.num = 99999
    print(B4.data)
    if B5.previousBlock.computeHash() == B5.previousHash:
            print("Attention, La modification n'a pas été détéctée")
    else:
            print("Modifcation détéctée")