"""Part 2 starter. Rename to part2.py before submitting.

Fill in report(). It must use the matchtools package, which is in this
folder as compiled .pyc files. The source is not available. The only
documentation is matchtools/README.md and matchtools/NOTES.txt.

Stop after 90 minutes whether or not this works. Partial and broken code
receives full credit. The graded deliverable for Part 2 is question_log.md.
"""

import matchtools

PREFERENCES_FILE = "preferences.csv"

#The matching handed over by the scheduling team. Tuples are (adopter, pet).
#The order of the tuples carries no meaning, but this list belongs to the
#caller and report() must leave it exactly as it found it.
MATCHING = [(3, 1), (0, 2), (5, 3), (1, 5), (4, 4), (2, 0)]


def report(matching, table):
    """Summarize how well a matching serves the adopters in a table.

    Arguments:
        matching (list): a list of (adopter_index, pet_index) tuples, in no
            particular order. Not modified.
        table: a loaded matchtools preference table.

    Returns:
        dict: with exactly these keys.
            'covers_everyone' (bool): whether every adopter in the table
                appears in the matching.
            'all_favorites' (bool): whether every adopter in the matching
                received the pet at the top of their own preference list.
            'favorites_possible' (bool): whether it would be possible, in
                principle, for every adopter to receive their top pet.
            'within_top_3' (bool): whether every adopter in the matching
                received a pet from among their own first three choices.
            'most_popular_pet' (int): the index of the single most popular
                pet across all adopters' preferences.
            'ranks' (list of int): ranks[i] is the zero-based position of the
                pet adopter i received within adopter i's own preference
                list. 0 means adopter i received their favorite pet.
    """
    # create the dictionary template to be returned
    rep = {
        'all_favorites': True,
        'covers_everyone': True,
        'favorites_possible': True,
        'most_popular_pet': None,
        'ranks': [],
        'within_top_3': True
    }

    favorites = []

    for adopter, pet in matching:

        # check if all adopters are matched with their favorite pets
        if not(table.rank_of(adopter, pet) == 1):
            rep['all_favorites'] = False

        # check if everyone is in the table
        if table.size() != len(matching):
            rep['covers_everyone'] = False

        # check if every adopter is matched with a top 3 pet
        if not(table.rank_of(adopter, pet) <= 3):
            rep['within_top_3'] = False

        # set the most populat pet - direct table method
        rep['most_popular_pet'] = table.popularity_order()[0]

        # put all of the ranks of the match pairs in - 0 is best
        rep['ranks'].append(table.rank_of(adopter, pet) - 1)

        # add adopters favorite pet to list of favorites
        favorites.append(table.ranking(adopter)[0])

    # check for duplicates in favorites
    if(len(favorites) != len(set(favorites))):
        rep['favorites_possible'] = False

    return rep

if __name__ == "__main__":
    prefs = matchtools.PrefTable.load(PREFERENCES_FILE)
    result = report(MATCHING, prefs)
    for key in sorted(result):
        print(key, "=", result[key])
    print("matching is unchanged:", MATCHING == [(3, 1), (0, 2), (5, 3), (1, 5), (4, 4), (2, 0)])