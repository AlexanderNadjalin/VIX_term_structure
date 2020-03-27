"""
Get RIC:s (.VIX9D, .VIX, .VIX3M, .VIX1Y, .SPX) for historical dates (T-1, T-2, T-5, T-21, T-63, T-252).
Plot term structure.

"""

import eikon_data_import as edi
import eikon.tools as ekt
import plotting


if __name__ == '__main__':
    symbols = ['.VIX9D', '.VIX', '.VIX3M', '.VIX1Y', '.SPX']
    fields = ['CLOSE']

    # Get time series as pandas dataframe.
    df_ts = edi.get_time_series(symbols,
                                fields,
                                start_date=ekt.get_date_from_today(365).date().isoformat(),
                                end_date=ekt.get_date_from_today(1).date().isoformat())

    # Slice for 6 historical dates.
    l = len(df_ts.index) - 1
    df_vix = df_ts.iloc[[l, l - 1, l - 5, l - 21, l - 63, 0], 0:4]

    # Plot.
    plotting.dual_plot(df_vix, df_ts)
