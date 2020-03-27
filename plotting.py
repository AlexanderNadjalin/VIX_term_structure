import matplotlib.pyplot as plt


def dual_plot(df_vix, df_idx) -> None:
    """
    Plots two plots. Generic function to be used with various time series contents.
    :param df_vix: Pandas dataframe with vix data.
    :param df_idx: Pandas dataframe with SP500 data.
    :return: None.
    """

    fig, axes = plt.subplots(2, 1, figsize=(10, 7))
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)

    df_vix.iloc[0:, ].plot(lw=1, alpha=0.60, ax=ax1, legend=True)

    df_idx.iloc[:, 4].plot(lw=1, color='blue', alpha=0.60, ax=ax2, label='SPX')

    ax1.minorticks_on()
    ax1.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    ax1.grid(b=True, which='major', color='#999999', linestyle='-', alpha=0.4)
    ax1.set_ylabel('Volatility (%)')
    ax1.set_xlabel('')
    ax1.set_title('VIX volatility term structure')
    ax1.legend(loc='best', prop={'size': 8})
    plt.setp(ax1.get_xticklabels(), visible=True, rotation=45, ha='center')

    ax2.minorticks_on()
    ax2.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    ax2.grid(b=True, which='major', color='#999999', linestyle='-', alpha=0.4)
    ax2.set_ylabel('Index value')
    # ax2.set_xlabel(x_labels[1])
    ax2.set_title(''.join('S&P500'))
    ax2.legend(loc='best', prop={'size': 8})
    plt.setp(ax2.get_xticklabels(), visible=True, rotation=45, ha='center')

    fig.tight_layout()
    plt.show()
