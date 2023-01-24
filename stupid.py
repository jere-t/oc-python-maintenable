# Methode STUPID (anti-patterns de design)

# Les idées qui empirent le code au lieu de l’améliorer !. Tout ce qui doit être éviter

# L’acronyme STUPID désigne ces éléments :

# Singleton.
# un objet qui garantit d’être la seule instance de son type. 
# Compliqué à maintenir et va pas être SOLID 

# Couplage fort (« Tight coupling »).
# Le couplage fort se produit lorsque deux classes (ou modules) dépendent tellement l’une de l’autre que 
#  si vous apportez des modifications à l’une, vous devez souvent apporter des modifications à l’autre

# Non-testabilité (« Untestability »).
# Une classe peut être difficile ou impossible à tester pour de nombreuses raisons. 
# Mais on en revient le plus souvent à un problème de couplage fort avec un autre composant. 
# Si une classe a besoin de nombreuses dépendances pour fonctionner correctement, ça indique qu’il faut la réécrire. 
# Le fait de tester un composant peut également être compliqué s’il viole la responsabilité unique et fait trop de choses.

# Optimisation prématurée (« Premature optimization »).
# L’optimisation prématurée désigne le fait de gérer un problème que l’on anticipe bien avant qu’il ne devienne un problème.
# L’optimisation prématurée prend du temps et complexifie le code. Il se peut même que cette implémentation ne serve pas ! À l’inverse, l’acronyme YAGNI (you ain't gonna need it, ou “vous n’en aurez pas besoin”), conseille d’aller au plus simple, et de n’ajouter que les fonctionnalités qui sont absolument nécessaires.

# Nommage non descriptif (« Indescriptive naming »).
# Eviter les noms pas descriptif

# Duplication.
# La duplication constitue un piège dans lequel il est très facile de tomber. Vous avez besoin d’ajouter une nouvelle fonctionnalité. 
# Elle doit fonctionner comme une fonctionnalité existante, mais un peu différemment. Que faites-vous ? Vous copiez, collez, et modifiez. 
# Si vous adoptez cette approche de façon suivie, vous vous retrouverez avec du code dupliqué en de nombreux endroits. 
# S’il faut modifier quelque chose de fondamental, tous ces emplacements copiés doivent être retrouvés et modifiés.
