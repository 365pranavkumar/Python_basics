class juggler:
    def __init__(self,name):
        self.__name=name

    def juggles(self,juggling_item):
        print(self.__name+"performs juggling using: "+juggling_item.get_name())




class jugglingItem:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

