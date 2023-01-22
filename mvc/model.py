""" Les informations relatives à l'etat (valeur a stocké sur le court terme,
     DB, ...)"""

PRICE_PER_SONG = 1.20
 

class Song:
    """Modèle représentant un son."""
 
    def __init__(self, name, artist, genre, artwork):
        """Initialise les détails relatifs au son."""
        self.artist = artist
        self.name = name
        self.genre = genre
        self.artwork = artwork
 

class Library:
    """Modèle qui stocke les sons."""
 
    def __init__(self):
        """Initialise une liste de sons."""
        self.songs = []
 

class ServiceInfo:
    """Modèle qui gère la maintenance de la jukebox."""

    def __init__(self, status, engineer_name):
        """Initialise les détails du service."""
        self.service_date = datetime.now()
        self.status = status
        self.engineer = engineer_name