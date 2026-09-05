# 05. Generación de Variables Aleatorias

---

## 1. El Principio Fundamental de Muestreo

Cualquier estudio de simulación parte de una fuente básica de números uniformes $U \sim U(0, 1)$. El objetivo de este módulo es **transformar** esos valores $U$ en variables aleatorias $X$ que sigan cualquier distribución teórica (Exponencial, Poisson, Binomial, Normal, etc.).

```
           ┌──────────────────────┐
           │    Generador U(0, 1) │
           └──────────┬───────────┘
                      │ U
                      ▼
           ┌─────────────────────────────────────────────────────────┐
           │                     MÉTODOS DE GENERACIÓN               │
           ├────────────────────────┬────────────────────────────────┤
           │ 1. Transformada        │ • Exponencial, Uniforme (a, b) │
           │    Inversa             │ • Poisson, Binomial, Geométrica│
           ├────────────────────────┼────────────────────────────────┤
           │ 2. Aceptación y        │ • Distribuciones con formas    │
           │    Rechazo             │   complejas o acotadas         │
           ├────────────────────────┼────────────────────────────────┤
           │ 3. Composición         │ • Mezclas de subdistribuciones │
           └────────────────────────┴────────────────────────────────┘
                      │
                      ▼
           Variable Aleatoria X deseada
```

---

## 2. Método de la Transformada Inversa

### A. Variables Continuas
Si $X$ tiene función de distribución acumulada continua $F(x) = P(X \le x)$, entonces la variable aleatoria $U = F(X)$ sigue una distribución uniforme $U(0, 1)$.  
Por lo tanto:
$$X = F^{-1}(U)$$

```
     F(x) ▲
        1 ┼───────────────────────┐
          │                  .·´  │   1. Generar U ~ U(0, 1) en el eje Y.
        U ┼─────────────►·        │   2. Proyectar horizontalmente a F(x).
          │            │          │   3. Bajar al eje X para obtener el valor simulado X.
        0 ┼────────────┼──────────┴──► x
          0            X
```

#### 1. Distribución Exponencial:
- **Función de Densidad:** $f(x) = \lambda e^{-\lambda x}, \quad x \ge 0$
- **Función Acumulada:** $F(x) = 1 - e^{-\lambda x}$
- **Inversión Matemática:**
  $$U = 1 - e^{-\lambda x} \implies e^{-\lambda x} = 1 - U \implies -\lambda x = \ln(1 - U)$$
  $$X = -\frac{1}{\lambda} \ln(1 - U)$$
  *(Nota: Como $1 - U$ también es $U(0, 1)$, computacionalmente se usa indistintamente $X = -\frac{1}{\lambda} \ln(U)$).*

- **Ejemplo del Material de Clase:**  
  Si la media entre llegadas es $\beta = 1/\lambda = 10$ minutos (es decir $\lambda = 0.1$) y se genera $U = 0.3067$:
  $$X = -10 \cdot \ln(1 - 0.3067) = -10 \cdot \ln(0.6933) = -10 \cdot (-0.3662) = \mathbf{3.66 \text{ minutos}}$$

#### 2. Distribución Uniforme Continua $U(a, b)$:
$$X = a + (b - a) U$$

---

### B. Variables Discretas
Para una variable aleatoria discreta $X$ que toma valores enteros $x_0 < x_1 < x_2 < \dots$ con probabilidades $p_j = P(X = x_j)$, la función acumulada $F(x) = \sum_{j=0}^k p_j$ es una **función escalonada**.

#### Algoritmo General:
1. Generar $U \sim U(0, 1)$.
2. Si $U < p_0$, hacer $X = x_0$ y terminar.
3. Si $U < p_0 + p_1$, hacer $X = x_1$ y terminar.
4. En general, devolver $X = x_k$ tal que $\sum_{j=0}^{k-1} p_j \le U < \sum_{j=0}^k p_j$.

```
     Intervalo de U:    [0 ────── p0 ────── p0+p1 ────── p0+p1+p2 ────── 1]
     Valor asignado:        X=x0        X=x1           X=x2
```

---

### C. Generación de Poisson (con Recursión Eficiente)

La distribución de Poisson modela el número de eventos en un intervalo de tiempo (media $\lambda$):
$$p_k = P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \dots$$

#### Relación de Recurrencia Clave:
Calcular factoriales $k!$ para $k$ grande desborda la memoria. Se aprovecha la relación entre términos consecutivos:
$$p_0 = e^{-\lambda}$$
$$p_{k+1} = \frac{\lambda}{k + 1} p_k$$

#### Algoritmo de Poisson por Transformada Inversa:
```python
def generar_poisson(lam, u):
    # lam: parámetro lambda (media)
    # u: número aleatorio U(0, 1)
    p = math.exp(-lam)   # p0
    F = p                # F(0)
    k = 0
    while u > F:
        k += 1
        p = (lam / k) * p
        F += p
    return k
```

---

### D. Distribución Binomial $Bi(n, p)$

