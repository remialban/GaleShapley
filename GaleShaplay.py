class GaleShapley:
    def __init__(self, wishers=[]):
        self.__wishers = wishers

    def play(self):

        finish = False

        while not finish:
            finish = True
            for wisher in self.__wishers:
                if wisher.is_finish() == False:
                    receiver = wisher.get_receiver()
                    receiver.add(wisher)
                    finish = False
        return self.__wishers