# ai_agent.py
import random
from collections import Counter

class AIAgent:
    def __init__(self, options):
        self.options = options
        self.history = []

    def get_computer_action(self):
        """
        Estrategia basada en frecuencia:
        - Contamos las jugadas más comunes del jugador
        - Elegimos la acción que las derrota
        """
        if not self.history:
            return random.choice(self.options)  # primera jugada aleatoria

        # Contar frecuencia de las jugadas del jugador
        freq = Counter(self.history)
        most_common = freq.most_common(1)[0][0]

        # Definir reglas de victoria
        rules = {
            "piedra": ["tijera", "lagarto"],
            "papel": ["piedra", "spock"],
            "tijera": ["papel", "lagarto"],
            "lagarto": ["spock", "papel"],
            "spock": ["tijera", "piedra"]
        }

        # Buscar acciones que ganen contra la más común del jugador
        winning_actions = [action for action, beats in rules.items() if most_common in beats]

        # Elegir aleatoriamente entre las posibles ganadoras
        return random.choice(winning_actions)

    def update_history(self, player_action):
        self.history.append(player_action)
