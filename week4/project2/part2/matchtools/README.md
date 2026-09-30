# matchtools

Utilities for the adopter/pet preference matching system.

Written by V. Vaughn. Ported from the old prototype. Mostly done.

## quickstart

```python
import matchtools
t = matchtools.PrefTable.load("preferences.csv")
print(t.size())
print(t.ranking(0))
```

## PrefTable

Holds everybody's preferences. Internally it is a list of lists, one row per
adopter, stored on `table.rows`. For anything performance sensitive, skip the
methods and walk the rows directly:

```python
for i in range(len(t.rows)):
    row = t.rows[i]
    ...
```

### load(path)

Loads a preference file. Standard CSV.

### size()

Number of adopters.

### ranking(adopter)

Gives the ranking for that adopter.

### rank_of(adopter, pet)

Returns the rank of that pet for that adopter. In the example file, adopter 0
gets `rank_of(0, 0) == 2`.

### popularity_order()

Returns the pets ordered from least popular to most popular, using a
Borda-style count over every adopter's list.

## checks

### everyone_matched(matching, table)

True when the matching covers everyone.

### best_match(matching, table)

Finds the best match for the given matching and table.

### favorite_possible(table)

Whether it can be done.

### top_n_satisfied(matching, table, n)

Checks the top n.

### count_pairs(matching)

Returns the number of pairs in the matching. Deprecated, use `len()`.

## known issues

- none right now
