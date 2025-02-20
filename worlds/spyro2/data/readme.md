A couple of notes about the data format and how it is to be interpreted, both by humans and by Archipelago:

# Accessibility Conditions
A common pattern on region connections and location/event accessibility is
```json
"accessible_from": {
    "SUBREGION/BEACH": [["ITEM/A", "ITEM/B"], ["ITEM/C"]]
}

```

This accessibility condition means that from the subregion *BEACH*, it requires (ITEM/A **AND** ITEM/B) **OR** (ITEM/C)