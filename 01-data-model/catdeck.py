import collections

Cat = collections.namedtuple('Cat', ['age', 'breed'])

class CatDeck:
    ages = [str(n) for n in range(1, 5)]
    breeds = 'maine_coon ragdoll british_shorthair'.split()

    def __init__(self):
        self._cats = [Cat(age, breed) for age in self.ages
                                      for breed in self.breeds]
        
    def __len__(self):
        return len(self._cats)
    
    def __getitem__(self, position):
        return self._cats[position]
