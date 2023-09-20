"""Python script to read csv file, 
    generate statistics summary 
        and plot interested columns """
import matplotlib.pyplot as plt
import lib


def pandas_ds():
    """Read csv file,
    generate statistics summary
        and plot interested columns"""

    # Read csv file
    data = lib.read_csv_file("world-small.csv")
    # convert column to integer
    data["gdppcap08"] = data["gdppcap08"].astype("int")

    # scatter plot visualization
    data.plot.scatter(x="gdppcap08", y="polityIV", alpha=0.5)
    plt.savefig("plot.png")
    # plt.show()

    # return statistics summary
    summary = lib.generate_statistics_summary(data[["gdppcap08", "polityIV"]])
    print(summary)
    return summary


if __name__ == "__main__":
    pandas_ds()
