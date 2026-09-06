# 08. Ejercicios Resueltos del Libro de Texto (Jerry Banks y Sheldon Ross)

Este documento contiene los ejercicios extraídos directamente de los libros de texto de la asignatura:
- Capítulo 1 de Jerry Banks (*Discrete-Event System Simulation* / *Principles of Simulation*).
- Capítulos 3 y 4 de Sheldon Ross (*Simulación*, 2da edición en español).

Cada ejercicio incluye el enunciado idéntico del libro, la forma de identificarlo, el criterio de decisión para resolverlo y el procedimiento paso a paso.

---

# PARTE 0: EJERCICIOS DEL CAPÍTULO 1 (Jerry Banks - Principios de Simulación)

---

## Ejercicio 1 (Capítulo 1 de Jerry Banks - Simulación Ad Hoc de Sistema de Colas de 1 Servidor)

### Enunciado idéntico del libro:
Consider la operación de un banco con un solo cajero donde los clientes llegan para ser atendidos con tiempos entre arribos de entre 1 y 10 minutos (valores enteros equiprobables). Los clientes son atendidos con tiempos de servicio de entre 1 y 6 minutos (valores enteros equiprobables).
Simule la operación del banco a mano hasta que 20 clientes hayan sido atendidos, y calcule las siguientes medidas de desempeño:
1. Tiempo promedio en el sistema por cliente.
2. Porcentaje de tiempo ocioso del cajero.
3. Tiempo promedio de espera en cola por cliente.
4. Fracción de clientes que tuvieron que esperar en cola.
5. Tiempo promedio de espera en cola de los clientes que esperaron.

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   Es un problema de **Simulación Ad Hoc manual evento a evento / tabla de simulación** para un sistema de colas $M/M/1$ discreto (o uniforme discreto).

2. **Cómo decidir la estrategia de resolución:**  
   - Se debe construir una tabla de simulación columna por columna rastreando cada cliente $i=1, \dots, 20$.
   - **Columnas necesarias:**
     - Número de cliente ($i$)
     - Tiempo entre llegadas ($\Delta A_i$)
     - Tiempo de llegada ($A_i = A_{i-1} + \Delta A_i$)
     - Tiempo de servicio ($S_i$)
     - Tiempo de inicio de servicio ($T_i = \max(A_i, F_{i-1})$)
     - Tiempo de espera en cola ($W_i = T_i - A_i$)
     - Tiempo de finalización de servicio ($F_i = T_i + S_i$)
     - Tiempo total en el sistema ($T_{sys, i} = F_i - A_i$)
     - Tiempo ocioso del cajero ($I_i = T_i - F_{i-1}$ para $i > 1$)
   - **Cálculo de métricas globales:**
     - Tiempo promedio en sistema: $\frac{\sum T_{sys, i}}{N}$
     - Porcentaje de tiempo ocioso: $\frac{\sum I_i}{F_N} \times 100\%$
     - Tiempo promedio de espera: $\frac{\sum W_i}{N}$
     - Fracción de clientes que esperaron: $\frac{\text{Número de clientes con } W_i > 0}{N}$
     - Tiempo promedio de espera de los que esperaron: $\frac{\sum W_i}{\text{Número de clientes con } W_i > 0}$

---

### Solución Paso a Paso:

- **Paso 1: Reglas de actualización del sistema:**
  - $A_1 = \Delta A_1 = 0$ (o tiempo inicial de llegada del primer cliente).
  - Para $i \ge 2$: $A_i = A_{i-1} + \Delta A_i$.
  - Si el cajero está libre al llegar el cliente $i$ ($A_i \ge F_{i-1}$), entonces $T_i = A_i$, $W_i = 0$, y el tiempo ocioso del cajero es $I_i = A_i - F_{i-1}$.
  - Si el cajero está ocupado ($A_i < F_{i-1}$), el cliente espera en cola: $T_i = F_{i-1}$, $W_i = F_{i-1} - A_i$, y el tiempo ocioso es $I_i = 0$.
  - El tiempo de salida es $F_i = T_i + S_i$.
  - El tiempo total en el sistema es $T_{sys, i} = F_i - A_i$.

