"""
Module containing Archipelago options definitions for Spyro 2 for Archipelago
"""

from Options import (
    Choice,
    Range,
    Toggle,
    DefaultOnToggle,
    OptionSet,
)


class Goal(Choice):
    """
    Determines the goal for this world:

    Ripto: Defeat Ripto in Winter Tundra.

    All Bosses: Defeat Crush in Summer Forest, Gulp in Autumn Plains, and Ripto in Winter Tundra.

    Orb Hunt: Find a certain number of Orbs in the multiworld.
    """

    display_name = "Goal"
    option_ripto = 0
    option_all_bosses = 1
    option_orb_hunt = 2
    default = 1


class NumberOfOrbs(Range):
    """
    Maximum number of Orbs that may be in the item pool.

    If there are not enough available locations in the pool (say, by excluding too many), then this number may be lowered to make the world beatable.

    All options that use a percentage of Orbs will be calculated based off of this number.
    """

    display_name = "Number of Orbs"
    range_start = 1
    range_end = 64
    default = 64


class PercentageOfOrbHuntOrbs(Range):
    """
    If 'Orb Hunt' is selected as the goal, what percentage of Orbs are requried to complete the goal.
    """

    display_name = "Orb Hunt Required Percentage"
    range_start = 1
    range_end = 100
    default = 63  # 62.5% of 64 is 40


class AllGemLocations(Choice):
    """
    Enable locations for obtaining all 400 Gems in each world. Different sized Gem Packets will be added as items to the multiworld depending on this and the 'Minor Gem Locations' option.

    If the 'Individual Speedway Objectives' option is enabled, then each of the 5 speedways objectives (e.g., Rings, Arches, Boats, Cars, and All In One for Ocean Speedway)
    are separate locations. Otherwise, the only Gem location for speedways is the 'All In One' objective.

    This will add 25 or 41 locations respectively.
    """

    display_name = "All-Gem Locations"
    option_all_gems_only = 0
    option_all_gems_individual_speedway_objectives = 1
    default = 1


class MinorGemLocations(Choice):
    """
    Enable locations pertaining to individual gems. Different sized Gem Packets will be added as items to the multiworld depending on this and the 'All-Gem Locations' option.

    None: No locations added.

    Magenta only: Magenta Gems (the ones worth 25 Gems normally) are available locations.

    Gemsanity: Every gem in the game is its own location. I take no responsibility for you ruining your multiworlds with this option.
    """

    display_name = "Minor Gem Locations"
    option_none = 0
    option_magenta_only = 1
    option_gemsanity = 2
    default = 1


class SkillPointLocations(Toggle):
    """
    When enabled, the Skill Points (the in-game achievement system) are available as locations.
    This will add 17 locations.
    """

    display_name = "Skill Point Locations"


class GuidebookEntryLocations(DefaultOnToggle):
    """
    When enabled, entering a level for the first time (except Dragon Shores) will be an available location.
    This will add 28 locations.
    """

    display_name = "Guidebook Entry Locations"


class DragonShoresTokenLocations(Toggle):
    """
    When enabled, the minigames in Dragon Shores are available as locations.
    The Dragon Shores tokens will be shuffled into the item pool and the Gnorcs will give a random multiworld item.
    Otherwise, they will have their vanilla tokens.
    This will add 10 locations.
    """

    display_name = "Dragon Shores Token Locations"


class SpiritParticleLocations(Choice):
    """
    Determines how locations for spirit particles (that you receive from defeating enemies) are added:

    None: No locations added.

    Maximum: Adds a location to each level for obtaining the maximum amount of spirit particles in that level. You can see this amount on the pause menu.

    Particlesanity: Adds a location for obtaining each number of spirit particle available each level. (e.g., in Glimmer, there would be '1 Spirit Particle', '2 Spirit Particles' ... '14 Spirit Particles' locations). I take no responsibility for you ruining your multiworlds with this option.

    These will add 18 and 416 locations respectively.
    """

    display_name = "Spirit Particle Locations"
    option_none = 0
    option_maximum = 1
    option_particlesanity = 2
    default = 1


class PermanentPowerflamePyramidsLocation(Toggle):
    """
    When enabled, the permanent powerflame pyramids in Dragon Shores (the normal reward for 100%ing the game) is a location.
    The door requires 64 Orbs and 10000 Gems to open. If the 'Number of Orbs' option value resolves to less than 64, this option will be forcibly disabled during generation.
    """

    display_name = "Permanent Powerflame Arch Location"


