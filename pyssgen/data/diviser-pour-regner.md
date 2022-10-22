---
title: Diviser pour régner (méthode algorithmique)
author: Kenneth Soares (cours de T. Tournier)
date: 24-09-2022
---

## 1. Explication du paradigme "Diviser pour régner"

Le paradigme diviser pour régner est une méthode algorithmique basée
sur le principe suivant: on prend un problème complexe que l'on divise
en une multitude de petits problèmes. Une fois les petits problèmes résolus,
on les recombine afin d'obtenir la solution au problème de départ.

### TL;DR

On a donc 3 étapes:
* Diviser: Diviser le problème en un certain nombre de sous-problèmes.
* Régner: Résoudre les sous-problèmes.
* Combiner: On combine les solutions des sous-problèmes afin d'obtenir la
  solution au problème de base.

## Application concrète

On va donc refaire en Python l'algorithme de tri fusion afin de mieux
comprendre cette notion.

``` python

# on se sert de cette fonction pour fusionner les deux listes
def fusion(l1,l2):
    lvide = []
    while l1 != [] and l2 != []:
        if l1[0] <= l2[0]:
            lvide.append(l1[0])
            l1 = l1[1:]
        else:
            lvide.append(l2[0])
            l2 = l2[1:]

        lvide = lvide + l1 + l2
        return lvide

# on décompose récursivement notre liste de départ en plusieurs listes
# que l'on recompose triées avec fusion()

def tri_fusion(t):
    if len(t) <= 1:
        return t
    else:
        l1 = tri_fusion(t[:len(t) // 2])
        l2 = tri_fusion(t[len(t) // 2:])
    return fusion(l1,l2)
```

Cet algorithme utilise donc la notion de [récursivité](https://www.youtube.com/watch?v=pg5YeSsOLZU)
pour trier un tableau avec une complexité inférieure a celle du tri par selection,
par exemple.

|                   | complexité |
|-------------------|------------|
| tri fusion        | O(nlog₂n)  |
| tri par selection | O(n²)      |
