madXOR
======

Preform Basic XOR Operations 
***

How To
---
***
**Encrypt** 

```
In [1]: import xor
In [2]: x = xor.Xor()
In [3]: x.encrypt(doc, output, key_out, entropy)
```
```
doc = file to encrypt
output = file to output encrypted data
key_out = file to write key
entropy = Shannon Entropy to abide by - it will decrease by 0.1 at every failed attempt
```
*Example*
```
In [4]: x.encrypt('index.html', 'encrypted_index.html', 'index.key', 7)
```

***
**Decrypt** 
```
In [1]: import xor
In [2]: x = xor.Xor()
In [3]: x.decrypt(doc, key, decrypted_file)
```
```
doc = encrypted file
key = key to (+)
decrypted_file = file to write decrypted data 
```
*Example*
```
In [4]: x.decrypt('encrypted_index.html', 'encrypted_index.html', 'index.key', 7)
```
***
**MadEncrypt** 
```
In [1]: import xor
In [2]: x = xor.Xor()
In [3]: x.MadEncrypt(doc, encryptedDoc, key_out, entropy, RubbishOutput, n, chunkSize, division_name, chunks, tarIN, tarName, tarkey)
```
```
doc = file to encrypt
encryptedDoc = file to output encrypted data
key_out = file to write key
entropy = Shannon Entropy to abide by - it will decrease by 0.1 at every failed attempt
RubbishOutput = file to write rubbish - it will generate a footer 1/n the length of doc - see n
n = int ^
chunkSize = KB - divide encryptedDoc
division_name = name of divided chunks
chunks = chunks folder
tarIN = tar to write chunks to
tarName = name of encrypted tar
tarkey = file to write tar key to
```
*Example-->From madEncrypt folder*
```
In [4]: x.MadEncrypt('madEncrypt/madEncrypt_example.txt', 'madEncrypt/encrypted/madEncrypt_example.txt', 'madEncrypt/madEncrypt_example.key', 7, 'madEncrypt/madEncrypt_example.rubbish', 3, 1000, 'madEncrypt/chunks/madEncrypt', 'madEncrypt/chunks', 'madEncrypt/madEncrypt_example.tar','madEncrypt/encrypted/madEncrypt_example.tar', 'madEncrypt/madEncrypt_example_tar.key')
```
***
**MadDecrypt** 
```

```  
***
[![Build Status](https://travis-ci.org/paypal/kraken-js.png)](https://travis-ci.org/paypal/kraken-js)

Notes On xor_webpage
---
A video of xor_webpage in action  
<http://youtu.be/fFiFOnOESL8>  
***
In order for the example to work, you'll need to change line 25 in xor.py  
```
def rand(self, size=[], chars=string.ascii_letters + string.digits + string.hexdigits + string.punctuation + string.whitespace)
```
TO
```
def rand(self, size=[], chars=string.ascii_letters + string.digits)
```
I have started an issue to resolve this *
