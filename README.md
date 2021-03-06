# SQLAlchemy Challenge - Surfs Up!

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

![hawaii](https://haleakalaecotours.com/wp-content/uploads/2019/04/hawaii-dangerous-waves.jpg)

## Folders Directory
- [Output_Data](https://github.com/RH-cmd/sqlalchemy-challenge/tree/main/Output_Data) includes saved graphs/analysis for each question saved by PNG
- [Resources](https://github.com/RH-cmd/sqlalchemy-challenge/tree/main/Resources) includes all the datasets used for the analysis. 
- [Climate_starter.ipynb](https://github.com/RH-cmd/sqlalchemy-challenge/blob/main/climate_starter.ipynb) will be the code for Climate Analysis and data exploration in Part 1.
- [app.py](https://github.com/RH-cmd/sqlalchemy-challenge/blob/main/app.py) will be the code for the Climate App (Flask API) in Part 2.

## Part 1 - Climate Analysis and Exploration
Use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


- Use the provided [starter notebook](https://github.com/RH-cmd/sqlalchemy-challenge/blob/main/climate_starter.ipynb) and [hawaii.sqlite](https://github.com/RH-cmd/sqlalchemy-challenge/blob/main/Resources/hawaii.sqlite) files to complete your climate analysis and data exploration.


- Use SQLAlchemy `create_engine` to connect to your sqlite database.


- Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.


- Link Python to the database by creating an SQLAlchemy session.




### Precipitation Analysis


- Start by finding the most recent date in the data set.


- Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. Note you do not pass in the date as a variable to your query.


- Select only the `date` and `prcp` values.


- Load the query results into a Pandas DataFrame and set the index to the date column.


- Sort the DataFrame values by `date`.


- Plot the results using the DataFrame `plot` method.

![Precipitation Analysis](https://github.com/RH-cmd/sqlalchemy-challenge/blob/main/Output_Data/Precipitation_Analysis.png)


- Use Pandas to print the summary statistics for the precipitation data.

![Summary Statistics](https://github.com/RH-cmd/sqlalchemy-challenge/blob/main/Output_Data/Precipitation_Summary_Statistics.png)

### Station Analysis


- Design a query to calculate the total number of stations in the dataset.


- Design a query to find the most active stations (i.e. which stations have the most rows?).


- List the stations and observation counts in descending order.


- Which station id has the highest number of observations?


- Using the most active station id, calculate the lowest, highest, and average temperature.


- Design a query to retrieve the last 12 months of temperature observation data (TOBS).






- Filter by the station with the highest number of observations.


- Query the last 12 months of temperature observation data for this station.


- Plot the results as a histogram with `bins=12`.

![Histogram](https://github.com/RH-cmd/sqlalchemy-challenge/blob/main/Output_Data/Station_Analysis.png)




## Part 2 - Climate App
Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed. 

* Use Flask to create your routes.


### Routes


- `/`

    * Home page.


    * List all routes that are available.




- `/api/v1.0/precipitation`

    * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.


    * Return the JSON representation of your dictionary.



- `/api/v1.0/stations`

    * Return a JSON list of stations from the dataset.



- `/api/v1.0/tobs`


    * Query the dates and temperature observations of the most active station for the last year of data.


    * Return a JSON list of temperature observations (TOBS) for the previous year.




- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`


    * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.


    * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.


    * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.





