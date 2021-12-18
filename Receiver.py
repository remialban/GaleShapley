from Wisher import Wisher

class Receiver:
    def __init__(self, callback, data=None, places_number=1):
        self.__data = data
        self.__places_number = places_number
        self.__wishers = []
        self.__calback = callback

    def __str__(self) -> str:
        return str(self.__data)

    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data

    def add(self, wisher: Wisher):
        if wisher in self.__wishers:
            return None

        wisher.accept()
        self.__wishers.append(wisher)

        if len(self.__wishers) > self.__places_number:
            callback_result = self.__calback(self.__wishers)
            if callback_result != None:
                wisher_index = self.__wishers.index(callback_result)
                callback_result.refuse()
                return self.__wishers.pop(wisher_index)
        else:
            return None