Representa el número de éxitos en $n$ ensayos independientes de Bernoulli con probabilidad de éxito $p$.

- **Método 1 (Suma de Bernoulli):**  
  Generar $n$ uniformes $U_1, U_2, \dots, U_n$.  
  $$X = \sum_{i=1}^n \mathbb{I}(U_i < p)$$
- **Método 2 (Transformada Inversa Recursiva):**  
  $$p_0 = (1 - p)^n, \quad p_{k+1} = \frac{n - k}{k + 1} \frac{p}{1 - p} p_k$$

---

### E. Distribución Geométrica ($p$)

Número de ensayos hasta el primer éxito:
$$X = \left\lfloor \frac{\ln(1 - U)}{\ln(1 - p)} \right\rfloor + 1$$

---

## 3. Método de Aceptación y Rechazo (Von Neumann)

Se utiliza cuando la función de distribución acumulada $F(x)$ no tiene inversa analítica o es muy costosa de invertir.

```
       Probabilidad ▲
                    │        Constante c * q(y) [Mayorante / Techo]
                    │       ┌─────────────────────────────────────┐
                    │      ╱   . - - - - - - - - - - - - - - .     ╲
                    │     ╱  .´                               `.    ╲
                    │    │  ´    p(y) [Distribución Objetivo]   `    │
                    │    │ │                                     │   │
                    └────┴─┴─────────────────────────────────────┴───┴──► y
```

### Procedimiento:
1. Se tiene la distribución objetivo $p_j$ que queremos simular.
2. Se elige una distribución propuesta $q_j$ fácil de simular (ej. uniforme).
3. Se calcula la **constante de dominación $c$**:
   $$c = \max_j \left( \frac{p_j}{q_j} \right) \ge 1$$
4. **Algoritmo:**
   - **Paso 1:** Simular un valor candidato $Y$ a partir de la distribución propuesta $q$.
   - **Paso 2:** Generar un número aleatorio uniforme $U \sim U(0, 1)$.
   - **Paso 3:** Si $U \le \frac{p_Y}{c \cdot q_Y}$, **ACEPTAR** y hacer $X = Y$.  
     En caso contrario, **RECHAZAR** y regresar al Paso 1.

> **Eficiencia:** El número promedio de iteraciones necesarias para generar una variable es exactamente igual a la constante $c$. Por ello, se busca que $c$ sea lo más cercana a $1$ posible.

#### Ejemplo Numérico:
Queremos generar $X \in \{1, 2, 3, 4, 5\}$ con probabilidades $p = [0.10, 0.20, 0.40, 0.20, 0.10]$.
1. Elegimos $Y$ uniforme discreta en $\{1, 2, 3, 4, 5\} \implies q_j = 0.20$ para todo $j$.
2. Constante $c = \max \left( \frac{0.10}{0.2}, \frac{0.20}{0.2}, \frac{0.40}{0.2}, \frac{0.20}{0.2}, \frac{0.10}{0.2} \right) = \frac{0.40}{0.20} = \mathbf{2.0}$.
3. Criterio de aceptación: Si $U_2 \le \frac{p_Y}{2.0 \times 0.20} = \frac{p_Y}{0.40}$.
   - Si se propone $Y = 3$ ($p_3 = 0.40$): Se acepta si $U_2 \le 0.40/0.40 = 1.0$ (¡siempre se acepta!).
   - Si se propone $Y = 1$ ($p_1 = 0.10$): Se acepta si $U_2 \le 0.10/0.40 = 0.25$.

---

## 4. Método de Composición (Mezclas de Distribuciones)

Se utiliza cuando la función de probabilidad o densidad puede expresarse como una **combinación lineal convexa (mezcla)** de otras distribuciones más sencillas:

$$f(x) = \sum_{i=1}^k \alpha_i f_i(x), \quad \text{con } \alpha_i \ge 0 \text{ y } \sum_{i=1}^k \alpha_i = 1$$

### Algoritmo en 2 Etapas:
```
           Generar U1 ~ U(0, 1)
                  │
                  ▼
       Seleccionar Subdistribución i
           con probabilidad αi
                  │
                  ▼
           Generar U2 ~ U(0, 1)
                  │
                  ▼
     Muestrear X a partir de fi(x)
```

#### Ejemplo Numérico:
Sea una variable $X$ cuya densidad es mezcla de 2 submodelos:
- Con probabilidad $\alpha_1 = 0.70$, $X \sim \text{Exponencial}(\lambda_1 = 2)$.
- Con probabilidad $\alpha_2 = 0.30$, $X \sim \text{Uniforme}(0, 5)$.

**Pasos de Ejecución:**
1. Generar $U_1$:
   - Si $U_1 < 0.70$: Seleccionar rama 1. Generar $U_2$ y calcular $X = -\frac{1}{2}\ln(1 - U_2)$.
   - Si $U_1 \ge 0.70$: Seleccionar rama 2. Generar $U_2$ y calcular $X = 0 + (5 - 0)U_2 = 5 U_2$.
