import sympy as sp

sp.init_printing()

x1, x2, x3 = sp.symbols('x1 x2 x3')

f1 = x1 + x2 ** 2 - x3 ** 2 - 13
print("\n", f1)

f2 = sp.ln(x2 / 4) + sp.exp(0.5*x3-1) - 1
print(f2)

f3 = (x2 - 3)**2 - x3**3 + 7
print(f3)

f = sp.Matrix([[f1], [f2], [f3]])
print('f(x1,x2,x3):\n', f)

X = sp.Matrix([x1, x2, x3])
Df = f.jacobian(X)
print(Df)

X0 = sp.Matrix([1.5,3,2.5])
T = f.subs([[x1,1.5],[x2,3],[x3,2.5]]) + Df.subs([[x1,1.5],[x2,3],[x3,2.5]])*(X-X0)
print(T)

