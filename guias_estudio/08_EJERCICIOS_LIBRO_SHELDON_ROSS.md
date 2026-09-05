# 08. Ejercicios Resueltos del Libro de Texto (Sheldon Ross)

Este documento contiene los ejercicios extraídos directamente de los Capítulos 3 y 4 del libro *Simulación* (Sheldon Ross, 2da edición en español). Cada ejercicio incluye el enunciado idéntico del libro, la forma de identificarlo, el criterio de decisión para resolverlo y el procedimiento paso a paso.

---

# PARTE 1: EJERCICIOS DEL CAPÍTULO 3 (Números Aleatorios y Monte Carlo)

---

## Ejercicio 1 (Capítulo 3, Ejercicio 2 de Sheldon Ross)

### Enunciado idéntico del libro:
Si $n = 3$ y $X_n = (5 X_{n-1} + 7) \pmod{200}$, determine $X_1, X_2, \dots, X_{10}$ comenzando con $X_0 = 3$.

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   El problema presenta una relación de recurrencia modular de la forma $X_n = (a X_{n-1} + c) \pmod m$. Esto corresponde a un **Generador Congruencial Lineal Mixto (LCG)**.

2. **Cómo decidir la estrategia de resolución:**  
   Al ser un algoritmo determinista iterativo, se aplica la fórmula paso a paso. Para cada iteración $n$, se toma el valor anterior $X_{n-1}$, se multiplica por el multiplicador $a = 5$, se suma el incremento $c = 7$, y se calcula el resto de la división entera entre el módulo $m = 200$. Para convertir el estado entero $X_n$ en un número pseudoaleatorio $U_n \in [0, 1)$, se divide entre $m$:  
   $$U_n = rac{X_n}{m}$$

---

### Solución Paso a Paso:

- **Iteración 1 ($n = 1$):**  
  $$X_1 = (5 \cdot X_0 + 7) \pmod{200} = (5 \cdot 3 + 7) \pmod{200} = 22 \pmod{200} = 22$$  
  $$U_1 = rac{22}{200} = 0.11$$

- **Iteración 2 ($n = 2$):**  
  $$X_2 = (5 \cdot 22 + 7) \pmod{200} = (110 + 7) \pmod{200} = 117 \pmod{200} = 117$$  
  $$U_2 = rac{117}{200} = 0.585$$

- **Iteración 3 ($n = 3$):**  
  $$X_3 = (5 \cdot 117 + 7) \pmod{200} = (585 + 7) \pmod{200} = 592 \pmod{200} = 192$$  
  $$U_3 = rac{192}{200} = 0.96$$

- **Iteración 4 ($n = 4$):**  
  $$X_4 = (5 \cdot 192 + 7) \pmod{200} = (960 + 7) \pmod{200} = 967 \pmod{200} = 167$$  
  $$U_4 = rac{167}{200} = 0.835$$

- **Iteración 5 ($n = 5$):**  
  $$X_5 = (5 \cdot 167 + 7) \pmod{200} = (835 + 7) \pmod{200} = 842 \pmod{200} = 42$$  
  $$U_5 = rac{42}{200} = 0.21$$

- **Iteración 6 ($n = 6$):**  
  $$X_6 = (5 \cdot 42 + 7) \pmod{200} = (210 + 7) \pmod{200} = 217 \pmod{200} = 17$$  
  $$U_6 = rac{17}{200} = 0.085$$

- **Iteración 7 ($n = 7$):**  
  $$X_7 = (5 \cdot 17 + 7) \pmod{200} = (85 + 7) \pmod{200} = 92 \pmod{200} = 92$$  
  $$U_7 = rac{92}{200} = 0.46$$

- **Iteración 8 ($n = 8$):**  
  $$X_8 = (5 \cdot 92 + 7) \pmod{200} = (460 + 7) \pmod{200} = 467 \pmod{200} = 67$$  
  $$U_8 = rac{67}{200} = 0.335$$

