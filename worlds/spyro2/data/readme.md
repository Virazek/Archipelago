A couple of notes about the data format and how it is to be interpreted, both by humans and by Archipelago:

# Accessibility Conditions
A common pattern on region connections and location/event accessibility is
```json
"accessible_from": {
    "SUBREGION/BEACH": [["ITEM/A", "ITEM/B"], ["ITEM/C"]],
}

```

This accessibility condition means that from SUBREGION/BEACH, this location/event requires (ITEM/A **AND** ITEM/B) **OR** (ITEM/C)

## Aliases

### _MOVE/ANY

The use of "_MOVE/ANY" for accessibility conditions for spirit particles and gems is an alias for (MOVE/FLAME) OR (MOVE/CHARGE) OR (MOVE/PERMANENT_POWERFLAME). This condition is usually explicitly listed for other accessibility conditions, but it would get extremely repetitive for these cases so it is abbreviated.

# Pseudoregions

All locations (including events) create their own pseudoregions to simplify multi-region accessibility.
From the perspective of AP, these are just normal regions, as with all other subregions.
These regions do not have entrances to other regions within them, unless defined by tricks.
They follow the same naming convention as the location (e.g., the 'Lizard hunt' Orb in Glimmer creates a pseudoregion named 'ORB/GLIMMER/LIZARD_HUNT')

# Tricks
Tricks are defined in *tricks.json*, and defines the following in its body
```json
"connects": [
    {
        "from": "SUBREGION/FOREST",
        "to": "SUBREGION/BEACH",
        "requires": [["ITEM/A", "ITEM/B"], ["ITEM/C"]]
    },
    {
        "from": "SUBREGION/MOUNTAIN",
        "to": "SUBREGION/CITY",
        "requires": [["ITEM/D", "ITEM/E"], ["ITEM/F"]]
    }
]
```

When this trick is enabled, each connection defined adds an entrance from the subregion *from* to the subregion *to*, which requires items in *requires*. For example, the above trick would allow traversing from SUBREGION/FOREST to SUBREGION/BEACH with (ITEM/A AND ITEM/B) OR (ITEM/C), and analoguously for traversing from SUBREGION/MOUNTAIN to SUBREGION/CITY.