## class `ListOfAdopters`
 A `ListOfAdopters` is a list of `Adopter` objects that stores information for potential adopters at the pet store and can evaluate criteria based on the preferences of the adopters.

---

### `__init__()`
Initializes with an empty list of adopters

---

### `new_adopter(preferences)`
Creates a new `Adopter` object by calling to store the preferences of a potential adopter and adds the object to the list of potential adopters.

| | |
|---|---|
| `preferences` (`list[int]`) | A list of pet indexes in preference order: n-1 index is nth preference. |
| **Raises** | `TypeError` if the inputed `preferences` object is not a list of integers. |

```
new_adopter([1st preference, 2nd preference, ..., nth preference])
```

---

### `pos_favorites()`
Decides wheather it is possible to have a matching where every adopter is matched with their favorite pet.

| | |
|---|---|
| **Returns** | `True` if there is a possible matching where every adopter is matched with their 1st choice pet. Otherwise returns `False`. |

---

### `pet_popularity(adopters)`
Ranks the pets based on their popularity given a list of adopters.

| | |
|---|---|
| `adopters` (`list[Adopters]`) | A list of adopter objects. |
| **Returns** | A ranked list of pet ids wit the most popular pet first. |
| **Raises** | `TypeError` if `adopters` is not specifically a list of adopter objects. |

---

### `all_favorites(matching)`
Determines if every adopter recieved their favorite pet.

| | |
|---|---|
| `matching` | A `Matching` object that contains pairs of adopter indexes and pet indexes. |
| **Returns** | `True` if every adopter in `matching` has their favorite pet. Otherwise returns `False`.|
| **Raises** | `TypeError` if `matching` is not a `Matching` object. |

---

### `all_matched(matching)`
Determines if every adopter recieved a pet.

| | |
|---|---|
| `matching` | A `Matching` object that contains pairs of adopter indexes and pet indexes. |
| **Returns** | `True` if every adopter in `matching` has a pet. Otherwise returns `False`.|
| **Raises** | `TypeError` if `matching` is not a `Matching` object. |

---

### `top_n(matching, n)`
Determines whether every adopter recieves a pet from amoung their top n choices.

| | |
|---|---|
| `matching` | A `Matching` object that contains pairs of adopter indexes and pet indexes. |
| **Returns** | `True` if each adopter is matched with a pet from their top n choices. Otherwise returns `False`. |
| **Raises** | `TypeError` if `matching` is not a `Matching` object, or `IndexError` if `n` is out of range. |

---