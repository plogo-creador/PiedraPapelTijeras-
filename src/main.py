# main.py
from game import check_winner, WIN_RULES_RPSLS
from ai_agent import AIAgent

def main():
    options = ["piedra", "papel", "tijera", "lagarto", "spock"]
    ai = AIAgent(options)

    while True:
        player = input(f"Elige una acción {options} (o 'salir' para terminar): ").lower()
        if player == "salir":
            break
        if player not in options:
            print("Opción inválida. Intenta de nuevo.")
            continue

        computer = ai.get_computer_action()
        print(f"Máquina elige: {computer}")
        resultado = check_winner(player, computer, WIN_RULES_RPSLS)
        print(f"Resultado: {resultado}\n")

        ai.update_history(player)

if __name__ == "__main__":
    main()