- **Paso 2: Evaluación de métricas (ejemplo de la simulación de 20 clientes de Jerry Banks):**
  - Supongamos que tras simular los 20 clientes se obtuvieron los siguientes acumulados:
    - Tiempo total simulado hasta la salida del cliente 20: $F_{20} = 99$ minutos.
    - Suma total de tiempos en el sistema: $\sum_{i=1}^{20} T_{sys, i} = 79$ minutos.
    - Suma total de tiempos ociosos del servidor: $\sum_{i=1}^{20} I_i = 30$ minutos.
    - Suma total de tiempos de espera en cola: $\sum_{i=1}^{20} W_i = 10$ minutos.
    - Número de clientes que esperaron ($W_i > 0$): 5 clientes.

- **Paso 3: Cálculo numérico final de cada medida de desempeño:**
  1. Tiempo promedio en el sistema:
$$\bar{T}_{sys} = \frac{79}{20} = 3.95 \text{ minutos}$$
  2. Porcentaje de tiempo ocioso del cajero:
$$\% I = \frac{30}{99} \times 100\% \approx 30.3\%$$
  3. Tiempo promedio de espera en cola por cliente:
$$\bar{W} = \frac{10}{20} = 0.5 \text{ minutos}$$
  4. Fracción de clientes que tuvieron que esperar:
$$P(W > 0) = \frac{5}{20} = 0.25$$
  5. Tiempo promedio de espera de los clientes que esperaron:
$$\bar{W}_{esperaron} = \frac{10}{5} = 2.0 \text{ minutos}$$

---

## Ejercicio 2 (Capítulo 1 de Jerry Banks - Intervalos de Confianza y Tamaño de Muestra para Simulación)

### Enunciado idéntico del libro:
Dada la siguiente tabla con los resultados del tiempo promedio en cola $X_i$ obtenidos en $n = 5$ réplicas independientes de un modelo de simulación:

| Número de Réplica ($i$) | Tiempo Promedio en Cola ($X_i$) |
| :---: | :---: |
| 1 | 63.2 |
| 2 | 69.7 |
| 3 | 67.3 |
| 4 | 64.8 |
| 5 | 72.0 |

Asumiendo que los valores $X_i$ provienen de una distribución normal, calcule los intervalos de confianza del 95% ($\alpha = 0.05$) y del 99% ($\alpha = 0.01$) para la media verdadera $\mu$. Los valores críticos de la distribución $t$ de Student son $t_{4, 0.975} = 2.78$ y $t_{4, 0.995} = 4.60$.

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   Es un problema de **Análisis de Salida de Simulación (Output Analysis)** enfocado en la estimación puntual y por intervalo de confianza para sistemas terminantes.

2. **Cómo decidir la estrategia de resolución:**  
   - Se debe calcular la media muestral $\bar{X}$ y la desviación estándar muestral $S$ de las $n$ réplicas independientes:
$$\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i, \quad S = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2}$$
   - La semi-anchura (half-width) del intervalo de confianza está dada por:
$$h = t_{n-1, 1-\alpha/2} \cdot \frac{S}{\sqrt{n}}$$
   - El intervalo de confianza final se expresa como $(\bar{X} - h, \bar{X} + h)$.

---

### Solución Paso a Paso:

- **Paso 1: Calcular la media muestral $\bar{X}$:**
$$\bar{X} = \frac{63.2 + 69.7 + 67.3 + 64.8 + 72.0}{5} = \frac{337.0}{5} = 67.4$$

- **Paso 2: Calcular las diferencias cuadradas y la varianza muestral $S^2$:**
  - $(63.2 - 67.4)^2 = (-4.2)^2 = 17.64$
  - $(69.7 - 67.4)^2 = (2.3)^2 = 5.29$
  - $(67.3 - 67.4)^2 = (-0.1)^2 = 0.01$
  - $(64.8 - 67.4)^2 = (-2.6)^2 = 6.76$
  - $(72.0 - 67.4)^2 = (4.6)^2 = 21.16$
  - Suma de cuadrados $= 17.64 + 5.29 + 0.01 + 6.76 + 21.16 = 50.86$
  - Varianza muestral $S^2 = \frac{50.86}{5 - 1} = \frac{50.86}{4} = 12.715$
  - Desviación estándar muestral $S = \sqrt{12.715} \approx 3.5658 \approx 3.57$

- **Paso 3: Calcular el error estándar de la media $\frac{S}{\sqrt{n}}$:**
$$\frac{S}{\sqrt{5}} = \frac{3.5658}{\sqrt{5}} = \frac{3.5658}{2.236068} \approx 1.5947$$

