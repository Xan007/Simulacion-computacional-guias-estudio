# Guía de estudio de simulación computacional

## Alcance y forma de lectura

Esta guía se elaboró a partir de los cinco textos extraídos de los PDF de
`recursos` (incluidos los separadores `===== PAGE n =====`). Se revisaron todas
las páginas indicadas por `metadata.json`: **1 (125 páginas), 2 (67), 3 (27),
4 Generación (24) y 4 Test (42)**. En las diapositivas que sólo contienen una
fotografía, un diagrama o una ecuación como imagen, el texto extraído no permite
reconstruir el contenido: se indica expresamente como **[figura/fórmula no
extraíble]**, sin inventar datos. Las referencias `p. n` son páginas del PDF,
no páginas impresas de una obra citada.

## Auditoría de cobertura de páginas

Como control contra los separadores `PAGE` de los cinco textos, se conserva
abajo un inventario explícito. Una página descrita como “título/separador” sí
fue revisada: no contiene desarrollo textual recuperable. “Figura/imagen” no
significa que se haya omitido, sino que el extractor no recuperó sus
elementos gráficos. Los intervalos son inclusivos.

* **Documento 1 (125 páginas):** 1 título; 2–8 sin texto recuperable; 9–10
  monumento; 11 sin texto; 12–14 retratos; 15–22 metodología/métodos (texto
  de las imágenes no recuperable); 23–27 RM/TAC; 28–30 separadores,
  métodos/historia; 31–36 definición, orígenes y probabilidad; 37–43
  Buffon/Gosset (39–41 figuras); 44 título del periodo formativo; 45–59
  historia, computadoras, Monte Carlo, lenguajes y problemas de Conway; 60
  título del periodo de expansión; 61–62 herramientas y trabajo analítico; 63
  título/pregunta sobre simulación; 64–73 definiciones, usos, decisión,
  aplicaciones y errores; 74 título de terminología; 75–77 estado, evento y
  modelo; 78–80 modelo (78–79 imagen); 81–92 ciencia computacional, escalas,
  métodos, flujo y V&V; 93 título de tipos de modelos; 94–101 clasificaciones;
  102 título de tipos de simulación; 103–105 trazas; 106–109 arquitectura
  DES; 110–112 simulación continua y máquinas; 113–120 ejemplo de integración
  (figuras/fórmulas); 121–124 Monte Carlo (figuras/fórmulas); 125 sin texto.
* **Documento 2 (67 páginas):** 1 portada; 2 temario; 3 título de definición;
  4–7 definición y banco; 8 figura/tabla sin texto; 9 medidas; 10–11
  conclusiones y preguntas; 12 título de conceptos; 13–21 conceptos DES;
  22 título de estructuras; 23 listado; 24–27 estructuras; 28 título de
  ventajas; 29–31 ventajas, desventajas y defensa; 32 título de aplicaciones;
  33–41 aplicaciones; 42 título de pasos; 43–44 sin texto recuperable; 45
  título de generación; 46 ejemplo (figuras); 47 “Which PDF?”; 48 ejemplo
  exponencial (fórmula en figura); 49 título de entradas; 50–52 entradas; 53
  título de V&V; 54–56 V&V; 57 título de análisis; 58–66 análisis, intervalos
  y estado estable; 67 referencia.
* **Documento 3 (27 páginas):** 1 portada; 2 título de historia; 3–5
  historia; 6 título de introducción; 7–9 significado y secuencia; 10 título
  de pseudoaleatorios; 11–14 imágenes de Baloto; 15 probabilidad; 16
  procedimiento físico; 17 título de generación; 18–19 MidSquare; 20
  congruencial multiplicativo; 21 mixto; 22–23 ejemplos/Colab (figuras); 24
  criterios; 25 parámetros recomendados; 26 lectura complementaria; 27
  separador.
* **Documento 4, generación (24 páginas):** 1 portada; 2 título; 3–5
  transformada inversa (figuras); 6 título/generación Poisson; 7–8 Poisson;
  9–10 algoritmo Poisson (figuras); 11 título binomial; 12 definición; 13–14
  generación binomial (figuras); 15–18 aceptación-rechazo (diagrama);
  19–20 composición (20 incluye ecuación 4.3 en figura); 21–23 ejemplo
  (figuras); 24 Colab.
* **Documento 5, tests (42 páginas):** 1 portada; 2–4 uniformes (figuras);
  5 objetivo de uniformidad; 6–7 títulos de pruebas; 8–18 K–S (fórmulas y
  tablas en figuras); 19 figura K–S; 20 título chi-cuadrado; 21–23
  distribución; 24–28 contraste (figuras); 29 Colab; 30 título de pares; 31
  procedimiento; 32 Colab; 33–35 aleatoriedad; 36 título de rachas; 37
  definición; 38–39 estadístico/decisión (figuras); 40 Colab; 41 sin texto;
  42 ejercicio.

---

# Documento 1 — Introducción a la Simulación Computacional
`1. Introducción Simulación Computacional - visual.pptx.pdf` (125 páginas)

## 1. Antecedentes históricos (pp. 9–62)

Las primeras diapositivas (pp. 1–8, 11, 15–22 y 28–30) son portadas o imágenes
sin texto recuperable. En las pp. 9–14 se muestran el monumento a Tycho Brahe y
Johannes Kepler, y después retratos de ambos. Las pp. 15–22 presentan la
**metodología científica** y los **métodos científicos**, pero las explicaciones
están en imágenes no extraíbles. Las pp. 23–27 muestran imágenes de resonancia
magnética (RM/MRI) y tomografía axial computarizada (TAC/CT); sirven como
ejemplos de tecnología científica, pero no contienen texto técnico legible.

