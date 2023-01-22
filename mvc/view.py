""" La vue représente la façon dont le modèle est présenté à l’utilisateur, et 
    dont il interagit avec lui (p.e.: interface API, ou une page web). """


class Touchscreen:
    """Vue qui gère l'interface de la jukebox."""
 
    def select_song(self):
        """Sélectionne un son."""
        pass
 
    def prompt_for_next_song(self, songs):
        """Demande un nouveau son."""
        for song in songs:
            # affiche les sons
            pass
        return "Dark Chest of Wonders"
 
 
class Speakers:
    """Vue qui gère le son."""
 
    def __init__(self):
        """Initialise le volume."""
        self.volume = 5
 
    def get_louder(self):
        """Augmente le volume."""
        self.volume += 1
 
    def get_quieter(self):
        """Baisse le volume."""
        self.volume -= 1
 
    def play_song(self, song):
        """Joue la musique."""
        pass
 
 
class CoinSlot:
    """Vue qui gère la reception de l'argent."""
 
    def __init__(self, amount):
        """Initialise le montant."""
        self.amount = amount
 
    def request_money(self, amount):
        """Attend un montant de l'utilisateur."""
        # attend l'argent
        # donne le change
        self.amount += amount
        return True
