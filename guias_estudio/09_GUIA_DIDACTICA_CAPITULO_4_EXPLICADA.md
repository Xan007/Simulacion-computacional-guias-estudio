# 09. Guía Didáctica Detallada del Capítulo 4 (Generación de Variables Aleatorias Discretas)

Este documento es un complemento explicativo paso a paso diseñado para entender a profundidad todos los conceptos, algoritmos y procedimientos del **Capítulo 4 de Sheldon Ross** y temas relacionados de **Jerry Banks**.

---

## INTRODUCCIÓN Y CONCEPTO CLAVE

En los capítulos anteriores aprendimos a generar números pseudoaleatorios $U$ entre 0 y 1 ($U \sim U(0, 1)$). 

El objetivo del **Capítulo 4** es resolver el siguiente problema práctico:

> ¿Cómo convertimos esos números $U \in (0, 1)$ en valores enteros o discretos $X$ (como $1, 2, 3, \dots$) para que salgan con las probabilidades exactas que requiere un modelo de simulación real?

Existen **3 métodos fundamentales** para lograr esto:

1. **Método de la Transformada Inversa Discreta** (Mapeo por intervalos).
2. **Método de Composición** (Mezcla de distribuciones / Divide y vencerás).
3. **Simulación por Relaciones entre Distribuciones Especiales** (Suma de variables sencillas como Geométrica $\to$ Binomial Negativa).

---

# MÉTODOS Y EJERCICIOS PASO A PASO

---

## SECCIÓN 1: EL MÉTODO DE LA TRANSFORMADA INVERSA DISCRETA

### 1.1 El Concepto Intuitivo (La Barra de Madera de 1 Metro)

Imagina una barra de madera que mide exactamente 1 metro de longitud ($[0, 1]$).

Si una variable aleatoria discreta $X$ toma varios valores posibles con probabilidades $p_1, p_2, p_3, \dots$ que suman 1, dividimos la barra de madera en pedazos de longitud igual a cada probabilidad $p_i$.

Luego, lanzamos un dardo o canica al azar sobre la barra (nuestro número uniforme $U$). El valor simulado $X$ será el pedazo de madera en el que haya caído la canica.

```
Longitud Total = 1.0
┌──────────────────┬──────────────┬────────────────┬──────────┐
│  Pedazo 1 (p1)   │ Pedazo 2 (p2)│  Pedazo 3 (p3) │ Resto... │
└──────────────────┴──────────────┴────────────────┴──────────┘
0                F(x1)          F(x2)            F(x3)        1.0
                        ▲
                        │ (Cae U aquí -> X = x2)
```

---

### 1.2 Algoritmo General de la Transformada Inversa Discreta

Dada una variable aleatoria $X$ que toma valores $x_1, x_2, \dots, x_n$ con probabilidades $p_1, p_2, \dots, p_n$:

1. Generar un número aleatorio $U \sim U(0, 1)$.
2. Si $U < p_1$, entonces $X = x_1$ y terminar.
3. Si $U < p_1 + p_2$, entonces $X = x_2$ y terminar.
4. Si $U < p_1 + p_2 + p_3$, entonces $X = x_3$ y terminar.
5. En general, asignar $X = x_k$ si $\sum_{j=1}^{k-1} p_j \le U < \sum_{j=1}^k p_j$.

---

### 1.3 El Criterio de Eficiencia (Ordenamiento Descendente)

En programación, cada pregunta `if (U < acumulado)` toma tiempo de procesador.

Si dejamos las probabilidades desordenadas o ponemos primero las probabilidades más pequeñas, el programa tendrá que hacer muchas comparaciones en la mayoría de los intentos.

**Regla de Eficiencia de Sheldon Ross:**
Para minimizar el número promedio de comparaciones de código, **se deben ordenar los valores $x_i$ de MAYOR a MENOR probabilidad $p_i$** antes de calcular las acumuladas.

---

### 1.4 Ejercicio Resuelto Paso a Paso 1 (Sheldon Ross Cap. 4, Ejercicio 3)