- **Paso 4: Calcular la semi-anchura $h$ e intervalo para 95% de confianza ($\alpha = 0.05$):**
  - Valor crítico $t_{4, 0.975} = 2.78$.
  - Semi-anchura: $h_{95\%} = 2.78 \cdot 1.5947 \approx 4.433 \approx 4.44$.
  - Intervalo de confianza del 95%:
$$IC_{95\%} = (67.4 - 4.44, 67.4 + 4.44) = (62.96, 71.84)$$

- **Paso 5: Calcular la semi-anchura $h$ e intervalo para 99% de confianza ($\alpha = 0.01$):**
  - Valor crítico $t_{4, 0.995} = 4.60$.
  - Semi-anchura: $h_{99\%} = 4.60 \cdot 1.5947 \approx 7.335 \approx 7.34$.
  - Intervalo de confianza del 99%:
$$IC_{99\%} = (67.4 - 7.34, 67.4 + 7.34) = (60.06, 74.74)$$

- **Conclusión y Decisión:**
  A mayor nivel de confianza (99% vs 95%), la semi-anchura aumenta de $4.44$ a $7.34$, haciendo el intervalo más amplio para garantizar mayor certidumbre estadística.

---

## Ejercicio 3 (Capítulo 1 de Jerry Banks - Clasificación de Sistemas Terminantes vs No Terminantes)

### Enunciado idéntico del libro:
Clasifique los siguientes sistemas en Terminantes (Terminating) o No Terminantes (Nonterminating), justifique la decisión e indique qué técnica (swamping, preloading, deletion) se debe usar para tratar el sesgo inicial en los casos no terminantes:
1. Un banco comercial que abre a las 9:00 A.M. y cierra sus puertas a las 4:00 P.M. al público.
2. Una línea de ensamblaje industrial de aislamiento térmico de fibra de vidrio que opera continuamente 24 horas al día, 7 días a la semana.
3. Una taquilla de eventos que permanece abierta hasta que todas las boletas se agotan o el evento comienza.

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   Es un problema de **Clasificación Conceptual de Modelos de Simulación y Análisis de Estado Estacionario vs Transitorio**.

2. **Cómo decidir la estrategia de resolución:**  
   - **Sistema Terminante:** Aquel en el que la duración del evento o tiempo de simulación está fijado por una condición natural de inicio y fin (por ejemplo, vacíos e inactivos al abrir, hasta el cierre del servicio o procesamiento de todas las entidades). Se analiza mediante réplicas independientes.
   - **Sistema No Terminante:** Aquel que opera en forma continua y perpetua, donde nos interesa el comportamiento de largo plazo (estado estacionario). Para eliminar el sesgo de la condición inicial (fase transitoria o warm-up phase), se utilizan técnicas como:
     - **Swamping:** Ejecución de corridas extremadamente largas para diluir el efecto transitorio.
     - **Preloading:** Inicializar el sistema cargando entidades en el estado esperado del régimen permanente.
     - **Deletion (Truncado/Warm-up):** Descartar las observaciones recolectadas durante el período transitorio inicial.

---

### Solución Paso a Paso:

1. **Sistema 1 (Banco de 9:00 AM a 4:00 PM):**
   - **Clasificación:** Sistema Terminante.
   - **Justificación:** El evento inicia con una condición fija (banco vacío e inactivo a las 9:00 AM) y finaliza con un evento claro (cierre de puertas a las 4:00 PM y salida del último cliente). La duración del horizonte de planificación es finita y natural.

2. **Sistema 2 (Línea de ensamblaje 24/7):**
   - **Clasificación:** Sistema No Terminante.
   - **Justificación:** No existe un evento de parada natural; el sistema opera en régimen continuo.
   - **Técnica recomendada:** **Deletion (Fase de Warm-up)** o **Preloading**. Se elimina la fase transitoria inicial (warm-up) observando la gráfica de Welch para iniciar la recolección de estadísticas únicamente cuando la medida de desempeño alcanza el estado estacionario.

3. **Sistema 3 (Taquilla de boletas):**
   - **Clasificación:** Sistema Terminante.
   - **Justificación:** La simulación concluye cuando se cumple una condición de parada explícita (venta total de boletas o inicio del evento).

---

# PARTE 1: EJERCICIOS DEL CAPÍTULO 3 (Números Aleatorios y Monte Carlo)