### Probabilidad antes de la computadora

* Hacia 3500 a. C. ya se usaban juegos de azar con objetos de hueso en Sumeria,
  Asiria y Egipto. El juego de las tabas empleaba el astrágalo (taba o chita),
  hueso del tobillo, con varias caras (p. 31–32).
* El acertijo del Chevalier de Méré pregunta la probabilidad de obtener **dos
  seises por lo menos una vez en 24 lanzamientos de un par de dados** (p. 33).
  Antoine Gombauld (Chevalier de Méré) planteó el problema y Blaise Pascal
  cuestionó matemáticamente la intuición de éxito y fracaso.
* Pierre de Fermat, Pascal y Gombauld son presentados como pioneros. Sus cartas
  constituyen el origen de la probabilidad académica; también se mencionan
  cálculos previos de Cardano y Galileo (p. 34).
* De Moivre, Bernoulli, Bayes y Lagrange aparecen como autores de fórmulas y
  técnicas de probabilidad; Laplace se presenta en la diapositiva siguiente
  (pp. 35–36). La fórmula concreta de Laplace no es extraíble.

**En sencillo:** antes de simular sistemas reales se aprendió a cuantificar el
azar de juegos. La probabilidad convirtió una intuición (“parece probable”) en
un cálculo repetible.

### De Buffon a la Segunda Guerra Mundial

El método de Monte Carlo suele situarse en el experimento de la **aguja de
Buffon** (1777): se lanzan agujas sobre un plano con líneas paralelas igualmente
espaciadas y se estima \(\pi\) contando los cruces (p. 38). Buffon publicó una
solución con un error que Laplace corrigió en 1812; por eso también se llama
problema de la aguja de Buffon–Laplace. Las pp. 39–41 son figuras del
experimento, sin fórmula legible.

William Sealy Gosset, químico y matemático que trabajó en Guinness, publicó
desde 1908 bajo el seudónimo **Student** (la empresa no permitía divulgar datos
propietarios). De allí surge la distribución *t* de Student (p. 42).
Como sus resultados analíticos eran incompletos, realizó una simulación manual
para comprobar la forma de su densidad. Es una aplicación temprana de
simulación al control de procesos y un ejemplo de cooperación entre
experimentación simulada y análisis exacto (p. 43).

### Periodo formativo y Monte Carlo electrónico (1945–1970)

Dos computadoras de propósito general sentaron las bases: **ENIAC** (1950,
Electronic Numerical Integrator And Computer) y **MANIAC** (1952), más pequeña,
basada en la arquitectura IAS y orientada a cálculos de física nuclear (p. 45).
Durante el Proyecto Manhattan se modeló la detonación nuclear como una
simulación de 12 esferas duras mediante Monte Carlo (p. 46).

Stanislaw Ulam, Nicholas Metropolis y John von Neumann emplearon Monte Carlo
para problemas de difusión de neutrones del diseño de la bomba de hidrógeno,
analíticamente intratables (p. 47). La idea de Ulam nació al estimar
probabilidades de jugadas de solitario: contar todos los casos era imposible,
pero jugar muchas veces y contar convierte el azar en herramienta de cálculo
(p. 48). En la década de 1950 la difusión de computadoras electrónicas impulsó
aplicaciones en muchas disciplinas.

### Primeros lenguajes y simuladores

* **K. D. Tocher** creó el *General Simulation Program* (GSP), primera
  herramienta general para describir sistemáticamente una planta industrial
  (p. 49). El estado de la planta combina el estado de cada máquina y los
  tiempos de sus próximas acciones. Una máquina puede estar ocupada, inactiva,
  no disponible o fallida; el GSP recorre esos ciclos automáticamente.
* Contribuciones de Tocher: método de tres fases (1960), *The Art of
  Simulation* (1963), diagrama de ciclo de actividad (ACD, 1964) y simulación
  combinada de modelos continuos y discretos (1966) (p. 50).
* **Geoffrey Gordon** presentó GPSS (General Purpose Simulation System,
  1960–61). Su modelo usa bloques para que programar no sea una barrera:
  `GENERATE` crea llegadas, `QUEUE` forma la cola, `SEIZE` toma el servidor,
  `ADVANCE` representa el servicio y `RELEASE` lo libera. Se aplicó a tráfico,
  telefonía, reservas aéreas y acerías (p. 51).
* **SIMSCRIPT** se construyó sobre FORTRAN (1963), evolucionó a SIMSCRIPT 1.5
  (1965) y SIMSCRIPT II (1968), con una arquitectura por niveles pensada para
  usuarios no informáticos (p. 52). La cifra exacta de niveles pretendidos era
  siete; la diapositiva muestra cinco niveles.
* GASP nació en U.S. Steel (1961), RAND impulsó SIMSCRIPT II (1963), y Alan
  Pritsker, Richard Conway, Cornell, RAND e IBM contribuyeron a su evolución
  (p. 53). Las organizaciones fueron tan importantes como las personas.
* **SIMULA I** (1961–65) fue creado por Kristen Nygaard y Ole-Johan Dahl en el
  Royal Norwegian Computing Center, como extensión de ALGOL 60; **SIMULA 67**
  introdujo orientación a objetos. Sus descendientes incluyen Smalltalk, C++,
  Java, C# y Python (p. 54).
