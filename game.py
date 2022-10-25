from random import choice

from play import *

insultos = ['¿Eres gallina McFly?', '¡Cobarde!']

def run_game():
    '''
    Arranca el juego
    '''
    display_game()

    while True:
        user_play = get_user_play()
        comp_play = random_play()
        display_match(user_play, comp_play)
        winner = get_winner(user_play, comp_play)

        if winner == None:
            display_tie(user_play, comp_play)
        else:
            display_victory(winner)
        
        if another_play():
            continue
        else:
            print(choice(insultos))
            break



def another_play():
    '''
    Pregunta si se quiere volver a jugar. 
    Devuelve True en caso de que si quiero jugar, False, en caso contrario.
    '''
    again = None

    while True:
        response = input('\nAnother round? \n\"y\" for YES, \"n\" for NO: ')
        response = response.lower()
        if response == 'y':
            again = True
            break
        elif response == 'n':
            again = False
            break
        else:
            continue

    return again



def display_game():
    '''
    Muestra el nombre del juego
    '''
    print('\n\n\t\tRock, Paper, Scissors, Lizard, Spock!\n')



def display_match(play1, play2):
    '''
    Muestra las jugadas
    '''
    print(f'\n{play1.description()} vs. {play2.description()}')



def get_user_response():
    '''
    Presenta un menu de opciones y pide que seleccione una
    Devuelve una cadena que indica lo que ha elegido
    '''
    response = None
    while True:
        print('\nChoose your play: ')
        print('1. Rock 🪨 \n2. Paper 📄 \n3. Scissors ✄ \n4. Lizard 🦎 \n5. Spock 🖖')
        raw = input('Enter 1, 2, 3, 4 or 5:\t')
        #validar raw
        raw = raw.strip()
        if raw == '1':
            response = 1
            break
        elif raw == '2':
            response = 2
            break
        elif raw == '3':
            response = 3
            break
        elif raw == '4':
            response = 4
            break
        elif raw == '5':
            response = 5
            break
        else:
            continue
    return response


def get_user_play():
    '''
    Le pregunta al usuario que quiere jugar y lo devuelve
    '''
    res = get_user_response()
    play = None
    if res == 1:
        play = Rock()
    elif res == 2:
        play = Paper()
    elif res == 3:
        play = Scissors()
    elif res == 4:
        play = Lizard()
    elif res == 5:
        play = Spock()
    return play


def random_play():
    '''
    Selecciona una jugada al azar para competir con el usuario
    '''
    return choice([Rock(), Paper(), Scissors(), Lizard(), Spock()])


def get_winner(play1, play2):
    '''
    Obtiene el vencedor o None si hay empate
    '''
    winner = ''
    if play1.compare(play2) == Result.LOSES:
        winner = play2
    elif play1.compare(play2) == Result.WINS:
        winner = play1
    else:
        winner = None
    return winner


def display_tie(play1, play2):
    '''
    Imprime que ha habido un empate
    '''
    print(f'\nEmpate entre dos {play1.description()}')


def display_victory(winner):
    '''
    Muestra que winner ha ganado
    '''
    print(f'\nHa ganado {winner.description()}')


if __name__ == '__main__':
    run_game()