- **Iteración 9 ($n = 9$):**  
  $$X_9 = (5 \cdot 67 + 7) \pmod{200} = (335 + 7) \pmod{200} = 342 \pmod{200} = 142$$  
  $$U_9 = rac{142}{200} = 0.71$$

- **Iteración 10 ($n = 10$):**  
  $$X_{10} = (5 \cdot 142 + 7) \pmod{200} = (710 + 7) \pmod{200} = 717 \pmod{200} = 117$$  
  $$U_{10} = rac{117}{200} = 0.585$$

---

## Ejercicio 2 (Capítulo 3, Ejercicio 3 de Sheldon Ross)

### Enunciado idéntico del libro:
Emplee la simulación para aproximar la siguiente integral:  
$$\int_0^1 e^{e^x} dx$$

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   Se pide evaluar una integral definida $\int_a^b g(x) dx$ utilizando simulación estocástica en lugar de cálculo analítico clásico.

2. **Cómo decidir la estrategia de resolución:**  
   - Primero se identifican los límites de integración: $a = 0$ y $b = 1$.  
   - Cuando el intervalo de integración es exactamente $[0, 1]$, la integral es equivalente al valor esperado de la función $g(U)$, donde $U \sim U(0, 1)$:  
     $$	heta = \int_0^1 g(x) dx = E[g(U)]$$  
   - Por la ley de los grandes números, se generan $k$ números aleatorios independientes $U_1, U_2, \dots, U_k$ uniformemente distribuidos en $(0, 1)$, y la integral se aproxima como el promedio aritmético de las evaluaciones de la función en dichos puntos:  
     $$\hat{	heta} = rac{1}{k} \sum_{i=1}^k g(U_i) = rac{1}{k} \sum_{i=1}^k e^{e^{U_i}}$$

---

### Solución Paso a Paso:

- **Paso 1:** Definir la función integrando $g(x) = e^{e^x}$.
- **Paso 2:** Formular el algoritmo de estimación por Monte Carlo:
  1. Fijar el número de réplicas $k$ (por ejemplo, $k = 10\,000$).
  2. Inicializar un acumulador $S = 0$.
  3. Para $i = 1$ hasta $k$:
     - Generar $U_i \sim U(0, 1)$.
     - Evaluar $y_i = e^{e^{U_i}}$.
     - Sumar $S = S + y_i$.
  4. La estimación final de la integral es:  
     $$\hat{	heta} = rac{S}{k}$$

---

## Ejercicio 3 (Capítulo 3, Ejercicio 12 de Sheldon Ross)

### Enunciado idéntico del libro:
Para $U_1, U_2, \dots$ variables aleatorias uniformes en $(0, 1)$, definimos:  
$$N = 	ext{Mínimo}\left\{n: \sum_{i=1}^n U_i > 1ight\}$$  
Es decir, $N$ es igual a la cantidad de números aleatorios que deben sumarse para exceder a 1. Estime $E[N]$ mediante simulación.

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   Es un problema de modelado de un proceso estocástico discreto donde la variable de interés $N$ es un conteo definido por una condición de parada sobre una suma acumulada.

2. **Cómo decidir la estrategia de resolución:**  
   Se debe simular la regla del proceso una corrida (réplica) a la vez. En cada réplica se acumulan números uniformes $U_i$ hasta que la suma supere $1$, contando cuántos números fueron necesarios ($N$). Repitiendo este experimento $k$ veces, la media muestral de los valores obtenidos de $N$ aproximará el valor esperado $E[N]$.

---

### Solución Paso a Paso:

- **Algoritmo para una sola réplica:**
  1. Inicializar la suma acumulada $S = 0$.
  2. Inicializar el contador $n = 0$.
  3. Mientras $S \le 1$:
     - Generar $U \sim U(0, 1)$.
     - Actualizar la suma: $S = S + U$.
     - Incrementar el contador: $n = n + 1$.
  4. Retornar $N = n$.

- **Algoritmo de estimación global:**
  1. Repetir la réplica anterior $M$ veces (por ejemplo, $M = 1\,000$ corridas), obteniendo valores $N_1, N_2, \dots, N_M$.
  2. Calcular el valor promedio:  
     $$\hat{E}[N] = rac{1}{M} \sum_{j=1}^M N_j$$