* La Winter Simulation Conference comenzó en 1967 con aplicaciones de GPSS y se
  convirtió en el principal foro internacional de avances en simulación
  (p. 55).

### Los problemas de Conway

Conway, Johnson y Maxwell (1959) y Conway (1963) separaron dos problemas
centrales (p. 56):

1. **Construir** la simulación: modularidad, memoria, error de
   discretización, avance del reloj y archivos de entidades.
2. **Usarla**: decidir cuándo medir, con qué precisión y cómo comparar
   alternativas.

Los problemas constructivos se resumen en diseño modular, gestión eficiente de
memoria, control del error al discretizar, mecanismo eficiente de avance del
tiempo y organización de entidades (p. 57). La mayoría tiene soluciones
conocidas; el avance eficiente del tiempo para ciertos eventos sigue siendo
investigación activa.

Al ejecutar hay un problema estratégico (diseñar el experimento) y tres
prácticos: puesta en marcha hasta el estado estacionario, precisión (varianza
de estimadores) y comparación de alternativas (p. 58). Soluciones de Conway:
regla de truncamiento para eliminar observaciones contaminadas por el inicio,
medias por lotes para estimar varianza y procedimientos de *ranking &
selection* en lugar del ANOVA tradicional (p. 59).

El periodo de expansión (1970–81) aportó GASP IV, SIMSCRIPT II.5, SLAM y
SIMAN; metodología cónica, gráficos de eventos, verificación/validación formal
y productos especializados (p. 61). El trabajo analítico avanzó en generación
de variables aleatorias, análisis de resultados, modelado de entrada y
optimización (p. 62).

**En sencillo:** construir el programa y saber interpretar sus corridas son
problemas distintos. Un programa rápido pero mal iniciado, mal validado o
comparado sin estadística puede producir decisiones equivocadas.

## 2. Qué es simular y cuándo hacerlo (pp. 63–73)

La simulación conecta **sistema real → modelo → programa de computador →
conclusiones**. El computador no sustituye al modelo: lo hace ejecutable
(p. 64). Ríos-Insua, Ríos-Insua y Martín la definen como construir un programa
que describa el sistema, experimentar con él y obtener conclusiones para la
toma de decisiones (p. 65). Banks (1998) añade cuatro ideas: imitación de la
operación de un proceso en el tiempo, generación y observación de una historia
artificial, metodología para problemas reales y preguntas “¿qué pasaría si?”;
sirve para sistemas existentes y conceptuales (p. 66).

Se simula para **explicar**, **entender** y **mejorar**: estudiar ingredientes e
interacciones y probar cambios sin alterar el sistema (p. 67). Conviene cuando
el sistema no existe o es caro, peligroso, lento o imposible de construir;
cuando experimentar con él es inviable; o cuando se necesitan otras escalas de
tiempo (pasado, presente, futuro, tiempo expandido o comprimido) (p. 68).

La evaluación analítica puede ser prohibitiva por falta de solución simple,
pero el modelo debe poder validarse. Colas, EDO no lineales y problemas
estocásticos son casos típicos sin solución analítica práctica (p. 69). Si
existe solución analítica simple, debe preferirse: es más barata y exacta.
Regla orientativa: “simular cuando todo lo demás falla”, sin usarla como excusa
para modelar mal (p. 70–71).

Áreas: producción, finanzas/economía, hardware/software, armamento, inventarios,
bosques, comunicaciones y protocolos, transporte y organizaciones como
hospitales, comedores y correo (p. 72). Errores frecuentes: detalle
inapropiado, lenguaje inadecuado, modelo no verificado o inválido, condiciones
iniciales incorrectas, corridas cortas, generadores o semillas inadecuados.
Son principalmente errores de método, no de programación (p. 73).

## 3. Modelos y clasificación (pp. 74–105)

Una **variable de estado** es la instantánea necesaria para caracterizar el
sistema en \(t\) (por ejemplo, clientes en cola, estado del servidor y tiempo
restante). El conjunto depende del objetivo y permite reanudar una corrida
detenida (p. 75). Un **evento** es un cambio de estado, como llegada o salida;
entre eventos nada cambia y se puede saltar directamente al próximo (p. 76).
Un **modelo** es una abstracción simplificada que conserva lo esencial para la
pregunta, o una representación matemática/computacional de un fenómeno
(p. 77–80).

La ciencia computacional combina pensamiento computacional, matemáticas, física,
química y dominios como biología y economía. El científico computacional integra
procesos y aprovecha la avalancha de datos; modelado y simulación son su núcleo
(p. 81–82). Un modelo sirve para describir, clasificar, entender, predecir y
controlar (p. 83). Un buen modelo depende de la pregunta: tráfico, emisiones y
consumo requieren modelos diferentes. Debe ser “lo más simple posible, pero no
más simple de lo necesario” (Einstein, p. 84).

Escalas: microscópica (átomos, moléculas, fluido, presión, clima), biológica
(células a seres vivos) y macroscópica (mecánica, automóviles, tráfico)
(p. 85). Hay que identificar ingredientes e interacciones y a veces modelar a
una escala más fina que la de análisis (p. 86). Métodos posibles: dinámica
molecular, EDO/EDP, Monte Carlo, autómatas celulares/Lattice Boltzmann,
sistemas multiagente, eventos discretos y redes complejas. No existe método
universal: mandan la escala y la pregunta (p. 89).

