# 06. Pruebas Estadísticas y Tests de Aleatoriedad

---

## 1. Marco General de Contrastes de Hipótesis

Para que una secuencia de números $u_1, u_2, \dots, u_n$ generada en el computador sea válida en una simulación, debe superar dos tipos de pruebas estadísticas:

$$H_0: \text{La secuencia proviene de una distribución } U(0, 1) \text{ continua, independiente e idénticamente distribuida (i.i.d.)}$$
$$H_1: \text{La secuencia NO es } U(0, 1) \text{ o NO es independiente}$$

```
                                  BATERÍA DE TESTS ESTADÍSTICOS
                                                │
                ┌───────────────────────────────┴───────────────────────────────┐
                ▼                                                               ▼
     1. PRUEBAS DE UNIFORMIDAD                                       2. PRUEBAS DE ALEATORIEDAD
    (¿La distribución es U(0, 1)?)                                  (¿Los números son independientes?)
    • Kolmogorov-Smirnov (K-S) [Muestras pequeñas]                  • Test de Pares No Solapados (2D)
    • Chi-Cuadrado (χ²) [Muestras grandes]                          • Test de Rachas (Runs Test con mediana)
```

---

## 2. Test de Kolmogorov-Smirnov (K-S) para Uniformidad

Compara la **Función de Distribución Acumulada Empírica** $F_n(x)$ de la muestra con la **Función Teórica** $F_0(x) = x$ para $x \in [0, 1]$.

```
     F(x) ▲
        1 ┼─────────────────────────────┐  CDF Teórica F0(x) = x
          │                        .·´  │  ─── ECDF Empírica Fn(x)
          │                   ┌───·     │
          │             ┌─────┘ ↕ D     │  D = Máxima distancia vertical
          │       ┌─────┘               │
        0 ┼───────┴─────────────────────┴──► x
          0                             1
```

### Algoritmo Paso a Paso:
1. Ordenar los $n$ números generados de menor a mayor:
   $$R_{(1)} \le R_{(2)} \le \dots \le R_{(n)}$$
2. Para cada $i = 1, 2, \dots, n$, calcular las desviaciones superior e inferior:
   $$D^+ = \max_{1 \le i \le n} \left( \frac{i}{n} - R_{(i)} \right)$$
   $$D^- = \max_{1 \le i \le n} \left( R_{(i)} - \frac{i-1}{n} \right)$$
3. **Estadístico de Prueba:**
   $$D = \max(D^+, D^-)$$
4. **Regla de Decisión:**
   - Buscar el valor crítico $D_{\alpha, n}$ en la tabla K-S para el nivel de significancia $\alpha$ (ej. $\alpha = 0.05$).
   - Si $D > D_{\alpha, n} \implies$ **Se rechaza la hipótesis de uniformidad**.
   - Si $D \le D_{\alpha, n} \implies$ **No se rechaza (se acepta uniformidad)**.

### Ejemplo Numérico Resuelto ($n = 5$, $\alpha = 0.05$):
Muestra ordenada: $[0.08, \, 0.22, \, 0.45, \, 0.65, \, 0.88]$.

| $i$ | $R_{(i)}$ | $i/n = i/5$ | $(i-1)/n = (i-1)/5$ | $D^+ = \frac{i}{n} - R_{(i)}$ | $D^- = R_{(i)} - \frac{i-1}{n}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0.08 | 0.20 | 0.00 | $0.20 - 0.08 = \mathbf{0.12}$ | $0.08 - 0.00 = \mathbf{0.08}$ |
| 2 | 0.22 | 0.40 | 0.20 | $0.40 - 0.22 = \mathbf{0.18}$ | $0.22 - 0.20 = \mathbf{0.02}$ |
| 3 | 0.45 | 0.60 | 0.40 | $0.60 - 0.45 = \mathbf{0.15}$ | $0.45 - 0.40 = \mathbf{0.05}$ |
| 4 | 0.65 | 0.80 | 0.60 | $0.80 - 0.65 = \mathbf{0.15}$ | $0.65 - 0.60 = \mathbf{0.05}$ |
| 5 | 0.88 | 1.00 | 0.80 | $1.00 - 0.88 = \mathbf{0.12}$ | $0.88 - 0.80 = \mathbf{0.08}$ |

