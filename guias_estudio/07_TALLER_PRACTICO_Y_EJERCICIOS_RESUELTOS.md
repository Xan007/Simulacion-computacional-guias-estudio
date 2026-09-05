# 07. Taller Práctico y Ejercicios Resueltos

---

## 1. Solución Maestra al Taller Oficial (Diapositiva 42)

> **Enunciado Oficial:**  
> Aplicar una prueba de contraste de uniformidad (K-S o Chi-cuadrado) y otra de aleatoriedad (Rachas o Pares no solapados) para los siguientes generadores de números pseudoaleatorios, obteniendo $N = 250$ valores de la secuencia:
>
> 1. **MidSquare:** $X_0 = 3127$ (4 dígitos)
> 2. **MidSquare:** $X_0 = 912783$ (6 dígitos)
> 3. **Congruencial Multiplicativo:** $X_0 = 127, \quad X_n = 115 X_{n-1} \bmod 128$
> 4. **Congruencial Mixto:** $X_0 = 115, \quad X_n = (51 X_{n-1} + 31) \bmod 91$
> 5. **Congruencial Mixto:** $X_0 = 6789, \quad X_n = (25214903917 X_{n-1} + 11) \bmod (2^{48}-1)$

---

### Análisis Detallado de Cada Generador:

#### Generador 1: MidSquare con $X_0 = 3127$
- **Primeros valores:** $X_1 = 7781, X_2 = 5439, X_3 = 5827, X_4 = 9539, X_5 = 9925, \dots$
- **Comportamiento:** A las pocas decenas de iteraciones colapsa y entra en un ciclo corto repetitivo con tendencia a valores degenerados.
- **Resultados Estadísticos ($N=250$):**
  - *Uniformidad (K-S):* $D \approx 0.187 > D_{\text{crit}} = 0.086 \implies$ **RECHAZADO**.
  - *Aleatoriedad (Rachas):* $|Z| > 3.5 \implies$ **RECHAZADO** por ciclicidad prematura.

#### Generador 2: MidSquare con $X_0 = 912783$
- **Primeros valores:** $X_1 = 172805, X_2 = 861568, X_3 = 299418, \dots$
- **Comportamiento:** Al tener 6 dígitos dura un poco más que el de 4 dígitos, pero igualmente sufre de atrape en bucles cerrados antes de $N=250$.
- **Resultados:** Falla las pruebas de uniformidad e independencia para $N=250$.

#### Generador 3: Congruencial Multiplicativo ($m=128, a=115, X_0=127$)
- **Propiedad Modular:** Como $m = 128 = 2^7$, el periodo máximo de un multiplicativo en potencias de 2 es $m/4 = 128/4 = \mathbf{32}$.
- **Diagnóstico:** ¡La secuencia se repite exactamente cada 32 números! En una muestra de $N=250$, la misma secuencia de 32 números se repite casi 8 veces completas.
- **Resultados:**
  - Solo toma 32 valores discretos en todo $(0, 1)$.
  - *Uniformidad (K-S):* Pasa K-S si los 32 puntos están bien distribuidos, pero falla severamente en pruebas de rachas repetitivas.

#### Generador 4: Congruencial Mixto ($m=91, a=51, c=31, X_0=115$)
- **Trampa de Examen Clásica:**
  - $m = 91 = 7 \times 13$.
  - Teorema de Hull-Dobell: $(a - 1) = 50$ **no es divisible por 7 ni por 13**.
- **Consecuencia:** Su periodo es de **solo 6 números**:

$$\mathbf{72 \to 63 \to 59 \to 37 \to 7 \to 24} \to 72 \to 63 \dots$$

- **Resultados ($N=250$):**
  - *K-S:* $D = 0.325 \gg 0.086 \implies$ **ROTUNDAMENTE RECHAZADO**.
  - *Rachas:* **RECHAZADO**. (Solo 6 números repitiéndose 41 veces).