Flujo de trabajo: especificar el modelo, programarlo, ejecutarlo muchas veces y
estudiar resultados; es un experimento numérico en un universo virtual. Exige
programación, algoritmos, estructuras de datos, ingeniería de software,
paralelismo/GPU, optimización y análisis de datos (p. 90).

### Verificación y validación

La **validación** pregunta “¿construimos el modelo correcto?” y compara casos
conocidos con el sistema real; la **verificación** pregunta “¿construimos bien
el modelo?” y comprueba que el programa implementa lo especificado (p. 91).
Además hay que conocer suficientemente el fenómeno para juzgar predicciones
nuevas. La p. 92 ilustra comparar cuantitativamente curva simulada y datos, no
sólo parecido visual.

Clasificaciones (pp. 94–101):

* Tiempo continuo: estado definido en todo instante; tiempo discreto: sólo en
  instantes particulares. La continuidad del tiempo no implica estado continuo.
* Estado continuo frente a estado discreto (eventos discretos).
* Determinista: misma entrada, mismo resultado; probabilístico: repeticiones
  pueden diferir.
* Estático: el tiempo no es variable; dinámico: el sistema cambia con él.
* Lineal: \(f(x)=a+bx\); no lineal: por ejemplo \(f(x)=a+b\sqrt{x}\).
* Abierto: entradas externas independientes; cerrado: las entidades circulan
  dentro de la frontera. Un tráfico puede ser abierto o cerrado según los
  supuestos.
* Estable: converge a un estado independiente del tiempo; inestable: no
  converge. En una taquilla simple, intervalo entre llegadas mayor que servicio
  sugiere estabilidad; menor o igual, inestabilidad.

### Simulación por trazas

Una traza es un registro temporal de eventos reales. Ejemplo: páginas
referenciadas (`t=001 página 14`, etc.) para comparar FIFO, aleatorio y LRU; la
traza debe ser independiente del sistema evaluado (p. 103). Ventajas:
credibilidad, validación sencilla, entrada determinista con menos varianza y
comparaciones con idéntica entrada (p. 104). Desventajas: detalle y complejidad,
trazas finitas no representativas, necesidad de varias trazas para validar y
falta de flexibilidad para estudiar condiciones que no aparecen en la traza
(p. 105).

## 4. Arquitectura de simulaciones (pp. 106–125)

En eventos discretos, el **manejador de eventos** mantiene una lista futura
ordenada (ejemplo: llegada 4.2, salida 5.1, llegada 7.0, avería 9.6), extrae
el próximo evento y puede programar otros (p. 106). El reloj global avanza a
esos tiempos; cada rutina de evento actualiza variables de estado y genera
eventos (p. 107).

Componentes adicionales: rutinas de entrada (parámetros como media entre
llegadas y servicio), generador de reportes, inicialización del estado y de
generadores aleatorios; cada conjunto de entradas define una iteración, que se
repite con semillas distintas (p. 108). Completan el conjunto rutinas de
trazado, manejo dinámico de memoria y programa principal. Los nueve
componentes son: manejador de eventos; reloj/avance; variables de estado;
rutinas de eventos; entrada; reportes; inicialización; trazado; memoria
(p. 109).

La simulación continua usa variables descritas por ecuaciones diferenciales y
algebraicas; puede coexistir con subsistemas discretos (p. 110). Los
computadores analógicos operan continuamente, en paralelo y tiempo real, con
almacenamiento limitado y necesidad de escalar valores; los digitales operan
secuencialmente sobre números discretos, almacenan mucho y resuelven
integración mediante métodos numéricos (pp. 111–112).

Las pp. 113–120 presentan un ejemplo de integración: cálculo analítico mediante
la función error `erf`, sustitución y evaluación en \(x=2\), serie de Taylor/
Maclaurin e integración numérica por trapecios. Las ecuaciones y valores están
como imágenes: **[fórmulas no extraíbles]**.

**Monte Carlo** se define aquí restrictivamente como simulación estática, sin
eje temporal, para fenómenos probabilísticos sin tiempo o para evaluar
expresiones no probabilísticas con métodos probabilísticos (p. 121). En el
ejemplo de las pp. 122–124 se generan \(x\) uniformes, se calcula \(y\) como
una función/densidad y se promedia para aproximar una integral; la integral,
programa y ejecuciones son imágenes no extraíbles. La p. 125 está vacía.

---

# Documento 2 — Principles of Simulation
`2. Principles of Simulation.pdf` (67 páginas)

## Definición y ejemplo de banco (pp. 1–11)

La diapositiva 1 es portada y la 2 presenta el temario: definición, conceptos y
estructuras de modelado, ventajas/desventajas, aplicaciones, pasos, generación
aleatoria, entradas, verificación/validación y análisis de resultados.

Simulation is imitation of the operation of a real-world process or system over
time. Genera una historia artificial, la observa y extrae inferencias sobre las
características de operación del sistema real; permite describir y analizar,
responder “what-if” y diseñar sistemas existentes o conceptuales (p. 4).

Ejemplo *ad hoc*: banco con un cajero. Interllegadas enteras uniformes de 1–10
minutos y servicios enteros uniformes de 1–6; discretizar el tiempo es una
abstracción útil (p. 5). Se simulan manualmente 20 clientes y se calculan
tiempo ocioso, espera media y otras medidas. Se usan una ruleta de 1–10 para
interllegadas y un dado de 1–6 para servicio (p. 6–7). La p. 8 contiene una
tabla/figura no extraíble. Resultados de la p. 9:

* tiempo medio en el sistema \(=79/20=3.95\) min;
* porcentaje ocioso \(=(30/99)100=30\%\);
* espera media por cliente \(=10/20=0.5\) min;
* fracción que espera \(=5/20=0.25\);
* espera media de quienes esperaron \(=10/5=2\) min.

Veinte clientes son insuficientes para conclusiones de largo plazo; corridas,
clientes y análisis estadístico hacen apropiado usar computador (p. 10).
Preguntas abiertas: determinar entradas, generar distribuciones no uniformes,
saber si se imita la realidad, elegir duración y número de corridas y analizar
salidas (p. 11).

## Conceptos y estructuras (pp. 12–27)

Un modelo representa el sistema; un evento ocurre y cambia su estado, pudiendo
ser exógeno o endógeno (p. 13). Tipos: eventos discretos, descriptivo,
matemático, estadístico e entrada-salida. Muchos explicitan entradas/salidas y
usan relaciones matemáticas/estadísticas internas; suelen ser estáticos.
Ejemplo físico: `force = mass × acceleration`. El modelo de eventos discretos
representa componentes e interacciones hasta cumplir los objetivos y es
dinámico (pp. 14–15).

Las variables de estado contienen toda la información necesaria en un instante;
en DES permanecen constantes entre eventos, mientras que en modelos continuos
se definen mediante ecuaciones diferenciales o en diferencias (p. 16). Una
entidad es un objeto explícito, dinámica si se mueve o estática si sirve a
otras; sus atributos son locales (por ejemplo, tiempo de llegada) (p. 17).

Un recurso presta servicio a entidades dinámicas, puede ser servidor paralelo y
se solicita en una o varias unidades. Si se deniega, la entidad espera en cola,
se desvía o sale; si captura el recurso, lo libera después. Estados mínimos:
idle/busy; también failed, blocked o starved (p. 18). Las listas representan
colas: FIFO, LIFO, aleatorio o por atributo. En SPT (shortest process time), se
ordena por menor tiempo de proceso (p. 19).

Una **actividad** tiene duración conocida al comenzar y puede terminar en un
tiempo programado: constante, muestra de una distribución, ecuación, archivo o
regla dependiente del estado. Un **delay** es una duración indefinida causada
por condiciones del sistema (p. 20). DES cambia variables sólo en eventos;
entidades compiten por recursos, esperan y el reloj avanza hasta el próximo
evento, actualizando estado y capturas/liberaciones (p. 21).

Estructuras de ejecución:

1. **Process interaction:** el programa sigue una entidad; avanza hasta que se
   retrasa, entra en actividad o sale, y el reloj salta al próximo movimiento
   (p. 24).
2. **Event scheduling:** se avanza al próximo suceso, normalmente una
   liberación, y éste reasigna entidades y agenda actividades (p. 25).
3. **Activity scanning (dos fases):** módulos independientes esperan
   condiciones; en incrementos fijos se decide si ocurre un evento y se
   actualiza el estado (p. 26).
4. **Tres fases:** (i) avanzar al siguiente tiempo, (ii) liberar recursos cuyas
   actividades terminan, (iii) iniciar actividades con la disponibilidad global
   ya actualizada (p. 27).

## Ventajas, límites y aplicaciones (pp. 28–41)

Ventajas enumeradas: elegir correctamente, comprimir/expandir tiempo, entender
causas, explorar posibilidades, diagnosticar, identificar restricciones,
desarrollar comprensión, visualizar planes, crear consenso, prepararse para
cambios, invertir sabiamente, entrenar al equipo y especificar requisitos
(p. 29). Desventajas: requiere formación, resultados difíciles de interpretar,
tiempo/costo y posible uso inapropiado (p. 30). Se contrarrestan con
simuladores, análisis de salida, herramientas cada vez más rápidas y reconocer
las limitaciones de modelos cerrados (p. 31).

Aplicaciones (pp. 33–41): manufactura y manejo de materiales (AGV, AS/RS,
ensamble, calidad); salud (aneurismas, inmunología, asma, trasplantes,
retinopatía, personal de enfermería y quirófanos); militar (equipos, barcos,
airlift, mantenimiento y defensa); recursos naturales (contaminación, malezas,
calidad del agua); servicios públicos (ambulancias, litigios, oficinas y
evacuación); transporte (autopistas inteligentes, zonas de obras, taxis,
peajes, puertos, tránsito rápido y rotondas); desempeño de computadores
(transacciones, bases de datos, memoria y protocolos); aviación (evacuación,
operaciones aeroportuarias, carga y embarque); comunicaciones (radio, telefonía,
PACS, banda ancha, realidad virtual y capacidad celular).

## Entradas, V&V y salidas (pp. 42–67)

Las pp. 42–47 son separadores/imágenes; la p. 48 muestra generación
exponencial: si \(R_1=0.3067\), se obtiene \(X_1=3.66\) min para el ejemplo
mostrado. La ecuación de transformación está en imagen y no es legible.