- $D^+ = \max(0.12, 0.18, 0.15, 0.15, 0.12) = 0.18$
- $D^- = \max(0.08, 0.02, 0.05, 0.05, 0.08) = 0.08$
- **Estadístico K-S:** $D = \max(0.18, 0.08) = \mathbf{0.18}$
- **Valor crítico de tabla:** $D_{0.05, \, 5} = 0.565$
- **Conclusión:** Como $D = 0.18 < 0.565$, **NO se rechaza la uniformidad**.

---

## 3. Test de Chi-Cuadrado ($\chi^2$) para Uniformidad

Se utiliza para muestras más grandes ($n \ge 30$).

### Algoritmo Paso a Paso:
1. Dividir el intervalo $(0, 1)$ en $k$ clases disjuntas de igual amplitud $\frac{1}{k}$ (regla empírica: $E_i \ge 5$).
2. Contar la **frecuencia observada** $O_i$ de números que caen en cada clase $i$.
3. La **frecuencia esperada** bajo uniformidad es igual para todas las clases:
   $$E_i = \frac{n}{k}$$
4. Calcular el estadístico de contraste:
   $$\chi^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i}$$
5. **Regla de Decisión:**
   - Grados de libertad: $df = k - 1$.
   - Si $\chi^2 > \chi^2_{k-1, \, 1-\alpha} \implies$ **Se rechaza la hipótesis de uniformidad**.
   - Si $\chi^2 \le \chi^2_{k-1, \, 1-\alpha} \implies$ **Se acepta la uniformidad**.

---

## 4. Test de Pares Consecutivos No Solapados (Independencia 2D)

Verifica si existe dependencia o correlación espacial en 2 dimensiones entre números contiguos:

### Algoritmo Paso a Paso:
1. Dividir el intervalo $(0, 1)$ en $k$ intervalos de amplitud $1/k$.
2. Categorizar la muestra $u_1, u_2, \dots, u_n$ en enteros $Y_i \in \{1, 2, \dots, k\}$.
3. Formar **$n/2$ pares no solapados:**
   $$(Y_1, Y_2), \, (Y_3, Y_4), \, (Y_5, Y_6), \, \dots, \, (Y_{n-1}, Y_n)$$
4. Contar la frecuencia observada $O_{ij}$ en la matriz $k \times k$.
5. Frecuencia esperada para cada celda:
   $$E_{ij} = \frac{n/2}{k^2} = \frac{n}{2k^2}$$
6. **Estadístico Chi-Cuadrado Bidimensional:**
   $$T = \sum_{i=1}^k \sum_{j=1}^k \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \sim \chi^2_{k^2 - 1}$$
7. **Regla de Decisión:** Rechazar independencia si $T > \chi^2_{k^2 - 1, \, 1-\alpha}$.

---

## 5. Test de Rachas (Runs Test para Independencia y Aleatoriedad)

Una **racha** es una sucesión ininterrumpida de valores que pertenecen a la misma categoría.  
En números continuos, la muestra se divide usando la **mediana** como punto de corte:

- Asignar $+$ si $X_i \ge \text{mediana}$
- Asignar $-$ si $X_i < \text{mediana}$

```
     Secuencia:  [ +  +  + ]  [ -  - ]  [ + ]  [ -  -  -  - ]  [ +  + ]
     Rachas:      Racha 1     Racha 2   Racha 3   Racha 4      Racha 5
     Número total de rachas R = 5
```

### Estadísticos Teóricos Bajo Aleatoriedad:
- $n_1 =$ número de signos $+$
- $n_2 =$ número de signos $-$ ($n_1 + n_2 = n$, típicamente $n_1 \approx n_2 \approx n/2$)
- $R =$ número total de rachas observadas.

