"""
Module containing Archipelago options definition for Spyro 2 for Archipelago
"""

from dataclasses import dataclass

from Options import (
    OptionGroup,
    Choice,
    Range,
    Toggle,
    DefaultOnToggle,
    OptionSet,
    OptionList,
    PerGameCommonOptions,
    DeathLink,
)


class Goal(Choice):
    """
    Determines the goal for this world:

    Ripto: Defeat Ripto in Winter Tundra

    All Bosses: Defeat Crush in Summer Forest, Gulp in Autumn Plains, and Ripto in Winter Tundra

    Orb Hunt: Find a certain number of Orbs in the multiworld
    """

    display_name = "Goal"
    option_ripto = 0
    option_all_bosses = 1
    option_orb_hunt = 2
    default = 1


class NumberOfOrbs(Range):
    """
    Maximum number of Orbs that may be in the item pool

    If there are not enough available locations in the pool (say, by excluding them), this number may be lowered to make the world beatable

    All options that use a percentage of Orbs will be calculated based off of this number
    """

    display_name = "Number of Orbs"
    range_start = 1
    range_end = 64
    default = 64


class PercentageOfOrbHuntOrbs(Range):
    """
    What percentage of Orbs are required to finish the Orb Hunt goal
    """

    display_name = "Orb Hunt Required Percentage"
    range_start = 1
    range_end = 100
    default = 63  # 62.5% of 64 is 40


class AllGemLocations(Choice):
    """
    Enable locations for obtaining all 400 Gems in each world. Different sized Gem Packets will be added as items to the multiworld depending on this and the 'Minor Gem Locations' option.

    If the 'Individual Speedway Goals' option is enabled, then each of the 5 speedways objectives (e.g., Rings, Arches, Boats, and Cars for Ocean Speedway)
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
    When enabled, the 17 Skill Points (the in-game achievement system) are available as locations.
    """

    display_name = "Skill Point Locations"


class GuidebookEntryLocations(DefaultOnToggle):
    """
    When enabled, entering a level for the first time (except Dragon Shores) will be an available location.
    """

    display_name = "Guidebook Entry Locations"


class DragonShoresTokenLocations(Toggle):
    """
    When enabled, the 10 minigames in Dragon Shores are available as locations.
    """

    display_name = "Dragon Shores Token Locations"


class PowerupPyramids(Choice):
    """
    Determines how powerup pyramids in levels (except the permanent powerflame pyramid in Dragon Shores) will provide their powerups.

    Vanilla: All pyramids provide their powerup at the vanilla spirit particle number

    Randomize Cost: Pyramids will have a randomized cost

    Shuffle: Each pyramid has its own item in the multiworld that is required to activate it

    Note that if 'Powerup Move Randomizer' is enabled, the item for the move itself is also required
    """

    display_name = "Powerup Pyramids"
    option_vanilla = 0
    option_randomize_cost = 1
    option_shuffle = 2
    default = 1


class SpiritParticleLocations(Choice):
    """
    Determines how locations for spirit particles (that you receive from killing enemies) are added

    None: No locations added.

    Maximum: Adds a location to each level for obtaining the maximum amount of spirit particles in that level. You can see this amount on the pause menu.

    Particlesanity: Adds a location for obtaining each number of spirit particle available each level. (e.g., in Gilmmer, there would be '1 Spirit Particle', '2 Spirit Particles' ... '14 Spirit Particles' locations)
    """

    display_name = "Spirit Particle Locations"
    option_none = 0
    option_maximum = 1
    option_particlesanity = 2
    default = 1


