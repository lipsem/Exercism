"""Functions to help the company calculate their power usage."""


def get_extra_hours(hours):
    """Return the amount of hours.

    :param: hours: int - amount of hours.
    :return: int - amount of "extra" hours.
    """
    new_hours = hours + 3
    extra_hours = new_hours % 24
    return extra_hours


def get_kW_value(watts):
    """Return the kW value of a given watt value.

    :param: watts: int - watt value.
    :return: float - kW value.
    """
    kw = watts * 1000
    return round(kw, 1)


def get_kwh_value(watts):
    """Return the kWh value of a given watt value and hours.

    :param: watts: int - watt value.
    :param: hours: int - kilowatt hour value.
    """
    return int(watts * 1000 / 3600)


def get_efficiency(power_factor):
    """Return the efficiency calculated from the power factor.

    :param: power_factor: float.
    :return: float - efficiency.
    """
    return power_factor / 100
    pass


def get_cost(watts, power_factor, price):
    """Calculate the cost of a given kWh value, efficiency and price.

    :param: watts: int - watt value.
    :param: power_factor: float - efficiency.
    :param: price: float - price of kWh.
    :return: float - cost of kWh.
    """
    kwh = get_kwh_value(watts)
    efficiency = get_efficiency(power_factor)
    return kwh / efficiency * price

