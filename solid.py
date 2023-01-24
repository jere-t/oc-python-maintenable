""" Methode SOLID :  """

# Pensez au principe KISS (Keep It Simple, Stupid)
# Votre solution sera plus facile à comprendre. Si elle est plus facile à comprendre, 
# alors elle est plus facile à modifier. De plus, vous pouvez avoir davantage de certitude qu’une modification ne cassera rien.
# Autre avantage, elle sera plus facile à tester. Mieux vos classes sont séparées, et plus il sera facile de les tester séparément.

# Pour ça on s'aide de Design patterns et de la méthode SOLID qu'on va voir ici. 
# Chacune des lettres de l’acronyme SOLID représente une excellente idée à garder à l’esprit lorsque vous construisez l’architecture de votre système. 

# « S » désigne la responsabilité unique (« Single responsibility »). 
# Philosophy UNIX : Do one thing and do it well. Elle ne doit avoir qu’une seule raison de changer.

# « O » désigne le principe ouvert/fermé (« Open/Closed »).
# Les classes doivent être ouvertes à l’extension, mais fermées à la modification.

# « L » désigne la substitution de Liskov.
# Les sous-classes doivent pouvoir faire tout ce que font leurs classes parentes. 
# Si vous remplacez une classe parente par l’une de ses sous-classes, cela ne doit pas casser votre système !

# « I » désigne la ségrégation des interfaces (« Interface Segregation »).
# Cela correspond essentiellement au principe de responsabilité unique, appliqué aux interfaces.

# « D » désigne l’inversion des dépendances (« Dependency Inversion »).
# Les classes parentes ne doivent pas avoir à changer lorsque l’une de leurs sous-classes est modifiée.