1. **Media Teórica de Rachas:**
   $$\mu_R = \frac{2 \, n_1 \, n_2}{n} + 1$$

2. **Varianza Teórica:**
   $$\sigma_R^2 = \frac{2 \, n_1 \, n_2 \, (2 \, n_1 \, n_2 - n)}{n^2 (n - 1)}$$

3. **Estadístico Estandarizado (Normal Estándar):**
   $$Z = \frac{R - \mu_R}{\sigma_R} \sim N(0, 1)$$

### Regla de Decisión (para $\alpha = 0.05$):
- Si $|Z| > 1.96 \implies$ **Se rechaza la hipótesis de aleatoriedad/independencia**.
  - Si $Z < -1.96$: Hay **muy pocas rachas** (indica tendencia o datos que cambian muy lentamente).
  - Si $Z > +1.96$: Hay **demasiadas rachas** (indica oscilación forzada tipo $+ - + - + -$).
- Si $|Z| \le 1.96 \implies$ **Se acepta la hipótesis de aleatoriedad**.

---

## 6. Tablas y Fórmulas de Valores Críticos

¿De dónde salen estos valores críticos? Igual que la tabla $t$-Student o la Normal $Z$, cada prueba estadística tiene su propia tabla de distribución:

### A. Tabla de Valores Críticos para Kolmogorov-Smirnov ($D_{\alpha, n}$)

| Tamaño de muestra ($n$) | $\alpha = 0.10$ (90%) | $\alpha = 0.05$ (95%) | $\alpha = 0.01$ (99%) |
| :---: | :---: | :---: | :---: |
| **1** | 0.950 | 0.975 | 0.995 |
| **2** | 0.776 | 0.842 | 0.929 |
| **3** | 0.642 | 0.708 | 0.828 |
| **4** | 0.564 | 0.624 | 0.733 |
| **5** | **0.510** | **0.565** | **0.669** |
| **10** | 0.368 | 0.410 | 0.490 |
| **20** | 0.264 | 0.294 | 0.356 |
| **30** | 0.218 | 0.242 | 0.295 |
| **35** | 0.202 | 0.224 | 0.274 |
| **$n > 35$ (Fórmula)** | $\mathbf{\frac{1.22}{\sqrt{n}}}$ | $\mathbf{\frac{1.36}{\sqrt{n}}}$ | $\mathbf{\frac{1.63}{\sqrt{n}}}$ |

> **Para $n > 35$ no necesitas tabla:** Usas directamente la fórmula asintótica.  
> Por ejemplo, para $N = 250$ y $\alpha = 0.05$:  
> $$D_{\text{crítico}} = \frac{1.36}{\sqrt{250}} = \frac{1.36}{15.811} \approx \mathbf{0.086}$$

---

### B. Valores Críticos de Chi-Cuadrado ($\chi^2_{df, \, 1-\alpha}$)

| Grados de libertad ($df$) | $\alpha = 0.10$ | $\alpha = 0.05$ | $\alpha = 0.01$ |
| :---: | :---: | :---: | :---: |
| **1** | 2.71 | 3.84 | 6.63 |
| **4** | 7.78 | 9.49 | 13.28 |
| **9** ($k=10$ clases) | 14.68 | **16.92** | 21.67 |
| **99** ($k^2=100$ pares) | 117.41 | **123.23** | 134.64 |

---

### C. Valores Críticos de la Normal Estándar $Z$ (para Test de Rachas)

| Nivel de Confianza ($1-\alpha$) | $\alpha$ | Valor Crítico Bilateral ($Z_{\alpha/2}$) | Regla de Rechazo |
| :---: | :---: | :---: | :---: |
| **90%** | 0.10 | $Z_{0.05} = \mathbf{1.645}$ | Rechazar si $|Z| > 1.645$ |
| **95%** | 0.05 | $Z_{0.025} = \mathbf{1.960}$ | Rechazar si $|Z| > 1.960$ |
| **99%** | 0.01 | $Z_{0.005} = \mathbf{2.576}$ | Rechazar si $|Z| > 2.576$ |
