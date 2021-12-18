from Receiver import Receiver
from Wisher import Wisher
from GaleShaplay import GaleShapley

alice = Wisher(data="Alice")
bob = Wisher(data="Bob")
charlie = Wisher(data="Charlie")

def callback_literature(wishers: list[Wisher]):
    if bob in wishers:
        return bob
    if charlie in wishers:
        return charlie
    return None
def callback_economie(wishers: list[Wisher]):
    if charlie in wishers:
        return charlie
    if alice in wishers:
        return alice
    return None
def callback_science(wishers: list[Wisher]):
    if bob in wishers:
        return bob
    if alice in wishers:
        return alice
    return None


literature = Receiver(callback_literature, data="Littérature", places_number=2)
economie = Receiver(callback_economie, data="Economie", places_number=1)
science = Receiver(callback_science, data="Science", places_number=1)

alice.add_wish(economie)
alice.add_wish(literature)
alice.add_wish(science)

bob.add_wish(literature)
bob.add_wish(economie)
bob.add_wish(science)

charlie.add_wish(literature)
charlie.add_wish(economie)
charlie.add_wish(science)

algo = GaleShapley([charlie, bob, alice])
algo.play()

print("========== Alice ==========")
for wish in alice.get_wishs():
    print(wish)

print("========== Bob ==========")
for wish in bob.get_wishs():
    print(wish)

print("========== Charlie ==========")
for wish in charlie.get_wishs():
    print(wish)