class PowerupPyramids(Choice):
    """
    Determines how powerup pyramids in levels (except the permanent powerflame pyramids in Dragon Shores) will provide their powerups.

    Vanilla: All pyramids provide their powerup at the vanilla spirit particle number.

    Randomize Cost: Pyramids will have a randomized spirit particle cost.

    Shuffle: Each level has an item in the multiworld that will activate its pyramids.

    Note that if 'Powerup Move Randomizer' is enabled, the item for the move itself is also required.
    """

    display_name = "Powerup Pyramids"
    option_vanilla = 0
    option_randomize_cost = 1
    option_shuffle = 2
    default = 1


class CrystalGlacierBridgeUnlockType(Choice):
    """
    Determines what type of collectable unlocks the bridge in Crystal Glacier from Moneybags.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Crystal Glacier Bridge Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Crystal Glacier Bridge' multiworld item.
    """

    display_name = "Crystal Glacier Bridge Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class CrystalGlacierBridgeUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Crystal Glacier Bridge Unlock Type' option) are required to unlock the bridge in Crystal Glacier from Moneybags.
    """

    display_name = "Crystal Glacier Bridge Unlock Percentage"
    range_start = 1
    range_end = 100


class AquariaTowersSubmarineUnlockType(Choice):
    """
    Determines what type of collectable unlocks the submarine in Aquaria Towers from Moneybags.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Aquaria Towers Submarine Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Aquaria Towers Submarine' multiworld item.
    """

    display_name = "Aquaria Towers Submarine Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class AquariaTowersSubmarineUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Aquaria Towers Submarine Unlock Type' option) are required to unlock the submarine in Aquaria Towers from Moneybags.
    """

    display_name = "Aquaria Towers Submarine Unlock Percentage"
    range_start = 1
    range_end = 100


class MagmaConeElevatorUnlockType(Choice):
    """
    Determines what type of collectable unlocks the elevator in Magma Cone from Moneybags.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Magma Cone Elevator Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Magma Cone Elevator' multiworld item.
    """

    display_name = "Magma Cone Elevator Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class MagmaConeElevatorUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Magma Cone Elevator Unlock Type' option) are required to unlock the elevator in Magma Cone from Moneybags.
    """

    display_name = "Magma Cone Elevator Unlock Percentage"
    range_start = 1
    range_end = 100


class SwimUnlockType(Choice):
    """
    Determines what type of collectable unlocks swim from Moneybags in Summer Forest.
    If swim is randomized (see 'Unlock Move Randomizer'), then this location will have a random multiworld item on it.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Swim Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Swim' multiworld item. If swim is randomized and the 'Item' option is enabled, this option will be forcibly changed to 'Vanilla'.
    """

    display_name = "Swim Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class SwimUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Swim Unlock Type' option) are required for swim from Moneybags in Summer Forest.
    """

    display_name = "Swim Unlock Percentage"
    range_start = 1
    range_end = 100


class ClimbUnlockType(Choice):
    """
    Determines what type of collectable unlocks climb from Moneybags in Autumn Plains.
    If climb is randomized (see 'Unlock Move Randomizer'), then this location will have a random multiworld item on it..

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Climb Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Climb' multiworld item. If climb is randomized and the 'Item' option is enabled, this option will be forcibly changed to 'Vanilla'.
    """

    display_name = "Climb Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class ClimbUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Climb Unlock Type' option) are required for climb from Moneybags in Autumn Plains.
    """

    display_name = "Climb Unlock Percentage"
    range_start = 1
    range_end = 100


class HeadbashUnlockType(Choice):
    """
    Determines what type of collectable unlocks headbash from Moneybags in Winter Tundra.
    If headbash is randomized (see 'Unlock Move Randomizer'), then this location will have a random multiworld item on it..

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Headbash Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Headbash' multiworld item. If headbash is randomized and the 'Item' option is enabled, this option will be forcibly changed to 'Vanilla'.
    """

    display_name = "Headbash Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class HeadbashUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Headbash Unlock Type' option) are required for headbash from Moneybags in Winter Tundra.
    """

    display_name = "Headbash Unlock Percentage"
    range_start = 1
    range_end = 100


