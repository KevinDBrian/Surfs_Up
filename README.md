# Surfs_Up

## Resources:
*   Software:
    *   Anaconda 4.11.0
    *   Jupyter Notebook 6.4.5
    *   Python 3.9.7
    *   Visual Studio Code 1.63.2
    *   Flask (Python Web Framework)
    *   Python Libraries
        *   Pandas
        *   NumPy
        *   SQLAlchemy
        *   datetime
*   Resources:
    *   hawaii.sqlite

## Overview/Purpose:

The goal of this analysis was to use advanced data storage to extract and visualize temperature trends in June and December on the island of O'auh. This is for use with a business plan to open a Surf Shop that also serves ice cream. This analysis will help determine if the business can operate viably all year vs seasonally.

## Results:

Using `sqlalchemy` I was able to generate a query session with the local database, `hawaii.sqlite`, to extract temp data specifically for the months of June and December. After retrieving the data, they were converted to lists then DataFrames to be easily read. 

The `june_temps_df` had 1,700 data points and the `dec_temps_df` had 19,550 data points.

![](images/june_temps_df.png)
![](images/dec_temps_df.png)

Lastly, using the `.describe()` method on the DataFrames, I was able to find all relevant statistics pertaining to the temps during these months.

![](images/june_temps_df.describe().png)
![](images/dec_temps_df.describe()png.png)

## Summary:

There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December. (5 pt)

The finding shows that the island of O'auh would appear to be a suitable location for the business to operate all year, when considering the consistency of high temperatures. The average temperatures between June and December differ by less than 2<sup>o</sup>F and both were greater than 73<sup>o</sup>F. This means that the time of year (Summer v Winter) does not have a significant enough change to the climate that surfing and ice cream would not be a possible at any time, give or take the occasional cold day that can occur at any point regardless of time of year.

A few additional queries would be helpful to get more accurate data.

1. There is nearly 10 time more data from the month of December compared to June. Gathering more data from the summer months might be helpful to get a more complete picture of what temperatures to expect.

2. While there are numerous data points from December, taking in data from of January may show a more accurate picture of what winter temps look like on the island. December is an early winter month, so getting data from January may reveal the coldest days of the year (i.e. when the possibility of the business slowing would be at its highest chance).