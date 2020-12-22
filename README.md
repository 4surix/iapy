# IAPy
Identifier Alias Python. Créer des alias d'identifiant en Python.

# Aperçu
```python
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
```