class GlimmerBridgeUnlockType(Choice):
    """
    Determines what type of collectable unlocks the bridge in Glimmer from Moneybags.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Glimmer Bridge Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Glimmer Bridge' multiworld item.
    """

    display_name = "Glimmer Bridge Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class GlimmerBridgeUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Glimmer Bridge Unlock Type' option) are required to unlock the bridge in Glimmer from Moneybags.
    """

    display_name = "Glimmer Bridge Unlock Percentage"
    range_start = 1
    range_end = 100


class AquariaTowersWallUnlockType(Choice):
    """
    Determines what type of collectable unlocks the wall blocking the Aquaria Towers portal from Moneybags in Summer Forest.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Aquaria Towers Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Aquaria Towers Wall' multiworld item.
    """

    display_name = "Aquaria Towers Wall Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class AquariaTowersWallUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Aquaria Towers Unlock Type' option) are required to unlock the wall blocking the Aquaria Towers portal from Moneybags in Summer Forest.
    """

    display_name = "Aquaria Towers Wall Unlock Percentage"
    range_start = 1
    range_end = 100


class OceanSpeedwayPortalUnlockType(Choice):
    """
    Determines what type of collectable unlocks the Ocean Speedway portal from Elora in Summer Forest.
    The portal behavior depends on the value of the 'Level Portal Shuffle' option:

    Disabled: Elora will move the portal in-bounds.

    Shuffle: The level portal item is required to enter the portal. Elora will move the portal in-bounds.

    Shuffle No OOB Access: Elora will give a random multiworld item. The level portal item will move the portal in-bounds.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Ocean Speedway Portal Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Ocean Speedway Portal' multiworld item. If 'Level Portal Shuffle' and the 'Item' options are enabled, this option will be forcibly changed to 'Vanilla'.
    """

    display_name = "Ocean Speedway Portal Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class OceanSpeedwayPortalUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Ocean Speedway Portal Unlock Type' option) are required to unlock the Ocean Speedway portal from Elora in Summer Forest.
    """

    display_name = "Ocean Speedway Portal Unlock Percentage"
    range_start = 1
    range_end = 100


class MetroSpeedwayPortalUnlockType(Choice):
    """
    Determines what type of collectable unlocks the Metro Speedway portal from Elora in Autumn Plains.

    If 'Level Portal Shuffle' is enabled, Elora will give a random multiworld item. The level portal item will move the portal in-bounds and allow you to enter it.
    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Metro Speedway Portal Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Metro Speedway Portal' multiworld item. If 'Level Portal Shuffle' and the 'Item' options are enabled, this option will be forcibly changed to 'Vanilla'.
    """

    display_name = "Metro Speedway Portal Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class MetroSpeedwayPortalUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Metro Speedway Portal Unlock Type' option) are required to unlock the Metro Speedway portal from Elora in Autumn Plains.
    """

    display_name = "Metro Speedway Portal Unlock Percentage"
    range_start = 1
    range_end = 100


class ZephyrPortalUnlockType(Choice):
    """
    Determines what type of collectable unlocks the Zephyr portal from Moneybags in Autumn Plains.

    If 'Level Portal Shuffle' is enabled, Moneybags will give a random multiworld item. The level portal item will move the portal in-bounds and allow you to enter it.
    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Zephyr Portal Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Zephyr Portal' multiworld item. If 'Level Portal Shuffle' and the 'Item' options are enabled, this option will be forcibly changed to 'Vanilla'.
    """

    display_name = "Zephyr Portal Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class ZephyrPortalUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Zephyr Portal Unlock Type' option) are required to unlock the Zephyr portal from Moneybags in Autumn Plains.
    """

    display_name = "Zephyr Portal Unlock Percentage"
    range_start = 1
    range_end = 100


class ShadyOasisBridgeUnlockType(Choice):
    """
    Determines what type of collectable unlocks the bridge leading to Shady Oasis in Autumn Plains from Moneybags.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Shady Oasis Bridge Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Shady Oasis Bridge' multiworld item.
    """

    display_name = "Shady Oasis Bridge Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class ShadyOasisBridgeUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Shady Oasis Bridge Unlock Type' option) are required to unlock the bridge leading to Shady Oasis in Autumn Plains from Moneybags.
    """

    display_name = "Shady Oasis Bridge Unlock Percentage"
    range_start = 1
    range_end = 100


