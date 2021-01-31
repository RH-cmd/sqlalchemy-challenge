import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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

# Variable for dates
date_2016 = '2016-08-23'

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

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

    """Return a list of the most active sessions """
    # Query all precipitation observations between 8/23/16 to 8/23/17
    tobs_query = session.query(Measurement.station, func.count(Measurement.station)).\
                                group_by(Measurement.station).\
                                order_by(func.count(Measurement.station).desc()).all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs_data = list(np.ravel(tobs_query))

    return jsonify(all_tobs_data)


if __name__ == '__main__':
    app.run(debug=True)