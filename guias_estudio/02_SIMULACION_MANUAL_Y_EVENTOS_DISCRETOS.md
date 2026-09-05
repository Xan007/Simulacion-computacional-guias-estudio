# 02. Simulación Manual y Eventos Discretos

---

## 1. El Reloj de Simulación y Mecanismos de Avance

El reloj de simulación ($T_{\text{NOW}}$) lleva el control del tiempo en el modelo. Existen dos formas de avanzar el tiempo:

```
1. Incremento Fijo (Fixed-Time Step Δt):
   t=0 ────► t=1 ────► t=2 ────► t=3 ────► t=4 ────► t=5
   (Evalúa el sistema cada Δt unidades, ocurra o no un evento. Lento si no pasa nada).

2. Avance por Próximo Evento (Next-Event Time Advance) [USADO EN DES]:
   t=0 ────────────────► t=4.2 ────────► t=7.0 ──────────────► t=15.4
   (Salta directamente al instante del evento cronológicamente más próximo en la FEL).
```

### Lista de Eventos Futuros (FEL - Future Event List):
Es una lista ordenada cronológicamente con los eventos pendientes de ejecución:
$$\text{FEL} = [(\text{Llegada}, t=4.2), (\text{Salida}, t=5.1), (\text{Llegada}, t=7.0), (\text{Falla}, t=9.6)]$$

### Paradigmas de Ejecución en DES:
1. **Event Scheduling (Programación de eventos):** El programa avanza al siguiente evento programado y ejecuta la rutina correspondiente que actualiza el estado y agenda futuros eventos.
2. **Process Interaction (Interacción de procesos):** Sigue la historia de vida de cada entidad individual a medida que interactúa con recursos (solicitar, esperar, usar, liberar).
3. **Activity Scanning (Exploración de actividades - 2 fases):** En cada paso revisa qué condiciones de inicio de actividad se cumplen.
4. **Three-Phase Approach (Tres fases):** (A) Avanzar tiempo al próximo evento $A$; (B) Ejecutar eventos obligatorios programados para ese tiempo; (C) Explorar e iniciar actividades condicionales ahora disponibles.

---

## 2. Simulación Manual Ad-Hoc: El Ejemplo Clásico del Banco

Imagina un banco con **un único cajero**.
- **Tiempo entre llegadas (IAT):** Entero uniforme entre 1 y 10 minutos.
- **Tiempo de servicio (ST):** Entero uniforme entre 1 y 6 minutos.
- **Mecanismo:** El cliente llega; si el cajero está libre, es atendido de inmediato; si está ocupado, espera en la cola FIFO.

### Traza de Simulación Paso a Paso (6 Clientes):