class IcySpeedwayPortalUnlockType(Choice):
    """
    Determines what type of collectable unlocks the Icy Speedway portal from Moneybags in Autumn Plains.

    If 'Level Portal Shuffle' is enabled, Moneybags will give a random multiworld item. The level portal item will move the portal in-bounds and allow you to enter it.
    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Icy Speedway Portal Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Icy Speedway Portal' multiworld item. If 'Level Portal Shuffle' and the 'Item' options are enabled, this option will be forcibly changed to 'Vanilla'.

    """

    display_name = "Icy Speedway Portal Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class IcySpeedwayPortalUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Icy Speedway Portal Unlock Type' option) are required to unlock the Icy Speedway portal from Moneybags in Autumn Plains.
    """

    display_name = "Icy Speedway Portal Unlock Percentage"
    range_start = 1
    range_end = 100


class DragonShoresPortalUnlockType(Choice):
    """
    Determines what type of collectable unlocks the Dragon Shores portal in Winter Tundra.
    The door to the theme park in Dragon Shores is always open.
    The portal behavior depends on the value of the 'Level Portal Shuffle' option:

    Disabled: Fulfilling the cost will move the portal in-bounds.

    Shuffle: The level portal item is required to enter the portal. Fulfilling the cost will move the portal in-bounds.

    Shuffle No OOB Access: The level portal item will move the portal in-bounds.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Icy Speedway Portal Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Dragon Shores Portal' multiworld item. If 'Level Portal Shuffle' and the 'Item' options are enabled, this option will be forcibly changed to 'Vanilla'.
    """

    display_name = "Dragon Shores Portal Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class DragonShoresPortalUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Dragon Shores Portal Unlock Type' option) are required to unlock the Dragon Shores portal in Winter Tundra.
    """

    display_name = "Dragon Shores Portal Unlock Percentage"
    range_start = 1
    range_end = 100


class CloudTemplesPortalUnlockType(Choice):
    """
    Determines what type of collectable unlocks the Cloud Temples portal from the Professor in Winter Tundra.
    The portal behavior depends on the value of the 'Level Portal Shuffle' option:

    Disabled: The Professor will move the portal in-bounds.

    Shuffle: The level portal item is required to enter the portal. The Professor will move the portal in-bounds.

    Shuffle No OOB Access: The Professor will give a random multiworld item. The level portal item will move the portal in-bounds.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Cloud Temples Portal Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Cloud Temples Portal' multiworld item. If 'Level Portal Shuffle' and the 'Item' options are enabled, this option will be forcibly changed to 'Vanilla'.
    """

    display_name = "Cloud Temples Portal Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class CloudTemplesPortalUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Cloud Temples Portal Unlock Type' option) are required to unlock the Cloud Temples portal from the Professor in Winter Tundra.
    """

    display_name = "Cloud Temples Portal Unlock Percentage"
    range_start = 1
    range_end = 100


class MetropolisPortalUnlockType(Choice):
    """
    Determines what type of collectable unlocks the Metropolis portal from the Professor in Winter Tundra.
    The portal behavior depends on the value of the 'Level Portal Shuffle' option:

    Disabled: The Professor will move the portal in-bounds.

    Shuffle: The level portal item is required to enter the portal. The Professor will move the portal in-bounds.

    Shuffle No OOB Access: The Professor will give a random multiworld item. The level portal item will move the portal in-bounds.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Metropolis Portal Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Metropolis Portal' multiworld item. If 'Level Portal Shuffle' and the 'Item' options are enabled, this option will be forcibly changed to 'Vanilla'.
    """

    display_name = "Metropolis Portal Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class MetropolisPortalUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Metropolis Portal Unlock Type' option) are required to unlock the Metropolis portal from the Professor in Winter Tundra.
    """

    display_name = "Metropolis Portal Unlock Percentage"
    range_start = 1
    range_end = 100


