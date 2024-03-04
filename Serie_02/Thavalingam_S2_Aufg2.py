import sympy as sp

sp.init_printing()

# Teilaufgabe a
x1, x2 = sp.symbols('x1 x2')

f1 = 5 * x1 * x2
print(f1)

f2 = x1 ** 2 * x2 ** 2 + x1 + 2 * x2
print(f2)

# diff
f = sp.Matrix([f1, f2])
print('f(x1,x2):\n', f)

X = sp.Matrix([x1, x2])
Df = f.jacobian(X)
print(Df)

Df0 = Df.subs([(x1, 1), (x2, 2)])
print(Df0)

# Teilaufgabe b
x1, x2, x3 = sp.symbols('x1 x2 x3')

f1 = sp.log(x1 ** 2 + x2 ** 2) + x3 ** 2
print("\n",f1)

f2 = sp.exp(x2 ** 2 + x3 ** 2) + x1 ** 2
print(f2)

f3 = 1 / (x3 ** 2 + x1 ** 2) + x2 ** 2
print(f3)

f = sp.Matrix([f1, f2, f3])
print('f(x1,x2):\n', f)

X = sp.Matrix([x1, x2, x3])
Df = f.jacobian(X)
print(Df)

Df0 = Df.subs([(x1, 1), (x2, 2), (x3, 3)])
print(Df0)
