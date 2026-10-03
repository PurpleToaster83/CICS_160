## class `ListOfAdopters`
 A `ListOfAdopters` is a list of `Adopter` objects that stores information for potential adopters at the pet store and can evaluate criteria based on the preferences of the adopters.

 All methods in `ListOfAdopters` is Read-Only except for `new_adopter`, which adds another `Adopter` object to the internal `adopters` list. Indexing of `list` objects begins at 0 while ranking begins at 1.

---

### `__init__()`
Initializes an empty list of adopters called `adopters`

---

### `new_adopter(preferences)`
Creates a new `Adopter` object by calling to store the preferences of a potential adopter and adds the object to the list of potential adopters.

| | |
|---|---|
| `preferences` (`list[int]`) | A list of pet indexes in preference order: n-1 index is nth preference. |
|**Returns**| The index of the new adopter in `self.adopters`. |
| **Raises** | `TypeError` if the inputted `preferences` object is not a list of integers. |

```
new_adopter([1st preference, 2nd preference, ..., nth preference])
```

---

### `pos_favorites()`
Decides weather it is possible to have a matching where every adopter is matched with their favorite pet.

| | |
|---|---|
| **Returns** | `True` if there is a possible matching where every adopter is matched with their 1st choice pet (when every adopter's first choice is distinct from the other adopters' first choices). Otherwise returns `False`. |
| **Calls** | `Adopter.get_preferences()` to check for overlap amoung adopters' first preference. |

---

### `pet_popularity(adopters)`
Ranks the pets based on their popularity among adopters in the input adopter parameter. The method ranks only based on the `Adopter` objects passed in through the `adopters` list

| | |
|---|---|
| `adopters` (`list[Adopter]`) | A list of adopter objects. |
| **Returns** | A ranked list of pet ids with the most popular pet first. |
| **Raises** | `TypeError` if `adopters` is not specifically a list of adopter objects. |

---

### `all_favorites(matching)`
Determines if every adopter received their favorite pet.

| | |
|---|---|
| `matching` | A `Matching` object that contains pairs of adopter indexes and pet indexes. Assumes `matching` contains no duplicate pairs that contain the same `Adopter` or pet. |
| **Returns** | `True` if every adopter in `matching` has their favorite pet. Otherwise returns `False`.|
| **Raises** | `TypeError` if `matching` is not a `Matching` object. |
| **Calls** | `Adopter.get_preferences()` to compare each adopter's match with their first preference. |

---

### `all_matched(matching)`
Determines if every adopter in `self.adopters` received a pet in `matching`.

| | |
|---|---|
| `matching` | A `Matching` object that contains pairs of adopter indexes and pet indexes. Assumes `matching` contains no duplicate pairs that contain the same `Adopter` or pet. |
| **Returns** | `True` if every adopter in `self.adopters` is in `matching` with a pet. Otherwise returns `False`.|
| **Raises** | `TypeError` if `matching` is not a `Matching` object. |

---

### `top_n(matching, n)`
Determines whether every adopter recieves a pet from amoung their top n choices.

| | |
|---|---|
| `matching` | A `Matching` object that contains pairs of adopter indexes and pet indexes. Assumes `matching` contains no duplicate pairs that contain the same `Adopter` or pet. |
| `n` (`int`)| an integer value that determines the how many preferneces to consider for a "successful" match. 0 ≤ n ≤  len(`preferences`). |
| **Returns** | `True` if each adopter is matched with a pet from their top n choices. Otherwise returns `False`. |
| **Raises** | `TypeError` if `matching` is not a `Matching` object, or `IndexError` if `n` is out of range. |
| **Calls** | `Adopter.top_npreferences()` to compare each adopter's match with their top n preferences. |

---