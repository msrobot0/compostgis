from flask import Flask, render_template
import gunicorn
app = Flask(__name__, template_folder='templates')
@app.route('/')
def index():
    markers=[
        {
        'lat':0,
        'lon':0,
        'popup':'This is the middle of the map.'
        }
   ]
   return render_template('index.html',markers=markers)