- **Resultado teórico conocido:**  
  La teoría demuestra analíticamente que $E[N] = e pprox 2.71828$. La simulación debe converger a este valor conforme aumenta $M$.

---

# PARTE 2: EJERCICIOS DEL CAPÍTULO 4 (Generación de Variables Aleatorias Discretas)

---

## Ejercicio 4 (Capítulo 4, Ejercicio 3 de Sheldon Ross)

### Enunciado idéntico del libro:
Dé un algoritmo eficiente para simular el valor de una variable aleatoria $X$ tal que:  
$$P(X=1) = 0.30, \quad P(X=2) = 0.20, \quad P(X=3) = 0.35, \quad P(X=4) = 0.15$$

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   Nos dan una distribución discreta arbitraria con un número finito de valores posibles y sus respectivas probabilidades puntuales.

2. **Cómo decidir la estrategia de resolución:**  
   Se debe emplear el **Método de la Transformada Inversa Discreta**. Para que el algoritmo sea **eficiente** (reduzca el número promedio de comparaciones en el código), se deben ordenar las probabilidades de **mayor a menor** antes de construir la tabla de distribución acumulada.

---

### Solución Paso a Paso:

- **Paso 1: Ordenar los valores por probabilidad descendente:**
  - $X = 3$ con $p_3 = 0.35$
  - $X = 1$ con $p_1 = 0.30$
  - $X = 2$ con $p_2 = 0.20$
  - $X = 4$ con $p_4 = 0.15$

- **Paso 2: Calcular los intervalos acumulados:**
  - Si $U < 0.35 \implies X = 3$
  - Si $0.35 \le U < 0.35 + 0.30 = 0.65 \implies X = 1$
  - Si $0.65 \le U < 0.65 + 0.20 = 0.85 \implies X = 2$
  - Si $0.85 \le U < 1.00 \implies X = 4$

- **Paso 3: Formular el algoritmo en pseudocódigo:**
  1. Generar un número aleatorio $U \sim U(0, 1)$.
  2. Si $U < 0.35$, hacer $X = 3$ y terminar.
  3. Si $U < 0.65$, hacer $X = 1$ y terminar.
  4. Si $U < 0.85$, hacer $X = 2$ y terminar.
  5. En caso contrario, hacer $X = 4$ y terminar.

- **Número promedio de comparaciones:**  
  $$1(0.35) + 2(0.30) + 3(0.20) + 3(0.15) = 0.35 + 0.60 + 0.60 + 0.45 = 2.00 	ext{ comparaciones}$$  
  *(Sin ordenar, el promedio habría sido $2.35$ comparaciones).*

---

## Ejercicio 5 (Capítulo 4, Ejercicio 15 de Sheldon Ross)

### Enunciado idéntico del libro:
Suponga que la variable aleatoria $X$ puede tomar cualquiera de los valores $1, 2, \dots, 10$ con probabilidades respectivas:  
$$0.06, \; 0.06, \; 0.06, \; 0.06, \; 0.06, \; 0.15, \; 0.13, \; 0.14, \; 0.15, \; 0.13$$  
Utilice el método de composición para dar un algoritmo que genere el valor de $X$.

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   Se pide explícitamente usar el **Método de Composición**, el cual se aplica cuando la función de masa de probabilidad $P(X=j)$ se puede descomponer como una mezcla ponderada de dos o más distribuciones más sencillas:  
   $$P(X=j) = lpha \cdot f_1(j) + (1 - lpha) \cdot f_2(j)$$