La elección de entrada depende de cantidad de datos, datos observados o
supuestos y dependencia entre variables (pp. 49–52). Para una variable
independiente: tratarla como determinista, ajustar una distribución o usar la
empírica. Procedimiento de ajuste: (1) proponer distribución, (2) estimar
parámetros, (3) prueba de bondad de ajuste, como chi-cuadrado. La p. 52 añade
el caso de no disponer de datos, pero la continuación es una figura no
extraíble.

**Verificación:** comprobar que la implementación corresponde al modelo
conceptual. Recomendaciones: programación estructurada, código autodocumentado,
revisión por otra persona, comprobar uso de entradas, probar valores variados,
usar depurador/IRC y animación (p. 55). **Validación:** decidir si el modelo
conceptual puede sustituir al real para experimentar; es iterativa y obliga a
examinar código o modificar supuestos cuando hay discrepancias (p. 54).
Técnicas: validación facial, análisis de sensibilidad, condiciones extremas,
validar supuestos, consistencia, prueba de Turing, validar transformaciones
entrada-salida y comparar con datos históricos (p. 56). Para una hipótesis
exponencial: consultar periodos pico, recoger interllegadas, comprobar
independencia, estimar parámetro y aplicar bondad de ajuste.

Las medidas de desempeño pueden ser ponderadas por tiempo, conteos o tablas de
expresiones (medias, varianzas, regalías, etc.) (pp. 57–60). Preguntas:
duración apropiada, interpretación y comparación de configuraciones (p. 61).

Un intervalo de confianza tiene probabilidad \(1-\alpha\) de contener el valor
verdadero; en muchas réplicas aproximadamente esa proporción de intervalos lo
contiene (p. 62). Para el ejemplo de cinco réplicas de tiempo medio en cola
(63.2, 69.7, 67.3, 64.8, 72.0), se usa la media, desviación \(S=3.57\) y
\(t_{n-1,1-\alpha/2}\); las ecuaciones intermedias están parcialmente ocultas.
Resultados: IC 95% **(62.96, 71.84)** e IC 99% **(60.6, 74.74)** (pp. 63–64).
La anchura disminuye al aumentar réplicas, aumenta al subir confianza y aumenta
con la variación (p. 65).

En sistemas terminantes se llega a un final natural; en no terminantes hay
fase transitoria (*warm-up*) y estado estable, por lo que se eliminan
observaciones iniciales (p. 66). Referencia del material: Jerry Banks,
*Handbook of Simulation*, Wiley, 1998, capítulo 1 (p. 67).

---

# Documento 3 — Números Aleatorios
`3. Números Aleatorios.pptx.pdf` (27 páginas)

## Historia, significado y pseudoaleatoriedad (pp. 1–17)

Las pp. 1–2, 6 y 10 son portada/separadores. La historia formal comienza en los
años cuarenta con Monte Carlo; Von Neumann, Metropolis, Ulam y Lehmer son
pioneros. Von Neumann anticipó en 1945 que el computador abriría un enfoque
experimental para la estadística matemática (p. 3). Metrópolis y Ulam
publicaron *The Monte Carlo Method* en 1949; Lehmer propuso en 1951 el
generador lineal congruencial, luego modificado por Thomson y Rotenberg (p. 4).
Antes de computadoras se usaban dispositivos físicos: 100 000 dígitos de
Kendall y Babington-Smith con un disco giratorio (1939) y un millón de RAND
Corporation mediante pulsos de frecuencia aleatoria (1955) (p. 5).

El núcleo de una simulación es producir valores que representen
\(U(0,1)\) (p. 7). La p. 8 muestra una larga secuencia de decimales; termina
con puntos suspensivos. En general el generador produce valores que se suponen
i.i.d. uniformes y después se transforman a distribuciones del modelo (p. 9).
La hipótesis i.i.d. es esencial para muchas transformaciones, pero no se cumple
literalmente: un generador informático es un programa determinista que intenta
parecer aleatorio.

Las pp. 11–14 son diapositivas/imágenes de Baloto. La probabilidad publicada de
ganar es \(p=1/8\,145\,060=0.000000122774\ldots\) (p. 15). Un sorteo por
computador podría generar desconfianza frente a extraer bolas; incluso el
método físico exige igual peso, mezcla completa y cambio periódico de bolas
(p. 16). Es impráctico para cientos de miles de valores, de ahí la necesidad
de pseudoaleatoriedad.

## Generadores (pp. 18–25)

**Cuadrados medios (MidSquare):** tomar semilla \(x_0\) de \(2n\) cifras
(originalmente cuatro), elevar al cuadrado (hasta \(4n\) cifras), añadir ceros
a la izquierda si hace falta, seleccionar las \(2n\) cifras centrales como
\(x_1\), y anteponer punto decimal para \(u_1\). Repetir desde \(x_1\)
(p. 18). La p. 19 anuncia un ejemplo, pero sus operaciones son imagen no
extraíble. El método puede caer rápidamente en ciclos o ceros: la semilla
importa.

**Congruencial multiplicativo:** \(x_0\) es semilla y \(a,m\) son enteros
positivos; se itera para \(n=0,1,\ldots,m-1\), aplicando una recurrencia
modular multiplicativa. El número pseudoaleatorio se obtiene normalizando el
estado; la expresión exacta de las diapositivas 20 y 22 es imagen y no
extraíble.

