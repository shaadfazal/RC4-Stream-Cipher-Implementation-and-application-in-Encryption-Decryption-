import numpy as np
import random
S = []
np.array(S)
for i in range(0,256):
    S.append(i)
print("Original S is",S)
keylen=16
K=[]
np.array(K)
for i in range(0,keylen):
    K.append(random.randint(0,255))
T=[]
np.array(T)
for i in range(0,256):
    T.append(K[i%keylen])
print("temporary T is",T)
j=0
for i in range(0,256):
    j=(j+S[i]+T[i])%256
    temp=S[i]
    S[i]=S[j]
    S[j]=temp
print("Permuted S is",S)
# Text Encryption procedure starts from here
fp = open('plaintextRC4.txt', "wt")
fp.write("Text encryption decryption in python using RC4")
fp.close()
val=[]
np.array(val)
fp = open('plaintextRC4.txt', "rt")
count=0
for i in fp:
    for a in i:
        val.append(ord(a))
        count+=1
print("ASCII values of",count,"read plaintext characters are",val)
enc=np.bitwise_xor(S[1:count+1],val)
print("The encrypted ASCII character value encoding is",enc)
encrypt=[]
for i in enc:
    encrypt.append(chr(i))
print("The corresponding encrypted ASCII characters",encrypt)
dec=np.bitwise_xor(enc,S[1:count+1])
print("The decrypted ASCII character value encoding",dec)
decrypt=[]
for i in dec:
    decrypt.append(chr(i))
print("The corresponding decrypted ASCII characters",decrypt)
lp=open("EncryptDecryptRC4.txt","wt")
lp.write("Encrypted text\n")
for i in encrypt:
    try:
        lp.write(i)
    except:
        lp.write("")
lp.write("\nThe decrypted text is\n")
for i in decrypt:
    try:
        lp.write(i)
    except:
        lp.write("")
lp.close()











