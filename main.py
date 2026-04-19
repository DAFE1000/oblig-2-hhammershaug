# main.py (Oblig 2)
# Løser toppunktet til f(x) = e^(-x/4) * arctan(x)
# Bruker likningen g(x) = arctan(x) - 4/(1+x^2) = 0

import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # f(x): funksjonen
    return math.exp(-x/4.0) * math.atan(x)

def g(x):
    # g(x)=0 gir toppunktet (fra f'(x)=0)
    return math.atan(x) - 4.0/(1.0 + x*x)

def gprime(x):
    # g'(x): trengs til Newton
    return 1.0/(1.0 + x*x) + 8.0*x/((1.0 + x*x)**2)

def bisect(h, a, b, tol=1e-12, maxit=100):
    # Biseksjon: finner rot i [a,b] (krever h(a)*h(b) < 0)
    fa, fb = h(a), h(b)
    if fa * fb > 0:
        raise ValueError("Velg [a,b] med tegnskifte for h(x).")
    for _ in range(maxit):
        m = 0.5*(a + b)
        fm = h(m)
        if abs(fm) < tol or 0.5*(b - a) < tol:
            return m
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5*(a + b)

def newton(h, hprime, x0, tol=1e-12, maxit=50):
    # Newton: rask finpuss av roten
    x = x0
    for _ in range(maxit):
        fx = h(x)
        dfx = hprime(x)
        if dfx == 0:
            break
        x_new = x - fx/dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

if __name__ == "__main__":
    # Finn x* (rot i g). Starter med biseksjon, så Newton
    x0 = bisect(g, 0.0, 10.0, tol=1e-10)   # g(0)<0, g(10)>0
    x_star = newton(g, gprime, x0, tol=1e-14)
    y_star = f(x_star)

    # Skriv ut (minst 4 desimaler)
    print(f"x* = {x_star:.10f}")
    print(f"f(x*) = {y_star:.10f}")
    print(f"Rundet (4 desimaler): x* = {x_star:.4f}, f(x*) = {y_star:.4f}")

    # Plott f og marker toppunktet
    a, b = -5.0, 8.0
    xs = np.linspace(a, b, 800)
    ys = np.array([f(x) for x in xs])

    plt.figure(figsize=(7, 4))
    plt.plot(xs, ys, label="f(x) = e^{-x/4} * arctan(x)")
    plt.scatter([x_star], [y_star], color="red", zorder=3,
                label=f"Toppunkt ({x_star:.4f}, {y_star:.4f})")
    plt.axvline(x_star, color="red", lw=0.8, ls="--")
    plt.axhline(y_star, color="red", lw=0.8, ls="--")
    plt.xlabel("x"); plt.ylabel("f(x)")
    plt.title("Maksimum av f(x)")
    plt.grid(True, ls=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("toppunkt.png", dpi=150)
    plt.show()