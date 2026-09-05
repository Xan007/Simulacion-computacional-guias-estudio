# 04. Generadores de Números Pseudoaleatorios

---

## 1. ¿Por qué "Pseudoaleatorios"?

En simulación computacional, **no usamos azar físico** (ruletas o decaimiento radiactivo), sino algoritmos deterministas que producen **números pseudoaleatorios**.

```
                           ¿Por qué determinismo en simulación?
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        ▼                                   ▼                                   ▼
  REPRODUCIBILIDAD                     DEPURACIÓN                      CONTROL EXPERIMENTAL
  (Misma semilla da exactamente       (Si hay un bug, podemos        (Comparar 2 políticas de
   los mismos resultados).             reproducir el fallo idéntico).  inventario con la MISMA demanda).
```

### Propiedades Deseadas de un Buen Generador:
1. **Uniformidad:** Los valores generados deben distribuirse uniformemente en $(0, 1)$.
2. **Independencia:** Cada número no debe depender de los anteriores (sin correlación serial).
3. **Periodo Largo:** Debe generar millones de números antes de que la secuencia empiece a repetirse.
4. **Eficiencia Computacional:** Pocas operaciones aritméticas por número generado.

---

## 2. Método de Cuadrados Medios (MidSquare - Von Neumann, 1946)

Fue el primer generador algorítmico de la historia.

### Algoritmo Paso a Paso:
1. Elegir una semilla inicial $X_0$ de $2n$ dígitos (típicamente 4 dígitos, $n=2$).
2. Elevar la semilla al cuadrado: $Y_0 = X_0^2$ (obteniendo hasta $4n$ dígitos).
3. Si tiene menos de $4n$ dígitos, **rellenar con ceros a la izquierda**.
4. Extraer los **$2n$ dígitos centrales** como el nuevo número $X_1$.
5. Normalizar: $U_1 = \frac{X_1}{10^{2n}} \in [0, 1)$.
6. Repetir el proceso con $X_1$ como nueva semilla.

```
       X0 = 3127 (4 dígitos)
           │ Elevación al cuadrado
           ▼
      X0^2 = 9778129 ──► Rellenar a 8 dígitos: [09] [7781] [29]
                                                    ▲
                                            Dígitos Centrales
                                                    │
                                           X1 = 7781 ──► U1 = 0.7781
```

### Traza con $X_0 = 3127$ ($2n=4$ dígitos):
- $i=1$: $3127^2 = 09\mathbf{7781}29 \implies X_1 = 7781, \, U_1 = 0.7781$
- $i=2$: $7781^2 = 60\mathbf{5439}61 \implies X_2 = 5439, \, U_2 = 0.5439$
- $i=3$: $5439^2 = 29\mathbf{5827}21 \implies X_3 = 5827, \, U_3 = 0.5827$
- $i=4$: $5827^2 = 33\mathbf{9539}29 \implies X_4 = 9539, \, U_4 = 0.9539$

### Defectos Fatales de MidSquare:
- Tiende a caer rápidamente en **ceros** (si $X_i = 0000$, todos los siguientes serán $0000$).
- Posee **periodos muy cortos** y bucles cerrados. **Hoy solo tiene valor histórico y pedagógico**.

---

## 3. Generadores Congruenciales Lineales (LCG - Lehmer, 1951)

Se basan en aritmética modular. Son la base de los generadores clásicos.

### A. Generador Congruencial Multiplicativo:

$$X_{n+1} = (a \cdot X_n) \bmod m$$

$$U_n = \frac{X_n}{m}$$

- **Semilla:** $X_0 > 0$.
- **Multiplicador:** $a > 0$.
- **Módulo:** $m > 0$.
- **Periodo Máximo:** Puede alcanzar como máximo $m - 1$ (si $m$ es primo y $a$ es raíz primitiva).

### B. Generador Congruencial Mixto (Lineal):

$$X_{n+1} = (a \cdot X_n + c) \bmod m$$

$$U_n = \frac{X_n}{m}$$

- **Incremento:** $c > 0$.
- **Periodo Máximo:** Puede alcanzar el periodo completo $m$ (generar todos los enteros de $0$ a $m-1$).

---

## 4. Teorema de Hull-Dobell (Periodo Completo $m$)

