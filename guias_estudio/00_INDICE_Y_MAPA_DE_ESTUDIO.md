# Guía de Estudio: Simulación Computacional

Bienvenido al conjunto de guías modulares de **Simulación Computacional**.

Esta colección de documentos fue estructurada para explicar cada tema de forma **directa, sencilla, con lenguaje claro, fórmulas matemáticas completas en LaTeX, diagramas y ejercicios resueltos paso a paso** sin omitir ninguna fórmula ni procedimiento.

---

## 📚 Índice de Módulos de Estudio

| Módulo | Documento | Temas Clave |
| :---: | :--- | :--- |
| **01** | [**01. Fundamentos y Conceptos Básicos**](./01_FUNDAMENTOS_Y_CONCEPTOS_BASICOS.md) | ¿Qué es simular?, componentes de un sistema DES (entidad, recurso, estado, evento, actividad vs delay), clasificación de modelos y Verificación vs Validación (V&V). |
| **02** | [**02. Simulación Manual y Eventos Discretos**](./02_SIMULACION_MANUAL_Y_EVENTOS_DISCRETOS.md) | Reloj de simulación, avance por próximo evento, tabla manual paso a paso de un banco con cajero, cálculo de métricas de desempeño e Intervalos de Confianza para réplicas. |
| **03** | [**03. Integración Numérica y Monte Carlo**](./03_INTEGRACION_NUMERICA_Y_METODO_MONTE_CARLO.md) | Regla del Trapecio, estimación de integrales estocásticas con variables $U(0,1)$, estimación de $\pi$ y el experimento clásico de la aguja de Buffon. |
| **04** | [**04. Generadores de Números Pseudoaleatorios**](./04_GENERADORES_DE_NUMEROS_PSEUDOALEATORIOS.md) | Método de Cuadrados Medios (MidSquare), Generador Congruencial Lineal (Multiplicativo y Mixto), Teorema de Hull-Dobell para periodo máximo y parámetros estándar de 32 bits. |
| **05** | [**05. Generación de Variables Aleatorias**](./05_GENERACION_DE_VARIABLES_ALEATORIAS.md) | Método de la Transformada Inversa (Exponencial, Poisson con recursión eficiente, Binomial, Geométrica), Método de Aceptación y Rechazo y Método de Composición (mezclas). |
| **06** | [**06. Pruebas Estadísticas y Tests de Aleatoriedad**](./06_PRUEBAS_ESTADISTICAS_Y_TESTS_DE_ALEATORIEDAD.md) | Pruebas de Uniformidad (Kolmogorov-Smirnov y Chi-cuadrado con sus tablas de valores críticos), Pruebas de Aleatoriedad / Independencia (Pares Consecutivos No Solapados y Test de Rachas por mediana). |
| **07** | [**07. Taller Práctico y Ejercicios Resueltos**](./07_TALLER_PRACTICO_Y_EJERCICIOS_RESUELTOS.md) | Solución completa del taller oficial de 5 generadores (MidSquare y Congruenciales), trampas comunes de periodo, ejercicio integrador de colas y código Python de comprobación. |
| **08** | [**08. Ejercicios Resueltos del Libro de Texto**](./08_EJERCICIOS_LIBRO_SHELDON_ROSS.md) | Ejercicios oficiales extraídos directamente del libro de Sheldon Ross (Capítulos 3 y 4) con solución paso a paso, razonamiento detallado y criterios de decisión. |

---

## 🎯 Lista de Comprobación para el Examen (Checklist)

- [ ] **Diferenciar Verificación vs Validación**:
  - *Verificación*: ¿El programa informático hace lo que dice el modelo conceptual? ("¿Construimos bien el modelo?").
  - *Validación*: ¿El modelo refleja fielmente la realidad observada? ("¿Construimos el modelo correcto?").
- [ ] **Construir a mano la tabla de un cajero/banco**:
  - Calcular: Tiempo de llegada, inicio de servicio, fin de servicio, tiempo en cola ($W_q$), tiempo en sistema ($W$) y tiempo ocioso del servidor.
- [ ] **Aproximar integrales por Monte Carlo**:
  - Conocer la fórmula: $\int_a^b g(x) dx pprox rac{b-a}{N}\sum_{i=1}^N g(a + (b-a)U_i)$.
- [ ] **Ejecutar a mano pasos de generadores**:
  - MidSquare (extraer dígitos centrales del cuadrado).
  - LCG Multiplicativo ($X_{n+1} = a X_n mod m$) y Mixto ($X_{n+1} = (a X_n + c) mod m$).
- [ ] **Enunciar las 3 condiciones de Hull-Dobell** para periodo completo $m$.
- [ ] **Aplicar la Transformada Inversa**:
  - Exponencial: $X = -rac{1}{\lambda}\ln(1-U)$.
  - Poisson: uso eficiente de la relación $p_{k+1} = rac{\lambda}{k+1} p_k$.
- [ ] **Aplicar el Método de Aceptación y Rechazo**:
  - Calcular la constante $c = \max rac{p_j}{q_j}$ y condición de aceptación $U \le rac{p_Y}{c q_Y}$.
- [ ] **Calcular los estadísticos de prueba**:
  - Kolmogorov-Smirnov: $D = \max(D^+, D^-)$.
  - Chi-cuadrado: $\chi^2 = \sum rac{(O_i - E_i)^2}{E_i}$.
  - Test de Rachas: Categorización por mediana, cálculo de $\mu_R$, $\sigma_R^2$ y normalización $Z = rac{R-\mu_R}{\sigma_R}$.
