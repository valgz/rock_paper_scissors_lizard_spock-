from enum import Enum

class Result(Enum):
    EQUAL = 0
    WINS = 1
    LOSES = 2


class Play(object):
    '''
    Representa una jugada 
    '''

    def compare(self, otherPlay):
        '''
        Compara papel con otras jugadas y devuelve un Result
        '''
        result = ''
        if self == otherPlay:
            result = Result.EQUAL
        elif otherPlay in self.beats():
            result = Result.WINS
        else:
            result = Result.LOSES
        return result

    def description(self):
        pass

    def __eq__(self, other):
        '''
        Devuelve true si self y other son equivalentes
        '''
        if isinstance(self, other.__class__):
            return self.description() == other.description()
        else:
            return False


    def __hash__(self):
        '''
        Devuelve un hash que representa  a self
        '''
        return hash(self.description())

    


class Paper(Play):

    def beats(self):
        return {Rock(), Spock()}

    def description(self):
        return 'Paper'



class Scissors(Play):

    def beats(self):
        return {Paper(), Lizard()}

    def description(self):
        return 'Scissors'



class Rock(Play):

    def beats(self):
        return {Scissors(), Lizard()}

    def description(self):
        return 'Rock'
    


class Lizard(Play):

    def beats(self):
        return {Spock(), Paper()}
    
    def description(self):
        return 'Lizard'
    


class Spock(Play):

    def beats(self):
        return {Scissors(), Rock()}

    def description(self):
        return 'Spock'
    