class PermanentPowerflameArchLocation(Toggle):
    """
    When enabled, the permanent powerflame pyramids in Dragon Shores (the normal reward for 100%ing the game) is a location.
    The door requires 64 Orbs and 10000 Gems to open.
    """

    display_name = "Permanent Powerflame Arch Location"


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

    There are 2 special alias options:
    "_Random" - Randomizes which moves are randomized
    "_Random_Except_Charge" - Same as the above, except charge is never randomized, since it might not be very fun to play this game without it.
    """

    display_name = "Randomized Basic Moves"
    valid_keys = [
        "Charge",
        "Glide",
        "Hover",
        "Flame",
        "Spit",
        "_Random",
        "_Random_Except_Charge",
    ]


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

    There is a special alias option:
    "_Random" - Randomizes which moves are randomized
    """

    display_name = "Randomized Unlock Moves"
    valid_keys = ["Swim", "Climb", "Headbash", "_Random"]


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

    There is a special alias option:
    "_Random" - Randomizes which moves are randomized
    """

    display_name = "Randomized Powerup Moves"
    valid_keys = [
        "Supercharge",
        "Superfly",
        "Bigbounce",
        "Superfreeze",
        "Temporary Powerflame",
        "Temporary Invincibility",
        "_Random",
    ]


class DoubleJump(DefaultOnToggle):
    """
    When enabled, the double jump glitch will be obtainable as an item in the multiworld. Otherwise, it will be patched out.
    If you want to have it from the start, use 'start_inventory'.
    """

    display_name = "Double Jump"


class PermanentPowerflame(Toggle):
    """
    When enabled, permanent powerflame (the normal reward for 100%ing the game) will be obtainable as an item in the multiworld.
    Otherwise, it will not be available, even from the pyramids in Dragon Shores (regardless of the value of the 'Permanent Powerflame Arch Location' option).
    """

    display_name = "Permanent Powerflame"


class LevelPortalShuffle(Toggle):
    """
    When enabled, all level portals (except Glimmer) require a multiworld item to enter their portal (or in the case of boss levels, to open the door leading to them).
    Boss level warps are still accessible from out-of-bounds (since they are handled differently by the game), but will require corresponding tricks to be enabled for logical access.
    """

    display_name = "Level Portal Shuffle"


class GuidebookEntriesAsItems(Toggle):
    """
    When enabled, Guidebok pages for each level are obtainable as items in the multiworld. These items are considered filler.
    If disabled, all Guidebook pages are available from the start.
    """

    display_name = "Guidebook Entries as Items"


class Tricks(OptionList):
    """
    A list of tricks to allow in-logic. Values should match the trick name found here:

    """

    display_name = "Trick Allow List"
    default = []


@dataclass
class Spyro2Options(PerGameCommonOptions):
    goal: Goal
    number_of_orbs: NumberOfOrbs
    percentage_of_orb_hunt_orbs: PercentageOfOrbHuntOrbs

    all_gem_locations: AllGemLocations
    minor_gem_locations: MinorGemLocations
    skill_point_locations: SkillPointLocations
    guidebook_entry_locations: GuidebookEntryLocations
    dragon_shores_token_locations: DragonShoresTokenLocations
    spirit_particle_locations: SpiritParticleLocations
    permanent_powerflame_arch_location: PermanentPowerflameArchLocation

    powerup_pyramids: PowerupPyramids
    level_portal_shuffle: LevelPortalShuffle

    basic_move_randomizer: BasicMoveRandomizer
    randomized_basic_moves: RandomizedBasicMoves
    unlock_move_randomizer: UnlockMoveRandomizer
    randomized_unlock_moves: RandomizedUnlockMoves
    powerup_move_randomizer: PowerupMoveRandomizer
    randomized_powerup_moves: RandomizedPowerupMoves
    double_jump: DoubleJump
    permanent_powerflame: PermanentPowerflame

    guidebook_entries_as_items: GuidebookEntriesAsItems

    tricks: Tricks

    death_link: DeathLink


spyro2_option_groups = [
    OptionGroup(
        "General",
        [
            Goal,
            NumberOfOrbs,
            PercentageOfOrbHuntOrbs,
        ],
    ),
    OptionGroup(
        "Locations",
        [
            AllGemLocations,
            MinorGemLocations,
            SkillPointLocations,
            GuidebookEntryLocations,
            DragonShoresTokenLocations,
            SpiritParticleLocations,
            PermanentPowerflameArchLocation,
        ],
    ),
    OptionGroup(
        "Move Randomizer",
        [
            BasicMoveRandomizer,
            RandomizedBasicMoves,
            UnlockMoveRandomizer,
            RandomizedUnlockMoves,
            PowerupMoveRandomizer,
            RandomizedPowerupMoves,
            DoubleJump,
            PermanentPowerflame,
        ],
    ),
]