**Congruencial mixto:** agrega un término constante a la recurrencia modular
(p. 21). Las diapositivas 22–23 son ejemplos/Colab sin texto recuperable.
Para que un generador sea útil, \(a,m\) deben permitir: apariencia i.i.d.
uniforme para cualquier semilla, periodo grande antes de repetirse y cálculo
eficiente (p. 24). Un criterio citado: para palabra de 32 bits, \(m=2^{31}-1\)
y \(a=75=16807\); para 36 bits se mencionan \(m=2^{35}-31\) y \(a=55\)
(p. 25; la tipografía de exponentes está parcialmente fragmentada).

Las pp. 26–27 son lectura complementaria (Mancilla Herrera, 2000, *Números
aleatorios. Historia, teoría y aplicaciones*, Ingeniería y Desarrollo 8,
49–69, DOI/enlace Redalyc) y separador.

**En sencillo:** una semilla fija hace reproducible la corrida, pero también
significa que la secuencia tiene periodo y patrones. Antes de usarla hay que
probar uniformidad y aleatoriedad.

---

# Documento 4 — Generación de Variables Aleatorias Discretas
`4. Generación de Variables Aleatorias.pptx.pdf` (24 páginas)

La extracción conserva títulos pero pierde muchas ecuaciones y diagramas;
por ello se distinguen los procedimientos conceptuales de las fórmulas que no
pueden verificarse en el texto.

## Transformada inversa (pp. 1–10)

Las pp. 1–5 introducen la **transformada inversa** para variables discretas,
pero las reglas, tabla de probabilidades y fórmulas aparecen como figuras no
extraíbles. Conceptualmente, se toma \(U\sim U(0,1)\), se acumulan
probabilidades \(F(x)\) y se devuelve el menor valor cuyo acumulado alcanza a
\(U\). Para una distribución discreta:

1. calcular probabilidades y acumulados;
2. generar \(U\);
3. ubicar \(U\) en el intervalo acumulado;
4. asignar el valor correspondiente.

Esta descripción es la regla del método; los límites numéricos de las
diapositivas no deben reconstruirse sin la figura original.

### Poisson

La distribución de Poisson es discreta y expresa, a partir de una frecuencia
media, la probabilidad de un número de eventos en un periodo; modela sucesos
raros (p. 7). Ejemplos (p. 8): autos que pasan por un punto, errores
ortográficos por página, llamadas por minuto, servidores web accedidos,
clientes que llegan a un banco, mutaciones tras radiación, núcleos que se
desintegran, estrellas por volumen y receptores visuales en retina.

Las pp. 6 y 9–10 muestran la generación de una variable Poisson y el algoritmo
de transformada inversa que aprovecha la recurrencia de probabilidades; la
fórmula y pseudocódigo están como imágenes, así que quedan
**[fórmula/pseudocódigo no extraíbles]**. La media se representa con la letra
griega lambda (codificada de forma ilegible en la extracción).

### Binomial

La binomial cuenta éxitos en \(n\) ensayos de Bernoulli independientes, con
probabilidad fija \(p\) de éxito (p. 12). Las pp. 11, 13–14 muestran su
generación por transformada inversa; ecuaciones, acumulados y ejemplo son
figuras no extraíbles. Para estudiarla, se acumulan las probabilidades
binomiales de \(x=0,\ldots,n\), se genera \(U\) y se selecciona el primer
acumulado que lo cubra.

## Aceptación-rechazo y composición (pp. 15–24)

Las pp. 15–18 presentan la técnica de **aceptación y rechazo** con un diagrama
de flujo: generar candidato, generar una segunda uniforme, decidir “Sí/No” y
repetir hasta aceptar. Las funciones de propuesta, constante de dominación,
inecuación y el diagrama completo son imágenes no extraíbles; no se deben
confundir con la transformada inversa.

El **método de composición** (pp. 19–20) representa una distribución como
mezcla de componentes. Se elige primero el componente según sus pesos y luego
se genera una observación de la distribución elegida. La ecuación marcada
(4.3) está en imagen. Las pp. 21–23 desarrollan un ejemplo gráfico paso a
paso, sin valores legibles; la p. 24 anuncia generación en Google Colab.

**En sencillo:** transformada inversa “busca en una tabla”; aceptación-rechazo
“propone y descarta”; composición “elige una subdistribución y luego muestrea
de ella”. En todos los casos la fuente básica es un uniforme confiable.

---

# Documento 5 — Tests o contrastes para números aleatorios
`4. Test para números aleatorios.pptx.pdf` (42 páginas)

## Uniformidad y Kolmogorov–Smirnov (pp. 1–19)

Las pp. 1–4 presentan las distribuciones uniforme continua y discreta; sus
densidades/masas son imágenes no extraíbles. Dada una secuencia, el objetivo es
verificar si puede considerarse una muestra aleatoria simple de \(U(0,1)\)
(p. 5). Las pp. 6–7 separan pruebas de uniformidad de pruebas de aleatoriedad.

El contraste **Kolmogorov–Smirnov (K–S)** aparece en pp. 8–18. La idea es
comparar la CDF empírica de los datos con la CDF uniforme y medir la máxima
distancia vertical; se rechaza uniformidad si supera el valor crítico para
el tamaño muestral y significancia elegidos. Las fórmulas, tablas y ejercicios
de pp. 9–18 están como imágenes, por lo que el estadístico y valores críticos
exactos no son recuperables. La p. 19 identifica la figura: CDF teórica roja,
ECDF azul y estadístico K–S negro; fuente Wikipedia.

## Chi-cuadrado (pp. 20–29)