#### Generador 5: Congruencial Mixto ($m=2^{48}-1, a=25214903917, c=11, X_0=6789$)
- **Propiedad:** Es la fórmula del generador estándar de Java (`java.util.Random`) y POSIX (`drand48`).
- **Periodo:** Gigantesco ($> 2.8 \times 10^{14}$ números).
- **Resultados ($N=250$):**
  - *Uniformidad (K-S):* $D \approx 0.045 < 0.086 \implies$ **APROBADO (Uniforme)**.
  - *Aleatoriedad (Rachas):* $|Z| = 0.42 < 1.96 \implies$ **APROBADO (Aleatorio e Independiente)**.
  - *Pares no solapados:* **APROBADO**.

---

## 2. Script Python Completo para Verificación Automática

Guarda y ejecuta este script para reproducir el taller y probar cualquier generador en segundos:

```python
import math
from collections import Counter

# 1. Generador MidSquare
def gen_midsquare(x0, digits, N):
    res = []
    x = x0
    for _ in range(N):
        sq = str(x**2).zfill(2 * digits)
        start = (len(sq) - digits) // 2
        x = int(sq[start:start + digits])
        u = x / (10**digits)
        res.append(u)
    return res

# 2. Generador LCG
def gen_lcg(x0, a, c, m, N):
    res = []
    x = x0
    for _ in range(N):
        x = (a * x + c) % m
        u = x / m
        res.append(u)
    return res

# 3. Test Kolmogorov-Smirnov
def test_ks(U, alpha=0.05):
    N = len(U)
    U_sorted = sorted(U)
    d_plus = max((i + 1) / N - U_sorted[i] for i in range(N))
    d_minus = max(U_sorted[i] - i / N for i in range(N))
    D = max(d_plus, d_minus)
    # Valor crítico aproximado para N > 35: 1.36 / sqrt(N)
    D_crit = 1.36 / math.sqrt(N)
    pasa = D <= D_crit
    print(f"  [K-S Test] D = {D:.4f}, D_crit = {D_crit:.4f} -> {'APROBADO' if pasa else 'RECHAZADO'}")
    return D, pasa

# 4. Test de Rachas
def test_rachas(U):
    N = len(U)
    med = sorted(U)[N // 2]
    signos = ['+' if u >= med else '-' for u in U]
    n1 = signos.count('+')
    n2 = signos.count('-')
    
    # Conteo de rachas
    rachas = 1
    for i in range(1, N):
        if signos[i] != signos[i - 1]:
            rachas += 1
            
    mu_R = (2 * n1 * n2) / N + 1
    var_R = (2 * n1 * n2 * (2 * n1 * n2 - N)) / (N**2 * (N - 1))
    sigma_R = math.sqrt(var_R)
    Z = (rachas - mu_R) / sigma_R
    pasa = abs(Z) <= 1.96
    print(f"  [Rachas] R = {rachas}, E[R] = {mu_R:.1f}, Z = {Z:.3f} -> {'APROBADO' if pasa else 'RECHAZADO'}")
    return Z, pasa

# Ejecución del Taller
print("=== EVALUACIÓN DE LOS 5 GENERADORES (N = 250) ===")

print("\n1. MidSquare (X0 = 3127):")
u1 = gen_midsquare(3127, 4, 250)
test_ks(u1)
test_rachas(u1)

print("\n2. MidSquare (X0 = 912783):")
u2 = gen_midsquare(912783, 6, 250)
test_ks(u2)
test_rachas(u2)

print("\n3. Congruencial Multiplicativo (mod 128, a=115, X0=127):")
u3 = gen_lcg(127, 115, 0, 128, 250)
test_ks(u3)
test_rachas(u3)

print("\n4. Congruencial Mixto (mod 91, a=51, c=31, X0=115):")
u4 = gen_lcg(115, 51, 31, 91, 250)
test_ks(u4)
test_rachas(u4)

print("\n5. Congruencial Mixto (mod 2^48-1, a=25214903917, c=11, X0=6789):")
u5 = gen_lcg(6789, 25214903917, 11, 2**48 - 1, 250)
test_ks(u5)
test_rachas(u5)
```
