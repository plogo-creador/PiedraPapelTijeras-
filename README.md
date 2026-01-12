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
