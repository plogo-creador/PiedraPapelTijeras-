# game.py

# Diccionario con quién gana contra quién
WIN_RULES_RPS = {
    "piedra": ["tijera"],
    "papel": ["piedra"],
    "tijera": ["papel"]
}

WIN_RULES_RPSLS = {
    "piedra": ["tijera", "lagarto"],
    "papel": ["piedra", "spock"],
    "tijera": ["papel", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["tijera", "piedra"]
}

def check_winner(player, computer, rules):
    if player == computer:
        return "Empate"
    elif computer in rules[player]:
        return "Jugador"
    else:
        return "Máquina"
