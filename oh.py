from py_eth_pairing import curve_add, curve_mul, pairing2, curve_negate
from py_ecc.bn128 import G1, G2,add, multiply, curve_order
from time import time
import random



#sk = random.getrandbits(4)
#sk = random.randint(1000,1000000)
sk = random.random()
#g1_pk = curve_mul(G1, sk)
#print(g1_pk)
#print(sk)
t0 = time()
print(time() - t0)