> **Condición Necesaria y Suficiente:**  
> Un generador congruencial mixto $X_{n+1} = (a X_n + c) \bmod m$ tiene **periodo máximo $m$** si y solo si se cumplen las siguientes **TRES condiciones**:
>
> 1. **$c$ y $m$ son coprimos:** $\gcd(c, m) = 1$ (no comparten ningún factor primo común).
> 2. **Para todo número primo $p$ que divida a $m$, $(a - 1)$ es múltiplo de $p$:**  
>    Si $p \mid m \implies (a - 1) \bmod p = 0$.
> 3. **Si $m$ es divisible por 4, $(a - 1)$ debe ser divisible por 4:**  
>    Si $4 \mid m \implies (a - 1) \bmod 4 = 0$.

### Ejemplo de Aplicación del Teorema de Hull-Dobell:

#### Caso A: $X_n = (51 X_{n-1} + 31) \bmod 91$ (¡Falla!)
- $m = 91 = 7 \times 13$.
- $c = 31$. Como $31$ es primo y no divide a $91$, $\gcd(31, 91) = 1$ (Cumple condición 1).
- Factores primos de $m$: $p_1 = 7$ y $p_2 = 13$.
- $a - 1 = 51 - 1 = 50$.
  - ¿$7$ divide a $50$? ¡NO! ($50 / 7 = 7.14$). **Falla la condición 2.**
- **Conclusión:** No tiene periodo completo $91$. (De hecho, su periodo real es de apenas 6 números).

#### Caso B: $X_n = (13 X_{n-1} + 7) \bmod 16$ (¡Cumple!)
- $m = 16 = 2^4$. Factores primos de $m$: solo $p = 2$.
- $c = 7$. $\gcd(7, 16) = 1$ (Condición 1).
- $a - 1 = 13 - 1 = 12$. Como $12$ es divisible por $2$ (Condición 2).
- Como $16$ es divisible por 4, revisamos si $a - 1 = 12$ es divisible por 4: $12 / 4 = 3$ (Condición 3).
- **Conclusión:** ¡Tiene periodo completo $m = 16$! Generará todos los números del 0 al 15.

---

## 5. Parámetros Estándar de la Industria

| Arquitectura | Módulo $m$ | Multiplicador $a$ | Incremento $c$ | Nombre / Referencia |
| :--- | :--- | :--- | :--- | :--- |
| **32 bits** | $m = 2^{31} - 1 = 2\,147\,483\,647$ (Primo Mersenne) | $a = 7^5 = 16\,807$ | $c = 0$ (Multiplicativo) | **MINSTD** (Park & Miller, 1988) |
| **32 bits** | $m = 2^{32} = 4\,294\,967\,296$ | $a = 1\,664\,525$ | $c = 1\,013\,904\,223$ | *Numerical Recipes* |
| **48 bits** | $m = 2^{48} = 281\,474\,976\,710\,656$ | $a = 25\,214\,903\,917$ | $c = 11$ | Java `java.util.Random` (POSIX `drand48`) |
| **36 bits** | $m = 2^{35} - 31$ | $a = 5^5 = 3\,125$ | $c = 0$ | Diapositivas clase |

---

## 6. Ejercicios con Traza Manual

### Ejercicio:
Ejecuta 4 pasos a mano del generador $X_{n+1} = (5 X_n + 3) \bmod 8$ con semilla $X_0 = 1$.  
¿Cumple Hull-Dobell para tener periodo completo 8?

### Solución:
1. **Comprobación Hull-Dobell:**
   - $m = 8 = 2^3$, $c = 3 \implies \gcd(3, 8) = 1$
   - Factores primos de 8: solo 2. $a - 1 = 5 - 1 = 4$. $2 \mid 4$
   - $4 \mid 8 \implies 4 \mid (a - 1) = 4$  
   *¡Sí cumple las 3 condiciones! Tendrá periodo completo 8.*
2. **Traza:**
   - $X_1 = (5(1) + 3) \bmod 8 = 8 \bmod 8 = \mathbf{0} \implies U_1 = 0/8 = 0.0$
   - $X_2 = (5(0) + 3) \bmod 8 = 3 \bmod 8 = \mathbf{3} \implies U_2 = 3/8 = 0.375$
   - $X_3 = (5(3) + 3) \bmod 8 = 18 \bmod 8 = \mathbf{2} \implies U_3 = 2/8 = 0.25$
   - $X_4 = (5(2) + 3) \bmod 8 = 13 \bmod 8 = \mathbf{5} \implies U_4 = 5/8 = 0.625$
