## class `ListOfAdopters`

 A `ListOfAdopters` is a list of `Adopter` objects that stores information for potential adopters at the pet store and can evaluate criteria based on the preferences of the adopters.

---

### `__init__()`
Initializes with an empty list of adopters

---

### `new_adopter(preferences)`
Creates a new `Adopter` object to store the preferences of a potential adopter and adds the object to the list of potential adopters.

| | |
|---|---|
| `preferences` (`list[int]`) | A list of pet indexes in preference order: n-1 index is nth preference. |
| **Raises** | TODO |

```
new_adopter([1st preference, 2nd preference, ..., nth preference])
```

---

### `pos_favorites()`
**TODO:** description

returns True if there is a possible matching where every adopter is matched with their 1st choice pet. Otherwise returns False.

| | |
|---|---|
| **Returns** | A list of pet indexes in preference order: n-1 index is nth preference. |

---

### `pet_popularity()`
**TODO:** description
given collection of adopters + preferences, return ranked list of pets with most popular pet first

| | |
|---|---|
| **Returns** | A list of pet indexes in preference order: n-1 index is nth preference. |
| **Raises** | TODO |


---

### `all_favorites(MATCHING)`
**TODO:** description
given a matching, determine wheather every adopter recieves a pet

| | |
|---|---|
| **Returns** | A list of pet indexes in preference order: n-1 index is nth preference. |
| **Raises** | TODO |

---

### `top_n(MATCHING, n)`
**TODO:** description
given a matching and a number n, determine wheather every adopter recieves a pet from amoung their top n choices

| | |
|---|---|
| **Returns** | A list of pet indexes in preference order: n-1 index is nth preference. |
| **Raises** | TODO |

---