#### Enunciado Exacto:
Dé un algoritmo eficiente para simular el valor de una variable aleatoria $X$ tal que:
$$P(X=1) = 0.30, \quad P(X=2) = 0.20, \quad P(X=3) = 0.35, \quad P(X=4) = 0.15$$

---

#### Resolución Detallada:

**Paso 1: Identificar las probabilidades puntuales dadas:**
- $p_1 = P(X=1) = 0.30$
- $p_2 = P(X=2) = 0.20$
- $p_3 = P(X=3) = 0.35$
- $p_4 = P(X=4) = 0.15$

**Paso 2: Ordenar de mayor a menor probabilidad:**
1. Valor $X = 3$ con $p_3 = 0.35$ (Mayor probabilidad)
2. Valor $X = 1$ con $p_1 = 0.30$
3. Valor $X = 2$ con $p_2 = 0.20$
4. Valor $X = 4$ con $p_4 = 0.15$ (Menor probabilidad)

**Paso 3: Construir los intervalos acumulados ($F(x)$):**
- **Intervalo 1 ($X=3$):** Desde $0.00$ hasta $0.35$.
- **Intervalo 2 ($X=1$):** Desde $0.35$ hasta $0.35 + 0.30 = 0.65$.
- **Intervalo 3 ($X=2$):** Desde $0.65$ hasta $0.65 + 0.20 = 0.85$.
- **Intervalo 4 ($X=4$):** Desde $0.85$ hasta $1.00$.

**Paso 4: Formular el pseudocódigo del algoritmo:**
1. Generar $U \sim U(0, 1)$.
2. Si $U < 0.35$, retornar $X = 3$ y terminar.
3. Si $U < 0.65$, retornar $X = 1$ y terminar.
4. Si $U < 0.85$, retornar $X = 2$ y terminar.
5. En caso contrario ($U \ge 0.85$), retornar $X = 4$ y terminar.

**Paso 5: Cálculo formal de la ganancia en eficiencia:**
- **Número esperado de comparaciones CON ordenamiento eficiente:**
$$E[C_{eficiente}] = 1(0.35) + 2(0.30) + 3(0.20) + 3(0.15) = 0.35 + 0.60 + 0.60 + 0.45 = 2.00$$

- **Número esperado de comparaciones SIN ordenamiento (en orden 1, 2, 3, 4):**
$$E[C_{natural}] = 1(0.30) + 2(0.20) + 3(0.35) + 3(0.15) = 0.30 + 0.40 + 1.05 + 0.45 = 2.20$$

*Conclusión:* El ordenamiento reduce en promedio las búsquedas en memoria.

---

# SECCIÓN 2: EL MÉTODO DE COMPOSICIÓN

### 2.1 El Concepto Intuitivo (Mezcla de Distribuciones)

El **Método de Composición** se utiliza cuando la función de probabilidad de una variable $X$ no es homogénea, pero puede dividirse o descomponerse en una suma ponderada de distribuciones más sencillas:

$$P(X = j) = \alpha \cdot f_1(j) + (1 - \alpha) \cdot f_2(j)$$

donde:
- $\alpha \in (0, 1)$ es la probabilidad de elegir la **Rama 1** ($f_1$).
- $1 - \alpha$ es la probabilidad de elegir la **Rama 2** ($f_2$).
- $f_1(j)$ y $f_2(j)$ son funciones de probabilidad válidas (suman 1 cada una en su dominio).

**Analogía Práctica:**
Tienes dos cajas con fichas numeradas:
- La **Caja 1** representa una distribución muy simple (por ejemplo, números uniformes).
- La **Caja 2** representa una distribución más compleja.
- Lanzas una primera moneda ($U_1$). Si $U_1 < \alpha$, sacas una ficha de la Caja 1. Si $U_1 \ge \alpha$, sacas una ficha de la Caja 2.

---

### 2.2 Ejercicio Resuelto Paso a Paso 2 (Sheldon Ross Cap. 4, Ejercicio 15)

