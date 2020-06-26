# RC4-Stream-Cipher-Implementation-and-application-in-Encryption-Decryption-
RC4 is a stream cipher designed in 1987 by Ron Rivest for RSA Security. It is a variable key size stream cipher with byte-oriented operations. The algorithm is based on random permutations.Analysis show that the period of the cipher is overwhelmingly likely to be greater than 10^100.
Using the python script 'RC4.py' the 'plaintextRC4.txt' file is read and the characters are counted, the RC4 permuted character stream is generated and XOR'ed with corresponding characters to get the encrypted text which is then decrypted using the same key to get the plaintext back.
The encrypted and decrypted text is written into the file 'EncryptDecryptRC4.txt'
