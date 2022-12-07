# Modulen kortlek

import random

class Kort:

    ftab = ('\N{BLACK CLUB SUIT}','\N{WHITE DIAMOND SUIT}','\N{WHITE HEART SUIT}','\N{BLACK SPADE SUIT}')
    vtab = ('E', '2', '3', '4','5','6','7','8','9','10','Kn','D','K')

    def __init__(self, färg, valör):
        self._färg = färg
        self._valör = valör

    def get_färg(self):
        return self._färg

    def get_valör(self):
        return self._valör

    def __str__(self):
        return Kort.ftab[self._färg-1] + ' ' + Kort.vtab[self._valör-1]


class Kortlek:

    def __init__(self):
        self._lek = []
        for i in range(1, 5):
            for j in range(1, 14):
                self._lek.append(Kort(i, j))
        random.shuffle(self._lek)
    
    def ge(self):
        if len(self._lek) > 0:
            return self._lek.pop()
        else:
            return None


print(Kortlek().ge())
    