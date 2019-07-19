import hashlib
from binascii import hexlify
orginal_data = 'data_string'

for nonce in range(2 ** 16):
  string = (orginal_data+str(nonce)) 
  hashval = hashlib.sha256(string.encode('utf-8')).hexdigest()  //sha256 hash of the data_string and nonce combined
  print(nonce,'==>',hashval)
  if hashval[3:7]=='0000':
    print(orginal_data,nonce)
    break
