import math

from autotraders.ship.states import FlightMode


def travel_fuel(distance, mode) -> int:
    if mode == FlightMode.CRUISE:
        return round(distance)
    elif mode == FlightMode.DRIFT:
        return 1
    elif mode == FlightMode.BURN:
        return 2 * round(distance)
    elif mode == FlightMode.STEALTH:
        return round(distance)


multiplier = {
    FlightMode.CRUISE: 25,
    FlightMode.DRIFT: 250,
    FlightMode.BURN: 12.5,
    FlightMode.STEALTH: 30
}


def travel_time(distance, ship_speed, mode) -> int:
    return round(round(max(1, distance)) * multiplier[mode] / ship_speed + 15)


"""
Take the following multipliers with a grain of salt. They have not been confirmed yet by the community and might be wrong.
"""
warp_multiplier = {
    FlightMode.CRUISE: 50,
    FlightMode.DRIFT: 300,
    FlightMode.BURN: 25,
    FlightMode.STEALTH: 60
}


def travel_time_warping(distance, ship_speed, mode) -> int:
    return round(round(max(1, distance)) * warp_multiplier[mode] / ship_speed + 15)


def distance(*args) -> int:
    """
    If there is one arg, then the arg should be a iterable of length 2 or 4.
    It will be expanded and used as a 2 or 4 arg.
    If there are 2 args, then they should both have x and y attributes
    if there are 4 args they should be in the format x_1, y_1, x_2, y_2

    :return: The euclidian distance between the two objects.
    """
    if len(args) == 1:
        return distance(*args)
    elif len(args) == 2:
        return distance(
            getattr(args[0], "x"),
            getattr(args[0], "y"),
            getattr(args[1], "x"),
            getattr(args[1], "y"),
        )
    else:
        return round(math.sqrt((args[0] - args[2]) ** 2 + (args[1] - args[3]) ** 2))
