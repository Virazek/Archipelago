A couple of notes about the data format and how it is to be interpreted, both by humans and by Archipelago:

# Accessibility Conditions
A common pattern on region connections and location/event accessibility is
```json
"accessible_from": {
    "SUBREGION/BEACH": [["ITEM/A", "ITEM/B"], ["ITEM/C"]]
}

```

This accessibility condition means that from the subregion *BEACH*, it requires (ITEM/A **AND** ITEM/B) **OR** (ITEM/C)

# Tricks
Tricks are defined in *tricks.json*, and can do either two things (in theory they could do both but they should probably only do 1)

*Connect subregions*
This trick defines the following in its body:
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

*Alternate accessibility condition*
The trick defines the following in its body:
```json
"allows_access": [
    {
        "to": "LOCATION/A",
        "from": "SUBREGION/B",
        "requires": [["ITEM/C"]]
    },
    {
        "to": "LOCATION/D",
        "from": "SUBREGION/E",
        "requires": [[]]
    }
]
```
When this trick is enabled, each location/event defined in *to* becomes accessible from the subregion *from* with items *requires*.