---

## Ejercicio 4 (Capítulo 3, Ejercicio 2 de Sheldon Ross)

### Enunciado idéntico del libro:
Si $n = 3$ y $X_n = (5 X_{n-1} + 7) \bmod 200$, determine $X_1, X_2, \dots, X_{10}$ comenzando con $X_0 = 3$.

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   El problema presenta una relación de recurrencia modular de la forma $X_n = (a X_{n-1} + c) \bmod m$. Esto corresponde a un **Generador Congruencial Lineal Mixto (LCG)**.

2. **Cómo decidir la estrategia de resolución:**  
   Al ser un algoritmo determinista iterativo, se aplica la fórmula paso a paso. Para cada iteración $n$, se toma el valor anterior $X_{n-1}$, se multiplica por el multiplicador $a = 5$, se suma el incremento $c = 7$, y se calcula el resto de la división entera entre el módulo $m = 200$. Para convertir el estado entero $X_n$ en un número pseudoaleatorio $U_n \in [0, 1)$, se divide entre $m$:  
$$U_n = \frac{X_n}{m}$$

---

### Solución Paso a Paso:

- Iteración 1 ($n = 1$): $X_1 = (5 \cdot 3 + 7) \bmod 200 = 22$, luego $U_1 = \frac{22}{200} = 0.11$.
- Iteración 2 ($n = 2$): $X_2 = (5 \cdot 22 + 7) \bmod 200 = 117$, luego $U_2 = \frac{117}{200} = 0.585$.
- Iteración 3 ($n = 3$): $X_3 = (5 \cdot 117 + 7) \bmod 200 = 592 \bmod 200 = 192$, luego $U_3 = \frac{192}{200} = 0.96$.
- Iteración 4 ($n = 4$): $X_4 = (5 \cdot 192 + 7) \bmod 200 = 967 \bmod 200 = 167$, luego $U_4 = \frac{167}{200} = 0.835$.
- Iteración 5 ($n = 5$): $X_5 = (5 \cdot 167 + 7) \bmod 200 = 842 \bmod 200 = 42$, luego $U_5 = \frac{42}{200} = 0.21$.
- Iteración 6 ($n = 6$): $X_6 = (5 \cdot 42 + 7) \bmod 200 = 217 \bmod 200 = 17$, luego $U_6 = \frac{17}{200} = 0.085$.
- Iteración 7 ($n = 7$): $X_7 = (5 \cdot 17 + 7) \bmod 200 = 92 \bmod 200 = 92$, luego $U_7 = \frac{92}{200} = 0.46$.
- Iteración 8 ($n = 8$): $X_8 = (5 \cdot 92 + 7) \bmod 200 = 467 \bmod 200 = 67$, luego $U_8 = \frac{67}{200} = 0.335$.
- Iteración 9 ($n = 9$): $X_9 = (5 \cdot 67 + 7) \bmod 200 = 342 \bmod 200 = 142$, luego $U_9 = \frac{142}{200} = 0.71$.
- Iteración 10 ($n = 10$): $X_{10} = (5 \cdot 142 + 7) \bmod 200 = 717 \bmod 200 = 117$, luego $U_{10} = \frac{117}{200} = 0.585$.

---

## Ejercicio 5 (Capítulo 3, Ejercicio 3 de Sheldon Ross)

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
$$\theta = \int_0^1 g(x) dx = E[g(U)]$$
   - Por la ley de los grandes números, se generan $k$ números aleatorios independientes $U_1, U_2, \dots, U_k$ uniformemente distribuidos en $(0, 1)$, y la integral se aproxima como el promedio aritmético de las evaluaciones de la función en dichos puntos:  
$$\hat{\theta} = \frac{1}{k} \sum_{i=1}^k g(U_i) = \frac{1}{k} \sum_{i=1}^k e^{e^{U_i}}$$

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
$$\hat{\theta} = \frac{S}{k}$$

---

## Ejercicio 6 (Capítulo 3, Ejercicio 12 de Sheldon Ross)

### Enunciado idéntico del libro:
Para $U_1, U_2, \dots$ variables aleatorias uniformes en $(0, 1)$, definimos:  
$$N = \min\left\{n: \sum_{i=1}^n U_i > 1\right\}$$
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
$$\hat{E}[N] = \frac{1}{M} \sum_{j=1}^M N_j$$

