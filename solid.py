""" Methode SOLID :  """

# Pensez au principe KISS (Keep It Simple, Stupid)
# Votre solution sera plus facile à comprendre. Si elle est plus facile à comprendre, 
# alors elle est plus facile à modifier. De plus, vous pouvez avoir davantage de certitude qu’une modification ne cassera rien.
# Autre avantage, elle sera plus facile à tester. Mieux vos classes sont séparées, et plus il sera facile de les tester séparément.

# Pour ça on s'aide de Design patterns et de la méthode SOLID qu'on va voir ici. 
# Chacune des lettres de l’acronyme SOLID représente une excellente idée à garder à l’esprit lorsque vous construisez l’architecture de votre système. 

# « S » désigne la responsabilité unique (« Single responsibility »). 
# Philosophy UNIX : Do one thing and do it well. Elle ne doit avoir qu’une seule raison de changer.
# Chaque personne qui utilise votre code doit pouvoir comprendre ce qu’il se passe. Le fait de réduire au minimum les responsabilités d’une classe aide à atteindre cet objectif.

# « O » désigne le principe ouvert/fermé (« Open/Closed »).
# Les classes doivent être ouvertes à l’extension, mais fermées à la modification.
# Extension = ajouter du code à une classe , Modification = modifier code existant. 
# Il faut préparer le code et enlever ce qui va potentiellement être modifié comme -->
  # Lorsque vous avez des algorithmes qui accomplissent des calculs (coût, taxe, score dans un jeu, etc.) : il est probable que l’algorithme change au fil du temps.
  # Lorsque vous avez des données qui entrent ou sortent du système : la destination finale (fichier, base de données, autre système) changera probablement, de même que le format concret des données.
# Exemple - Avant :


class Controller : 
    """Main controller."""
    
    def __init__(self, deck: Deck, view):
        """Has a deck, a list of players and a view."""
        # models
        self.players: List[Player] = []
        self.deck = deck

        # views
        self.view = view
    
    # (...)    
    
    def evaluate_game(self):
        last_player = self.players[0]
        best_candidate = self.players[0]

        for player in self.players[1:]:
            player_card = player.hand[0]
            last_player_card = last_player.hand[0]

            score = (RANKS.index(player_card.rank), SUITS.index(player_card.suit))
            last_score = (
                RANKS.index(last_player_card.rank),
                SUITS.index(last_player_card.suit),
            )

            if score[0] == last_score[0]:
                if score[1] > last_score[1]:
                    best_candidate = player
            elif score[0] > last_score[0]:
                best_candidate = player

            last_player = player

        return best_candidate.name
# Après :      
# Nouveau fichier dans le package controller : 
class CheckerRankAndSuitIndex:
  """Check the cards according to their rank and sequence."""

    def check(self, players: List[Player]):
      # (...)

      
class Controller:
    """Main controller."""

    def __init__(self, deck: Deck, view, checker_strategy):
        """Has a deck, a list of players and a view."""
        # models
        self.players: List[Player] = []
        self.deck = deck

        # views
        self.view = view

        # check strategy
        self.checker_strategy = checker_strategy

    # (...)    
          
    def evaluate_game(self):
        """Evaluate the game."""
        return self.checker_strategy.check(self.players)
  
  def main():
    deck = Deck()

    active_view = PlayerView()
    passive_views = (active_view, BroadcastView(), InternetStreamingView())
    views = Views(active_view, passive_views)

    checker = CheckerRankAndSuitIndex()

    game = Controller(deck, views, checker)
    game.run()


if __name__ == "__main__":
    main()
        
# « L » désigne la substitution de Liskov.
# Les sous-classes doivent pouvoir faire tout ce que font leurs classes parentes. 
# Si vous remplacez une classe parente par l’une de ses sous-classes, cela ne doit pas casser votre système !

# « I » désigne la ségrégation des interfaces (« Interface Segregation »).
# Cela correspond essentiellement au principe de responsabilité unique, appliqué aux interfaces.

# duck typing. This term comes from the saying “If it walks like a duck, and it quacks like a duck, then it must be a duck.” 
# Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.

# « D » désigne l’inversion des dépendances (« Dependency Inversion »).
# Les classes parentes ne doivent pas avoir à changer lorsque l’une de leurs sous-classes est modifiée.
# L’inversion des dépendances dit que les concepts de haut niveau doivent communiquer à travers des abstractions de haut niveau. 
# En d’autres termes : les classes de haut niveau ne doivent pas avoir à changer juste parce que les classes de bas niveau changent.
# Soyez attentif à ce que les classes n’en sachent pas trop sur les implémentations des autres classes.
