# 03. Integración Numérica y Método de Monte Carlo

---

## 1. De los Métodos Analíticos a Monte Carlo

Cuando necesitamos resolver una integral definida $I = \int_a^b g(x) dx$, tenemos tres caminos:

```
                      ┌──────────────────────────────────────────────┐
                      │    ¿Cómo calcular ∫_a^b g(x) dx?             │
                      └──────────────────────┬───────────────────────┘
                                             │
             ┌───────────────────────────────┼───────────────────────────────┐
             ▼                               ▼                               ▼
    1. ANALÍTICO EXACTO            2. NUMÉRICO CLÁSICO              3. MONTE CARLO
    (Antiderivada, Tablas)         (Regla del Trapecio, Simpson)    (Muestreo Estocástico)
    • Exacto.                      • Divide en intervalos Δx.       • Evalúa g(x) en puntos
    • Rápido.                      • Excelente en 1D y 2D.            aleatorios U(a, b).
    • A menudo NO EXISTE           • Sufre en alta dimensión        • Tasa de error O(1/√N)
      (ej. e^(-x^2)).                (maldición dimensional).         ¡INDEPENDIENTE de la dimensión!
```

---

## 2. Integración Numérica Clásica: Regla del Trapecio

Aproxima el área bajo la curva dividiendo el intervalo $[a, b]$ en $n$ subintervalos de ancho $h = \frac{b-a}{n}$:

```
     y ▲            f(x1)      f(x2)
       │           ┌───────┐
       │   f(a)    │       │     f(b)
       │   ┌───────┘       └──────┐
       │───┴───────┴───────┴──────┴─────► x
           a      x1      x2      b
          |◄──h──►|
```

### Fórmula de Trapecios Compuesta:
$$\int_a^b f(x) dx \approx \frac{h}{2} \left[ f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b) \right]$$

### Ejemplo con $I = \int_0^2 e^{-x^2} dx$:
- Valor analítico exacto: $I = \frac{\sqrt{\pi}}{2} \text{erf}(2) \approx 0.88208139$
- Con paso $h = 0.5$ ($n=4$ intervalos: $x_0=0, x_1=0.5, x_2=1.0, x_3=1.5, x_4=2.0$):
  - $f(0) = e^0 = 1.0000$
  - $f(0.5) = e^{-0.25} = 0.7788$
  - $f(1.0) = e^{-1.00} = 0.3679$
  - $f(1.5) = e^{-2.25} = 0.1054$
  - $f(2.0) = e^{-4.00} = 0.0183$
  $$\text{Área} \approx \frac{0.5}{2} [1.0000 + 2(0.7788 + 0.3679 + 0.1054) + 0.0183] = 0.25 [1.0 + 2(1.2521) + 0.0183] = 0.8806$$
  *(Error relativo: solo $0.16\%$).*

---

## 3. Integración por Monte Carlo

### Fundamento Matemático:
Sea $X \sim U(a, b)$ una variable aleatoria uniforme en $[a, b]$. Su función de densidad es $f(x) = \frac{1}{b-a}$.  
La esperanza matemática de la función $g(X)$ es:
$$\mathbb{E}[g(X)] = \int_a^b g(x) f(x) dx = \int_a^b g(x) \frac{1}{b-a} dx = \frac{1}{b-a} \int_a^b g(x) dx$$

Despejando la integral $\theta = \int_a^b g(x) dx$:
$$\theta = (b - a) \, \mathbb{E}[g(X)]$$

Por la **Ley Fuerte de los Grandes Números**, estimamos la esperanza muestreando $N$ números aleatorios uniformes $U_i \sim U(0, 1)$, transformándolos a $X_i = a + (b-a)U_i$:

$$\hat{\theta}_N = \frac{b - a}{N} \sum_{i=1}^N g(a + (b - a) U_i)$$

### Error Estándar del Estimador:
$$\text{Var}(\hat{\theta}_N) = \frac{(b-a)^2 \sigma_g^2}{N} \implies \text{Error Estándar} = \frac{(b-a) S_g}{\sqrt{N}}$$

