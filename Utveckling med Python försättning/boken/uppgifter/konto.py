class Konto:

    ## KLASS använder cls

    # klassvarabler
    _räntesats = 0

    # klassmetoder

    @classmethod
    def set_räntesats(cls, p):
        assert p >= 0, ('Negativa ränta', p)
        cls._räntesats = p
    
    @classmethod
    def get_räntesats(cls):
        return cls._räntesats

    ## INSTANS använder self

    # instanvariabler
    def __init__(self, nr):
        self._nr = nr
        self.kontohavare = None
        self.saldo = 0
        self.intjänade_ränta = 0

    # instansmetoder
    def get_nr(self):
        return self._nr
    
    def lägg_till_ränta(self):
        self.intjänade_ränta = self.intjänade_ränta + self.saldo*Konto._räntesats/100/365


# att använda en kals variabel måste man anvenda classen direkt, inte objeckt:
Konto.set_räntesats(5)