| Cliente ($i$) | Tiempo Interllegada (IAT) | Tiempo de Llegada ($T_{\text{llegada}}$) | Tiempo de Servicio ($ST$) | Inicio de Servicio ($T_{\text{inicio}}$) | Fin de Servicio ($T_{\text{fin}}$) | Tiempo Espera en Cola ($W_q$) | Tiempo Total en Sistema ($W$) | Tiempo Ocioso del Cajero ($Idle$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | — | **0** | **4** | 0 | 4 | **0** | **4** | **0** |
| **2** | 8 | **8** | **1** | 8 | 9 | **0** | **1** | **4** (de $t=4$ a $8$) |
| **3** | 2 | **10** | **4** | 10 | 14 | **0** | **4** | **1** (de $t=9$ a $10$) |
| **4** | 1 | **11** | **3** | 14 | 17 | **3** ($14-11$) | **6** ($17-11$) | **0** |
| **5** | 3 | **14** | **2** | 17 | 19 | **3** ($17-14$) | **5** ($19-14$) | **0** |
| **6** | 4 | **18** | **3** | 19 | 22 | **1** ($19-18$) | **4** ($22-18$) | **0** |
| **TOTAL** | — | — | **17** | — | **22** (Fin) | **7** | **24** | **5** |

### Reglas de Cálculo para Llenar la Tabla:
1. $T_{\text{llegada}, i} = T_{\text{llegada}, i-1} + IAT_i$
2. $T_{\text{inicio}, i} = \max(T_{\text{llegada}, i}, \, T_{\text{fin}, i-1})$
3. $T_{\text{fin}, i} = T_{\text{inicio}, i} + ST_i$
4. **Espera en cola:** $W_{q, i} = T_{\text{inicio}, i} - T_{\text{llegada}, i}$
5. **Tiempo en sistema:** $W_i = T_{\text{fin}, i} - T_{\text{llegada}, i} = W_{q, i} + ST_i$
6. **Tiempo Ocioso:** $Idle_i = \max(0, \, T_{\text{llegada}, i} - T_{\text{fin}, i-1})$

---

## 3. Cálculo de Métricas de Desempeño

A partir de la tabla obtenemos los indicadores clave del sistema:

1. **Tiempo Medio de Espera en Cola ($\\bar{W}_q$):**
   $$\bar{W}_q = \frac{\sum W_{q, i}}{N} = \frac{7}{6} = 1.17 \text{ minutos}$$

2. **Tiempo Medio en el Sistema ($\\bar{W}$):**
   $$\bar{W} = \frac{\sum W_i}{N} = \frac{24}{6} = 4.00 \text{ minutos}$$

3. **Porcentaje de Tiempo Ocioso del Cajero:**
   $$\% \text{Ocio} = \left( \frac{\text{Tiempo Ocioso Total}}{T_{\text{simulación}}} \right) \times 100 = \left( \frac{5}{22} \right) \times 100 = 22.73\%$$

4. **Utilización del Cajero (Factor de Ocupación $\\rho$):**
   $$\rho = \left( \frac{\text{Tiempo Total de Servicio}}{T_{\text{simulación}}} \right) \times 100 = \left( \frac{17}{22} \right) \times 100 = 77.27\%$$

5. **Fracción de Clientes que Tuvieron que Esperar en Cola:**
   $$P(\text{espera}) = \frac{\text{Número de clientes con } W_q > 0}{N} = \frac{3}{6} = 0.50 \quad (50\%)$$

6. **Tiempo Medio de Espera de Quienes Realmente Esperaron:**
   $$\bar{W}_{q, \text{esperaron}} = \frac{\sum W_{q, i}}{\text{Número de clientes con } W_q > 0} = \frac{7}{3} = 2.33 \text{ minutos}$$

---

## 4. Análisis Estadístico y Réplicas (Intervalos de Confianza)

Una sola corrida de simulación representa únicamente **una realización muestral** aleatoria. Para obtener conclusiones confiables, se realizan $n$ réplicas independientes con semillas distintas.

```
Réplica 1 (Semilla A) ───► Resultado X1
Réplica 2 (Semilla B) ───► Resultado X2   ───► Promedio X̄ ± t(α/2, n-1) * (S / √n)
Réplica 3 (Semilla C) ───► Resultado X3
```

### Fórmula del Intervalo de Confianza (IC $1-\alpha$):
$$\bar{X} \pm t_{n-1, \, 1-\alpha/2} \cdot \frac{S}{\sqrt{n}}$$

Donde:
- $\bar{X} = \frac{1}{n}\sum X_i$ (media muestral de las réplicas).
- $S = \sqrt{\frac{1}{n-1}\sum (X_i - \bar{X})^2}$ (desviación estándar muestral).
- $t_{n-1, \, 1-\alpha/2}$ es el valor crítico de la distribución $t$-Student con $n-1$ grados de libertad.

### 📊 Ejemplo Numérico Real (del material de clase):
Se ejecutaron $n = 5$ réplicas independientes del tiempo medio en cola (minutos):
$$[63.2, \, 69.7, \, 67.3, \, 64.8, \, 72.0]$$

1. **Media:** $\bar{X} = \frac{63.2 + 69.7 + 67.3 + 64.8 + 72.0}{5} = 67.4$ min
2. **Desviación Estándar:** $S = 3.57$ min
3. **Error Estándar:** $\frac{S}{\sqrt{n}} = \frac{3.57}{\sqrt{5}} = 1.596$ min

- **Para 95% de Confianza ($\\alpha=0.05$):** $t_{4, \, 0.975} = 2.776$
  $$\text{IC}_{95\%} = 67.4 \pm (2.776)(1.596) = 67.4 \pm 4.43 = [62.97, \, 71.83] \text{ min}$$

- **Para 99% de Confianza ($\\alpha=0.01$):** $t_{4, \, 0.995} = 4.604$
  $$\text{IC}_{99\%} = 67.4 \pm (4.604)(1.596) = 67.4 \pm 7.35 = [60.05, \, 74.75] \text{ min}$$

> 📌 **Propiedad clave:** A mayor nivel de confianza (99% vs 95%), el intervalo es **más ancho**. A mayor número de réplicas ($n$), el intervalo es **más estrecho y preciso**.

---

## 5. Sistemas Terminantes vs No Terminantes

| Tipo | Definición | Condición de Parada | Tratamiento |
| :--- | :--- | :--- | :--- |
| **Terminante** | Tiene un inicio y fin natural y bien definido. | Tiempo fijo (ej. 8 horas de turno) o número fijo de entidades (ej. 100 clientes). | Se analiza el transitorio completo desde el estado inicial vacío. |
| **No Terminante** (Continuo) | Opera indefinidamente sin interrupciones (ej. refinería, telecomunicaciones). | Cuando se alcanza el **estado estable** (régimen permanente). | Se debe descartar el periodo inicial transitorio (**Warm-up period**) para no sesgar las estadísticas. |
