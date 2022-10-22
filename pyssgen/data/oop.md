---
title: Vocabulaire de la programmation orienté objet
author: Kenneth Soares (cours de T. Tournier)
date: 06-10-2022
---

## Définitions

<u>Classe</u>: Type de données composites qui sont un assemblage d'un autre
type de données qui permettent d'encapsuler les données dans de nouveaux objets.

<u>Objet</u>: Assemblage unique constitué de données dont le type est déterminé
par une classe.

<u>Instance</u>: Propriété pour un objet d'être d'une classe donnée. On dit qu'un
objet crée à partir de la classe `A` est une instance de `A`.

<u>Méthode</u>: Cas particulier de fonction définie à l'intérieur d'une classe.
Une méthode ne s'exécute que dans le contexte d'une instance de classe donnée.
Les méthodes correspondent aux actions que peut effectuer cet objet.

<u>Attribut</u>: Ils correspondent aux caractéristiques de l'objet, ils
représentent son état.

### BONUS

<u>Getters et Setters</u>: Les getters et setters sont des types de méthodes
permettant d'accéder aux attributs d'un objet pour les lire ou les modifier
sans avoir à modifier manuellement ces derniers.

## Application

On va donc écrire une classe `Chien` avec la méthode `cri()` dans laquelle
on va retourner la string "waf waf" et l'attribut `nom`. ON va ensuite créer
une instance de `Chien` `best_dog` ayant pour attributs `nom = "Mikado"`. Enfin
on va faire appel à sa méthode `cri()` et afficher son nom avec un *getter*
`get_name()`.

```
class Chien:
    def __init__(self, nom):
        self.nom = nom
    def cri(self):
        return "waf waf"
    def get_name(self):
        return self.nom

best_dog = Chien("Mikado")
print(best_dog.cri())
print(best_dog.get_name())
```