#### Enunciado Exacto:
Suponga que la variable aleatoria $X$ puede tomar cualquiera de los valores $1, 2, \dots, 10$ con probabilidades respectivas:
$$0.06, \; 0.06, \; 0.06, \; 0.06, \; 0.06, \; 0.15, \; 0.13, \; 0.14, \; 0.15, \; 0.13$$
Utilice el método de composición para dar un algoritmo que genere el valor de $X$.

---

#### Resolución Detallada:

**Paso 1: Analizar la estructura de las probabilidades dadas:**
Observemos los primeros 5 valores ($j = 1, 2, 3, 4, 5$):
- $P(X=1) = 0.06$
- $P(X=2) = 0.06$
- $P(X=3) = 0.06$
- $P(X=4) = 0.06$
- $P(X=5) = 0.06$

Todos estos 5 valores tienen exactamente **la misma probabilidad ($0.06$)**.

Ahora observemos los últimos 5 valores ($j = 6, 7, 8, 9, 10$):
- $P(X=6) = 0.15$
- $P(X=7) = 0.13$
- $P(X=8) = 0.14$
- $P(X=9) = 0.15$
- $P(X=10) = 0.13$

**Paso 2: Calcular el peso $\alpha$ de la descomposición:**
- Suma de probabilidades del Grupo 1 ($j=1 \dots 5$):
$$\alpha = 0.06 + 0.06 + 0.06 + 0.06 + 0.06 = 5 \times 0.06 = 0.30$$

- Suma de probabilidades del Grupo 2 ($j=6 \dots 10$):
$$1 - \alpha = 0.15 + 0.13 + 0.14 + 0.15 + 0.13 = 0.70$$

**Paso 3: Definir la Subdistribución 1 ($f_1$):**
Como el grupo 1 tiene peso total $\alpha = 0.30$ y 5 elementos equiprobables:
$$f_1(j) = \frac{0.06}{0.30} = \frac{1}{5} = 0.20 \quad \text{para } j \in \{1, 2, 3, 4, 5\}$$
Esta es una **distribución uniforme discreta** en $\{1, 2, 3, 4, 5\}$.

**Paso 4: Definir la Subdistribución 2 ($f_2$):**
Re-escalamos las probabilidades del grupo 2 dividiendo cada una entre $0.70$:
- $f_2(6) = \frac{0.15}{0.70} \approx 0.2143$
- $f_2(7) = \frac{0.13}{0.70} \approx 0.1857$
- $f_2(8) = \frac{0.14}{0.70} = 0.2000$
- $f_2(9) = \frac{0.15}{0.70} \approx 0.2143$
- $f_2(10) = \frac{0.13}{0.70} \approx 0.1857$

**Paso 5: Construir el Algoritmo de Composición:**

1. Generar $U_1 \sim U(0, 1)$.
2. **Si $U_1 < 0.30$ (Rama 1):**
   - Generar un segundo número aleatorio $U_2 \sim U(0, 1)$.
   - Generar una uniforme discreta en $\{1, 2, 3, 4, 5\}$ mediante la fórmula:
$$X = \lfloor 5 \cdot U_2 \rfloor + 1$$
   - Retornar $X$ y terminar.

3. **Si $U_1 \ge 0.30$ (Rama 2):**
   - Generar un segundo número aleatorio $U_2 \sim U(0, 1)$.
   - Aplicar transformada inversa discreta sobre los acumulados de $f_2$:
     - Acumulado para $X=6$: $0.2143$
     - Acumulado para $X=7$: $0.2143 + 0.1857 = 0.4000$
     - Acumulado para $X=8$: $0.4000 + 0.2000 = 0.6000$
     - Acumulado para $X=9$: $0.6000 + 0.2143 = 0.8143$
     - Acumulado para $X=10$: $1.0000$
   - Evaluar las condiciones:
     - Si $U_2 < 0.2143 \implies X = 6$
     - Si $U_2 < 0.4000 \implies X = 7$
     - Si $U_2 < 0.6000 \implies X = 8$
     - Si $U_2 < 0.8143 \implies X = 9$
     - En otro caso $\implies X = 10$
   - Retornar $X$ y terminar.

---

