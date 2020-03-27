import eikon as ek
import configparser as cp
import pandas as pd


# Set global variables.
cfg = cp.ConfigParser()
cfg.read('eikon_cfg.cfg')
ek.set_app_key(cfg['eikon']['app_id'])


def get_time_series(rics: list, fields: list, start_date, end_date) -> pd.DataFrame:
    """

    Retrieve time series data as Pandas DataFrame.
    :param rics: List of RIC:s to get.
    :param fields: List fields to get.
    :param start_date: Start date of time series.
    :param end_date: End date of time series.
    :return: Pandas DataFrame.
    """
    data = ek.get_timeseries(rics, fields, start_date=start_date, calendar='native',
                             end_date=end_date, interval='daily')
    return data