Si \(Z_1,\ldots,Z_k\) son normales estándar independientes, la suma de sus
cuadrados sigue una chi-cuadrado con \(k\) grados de libertad:
\[
\chi^2_k=\sum_{i=1}^{k}Z_i^2.
\]
El parámetro \(k\) es entero positivo y representa los grados de libertad
(p. 21). Las pp. 22–23 muestran la distribución; pp. 24–28 el contraste,
incluyendo símbolos y tablas que no se extrajeron completamente; p. 29 anuncia
implementación en Colab.

Para una prueba de uniformidad por clases, se divide (0,1) en categorías,
cuenta observaciones \(O_i\), calcula esperados \(E_i\) (iguales si las clases
tienen la misma amplitud) y usa:
\[
\chi^2=\sum_i\frac{(O_i-E_i)^2}{E_i}.
\]
Se compara con el crítico de grados de libertad apropiados y se rechaza si el
estadístico es mayor. La fórmula general de la diapositiva está parcialmente
oculta; esta escritura expresa el procedimiento estándar sin atribuirle datos
no visibles.

## Pares consecutivos no solapados (pp. 30–32)

Para \(X_1,\ldots,X_n\), \(n\) par, nivel \(\alpha\):

1. dividir (0,1) en \(k\) clases disjuntas de amplitud \(1/k\);
2. discretizar cada \(X_i\) en el índice de su clase, obteniendo
   \(Y_1,\ldots,Y_n\);
3. formar pares no solapados
   \((Y_1,Y_2),(Y_3,Y_4),\ldots,(Y_{n-1},Y_n)\);
4. contar \(O_{ij}\), apariciones del par \((i,j)\). Bajo uniformidad,
   \(O_{ij}\sim\operatorname{Binomial}(n/2,1/k^2)\), por lo que
   \(E_{ij}=n/(2k^2)\);
5. calcular chi-cuadrado con \(k^2-1\) grados de libertad y rechazar si supera
   \(\chi^2_{k^2-1,\alpha}\) (p. 31).

La p. 30 introduce el contraste y la p. 32 muestra su implementación en
Colab; no hay código textual recuperable.

## Aleatoriedad y test de rachas (pp. 33–40)

Una prueba de aleatoriedad decide si una muestra sigue un patrón o puede
considerarse aleatoria. En modelización estocástica interesa demostrar
cuantitativamente que los datos de entrada son aleatorios y representativos
(p. 35). La secuencia `4 3 2 1 0 4 3 2 1...` para dígitos 0–9 ilustra un patrón
improbable: nunca supera 4. Si una serie falla, puede sustituirse por otra
aleatorizada que pase el test; esta afirmación es una recomendación del
material, no garantía de que la nueva serie sea buena para todo modelo.

En el **test de rachas**, una muestra de tamaño \(n\) se divide en dos
categorías con \(n_1,n_2\). Una racha es una sucesión de valores de la misma
categoría. El número de rachas no debería ser ni demasiado pequeño ni
demasiado grande. Para números se puede usar la mediana, obteniendo categorías
de tamaños aproximadamente iguales (\(n_1=n_2\pm1\)) (p. 37). Las pp. 36 y
38–39 presentan el estadístico y la región de decisión como imágenes no
extraíbles; la p. 40 anuncia Colab y la p. 41 está vacía.

## Ejercicio integrador (p. 42)

Aplicar una prueba de uniformidad y otra de aleatoriedad a \(N=250\) valores
de cada secuencia:

1. MidSquare, \(X_0=3127\).
2. MidSquare, \(X_0=912783\).
3. Congruencial multiplicativo,
   \(X_0=127,\;X_n=115X_{n-1}\bmod128\).
4. Congruencial mixto,
   \(X_0=115,\;X_n=(51X_{n-1}+31)\bmod91\).
5. Congruencial mixto,
   \(X_0=6789,\;X_n=(25214903917X_{n-1}+11)\bmod(2^{48}-1)\).

Para resolverlo reproduciblemente: generar exactamente 250 estados/valores,
normalizar al intervalo uniforme según la convención del generador, aplicar
K–S o chi-cuadrado para uniformidad y rachas o pares no solapados para
aleatoriedad, fijar \(\alpha\), reportar estadístico, grados de libertad,
valor crítico o *p*-valor y decisión. Registrar periodos cortos, ceros,
repeticiones y clases con esperados muy pequeños, porque son diagnósticos del
generador y no simples detalles de redondeo.

---

## Lista final de comprobación para estudiar

1. Poder definir sistema, modelo, estado, evento, entidad, atributo, recurso,
   actividad, delay y DES.
2. Distinguir verificación (programa contra modelo) de validación (modelo
   contra realidad), y terminante de no terminante.
3. Explicar process interaction, event scheduling, activity scanning y tres
   fases.
4. Clasificar modelos por tiempo, estado, azar, dinámica, linealidad, frontera
   y estabilidad.
5. Justificar cuándo simular y cuándo resolver analíticamente.
6. Generar \(U(0,1)\) con MidSquare/congruenciales y discutir semilla, periodo,
   eficiencia, uniformidad e independencia.
7. Aplicar transformada inversa, aceptación-rechazo y composición a variables
   discretas, identificando qué fórmulas de una diapositiva deben consultarse
   en el PDF original por estar dibujadas.
8. Diferenciar pruebas de uniformidad (K–S, chi-cuadrado) de aleatoriedad
   (pares y rachas), declarar \(\alpha\), estadístico, grados de libertad y
   decisión.