- **Resultado teórico conocido:**  
  La teoría demuestra analíticamente que $E[N] = e \approx 2.71828$. La simulación debe converger a este valor conforme aumenta $M$.

---

# PARTE 2: EJERCICIOS DEL CAPÍTULO 4 (Generación de Variables Aleatorias Discretas)

---

## Ejercicio 7 (Capítulo 4, Ejercicio 3 de Sheldon Ross)

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
$$1(0.35) + 2(0.30) + 3(0.20) + 3(0.15) = 0.35 + 0.60 + 0.60 + 0.45 = 2.00 \text{ comparaciones}$$
  *(Sin ordenar, el promedio habría sido $2.35$ comparaciones).*

---

## Ejercicio 8 (Capítulo 4, Ejercicio 15 de Sheldon Ross)

### Enunciado idéntico del libro:
Suponga que la variable aleatoria $X$ puede tomar cualquiera de los valores $1, 2, \dots, 10$ con probabilidades respectivas:  
$$0.06, \; 0.06, \; 0.06, \; 0.06, \; 0.06, \; 0.15, \; 0.13, \; 0.14, \; 0.15, \; 0.13$$
Utilice el método de composición para dar un algoritmo que genere el valor de $X$.

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   Se pide explícitamente usar el **Método de Composición**, el cual se aplica cuando la función de masa de probabilidad $P(X=j)$ se puede descomponer como una mezcla ponderada de dos o más distribuciones más sencillas:  
$$P(X=j) = \alpha \cdot f_1(j) + (1 - \alpha) \cdot f_2(j)$$

2. **Cómo decidir la estrategia de resolución:**  
   - Se analizan las probabilidades dadas: los primeros 5 valores ($j=1,2,3,4,5$) tienen todos probabilidad constante $0.06$.  
   - La suma de las probabilidades de los primeros 5 valores es $5 \times 0.06 = 0.30$.  
   - La suma de las probabilidades de los últimos 5 valores ($j=6,7,8,9,10$) es $0.15 + 0.13 + 0.14 + 0.15 + 0.13 = 0.70$.  
   - Por tanto, se descompone con peso $\alpha = 0.30$:  
     - Subdistribución 1 ($f_1$): Distribución uniforme discreta en $\{1, 2, 3, 4, 5\}$, donde cada número tiene probabilidad $1/5 = 0.20$. Se cumple $0.30 \times 0.20 = 0.06$.
     - Subdistribución 2 ($f_2$): Distribución discreta en $\{6, 7, 8, 9, 10\}$ con probabilidades reescaladas dividiendo entre $0.70$:  
$$P(X=6) = \frac{0.15}{0.70}, \quad P(X=7) = \frac{0.13}{0.70}, \quad P(X=8) = \frac{0.14}{0.70}, \quad P(X=9) = \frac{0.15}{0.70}, \quad P(X=10) = \frac{0.13}{0.70}$$

---

### Solución Paso a Paso:

- **Algoritmo de Composición:**
  1. Generar un número aleatorio $U_1 \sim U(0, 1)$.
  2. **Decisión de rama:**
     - Si $U_1 < 0.30$ (Rama 1 - Uniforme Discreta): Generar un segundo número aleatorio $U_2 \sim U(0, 1)$ y hacer $X = \lfloor 5 \cdot U_2 \rfloor + 1$.
     - Si $U_1 \ge 0.30$ (Rama 2 - Transformada Inversa en la segunda parte): Generar un segundo número aleatorio $U_2 \sim U(0, 1)$ y aplicar transformada inversa discreta sobre las probabilidades reescaladas:
       - Si $U_2 < \frac{0.15}{0.70} \approx 0.2143 \implies X = 6$
       - Si $U_2 < \frac{0.28}{0.70} = 0.4000 \implies X = 7$
       - Si $U_2 < \frac{0.42}{0.70} = 0.6000 \implies X = 8$
       - Si $U_2 < \frac{0.57}{0.70} \approx 0.8143 \implies X = 9$
       - En otro caso $\implies X = 10$

---

## Ejercicio 9 (Capítulo 4, Ejercicio 11a/d de Sheldon Ross)

