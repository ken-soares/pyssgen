---
title: La récursivité
author: Kenneth Soares (cours de T. Tournier)
date: 22-10-2022
---

## Récursivité

<u>définition</u>: Une fonction est dite récursive si elle fait appel à elle-même.


### Règles importantes concernant l'utilisation de la récursivité
* Une fonction récursive doit contenir une ou plusieurs conditions d'arrêt
(pour éviter que le programme tourne indéfiniment)
* Les valeurs passées dans les appels récursifs doivent être différents de celles
utilisées dans les appels précédents. (par exemple, foo(bar) peut appeler foo(bar-1))
* Après un certain nombre fini d'appels, la ou les valeurs passées en paramètre doivent
permettre de satisfaire une des conditions d'arrêt.
* Le nombre d'appels récursifs ne doit pas dépasser la profondeur de récursivité
(en Python, elle est aux alentours de 1000).

### Récursivité simple et multiple

Lorsque chaque appel de fonction engendre au plus un appel récursif, on parle
de récursivité simple mais on peut rencontrer une récursivité multiple où chaque
appel de fonction peut en effectuer plusieurs.

**Attention**: Avec les récursivités multiples, le nombre d'appels récursifs
peut être exponentiel et vite "exploser" (ce qui violerait la règle 4).


## Application concrète

On va implémenter la fonction factorielle (`facto(n)`) en Python pour montrer
un cas concrèt d'utilisation pour la récursivité

```python

def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n-1)
```
