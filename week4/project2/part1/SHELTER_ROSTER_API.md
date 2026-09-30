# shelter_roster API

Version 2.1. Last updated before this assignment was released.

Read-only access to a shelter roster. A roster records which pets are
currently at the shelter and which adopters are in talks with the shelter.
It does not record anyone's preferences, and it does not perform matching.

## Identifiers

Pets and adopters are identified by index. Both sets of indices are
zero-based and contiguous: a roster holding 3 pets uses pet indices 0, 1,
and 2. Pet indices and adopter indices are separate numbering schemes, so
pet 0 and adopter 0 are unrelated.

Every roster holds an equal number of pets and adopters.

## Module constant

### `SPECIES`

`tuple` of `str`. Every species name the roster format recognizes, in sorted
order: `("bird", "cat", "dog", "rabbit", "reptile")`.

## Roster file format

One record per line. Blank lines and lines beginning with `#` are ignored.

```
pet,<name>,<species>
adopter,<name>,<has_yard>,<other_pets>,<hours_away>
```

Indices are assigned in the order the records appear in the file, counting
pets and adopters separately. `<has_yard>` is either `yes` or `no`.
`<other_pets>` and `<hours_away>` are non-negative integers.

## class `ShelterRoster`

A snapshot of the pets and adopters at one shelter.

A `ShelterRoster` is read-only. No method on this class changes the roster
after it is loaded, and no method changes any argument it is given. Any
mutable value returned by a method is a fresh copy, so the caller is free to
modify it.

---

### `ShelterRoster.from_file(path)`

Static method. Loads a roster from a roster file.

| | |
|---|---|
| `path` (`str`) | Path to a roster file, in the format above. |
| **Returns** | `ShelterRoster`. The roster described by the file. |
| **Raises** | `FileNotFoundError` if no file exists at `path`. `ValueError` if a line is not a valid record, if a species is unknown, or if the file does not hold an equal number of pets and adopters. |

```python
roster = ShelterRoster.from_file("roster_small.txt")
```

---

### `roster.pet_count()`

Counts the pets on the roster.

| | |
|---|---|
| **Returns** | `int`. The number of pets. Valid pet indices run from 0 up to `pet_count() - 1`. |

---

### `roster.adopter_count()`

Counts the adopters on the roster.

| | |
|---|---|
| **Returns** | `int`. The number of adopters. Valid adopter indices run from 0 up to `adopter_count() - 1`. Always equal to `pet_count()`. |

---

### `roster.pet_name(pet_index)`

Looks up the name of a pet.

| | |
|---|---|
| `pet_index` (`int`) | A pet index, from 0 to `pet_count() - 1`. |
| **Returns** | `str`. The pet's name, for example `'Bella'`. |
| **Raises** | `IndexError` if `pet_index` is out of range. Negative indices are rejected rather than counting from the end. |

---

### `roster.adopter_name(adopter_index)`

Looks up the name of an adopter.

| | |
|---|---|
| `adopter_index` (`int`) | An adopter index, from 0 to `adopter_count() - 1`. |
| **Returns** | `str`. The adopter's name, for example `'Alice'`. |
| **Raises** | `IndexError` if `adopter_index` is out of range. Negative indices are rejected rather than counting from the end. |

---

### `roster.pet_species(pet_index)`

Looks up the species of a pet.

| | |
|---|---|
| `pet_index` (`int`) | A pet index, from 0 to `pet_count() - 1`. |
| **Returns** | `str`. One of the values in `SPECIES`, for example `'dog'`. |
| **Raises** | `IndexError` if `pet_index` is out of range. |

---

### `roster.index_of_pet(name)`

Finds the index of a pet by name.

| | |
|---|---|
| `name` (`str`) | A pet name. The comparison is case-sensitive. |
| **Returns** | `int`. The index of the pet with that name. If two pets share a name, the lower index is returned. |
| **Raises** | `KeyError` if no pet on the roster has that name. |

---

### `roster.index_of_adopter(name)`

Finds the index of an adopter by name.

| | |
|---|---|
| `name` (`str`) | An adopter name. The comparison is case-sensitive. |
| **Returns** | `int`. The index of the adopter with that name. If two adopters share a name, the lower index is returned. |
| **Raises** | `KeyError` if no adopter on the roster has that name. |

---

### `roster.pets_of_species(species)`

Lists every pet of one species.

| | |
|---|---|
| `species` (`str`) | A species name. Values outside `SPECIES` are allowed and simply match nothing. |
| **Returns** | `list` of `int`. The indices of every pet of that species, sorted in ascending order. Empty if the roster holds no such pet. The returned list is a fresh list and is safe to modify. |

```python
roster.pets_of_species("cat")   # [2, 3]
roster.pets_of_species("fish")  # []
```

---

### `roster.adopter_household(adopter_index)`

Describes an adopter's household.

| | |
|---|---|
| `adopter_index` (`int`) | An adopter index, from 0 to `adopter_count() - 1`. |
| **Returns** | `dict`. A fresh dict, safe to modify, with exactly these keys: `'has_yard'` (`bool`), whether the household has a yard; `'other_pets'` (`int`), how many pets the household already has; `'hours_away'` (`int`), hours per weekday nobody is home. |
| **Raises** | `IndexError` if `adopter_index` is out of range. |

```python
roster.adopter_household(0)
# {'has_yard': True, 'other_pets': 0, 'hours_away': 6}
```
