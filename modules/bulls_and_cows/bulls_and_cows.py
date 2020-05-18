""" Module of class : BullsAndCows """
import random


class BullsAndCows(): 
    """ Class for playing in Bulls and Cows """ 
    __players_sequence = None
    __computers_sequence = None
    status = "Game is not initialized"
    def __init__(self, input_sequence):
        """ Init game-session """ 
        if input_sequence.isdigit() and len(input_sequence) == 4 and (len(set(input_sequence)) == 4):
            self.__players_sequence = input_sequence
            self.__create_sequence()
            self.status = 'Game started'
        else: 
            self.status = 'Wrong input. Value must contain 4 unique digits'

    def __create_sequence(self):
        """ Generate __computer_sequence """ 
        self.__computers_sequence = str()
        while len(self.__computers_sequence) != 4:
            rand = random.randint(0, 9)
            if str(rand) not in self.__computers_sequence:
                self.__computers_sequence  += str(rand)
