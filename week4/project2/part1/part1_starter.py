"""Part 1 starter. Rename to part1.py before submitting.

Both functions below use the shelter_roster module. Its documentation is in
SHELTER_ROSTER_API.md, in this folder. Everything needed is in that file.
"""

from shelter_roster import ShelterRoster


def yard_candidates(roster):
    """Find the adopters whose household has a yard.

    Arguments:
        roster (ShelterRoster): the roster to inspect.

    Returns:
        list of str: the names of every adopter with a yard, sorted
            alphabetically. Empty if no adopter has a yard.
    """

    candidates = []
    for i in range(roster.adopter_count()):
        if roster.adopter_household(i)['has_yard']:
            candidates.append(roster.adopter_name(i))

    return candidates    


def species_census(roster):
    """Count the pets of each species on the roster.

    Arguments:
        roster (ShelterRoster): the roster to inspect.

    Returns:
        dict: maps each species name that appears on the roster to the number
            of pets of that species. Species with no pets on the roster are
            left out entirely.
    """
    census = dict()

    for i in range(roster.pet_count()):
        pet_sp = roster.pet_species(i)
        if not census.get(pet_sp):
            census.update({pet_sp: 1})
        else:
            census[pet_sp] += 1
    return census


if __name__ == "__main__":
    shelter = ShelterRoster.from_file("roster_small.txt")
    print(yard_candidates(shelter))
    print(species_census(shelter))
