from flask import Flask, render_template
import gunicorn
app = Flask(__name__, template_folder='templates')
@app.route('/')
def index():
   markers=[
        {
        'lat':40.7,
        'lon':-73.9,
        'popup':'This is nyc.'
        }
   ]
   return render_template('index.html',markers=markers)