class AutumnPlainsProfessorDoorUnlockType(Choice):
    """
    Determines what type of collectable unlocks the door locked by the Professor in Autumn Plains.


    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Autumn Plains Professor Door Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Autumn Plains Professor Door' multiworld item.
    """

    display_name = "Autumn Plains Professor Door Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class AutumnPlainsProfessorDoorUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Autumn Plains Professor Door Unlock Type' option) are required to unlock the door locked by the Professor in Autumn Plains.
    """

    display_name = "Autumn Plains Professor Door Unlock Percentage"
    range_start = 1
    range_end = 100


class CanyonSpeedwayPortalUnlockType(Choice):
    """
    Determines what type of collectable unlocks the Canyon Speedway portal from the Professor in Summer Forest.
    The portal behavior depends on the value of the 'Level Portal Shuffle' option:

    Disabled: The Professor will move the portal in-bounds.

    Shuffle: The level portal item is required to enter the portal. The Professor will move the portal in-bounds.

    Shuffle No OOB Access: The Professor will give a random multiworld item. The level portal item will move the portal in-bounds.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Canyon Speedway Portal Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Canyon Speedway Portal' multiworld item. If 'Level Portal Shuffle' and the 'Item' options are enabled, this option will be forcibly changed to 'Vanilla'.
    """

    display_name = "Canyon Speedway Portal Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class CanyonSpeedwayPortalUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Canyon Speedway Portal Unlock Type' option) are required to unlock the Canyon Speedway portal from the Professor in Summer Forest.
    """

    display_name = "Canyon Speedway Portal Unlock Percentage"
    range_start = 1
    range_end = 100


class CrushUnlockType(Choice):
    """
    Determines what type of collectable unlocks the door to Crush's Dungeon from Elora in Summer Forest.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Crush Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Door to Crush' multiworld item.
    """

    display_name = "Crush Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class CrushUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Crush Unlock Type' option) are required to unlock the door to Crush's Dungeon from Elora in Summer Forest.
    """

    display_name = "Crush Unlock Percentage"
    range_start = 1
    range_end = 100


class GulpUnlockType(Choice):
    """
    Determines what type of collectable unlocks the door to Gulp's Overlook from Elora in Autumn Plains.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Gulp Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Door to Gulp' multiworld item.
    """

    display_name = "Gulp Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class GulpUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Gulp Unlock Type' option) are required to unlock the door to Gulp's Overlook from Elora in Autumn Plains.
    """

    display_name = "Gulp Unlock Percentage"
    range_start = 1
    range_end = 100


class RiptoUnlockType(Choice):
    """
    Determines what type of collectable unlocks the door to Ripto's Dungeon from Elora in Winter Tundra.

    A special value, 'Vanilla', is available, which will leave the unlock at its vanilla cost. Choosing this option will ignore the 'Ripto Unlock Percentage' option.
    The 'Item' option will unlock upon receiving the 'Unlock - Door to Ripto' multiworld item.
    """

    display_name = "Ripto Unlock Type"
    option_gems = 0
    option_orbs = 1
    option_talismans = 2
    option_tokens = 3
    option_vanilla = 4
    option_item = 5
    default = 4


class RiptoUnlockPercentage(Range):
    """
    Determines what percentage of collectables in the pool (of type determined by the 'Ripto Unlock Type' option) are required to unlock the door to Ripto's Dungeon from Elora in Winter Tundra.
    """

    display_name = "Ripto Unlock Percentage"
    range_start = 1
    range_end = 100


class BasicMoveRandomizer(Toggle):
    """
    When enabled, Spyro will be unable to perform certain basic actions until a corresponding multiworld item is obtained.
    Which actions are randomized is determined in the 'Randomized Basic Moves' option.
    """

    display_name = "Enable Basic Move Randomizer"


class RandomizedBasicMoves(OptionSet):
    """
    If 'Enable Basic Move Randomizer' is enabled, which moves are randomized.

    Available options are 'Charge', 'Glide', 'Hover', 'Flame', and 'Spit'.

    There are 2 special alias options. These assume priority over individual options if both are specified:
    "_Random" - Randomizes which moves are randomized.
    "_Random_Except_Charge" - Same as the above, except charge is never randomized.
    """

    display_name = "Randomized Basic Moves"
    valid_keys = frozenset([
        "Charge",
        "Glide",
        "Hover",
        "Flame",
        "Spit",
        "_Random",
        "_Random_Except_Charge",
    ])


class UnlockMoveRandomizer(Toggle):
    """
    When enabled, Spyro will be unable to perform certain unlockable actions until a corresponding multiworld item is obtained.
    Which actions are randomized is determined in the 'Randomized Unlock Moves' option.
    """

    display_name = "Enable Unlock Move Randomizer"


