# ai_agent.py
import random

class AIAgent:
    def __init__(self, options):
        self.options = options
        self.history = []  # historial de jugadas del jugador

    def get_computer_action(self):
        """
        Estrategia inicial:
        - Por ahora aleatoria
        - Se puede reemplazar por aprendizaje de frecuencias
        """
        return random.choice(self.options)

    def update_history(self, player_action):
        self.history.append(player_action)