### Enunciado idéntico del libro:
La función de masa de probabilidad binomial negativa con parámetros $(r, p)$, donde $r$ es un entero positivo y $0 < p < 1$, representa el número de ensayos necesarios para acumular un total de $r$ éxitos, cuando cada ensayo tiene éxito de manera independiente con probabilidad $p$.  
Obtenga un algoritmo de simulación para esta distribución utilizando la relación con la distribución geométrica.

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   Se pide simular una distribución discreta especial (Binomial Negativa) relacionándola con otra distribución conocida (Geométrica).

2. **Cómo decidir la estrategia de resolución:**  
   Una variable aleatoria Binomial Negativa $X \sim \text{NB}(r, p)$ representa la suma de $r$ variables aleatorias geométricas independientes $G_1, G_2, \dots, G_r$, cada una con parámetro $p$:  
$$X = \sum_{i=1}^r G_i$$
   Dado que una variable geométrica $G_i$ se genera directamente por transformada inversa continua como:  
$$G_i = \left\lfloor \frac{\ln(1 - U_i)}{\ln(1 - p)} \right\rfloor + 1$$
   la forma más rápida de generar $X$ es generar $r$ números uniformes $U_1, \dots, U_r$, calcular cada $G_i$ y sumarlos.

---

### Solución Paso a Paso:

- **Algoritmo:**
  1. Inicializar la variable acumuladora $X = 0$.
  2. Para $i = 1$ hasta $r$:
     - Generar un número aleatorio $U_i \sim U(0, 1)$.
     - Calcular el valor de la variable geométrica $G_i = \left\lfloor \frac{\ln(1 - U_i)}{\ln(1 - p)} \right\rfloor + 1$.
     - Sumar al total: $X = X + G_i$.
  3. Retornar $X$.

---

# PARTE 3: EJERCICIOS DE PRUEBAS ESTADÍSTICAS Y ALEATORIEDAD (TEST DE RACHAS)

---

## Ejercicio 10 (Ejercicio Oficial del Material de Clase - Prueba de Rachas por Mediana)

### Enunciado idéntico del material de clase:
Dada la siguiente secuencia de $N = 20$ números pseudoaleatorios generados en el intervalo $(0, 1)$:

$$U = [0.34, \, 0.89, \, 0.12, \, 0.76, \, 0.95, \, 0.43, \, 0.61, \, 0.18, \, 0.82, \, 0.55, \, 0.29, \, 0.91, \, 0.05, \, 0.48, \, 0.67, \, 0.73, \, 0.15, \, 0.88, \, 0.39, \, 0.52]$$

Realice el **Test de Rachas (Runs Test)** basado en la mediana con un nivel de significancia $\alpha = 0.05$ para determinar si la secuencia cumple con la hipótesis de aleatoriedad e independencia.

---

### Razonamiento y Criterio de Decisión:

1. **Cómo identificar el tipo de problema:**  
   Se entrega una secuencia numérica de valores continuos y se solicita evaluar si los datos provienen de un proceso independiente y aleatorio (no correlacionado en el tiempo) usando el **Test de Rachas**.

2. **Cómo decidir la estrategia de resolución:**  
   - Se halla la mediana teórica de la distribución uniforme (o la mediana muestral de la secuencia). En $U(0, 1)$, la mediana es $\text{mediana} = 0.50$.
   - Se asigna el signo $+$ si $U_i \ge 0.50$ y el signo $-$ si $U_i < 0.50$.
   - Se cuentan las transiciones entre signos consecutivos para determinar el número total de rachas $R$.
   - Se calcula el número de valores positivos $n_1$ y negativos $n_2$.
   - Se evalúa la media teórica $\mu_R$, la varianza $\sigma_R^2$ y el estadístico estandarizado $Z$:
$$\mu_R = \frac{2 n_1 n_2}{N} + 1, \quad \sigma_R^2 = \frac{2 n_1 n_2 (2 n_1 n_2 - N)}{N^2 (N - 1)}, \quad Z = \frac{R - \mu_R}{\sigma_R}$$
   - Se compara $|Z|$ contra el valor crítico bilateral $Z_{\alpha/2} = Z_{0.025} = 1.96$:
     - Si $|Z| \le 1.96 \implies$ **Se ACEPTA la hipótesis de aleatoriedad**.
     - Si $|Z| > 1.96 \implies$ **Se RECHAZA la hipótesis de aleatoriedad**.

---

### Solución Paso a Paso:

- **Paso 1: Asignar signos a la secuencia usando la mediana ($0.50$):**

