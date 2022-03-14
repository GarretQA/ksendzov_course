import numpy as np
import pandas as pd


def random_datetimes_or_dates(start, end, n, out_format='datetime'):
    """
    unix timestamp is in ns by default.
    I divide the unix time value by 10**9 to make it seconds (or 24*60*60*10**9 to make it days).
    The corresponding unit variable is passed to the pd.to_datetime function.
    Values for the (divide_by, unit) pair to select is defined by the out_format parameter.
    for 1 -> out_format='datetime'
    for 2 -> out_format=anything else
    """
    (divide_by, unit) = (10 ** 9, 's') if out_format == 'datetime' else (24 * 60 * 60 * 10 ** 9, 'D')

    start_u = start.value // divide_by
    end_u = end.value // divide_by

    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit=unit)
