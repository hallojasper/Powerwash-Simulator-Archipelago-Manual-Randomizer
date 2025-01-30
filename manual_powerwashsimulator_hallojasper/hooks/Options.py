# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class Starting_level(Choice):
    """Choose your starting level, the level must be enabled in the yaml.
    Not all levels are included because no checks would be available with the starting gear in those levels.
    Random_level will give you a random starting level among your enabled levels.
    """
    option_random_level = -1
    option_van = 0
    option_back_garden = 1
    option_playground = 2
    option_detached_house = 3
    option_vintage_car = 4
    option_skatepark = 5
    option_fire_truck = 6
    option_dirt_bike = 7
    option_golf_cart = 8
    option_motorbike_and_sidecar = 9
    option_suv = 10
    option_fire_helicopter = 11
    option_mayors_mansion = 12
    option_tree_house = 13
    option_drill = 14
    option_temple = 15
    option_monster_truck = 16
    option_ferris_wheel = 17
    option_subway_platform = 18
    option_stunt_plane = 19
    option_recreational_vehicle_again = 20

class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    options.update({
        'starting_level': Starting_level
    })
    return options