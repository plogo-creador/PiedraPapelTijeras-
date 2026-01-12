🧠 Piedra – Papel – Tijera – Lagarto – Spock
Axente Reactivo con Aprendizaxe por Frecuencias
Autor: Adrián Rodríguez Sebastián
Curso: MIA
Profesor: @dfleta
 1. Especificación do contorno de tarefas

A continuación analízase o contorno segundo os criterios dados en clase:

Propiedade	Valor	Xustificación
Observable	Parcialmente observable	O axente só percibe a xogada do xogador, pero non coñece intencións nin estratexia.
Axentes	Dous axentes (IA e xogador)	Ambos toman decisións independentes, interactuando entre si.
Determinista / Non determinista	Non determinista	Non se pode predicir con certeza a xogada do xogador.
Episódico / Secuencial	Episódico	Cada ronda é independente; non existe un obxectivo a longo prazo máis alá de gañar cada ronda.
Estático / Dinámico	Estático	O estado do ambiente non cambia mentres o axente está a decidir.
Discreto / Continuo	Discreto	Só existen 5 accións posibles ben definidas.
Coñecido / Descoñecido	Coñecido	As regras do xogo son fixas e coñecidas previamente polo axente.
 2. Tipo de axente e estrutura

O axente implementado é un Axente Reactivo Baseado en Modelo, xa que:

Percibe a xogada do xogador (“percept”).

Actualiza un estado interno baseado no historial.

Utiliza o estado interno para tomar decisións.

A decisión depende do modelo de aprendizaxe por frecuencias.

 Diagrama do Axente
<p align="center"> <img src="docs/diagramaagente.png" alt="Diagrama del agente" width="600"/> </p>
 Explicación da estrutura

Sensores: reciben a xogada do xogador.

Estado Interno: historial de accións do xogador.

Función de actualización: identifica a xogada máis frecuente.

Función de decisión: escolla a acción que derrota á máis frecuente.

Actuadores: envían a acción da IA como resposta.

 3. Implementación en Python
 Estrutura do proxecto
├── src/
│   ├── main.py
│   ├── ai_agent.py
│   ├── rules.py
├── images/
│   └── agent_diagram.png
├── README.md
└── .gitignore

 Principios SOLID aplicados

SRP: cada ficheiro cumpre unha única responsabilidade.

OCP: o sistema é extensible (engadir novas accións e regras sen modificar o núcleo).

Módulos independentes: regras, axente e interface separados.

 IA que aprende por frecuencias
Código principal da IA
# ai_agent.py
import random
from collections import Counter

class AIAgent:
    def __init__(self, options):
        self.options = options
        self.history = []

    def get_computer_action(self):
        if not self.history:
            return random.choice(self.options)

        freq = Counter(self.history)
        most_common = freq.most_common(1)[0][0]

        rules = {
            "piedra": ["tijera", "lagarto"],
            "papel": ["piedra", "spock"],
            "tijera": ["papel", "lagarto"],
            "lagarto": ["spock", "papel"],
            "spock": ["tijera", "piedra"]
        }

        winning_actions = [action for action, beats in rules.items() if most_common in beats]
        return random.choice(winning_actions)

    def update_history(self, player_action):
        self.history.append(player_action)

4. Extensión a RPS + Lagarto + Spock

Engadíronse dúas novas accións ao sistema:

Lagarto

Spock

 Novas regras de victoria

Piedra aplasta Tijera e aplasta Lagarto

Papel cubre Piedra e refuta Spock

Tijera corta Papel e decapita Lagarto

Lagarto envenena Spock e devora Papel

Spock rompe Tijera e vaporiza Piedra

 Adaptación da IA

A IA non require modificacións estruturais:
a mesma estratexia de frecuencias funciona cos 5 símbolos.

A clave é que o axente:

Observa a xogada do xogador.

Aprende cal é a máis frecuente.

Escolla entre as accións que lle gañan.

Actualiza o historial.

 5. Como executar o programa
python3 src/main.py

 6. .gitignore recomendado
__pycache__/
*.pyc
venv/
.env/
.vscode/

 7. Traballo futuro (opcional)

Engadir aprendizaxe por cadeas de Markov.

Usar redes neuronais simples para predición.

Crear interface gráfica.

 8. Licenza

Licenza libre para uso académico.