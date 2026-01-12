Piedra – Papel – Tijera – Lagarto – Spock
Axente Reactivo con Aprendizaxe por Frecuencias

Autor: Adrián Rodríguez Sebastián
Curso: MIA
Profesor: @dfleta

Índice

Especificación do contorno de tarefas

Tipo de axente e estrutura

Implementación en Python

Extensión a RPS-Lagarto-Spock

Execución do programa

.gitignore utilizado

Traballo futuro

1. Especificación do contorno de tarefas

A seguinte táboa describe o contorno segundo os criterios establecidos:

Propiedade	Valor	Xustificación
Observable	Parcialmente observable	O axente percibe a xogada do xogador, pero non coñece as súas intencións nin a súa estratexia.
Axentes	Dous axentes	IA contra xogador humano.
Determinismo	Non determinista	Non é posible predicir con certeza a xogada do xogador.
Episodicidade	Episódico	Cada ronda é independente doutra.
Estabilidade	Estático	O ambiente non cambia mentres o axente decide.
Granularidade	Discreto	Só existen cinco accións posibles.
Coñecemento	Coñecido	As regras e relacións entre accións son fixas e coñecidas.
2. Tipo de axente e estrutura

O axente implementado corresponde ao tipo Axente Reactivo Baseado en Modelo.

Este tipo de axente cumpre estas características:

Emprega percepcións (xogada do xogador).

Mantén un estado interno (historial de xogadas do xogador).

Actualiza ese estado en cada paso.

A decisión non é puramente reactiva, senón que depende do historial acumulado.

A acción xorde dunha función que analiza patróns e tendencias para predicir a mellor resposta.

Diagrama do Axente

Engadir a seguinte imaxe no directorio images/agent_diagram.png e referenciala así:

![Diagrama do axente](images/agent_diagram.png)

3. Implementación en Python
Estrutura básica do proxecto
├── src/
│   ├── main.py
│   ├── ai_agent.py
│   ├── rules.py
├── images/
│   └── agent_diagram.png
├── README.md
└── .gitignore

Lóxica da IA

A IA utiliza un modelo sinxelo pero efectivo:

Gárdase un historial das xogadas do xogador.

Calcúlase cal é a xogada máis frecuente no historial.

Determínanse as accións que gañan contra esa xogada frecuente.

Escóllese unha delas de maneira pseudorandomizada.

Código da IA (ai_agent.py)
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

4. Extensión a RPS-Lagarto-Spock

O xogo foi ampliado engadindo dúas novas accións:

Lagarto

Spock

As regras ampliadas quedan definidas así:

Piedra aplasta Tijera e Lagarto

Papel cubre Piedra e refuta Spock

Tijera corta Papel e decapita Lagarto

Lagarto envenena Spock e devora Papel

Spock rompe Tijera e vaporiza Piedra

A IA pode utilizar correctamente estas accións porque o modelo de aprendizaxe por frecuencias é independente do número de opcións.

5. Execución do programa

Execución desde o directorio principal:

python3 src/main.py

6. .gitignore utilizado
__pycache__/
*.pyc
venv/
.env/
.vscode/

7. Traballo futuro

Emprego dun modelo de Markov baseado en transicións entre xogadas.

Introdución dunha pequena rede neuronal para predición.

Creación dunha interface gráfica para facilitar interacción.