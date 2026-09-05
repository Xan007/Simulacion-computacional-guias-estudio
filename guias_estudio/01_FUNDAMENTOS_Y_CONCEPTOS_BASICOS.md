# 01. Fundamentos y Conceptos Básicos de Simulación

---

## 1. ¿Qué es la Simulación Computacional?

> **Definición Clave (Jerry Banks, 1998):**  
> La **simulación** es la **imitación de la operación de un sistema o proceso del mundo real a lo largo del tiempo**.  
> Involucra generar una **historia artificial** del sistema, observarla y obtener conclusiones sobre las características del sistema real.

```
┌─────────────────┐      Abstracción      ┌───────────────────┐      Codificación      ┌────────────────────┐
│  SISTEMA REAL   │ ───────────────────► │ MODELO CONCEPTUAL │ ─────────────────────► │ PROGRAMA COMPUTADOR│
└─────────────────┘                      └───────────────────┘                        └────────────────────┘
         ▲                                                                                      │
         │                         Toma de Decisiones y Mejoras                                 │
         └──────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. ¿Cuándo Simular y Cuándo NO Simular?

| Escenario | ¿Conviene Simular? | Razón |
| :--- | :---: | :--- |
| **Existe solución matemática cerrada simple** (ej. fórmula directa $M/M/1$) | ❌ **NO** | La solución analítica es exacta, más rápida y más barata. |
| **El sistema real es peligroso o destructivo** (ej. pruebas de choque, reactores nucleares) | ✅ **SÍ** | La simulación permite experimentar sin riesgos físicos ni pérdidas de vidas. |
| **El sistema real no existe aún** (ej. diseño de una nueva fábrica o aeropuerto) | ✅ **SÍ** | Permite evaluar alternativas de diseño antes de invertir millones. |
| **El sistema real es demasiado lento o rápido** (ej. evolución de bosques o microprocesadores) | ✅ **SÍ** | La simulación puede comprimir años en segundos o expandir nanosegundos. |
| **Problemas estocásticos complejos** (ej. colas con prioridades y fallas aleatorias) | ✅ **SÍ** | Las matemáticas exactas se vuelven intratables analíticamente. |

> 💡 **Regla de oro:** *"Simular cuando todo lo demás falla"* (pero sin usarlo como excusa para no formular bien el modelo).

---

## 3. Elementos Clave de un Sistema de Eventos Discretos (DES)

En la **Simulación de Eventos Discretos (DES)**, el estado del sistema cambia únicamente en instantes discretos de tiempo (cuando ocurre un evento).

```
Tiempo: t0 ──────────────► t1 ─────────────────────────► t2 ──────────────► t3
        │                  │                             │                  │
     [Llegada]          [Llegada]                     [Salida]           [Llegada]
  (Cambia estado)    (Cambia estado)               (Cambia estado)    (Cambia estado)
        └───────────────┴─────────────────────────────┴──────────────────┘
                      Entre eventos: ¡NADA CAMBIA! El reloj puede saltar.
