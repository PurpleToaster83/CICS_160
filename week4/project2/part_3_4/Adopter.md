## class `Adopter`
An objects that stores important information about a potential pet adopter.

---

### `__init__(preferences)`
Initializes the specific `Adopter` instance with their preferences.

| | |
|---|---|
| `preferences` (`list[int]`) | A list of pet indexes in preference order: n-1 index is nth preference. |
| **Raises** | `TypeError` if the inputed `preferences` object is not a list of integers. |

```
Adopter([1st preference, 2nd preference, ..., nth preference])
```

---

### `get_preferences()`
Returns the `preferences` of the `Adopter` object.

| | |
|---|---|
| **Returns** | The adopter's `preferences`: a list of integers representing pets with the 0th element being the favorite pet. |

---

### `top_npreferences()`
Returns the n favorite pets of the `Adopter` object.

| | |
|---|---|
| **Returns** | The a sublist of the adopter's `preferences`: a list of integers representing pets with the 0th element being the favorite pet up to the n-1 position being the nth preference. |
---