> **Gran ventaja de Monte Carlo:** El error decrece como $\mathcal{O}(1/\sqrt{N})$ para cualquier número de dimensiones $d$. En integrales múltiples de dimensión 10 o 20, Monte Carlo es el **único método viable**.

---

## 4. Estimación de $\pi$ por Monte Carlo

Imagina un círculo de radio $r=1$ inscrito en un cuadrado de lado $L=2$ centrado en el origen:

```
     y ▲
     1 ┼───────┌───────┐───────┐
       │     ╱   │   │   ╲     │   Área del Círculo = π * r^2 = π
       │   ╱     │   │     ╲   │   Área del Cuadrado = 2 * 2 = 4
       │  │──────┼───┼──────│  │
     0 ┼──│──────┼───┼──────│──┼──► x
       │  │      │   │      │  │   Probabilidad de caer dentro = π / 4
       │   ╲     │   │     ╱   │
       │     ╲   │   │   ╱     │
    -1 ┼───────└───────┘───────┘
      -1         0           1
```

### Algoritmo:
1. Generar $X_i = 2U_1 - 1 \in [-1, 1]$ y $Y_i = 2U_2 - 1 \in [-1, 1]$.
2. Verificar si el punto cae dentro del círculo: $X_i^2 + Y_i^2 \le 1$.
3. Contar los puntos dentro ($N_{\text{dentro}}$) tras $N$ lanzamientos.
4. **Estimación:**
   $$\frac{N_{\text{dentro}}}{N} \approx \frac{\text{Área Círculo}}{\text{Área Cuadrado}} = \frac{\pi}{4} \implies \hat{\pi} = 4 \times \frac{N_{\text{dentro}}}{N}$$

---

## 5. El Experimento Histórico de la Aguja de Buffon (1777)

Se lanza una aguja de longitud $L$ al azar sobre una superficie con líneas paralelas separadas por una distancia $D$ (con $L \le D$).

```
     Línea 1 ════════════════════════════════════════
                     ╲  θ
                      ╲ L     (Aguja cruza la línea)
     ──────────────────┼─────────────────────────────
                       │ y
     Línea 2 ══════════╧═════════════════════════════
             |◄─────────────── D ───────────────►|
```

- La posición vertical del centro de la aguja es $Y \sim U(0, D/2)$.
- El ángulo con las líneas es $\theta \sim U(0, \pi/2)$.
- La aguja cruza una línea si: $Y \le \frac{L}{2} \sin(\theta)$.

### Probabilidad Teórica de Cruce:
$$P(\text{cruce}) = \int_0^{\pi/2} \left( \int_0^{\frac{L}{2}\sin\theta} \frac{1}{D/2} dy \right) \frac{1}{\pi/2} d\theta = \frac{2L}{\pi D}$$

### Fórmula para Estimar $\pi$:
$$\hat{\pi} = \frac{2 \cdot L \cdot N}{D \cdot (\text{Número de Cruces})}$$

---

## 6. Código Python Didáctico

```python
import numpy as np

def estimar_pi_montecarlo(N=100_000):
    u1 = np.random.uniform(-1, 1, N)
    u2 = np.random.uniform(-1, 1, N)
    dentro = (u1**2 + u2**2) <= 1.0
    pi_estimado = 4.0 * np.sum(dentro) / N
    print(f"Pi Estimado ({N} puntos): {pi_estimado:.5f}")
    return pi_estimado

def integral_montecarlo_exp(N=100_000):
    # Integral de exp(-x^2) en [0, 2]
    u = np.random.uniform(0, 2, N)
    evaluaciones = np.exp(-(u**2))
    integral = (2.0 - 0.0) * np.mean(evaluaciones)
    print(f"Integral Estimada: {integral:.5f} (Exacta: 0.88208)")
    return integral

# Ejecución
estimar_pi_montecarlo()
integral_montecarlo_exp()
```
