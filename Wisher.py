from collections import deque

class Wisher:
    def __init__(self, data=None):
        self.__wishs = deque()
        self.__data = data
        self.__is_accepted = False

    def get_wishs(self):
        return self.__wishs
    def add_wish(self, receiver):
        self.__wishs.append(receiver)

    def remove_wish(self):
        return self.__wishs.popleft()
    
    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data
    
    def is_accepted(self) -> bool:
        return self.__is_accepted
    
    def accept(self):
        self.__is_accepted = True
    
    def refuse(self):
        self.remove_wish()
        self.__is_accepted = False

    def get_receiver(self):
        return self.__wishs[0] if len(self.__wishs) > 0 else None
        
    def is_finish(self) -> bool:
        return self.is_accepted() or len(self.__wishs) == 0

    def __str__(self) -> str:
        return str(self.__data)