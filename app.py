# Import Flask
from flask import Flask, jsonify

#Setup dependecies
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Declare variable for queries latier
date_2016 = '2016-08-23'
most_active_station = 'USC00519281'

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return """<html>


    <h1>Climate App</h1>
    <br>
    <p><strong>All Available Routes:</strong></p>

  <ul>
    <li>Preciptation Observations: <a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a></li>
    <br>
    <li>Stations Analysis: <a href="/api/v1.0/stations">/api/v1.0/stations</a></li>
    <br>
    <li>Temperature Observations: <a href="/api/v1.0/tobs">/api/v1.0/tobs</a></li>
    <br>
    <li>Start Day: <a href="/api/v1.0/2016-08-23">/api/v1.0/2016-08-23</a></li>
    <br>
    <li>Start and End Day: <a href="/api/v1.0/2016-08-23/2017-08-23">/api/v1.0/2016-08-23/2017-08-23</a></li>
  </ul>
    
    </html>
    """

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation observations """
    # Query all precipitation observations between 8/23/16 to 8/23/17
    precipitation_query = session.query(Measurement.date, Measurement.prcp).\
                        filter(Measurement.date >= date_2016).\
                        order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    all_precip_data = list(np.ravel(precipitation_query))

    return jsonify(all_precip_data)

# Stations Route
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of unique stations """
    # Query all the station names 
    all_stations_query = session.query(Station.station).all()

    session.close()

    # Convert list into JSON
    return jsonify(all_stations_query)

# Tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of dates and temperature observations of the most active station: USC00519281 """
    # Query all temperature observations for the most active station between 8/23/16 to 8/23/17
    tobs_query = session.query(Measurement.date, Measurement.tobs).\
                            filter(Measurement.station == most_active_station).\
                            filter(Measurement.date >= date_2016).all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs_data = list(np.ravel(tobs_query))

    return jsonify(all_tobs_data)

# Start Day Route
@app.route("/api/v1.0/<start>")
def start_day(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of the minimum temperature, the average temperature, and the max temperature for a given start date"""
    #Use the start date: 2016-08-23 for the app home page
    start_day_query = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start).\
                    group_by(Measurement.date).all()
    
    session.close()
    
    # Convert list of tuples into normal list
    start_day_data = list(np.ravel(start_day_query))

    return jsonify(start_day_data)

# Start Day Route
@app.route("/api/v1.0/<start>/<end>")
def start_end_day(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of the minimum temperature, the average temperature, and the max temperature for a given start date and end date range"""
    #Use the start date: 2016-08-23 and end date: 2017-08-23 for the app home page
    start_end_day_query = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start).\
                    filter(Measurement.date <= end).\
                    group_by(Measurement.date).all()
    
    session.close()
    
    # Convert list of tuples into normal list
    start_end_day_data = list(np.ravel(start_end_day_query))

    return jsonify(start_end_day_data)

if __name__ == '__main__':
    app.run(debug=True)