class RandomizedUnlockMoves(OptionSet):
    """
    If 'Enable Unlock Move Randomizer' is enabled, which moves are randomized.

    Available options are 'Swim', 'Climb', and 'Headbash'.

    There is a special alias option. This assumes priority over individual options if both are specified:
    "_Random" - Randomizes which moves are randomized.
    """

    display_name = "Randomized Unlock Moves"
    valid_keys = frozenset(["Swim", "Climb", "Headbash", "_Random"])


class PowerupMoveRandomizer(Toggle):
    """
    When enabled, Spyro will be unable to perform certain powerup actions until a corresponding multiworld item is obtained.
    Which actions are randomized is determined in the 'Randomized Powerup Moves' option.
    """

    display_name = "Enable Powerup Move Randomizer"


class RandomizedPowerupMoves(OptionSet):
    """
    If 'Enable Powerup Move Randomizer' is enabled, which moves are randomized.

    Available options are 'Supercharge', 'Superfly', 'Bigbounce', 'Superfreeze', 'Temporary Powerflame', and 'Temporary Invincibility'.

    There is a special alias option. This assumes priority over individual options if both are specified:
    "_Random" - Randomizes which moves are randomized
    """

    display_name = "Randomized Powerup Moves"
    valid_keys = frozenset([
        "Supercharge",
        "Superfly",
        "Bigbounce",
        "Superfreeze",
        "Temporary Powerflame",
        "Temporary Invincibility",
        "_Random",
    ])


class DoubleJump(DefaultOnToggle):
    """
    When enabled, the double jump glitch will be obtainable as an item in the multiworld. Otherwise, it will be patched out.
    If 'Basic Move Randomizer' is enabled, charge is also required to be able to double jump.
    To have double jump avalable from the start (as in the vanilla game), use 'start_inventory'.
    """

    display_name = "Double Jump"


class PermanentPowerflame(Toggle):
    """
    When enabled, permanent powerflame (the normal reward for 100%ing the game) will be obtainable as a progression item in the multiworld.
    Otherwise, it will not be available, even from the pyramids in Dragon Shores (regardless of the value of the 'Permanent Powerflame Arch Location' option).
    """

    display_name = "Permanent Powerflame"


class LevelPortalShuffle(Choice):
    """
    Determines how level portals are traversable in this world:

    Disabled: All level portals may be entered.

    Shuffled: A corresponding 'Level Portal - (level)' item is required to enter any level portal (you will start with one accessible from your hubworld spawn).

    Shuffled No OOB Access: Same as 'Shuffled', however will change how portals that are unlocked are handled (e.g., see the 'Ocean Speedway Unlock Type' option).

    Boss portals are always traversable.
    """

    display_name = "Level Portal Shuffle"
    option_disabled = 0
    option_shuffled = 1
    option_shuffled_no_oob_access = 2
    default = 0


class LevelPortalRandomization(Toggle):
    """
    When enabled, level portals will send you to a random level within the hubworld.
    """

    display_name = "Level Portal Randomization"


class RandomStartLocation(Choice):
    """
    Determines if the locations where Spyro can spawn within levels will be randomized:

    None: Spyro spawns at the vanilla location in all levels.
    Hubworld Only: Spawn locations in hubworlds are randomized, but not within levels.
    Levels Only: Spawn location in hubworlds are vanilla, but are randomized within levels.
    All: Spawn locations for both hubworlds and levels are randomized.
    """

    display_name = "Random Start Location"
    option_none = 0
    option_hubworld_only = 1
    option_levels_only = 2
    option_all = 3
    default = 0


class GuidebookEntriesAsItems(Toggle):
    """
    When enabled, Guidebook pages for each level are obtainable as items in the multiworld. These items are considered filler.
    If disabled, all Guidebook pages are available from the start.
    """

    display_name = "Guidebook Entries as Items"


class MaxHealthItems(Range):
    """
    Determines how many max health items to put in the pool, and correspondingly how much to lower Spyro's initial max health by.
    These items are considered progression, and may be logically required for certain damage boosts.
    Additional max health items (by !getitem, server send, etc.) will not increase max health past three.
    Vanilla behavior is zero (Spyro starts with three max health).
    """

    display_name = "Max Health Items"
    range_start = 0
    range_end = 3
    default = 0


class Tricks(OptionSet):
    """
    A list of tricks to allow in-logic.
    Values should be formatted as '{map_name} - {trick_name}'. See the world docs page for more details.
    """

    display_name = "Tricks"
    default = frozenset()
