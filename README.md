madXOR
======
[![Build Status](https://travis-ci.org/Logic-gate/madXOR.png)](https://travis-ci.org/Logic-gate/madXOR)  

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
**What is Goinig on**
```
[doc (+) key_out(entropy)] + RubbishOutput(n) = encryptedDoc
encryptedDoc / chunkSize = division_name(chunkSize)
tar[division_name(chunkSize)] (+) tarkey = tarName
```
*Example-->From madEncrypt folder*
```
In [4]: x.MadEncrypt('madEncrypt/madEncrypt_example.txt', 'madEncrypt/encrypted/madEncrypt_example.txt', 'madEncrypt/madEncrypt_example.key', 7, 'madEncrypt/madEncrypt_example.rubbish', 3, 1000, 'madEncrypt/chunks/madEncrypt', 'madEncrypt/chunks', 'madEncrypt/madEncrypt_example.tar','madEncrypt/encrypted/madEncrypt_example.tar', 'madEncrypt/madEncrypt_example_tar.key')
```
***
**MadDecrypt** 
```
In [1]: import xor
In [2]: x = xor.Xor()
In [3]: x.MadDecrypt(division_name, noOfChunks, chunkSize, key, decrypted_file, tarName, tarkey, tarOut, tarOutFolder):
```
```
division_name = name of divided chunks
noOfChunks = how many chunks are there - see info.txt at root path
chunkSize = KB - divide encryptedDoc
key = key to decrypt with
decrypted_file = name of decrypted file
tarName = name of encrypted tar
tarkey = key to decrypt encrypted tar
tarOut = name of decrypted tar
tarOutFolder = name folder to write ecrypted data
```

*Example--> From madEncrypt folder*  
do not forget to delete the contents of chunks
```
In [4]: x.MadDecrypt('madEncrypt/chunks/madEncrypt', 3, 1000, 'madEncrypt/madEncrypt_example.key', 'decrypted_example.txt', 'madEncrypt/encrypted/madEncrypt_example.tar', 'madEncrypt/madEncrypt_example_tar.key', 'madEncrypt/decrypted_example.tar', '.')
```
***

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
***<https://github.com/Logic-gate/madXOR/issues/1>***  

***
Theory
---
The final goal is to accomplish real-time XOR-communictation.  

![Alt text](http://sysbase.org/xor.png "Optional title")  
***Based on <http://penbang.sysbase.org/other_projects/simple_xor.pdf>***
```
where EN is the data to be encrypted and DE is the data to be decrypted
```

I am fully aware of the challenges that await me, especially since the container will be in clear-text.  
Check <http://penbang.sysbase.org/other_projects/simple_xor.pdf> for more info.