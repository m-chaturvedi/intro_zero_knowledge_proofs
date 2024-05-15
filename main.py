import sympy
import random

p = 203363
# Public
# Safe prime to easily find generator .
q = 101681
assert p == 2 * q + 1
sympy.isprime(p)
sympy.isprime(q)
g = 127
# Now Z_p has 4 possible orders (1 , 2 , q , 2q )
assert pow(g, 2, p) != 1 and pow(g, 2, p) != 1
# Assertion that g is indeed a generator .
X = set()
for ind in range(1, p):
    X.add(pow(g, ind, p))

assert len(X) == p - 1
w = 3894  # Secret
h = pow(g, w, p)  # Public
# Step 1 :
# A ( prover ) chooses r in Z_p and sends a :
r = random.randint(1, p - 1)
a = pow(g, r, p)
# Step 2 :
# B ( verifier ) chooses a random c
c = random.randint(1, p - 1)
# Step 3 :
# A ( prover ) sends z after receiving c
z = r + c * w
# Prover verifies if the z is acceptable .
assert pow(g, z, p) == (pow(h, c, p) * a) % p