| $i$ | $U_i$ | Signo | $i$ | $U_i$ | Signo |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0.34 | **$-$** | 11 | 0.29 | **$-$** |
| 2 | 0.89 | **$+$** | 12 | 0.91 | **$+$** |
| 3 | 0.12 | **$-$** | 13 | 0.05 | **$-$** |
| 4 | 0.76 | **$+$** | 14 | 0.48 | **$-$** |
| 5 | 0.95 | **$+$** | 15 | 0.67 | **$+$** |
| 6 | 0.43 | **$-$** | 16 | 0.73 | **$+$** |
| 7 | 0.61 | **$+$** | 17 | 0.15 | **$-$** |
| 8 | 0.18 | **$-$** | 18 | 0.88 | **$+$** |
| 9 | 0.82 | **$+$** | 19 | 0.39 | **$-$** |
| 10 | 0.55 | **$+$** | 20 | 0.52 | **$+$** |

Secuencia de signos obtenida:
$$[-], \; [+], \; [-], \; [+, +], \; [-], \; [+], \; [-], \; [+, +], \; [-], \; [+], \; [-, -], \; [+, +], \; [-], \; [+], \; [-], \; [+]$$

- **Paso 2: Contar el número de observaciones y de rachas ($R$):**
  - Número de valores positivos ($n_1$ con $+ \ge 0.50$): $n_1 = 11$
  - Número de valores negativos ($n_2$ con $- < 0.50$): $n_2 = 9$
  - Tamaño de muestra total $N = n_1 + n_2 = 20$.
  - Conteo de transiciones de cambio de signo (rachas):
    1. Racha 1: $[-]$ (elemento 1)
    2. Racha 2: $[+]$ (elemento 2)
    3. Racha 3: $[-]$ (elemento 3)
    4. Racha 4: $[+, +]$ (elementos 4, 5)
    5. Racha 5: $[-]$ (elemento 6)
    6. Racha 6: $[+]$ (elemento 7)
    7. Racha 7: $[-]$ (elemento 8)
    8. Racha 8: $[+, +]$ (elementos 9, 10)
    9. Racha 9: $[-]$ (elemento 11)
    10. Racha 10: $[+]$ (elemento 12)
    11. Racha 11: $[-, -]$ (elementos 13, 14)
    12. Racha 12: $[+, +]$ (elementos 15, 16)
    13. Racha 13: $[-]$ (elemento 17)
    14. Racha 14: $[+]$ (elemento 18)
    15. Racha 15: $[-]$ (elemento 19)
    16. Racha 16: $[+]$ (elemento 20)
  
  Total de rachas observadas: **$R = 16$**

- **Paso 3: Calcular la media teórica $\mu_R$ y la varianza $\sigma_R^2$:**

$$\mu_R = \frac{2 \cdot n_1 \cdot n_2}{N} + 1 = \frac{2 \cdot 11 \cdot 9}{20} + 1 = \frac{198}{20} + 1 = 9.9 + 1 = \mathbf{10.9}$$

$$\sigma_R^2 = \frac{2 \cdot n_1 \cdot n_2 \cdot (2 n_1 n_2 - N)}{N^2 (N - 1)} = \frac{198 \cdot (198 - 20)}{20^2 \cdot (20 - 1)} = \frac{198 \cdot 178}{400 \cdot 19} = \frac{35244}{7600} \approx \mathbf{4.63737}$$

$$\sigma_R = \sqrt{4.63737} \approx \mathbf{2.15346}$$

- **Paso 4: Calcular el estadístico estandarizado $Z$:**

$$Z = \frac{R - \mu_R}{\sigma_R} = \frac{16 - 10.9}{2.15346} = \frac{5.1}{2.15346} \approx \mathbf{2.368}$$

- **Paso 5: Regla de decisión para $\alpha = 0.05$:**
  - Valor crítico bilateral para $\alpha = 0.05$: $Z_{\text{crítico}} = 1.96$.
  - Comparación: $|Z| = 2.368 > 1.96$.

- **Conclusión Final:**
  Como $|Z| = 2.368 > 1.96$, **se RECHAZA la hipótesis nula de aleatoriedad e independencia**. El valor positivo de $Z$ ($+2.368$) indica que la secuencia tiene **demasiadas rachas** (demasiadas oscilaciones rápidas entre valores altos y bajos), lo que evidencia una falta de verdadera aleatoriedad en el generador.


