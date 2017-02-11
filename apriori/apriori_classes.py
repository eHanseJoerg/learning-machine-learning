
class Item:
    def __init__(self, name):
        '''
        Diese Klasse repräsentiert die Items.

        :param name: der Name des Items
        '''
        self.name = name


class Itemmenge(set):
    def __init__(self):
        '''
        Bei der Init direkt die Itemmenge übergeben.

        :param j: Item[]
        '''
        list.__init__([])


