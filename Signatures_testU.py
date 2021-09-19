#Signatures.py

def generate_keys():
    private = 'aaa'
    public = 'bbbb'
    return private, public

def sign(message, private):
    sig = 'as5&*#'
    return sig

def verify(message, sig, public):
    return False
    

if __name__ == '__main__':
    pr,pu = generate_keys()
    print(pr)
    print(pu)
    message = "This is a secret message"
    sig = sign(message, pr)
    print(sig)
    correct = verify(message, sig, pu)
    print(correct)

    if correct:
        print("Success! Good sig")
    else:
        print ("ERROR! Signature is bad")

    # Generate an attacker's public and private keys
    pr2, pu2 = generate_keys()

    # Try to sign with the attacker's private key and pass it off as
    # another user's signature
    sig2 = sign(message, pr2)

    correct= verify(message, sig2, pu)
    if correct:
        print("ERROR! Bad signature checks out!")
    else:
        print("Success! Bad sig detected")

    # Modify the message and try to pass the original signature
    badmess = message + "Q"
    correct= verify(badmess, sig, pu)
    if correct:
        print("ERROR! Tampered message checks out!")
    else:
        print("Success! Tampering detected")
    
    
    
        
    
