from py_eth_pairing import curve_add, curve_mul, pairing2, curve_negate
from py_ecc.bn128 import G1, G2,add, multiply, curve_order
from time import time
import random

curve_add(G1, G1)
print("curve_add")
#print("curve_add")
t0 = time()
#sk = random.getrandbits(4)
#sk = random.randint(1000,1000000)
sk = random.random()
#print(sk)
g1_pk = curve_mul(G1, sk)
#print(g1_pk)
print(time() - t0)

print("curve_mul")
sc = curve_order - 10000
g1_pk = multiply(G1, sc)
t0 = time()
actual = curve_mul(g1_pk, sc)
print(time() - t0)

print("pairing2: expect true")
#sc = 123
g1_pk = multiply(G1, sc)
g2_pk = multiply(G2, sc)
#t0 = time()
actual = pairing2(curve_negate(g1_pk), G2, G1, g2_pk)
print(time() - t0)
expected = True
assert actual == expected

print("pairing2: expect true")
sc = 123
g1_pk = multiply(G1, sc)
g2_pk = multiply(G2, sc)
t0 = time()
actual = pairing2(curve_negate(g1_pk), G2, G1, g2_pk)
print(time() - t0)
#expected = True
#assert actual == expected