# SECCIÓN 3: SIMULACIÓN POR RELACIONES ENTRE DISTRIBUCIONES ESPECIALES

### 3.1 El Concepto Intuitivo (Suma de Ensayos)

Muchas distribuciones discretas avanzadas nacen de repetir experimentos sencillos de éxito o fracaso (ensayos de Bernoulli).

- **Distribución Geométrica ($G$):** Representa el número de intentos independientes necesarios para obtener **1 primer éxito** con probabilidad de éxito $p$.
- **Distribución Binomial Negativa ($NB$):** Representa el número total de intentos necesarios para acumular **$r$ éxitos independientes**.

Por definición matemática pura:
$$NB(r, p) = \sum_{i=1}^r G_i$$
donde $G_1, G_2, \dots, G_r$ son variables aleatorias geométricas independientes e idénticamente distribuidas con parámetro $p$.

---

### 3.2 Generación Directa de una Variable Geométrica $G_i$

Para generar una variable aleatoria geométrica $G_i \sim \text{Geom}(p)$ usando un único número aleatorio $U_i$, aplicamos la fórmula de la transformada inversa continua truncada:

$$G_i = \left\lfloor \frac{\ln(1 - U_i)}{\ln(1 - p)} \right\rfloor + 1$$

---

### 3.3 Ejercicio Resuelto Paso a Paso 3 (Sheldon Ross Cap. 4, Ejercicio 11)

#### Enunciado Exacto:
La función de masa de probabilidad binomial negativa con parámetros $(r, p)$, donde $r$ es un entero positivo y $0 < p < 1$, representa el número de ensayos necesarios para acumular un total de $r$ éxitos, cuando cada ensayo tiene éxito de manera independiente con probabilidad $p$.  
Obtenga un algoritmo de simulación para esta distribución utilizando la relación con la distribución geométrica.

---

#### Resolución Detallada:

**Paso 1: Establecer la relación física entre variables:**
Sea $X \sim \text{NB}(r, p)$.  
Podemos descomponer la simulación de $X$ en el proceso secuencial de alcanzar $r$ éxitos consecutivos:
- $G_1$: número de ensayos hasta el 1er éxito.
- $G_2$: número de ensayos adicionales desde el 1er éxito hasta el 2do éxito.
- $\dots$
- $G_r$: número de ensayos adicionales desde el éxito $(r-1)$ hasta el éxito $r$.

La suma acumulada de ensayos totales es:
$$X = \sum_{i=1}^r G_i$$

**Paso 2: Formular el algoritmo iterativo:**

1. Definir los parámetros de entrada $r$ (número de éxitos deseados) y $p$ (probabilidad de éxito).
2. Inicializar la variable acumuladora de ensayos $X = 0$.
3. Para $i = 1$ hasta $r$:
   - Generar un número aleatorio $U_i \sim U(0, 1)$.
   - Calcular los ensayos requeridos para este $i$-ésimo éxito:
$$G_i = \left\lfloor \frac{\ln(1 - U_i)}{\ln(1 - p)} \right\rfloor + 1$$
   - Acumular al total: $X = X + G_i$.
4. Retornar $X$ y terminar.

---

# GUÍA RÁPIDA DE DECISIÓN EN EXÁMENES

| Si en el examen te presentan... | ¿Qué método debes elegir? | ¿Cuál es la clave del procedimiento? |
| :--- | :--- | :--- |
| Una tabla con probabilidades $P(X=x)$ desordenadas. | **Transformada Inversa Discreta Eficiente** | Ordenar de mayor a menor probabilidad antes de acumular. |
| Probabilidades donde varios valores son iguales y otros no (o mencionan mezclas). | **Método de Composición** | Calcular $\alpha$ (suma del grupo simple), usar $U_1$ para rama y $U_2$ para valor. |
| Simular número de ensayos para $r$ éxitos (Binomial Negativa). | **Suma de Geométricas** | Usar la fórmula $G_i = \lfloor \frac{\ln(1-U_i)}{\ln(1-p)} \rfloor + 1$ y sumar $r$ veces. |
