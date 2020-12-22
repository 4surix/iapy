import iapy


@iapy.alias(n = 'number')
def increment(n):
    return n + 1

increment(number = 6) == 7


@iapy.alias(couleur = 'color')
class Pomme:

    def __init__(self, couleur):

        self.couleur = couleur

pomme = Pomme(color = 'red')
pomme.color == pomme.couleur == 'red'


@iapy.alias(
    # français |  anglais | español   | japonais
    heure    = ['hour'    , 'hora'    , '時'],
    minute   = ['minute'  , 'minuto'  , '分'],
    seconde  = ['second'  , 'segundo' , '瞬']
)
class Horloge:

    import pytz
    import datetime

    @iapy.alias(tz = 'timezone')
    def update(self, tz = None):

        self.heure, self.minute, self.seconde = (
            self.pytz.timezone(tz)
            .localize(self.datetime.datetime.now())
            .timetuple()[3:6]
        )

H = Horloge()
H.update(timezone = 'Europe/Lisbon')
print(H.hour, H.minuto, H.瞬)


dict__ = iapy.alias(item1 = 'item2')(
    {
        'item1': 1
    }
)

dict__['item1'] == dict__['item2'] == 1