2. **Cómo decidir la estrategia de resolución:**  
   - Se analizan las probabilidades dadas: los primeros 5 valores ($j=1,2,3,4,5$) tienen todos probabilidad constante $0.06$.  
   - La suma de las probabilidades de los primeros 5 valores es $5 	imes 0.06 = 0.30$.  
   - La suma de las probabilidades de los últimos 5 valores ($j=6,7,8,9,10$) es $0.15 + 0.13 + 0.14 + 0.15 + 0.13 = 0.70$.  
   - Por tanto, se descompone con peso $lpha = 0.30$:  
     - Subdistribución 1 ($f_1$): Distribución uniforme discreta en $\{1, 2, 3, 4, 5\}$, donde cada número tiene probabilidad $1/5 = 0.20$. Se cumple $0.30 	imes 0.20 = 0.06$.
     - Subdistribución 2 ($f_2$): Distribución discreta en $\{6, 7, 8, 9, 10\}$ con probabilidades reescaladas dividiendo entre $0.70$:  
       $$P(X=6) = rac{0.15}{0.70}, \quad P(X=7) = rac{0.13}{0.70}, \quad P(X=8) = rac{0.14}{0.70}, \quad P(X=9) = rac{0.15}{0.70}, \quad P(X=10) = rac{0.13}{0.70}$$

---

### Solución Paso a Paso:

- **Algoritmo de Composición:**
  1. Generar un número aleatorio $U_1 \sim U(0, 1)$.
  2. **Decisión de rama:**
     - **Si $U_1 < 0.30$ (Rama 1 - Uniforme Discreta):**  
       Generar un segundo número aleatorio $U_2 \sim U(0, 1)$ y asignar:  
       $$X = \lfloor 5 \cdot U_2 floor + 1$$  
       *(Esto genera los valores 1, 2, 3, 4 o 5 con igual probabilidad).*
     - **Si $U_1 \ge 0.30$ (Rama 2 - Transformada Inversa en la segunda parte):**  
       Generar un segundo número aleatorio $U_2 \sim U(0, 1)$ y aplicar transformada inversa discreta sobre las probabilidades reescaladas:
       - Si $U_2 < rac{0.15}{0.70} pprox 0.2143 \implies X = 6$
       - Si $U_2 < rac{0.28}{0.70} = 0.4000 \implies X = 7$
       - Si $U_2 < rac{0.42}{0.70} = 0.6000 \implies X = 8$
       - Si $U_2 < rac{0.57}{0.70} pprox 0.8143 \implies X = 9$
       - En otro caso $\implies X = 10$

---

## Ejercicio 6 (Capítulo 4, Ejercicio 11a/d de Sheldon Ross)

### Enunciado idéntico del libro:
La función de masa de probabilidad binomial negativa con parámetros $(r, p)$, donde $r$ es un entero positivo y $0 < p < 1$, representa el número de ensayos necesarios para acumular un total de $r$ éxitos, cuando cada ensayo tiene éxito de manera independiente con probabilidad $p$.  
Obtenga un algoritmo de simulación para esta distribución utilizando la relación con la distribución geométrica.

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   Se pide simular una distribución discreta especial (Binomial Negativa) relacionándola con otra distribución conocida (Geométrica).

2. **Cómo decidir la estrategia de resolución:**  
   Una variable aleatoria Binomial Negativa $X \sim 	ext{NB}(r, p)$ representa la suma de $r$ variables aleatorias geométricas independientes $G_1, G_2, \dots, G_r$, cada una con parámetro $p$:  
   $$X = \sum_{i=1}^r G_i$$  
   Dado que una variable geométrica $G_i$ se genera directamente por transformada inversa continua como:  
   $$G_i = \left\lfloor rac{\ln(1 - U_i)}{\ln(1 - p)} ightfloor + 1$$  
   la forma más rápida de generar $X$ es generar $r$ números uniformes $U_1, \dots, U_r$, calcular cada $G_i$ y sumarlos.

---

### Solución Paso a Paso:

- **Algoritmo:**
  1. Inicializar la variable acumuladora $X = 0$.
  2. Para $i = 1$ hasta $r$:
     - Generar un número aleatorio $U_i \sim U(0, 1)$.
     - Calcular el valor de la variable geométrica $G_i$:  
       $$G_i = \left\lfloor rac{\ln(1 - U_i)}{\ln(1 - p)} ightfloor + 1$$
     - Sumar al total: $X = X + G_i$.
  3. Retornar $X$.
