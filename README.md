## 1. Especificación do contorna de tarefas

| Contorno | Observable | Agentes | Determinista | Episódico | Estático | Discreto | Coñecido |
|----------|------------|---------|--------------|-----------|---------|----------|----------|
| RPS      | Parcialmente observable | 2 | Parcialmente determinista | Episódico | Estático | Discreto | Conocido |
| RPSLS   | Parcialmente observable | 2 | Parcialmente determinista | Secuencial | Estático | Discreto | Conocido |

**Justificación:**

- **Observable:** Cada jugador solo ve la jugada del otro después de realizar la suya.  
- **Agentes:** Dos agentes: jugador y máquina.  
- **Determinista:** Las reglas son fijas, pero la IA introduce variabilidad.  
- **Episódico/Secuencial:** Cada jugada es un episodio; si la IA aprende, es secuencial.  
- **Estático:** El entorno no cambia por sí solo durante el juego.  
- **Discreto:** Conjunto finito de acciones posibles (3 o 5 según versión).  
- **Conocido:** Reglas conocidas para ambos jugadores.



## 2. Identificación do tipo de axente

El agente que implementamos es **reactivo basado en modelo**.  
Recuerda el historial de jugadas del jugador para predecir la próxima acción y maximizar sus posibilidades de ganar.

### Diagrama del agente




### Explicación de los componentes

- **Percepción:** recibe la jugada del jugador en la ronda actual.  
- **Estado interno:** almacena el historial de jugadas para predecir patrones.  
- **Función de actualización:** decide la mejor jugada según el historial y la estrategia elegida.  
- **Actuador / Acción:** devuelve la jugada seleccionada por la IA.
