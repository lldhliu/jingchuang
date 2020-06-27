"""
 Created by ldh on 18-12-6
"""
__author__ = "ldh"
from itsdangerous import JSONWebSignatureSerializer as Serializer
s1 = Serializer('this is a secret key build by your dad', '600')
a = s1.dumps({'id': 123456789123}).decode('utf-8')
print(a)

s2 = Serializer('this is a secret key build by your dad')
b = s1.loads(a.encode('utf-8'))
print(b)
