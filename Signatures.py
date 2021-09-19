# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 01:20:11 2021

@author: etudiant
"""

# Signatures.py
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

def generate_keys() : 
   
    private = rsa.generate_private_key(
           public_exponent=65537,
           key_size=2048,
           backend = default_backend()
           )
    public = private.public_key()
   
    return private, public




"""ici le padding c'est pour le hash
PSS est un type de sel pseudo aléatoire que nous ajoutons 
au message afin de rendre plus difficile l'inversion du hachage,
 alors nous le remplissage afin que vous voyiez toutes ces références
 à sha-256, c'est le type particulier de hachage que nous sommes en utilisant
 il y en a beaucoup mais sha-256 est un type très courant de fonction 
 de hachage, nous passons la longueur du sel que nous ajoutons et puis
 bien sûr nous avons passé la moitié du hachage directement sha-256 et
 cela donne nous une signature
 -Pour remerdier à cela on va mettre la ligne ou y'a le message = bytes... 
 
 quand je faisais message = bytes(message, 'utf-8')
 je ne pouvais qu'avoir des String passé comme message
 pour cela on ajout le str pour message comme ça on va convertir tout le
 message en String et on pourra ainsi faire passer le message qu'il soit un 
 entier, bytes ou n'importe quels types
 
 """
 
       
def sign(message, private) :
   # message = b"A message I want to sign"
    message = bytes(str(message), 'utf-8')
    sig = private.sign(
         message,
         padding.PSS(
             mgf=padding.MGF1(hashes.SHA256()),
             salt_length=padding.PSS.MAX_LENGTH
         ),
         hashes.SHA256()
     )

    return sig



def verify(message, sig, public) : 
 #   public = pr.public_key()
     message = bytes(str(message), 'utf-8')

     try: 
        public.verify(
             sig,
             message,
             padding.PSS(
                 mgf=padding.MGF1(hashes.SHA256()),
                 salt_length=padding.PSS.MAX_LENGTH
             ),
             hashes.SHA256()
         )
        return True
    
     except InvalidSignature:
        return False
    
     except:
        print("Error executing public_key.verify")
        return False
    
      
     

if __name__ == '__main__' :
    pr, pu = generate_keys()
    print(pr)
    print(pu) 
    """Concernant le b c'est le b de bytes 
    et si j'essaie de l'enlever j'aurai une erreur de type 
    data must be bytes-like 
    donc il faut comprendre qu'on utilise des bytes et non des string
    pour le cryptage"""
    message = "this is secret message"
    sig = sign(message, pr)
    print("key is : ")
    """tous les caractères que je pourrais représenter en ascii mais
    la barre oblique x80 qui est une valeur hexadécimale 
    que je ne pourrais pas représenter donc mais voici la
    signature c'est un peu long """
    print(sig)
    correct = verify(message, sig, pu)
    print(correct)
    if correct :
        print("Bravo, signature validée")
    else :
        print("Erreur, mauvaise signature")
        
        
        """Je vais faire un autre exemple sur le premier la signature 
        etait vrais"""
    pr1, pu1 = generate_keys()
    sig1 = sign(message, pr1)
    """Je vais passer la clé publique de la premiere clé pr
    avoir une signature fausse pr vous montrer la difference
       la vrai version pr avoir une signature valide :
           correct = verify(message, sig1, pu1) 
        """
    correct = verify(message, sig1, pu) 
    if correct :
        print("Bravo, signature validée")
    else :
        print("Erreur, mauvaise signature")
        
        """Je vais modifier le message et je vais utiliser les bonnes clés 
        
        Une autre remarque importante le b que vous voyez au debut du message
        c'est le b de Bytes
        """
    badmessage = message + "Q"
    sig1 = sign(message, pr1)
    correct = verify(badmessage, sig, pu) 
    if correct :
        print("Bravo, message inchangé")
    else :
        print("Erreur, message modifié")
        