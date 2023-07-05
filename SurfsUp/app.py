# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station



#################################################
# Flask Setup
#################################################
app = Flask(__name__)



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
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
def precipitation():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    end_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    start_date = dt.datetime.strptime(end_date, '%Y-%m-%d') - dt.timedelta(days=365)
    data = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date.desc()).filter(Measurement.date>=start_date).all()

    session.close()

    precipitation_dict = [{"date": datum[0], "prcp": datum[1]} for datum in data]

    return jsonify(precipitation_dict)



# Return a JSON list of stations from the dataset.
# @app.route("/api/v1.0/stations")
# def stations():


# # Query the dates and temperature observations of the most-active station for the previous year of data.
# # Return a JSON list of temperature observations for the previous year.
# @app.route("/api/v1.0/tobs")
# def tobs():


# # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
# # For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
# @app.route("/api/v1.0/<start>")
# def start(start):


# # For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
# @app.route("/api/v1.0/<start>/<end>")
# def start_end(start, end):






if __name__ == '__main__':
    app.run(debug=True)