```

### Conceptos Fundamentales:

1. **Sistema:** Colección de entidades e interacciones que actúan juntas para lograr un fin.
2. **Modelo:** Representación simplificada de un sistema con el nivel de detalle adecuado para responder una pregunta.
3. **Entidad:** Objeto de interés en el sistema.
   - *Dinámica:* Circula por el sistema (ej. clientes en un banco, paquetes en una red, piezas en una línea).
   - *Estática:* Permanece fija prestando soporte (ej. cajeros, servidores, máquinas).
4. **Atributo:** Propiedad local que describe a una entidad específica (ej. hora de llegada del cliente, saldo en cuenta, tipo de trámite).
5. **Recurso:** Elemento de capacidad limitada que presta servicio a las entidades.
   - *Estados de un recurso:* **Libre (Idle)**, **Oocupado (Busy)**, **Bloqueado (Blocked)** o **En Falla (Failed)**.
6. **Variable de Estado:** Conjunto de variables necesarias para describir el sistema en un instante $t$ (ej. $L(t)$ = número de clientes en cola, $B(t)$ = estado del cajero: 0 libre, 1 ocupado).
7. **Evento:** Suceso instantáneo que cambia el estado del sistema (ej. llegada de un cliente, finalización de atención).
8. **Actividad vs Retraso (Delay):**
   - **Actividad:** Duración **conocida o programada** al comenzar (ej. tiempo de servicio generado por una distribución exponencial de media 5 min).
   - **Retraso (Delay):** Duración **indefinida a priori**; depende de las condiciones del sistema (ej. tiempo que pasa un cliente esperando en la fila antes de ser atendido).
9. **Reloj de Simulación ($T_{\text{NOW}}$):** Variable global que lleva la cuenta del tiempo transcurrido en el modelo.

---

## 4. Clasificación de Modelos

| Criterio | Tipo A | Tipo B | Explicación sencilla |
| :--- | :--- | :--- | :--- |
| **Tiempo** | **Continuo** | **Discreto** | ¿El estado cambia continuamente en todo $t$ (ecuaciones diferenciales) o en instantes aislados? |
| **Dinámica** | **Estático (Monte Carlo)** | **Dinámico (DES)** | ¿El tiempo es irrelevante (ej. calcular un área) o el sistema evoluciona temporalmente? |
| **Azar** | **Determinista** | **Estocástico** | ¿Mismas entradas dan siempre la misma salida o intervienen variables aleatorias? |
| **Frontera** | **Abierto** | **Cerrado** | ¿Las entidades entran y salen del sistema o una población fija circula indefinidamente? |
| **Estabilidad** | **Estable** ($\\lambda < \\mu$) | **Inestable** ($\\lambda \ge \\mu$) | Si la tasa de llegada $\\lambda$ supera la de servicio $\\mu$, la cola crece infinitamente. |

---

## 5. Verificación vs Validación (V&V)

Este es el concepto más evaluado en los exámenes teóricos.

```
       ¿Construimos el modelo CORRECTO?            ¿Construimos BIEN el modelo?
                  (VALIDACIÓN)                              (VERIFICACIÓN)
                        │                                          │
            ┌───────────┴───────────┐                  ┌───────────┴───────────┐
            ▼                       ▼                  ▼                       ▼
      ¿El modelo refleja       Compara con la     ¿El software cumple     ¿Hay errores de
      la realidad física?      realidad (datos)   la especificación?      programación/bugs?
```

### Tabla de Técnicas de V&V:

| Fase | Pregunta Clave | Técnicas Prácticas |
| :--- | :--- | :--- |
| **Verificación** | ¿Construimos **bien** el modelo? (Software vs Especificación) | • Trazas de eventos en consola.<br>• Animación visual del flujo.<br>• Pruebas con entradas deterministas simples.<br>• Balance de flujo (entradas = salidas + en sistema). |
| **Validación** | ¿Construimos el **modelo correcto**? (Modelo vs Realidad) | • **Validación Facial:** Expertos del dominio revisan si los resultados tienen sentido.<br>• **Prueba de Turing:** Un experto no puede distinguir entre reportes del sistema real y de la simulación.<br>• **Comparación Histórica:** Probar el modelo con datos pasados conocidos y contrastar salidas.<br>• **Prueba de Condiciones Extremas:** Si la tasa de llegada es 0, la cola debe ser 0. Si es infinita, la cola debe saturar. |

---

## ✏️ Ejercicio de Autoevaluación

### Pregunta:
En un sistema de atención en un peaje:
1. Identifica: **Entidad**, **Atributo**, **Recurso**, **Evento**, **Actividad** y **Delay**.
2. Clasifica el modelo según sus características (tiempo, dinámica, azar, frontera).
3. Da un ejemplo de **Verificación** y uno de **Validación** para este sistema.

### Solución Explicada:
1. **Componentes:**
   - *Entidad:* Vehículo.
   - *Atributo:* Tipo de vehículo (automóvil, camión, moto) y hora de llegada a la caseta.
   - *Recurso:* Caseta / Cobrador del peaje (1 unidad de capacidad).
   - *Evento:* Llegada del auto a la fila; inicio de cobro; salida del auto del peaje.
   - *Actividad:* Tiempo de transacción/cobro (ej. 30 segundos tomados de una distribución uniforme).
   - *Delay:* Tiempo que el auto pasa esperando en la fila detrás de otros vehículos.
2. **Clasificación:**
   - Dinámico (evoluciona en el tiempo).
   - Discreto (eventos en instantes puntuales).
   - Estocástico (llegadas y tiempos de cobro aleatorios).
   - Abierto (los autos llegan desde el exterior y se van por la autopista).
3. **V&V:**
   - *Verificación:* Revisar que si el cobro dura 30s, el reloj avance exactamente 30s en el código sin saltos erróneos ni duplicación de cobradores.
   - *Validación:* Comparar el tiempo promedio de cola simulado (ej. 4.2 min) con las mediciones reales de cámaras de tráfico en hora pico (4.0 min).
