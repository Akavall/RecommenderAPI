from app import app
from flask import render_template, request
import StringIO
import pandas as pd 

from models.svd import SVD_Model
from recommender import Recommender

recommender_obj = Recommender()

@app.route("/recommender")

def recommender():
    return render_template('index.html')

# 1) Create upload function
# that creates a data array

# 2) Create compute function
# that operates on that array 
# and uploads the result 

@app.route("/upload", methods=["POST"])

def upload():
    # It seems that I need to modify a mutable object here
    print "uploading"
    raw_data = request.form.keys()[0]
    f = StringIO.StringIO(raw_data)
    my_df = pd.read_csv(f)
    print "upload finished, initializing"
    recommender_obj.initialize_matrices(my_df)

    print recommender_obj.actions

    svd_model = SVD_Model(recommender_obj.actions, 3)
    scores = svd_model.calc_scores()

    print scores
    recommender_obj.make_recs(scores, 3)

    print recommender_obj.recs

    return "Upload Successful and Initialization Successfull"

@app.route("/compute", methods=["GET"])

def compute():
    print "Computing Recommendations"
    svd_model = SVD_Model(recommender_obj.actions, 3)
    scores = svd_model.calc_scores()

    n_recs = int(request.args.get("n_recs"))
    print scores
    recommender_obj.make_recs(scores, n_recs)

    print recommender_obj.recs
    recommender_obj.convert_recs_to_csv_string()
    print recommender_obj.csv_string_recs

    return recommender_obj.csv_string_recs
    
