from flask import Flask, render_template
from jinja2 import TemplateNotFound
from .app_logger import AppLogger 

"""
Main application file for the backend server.
Sets up the Flask app to serve the web interface directly from the frontend directory, 
and handles basic routing with safe error logging.
"""

# App logger
log = AppLogger().logger

# Initialize Flask application
app = Flask(__name__,    template_folder="../frontend/templates", static_folder="../frontend/static", static_url_path="/static")

# Route for the index page
@app.route("/")
def index():
     
     try:
        log.info("Attempting to load index page ...")
        # Render the app's main HTML entrypoint
        return render_template("index.html")

     except TemplateNotFound:
         # Triggers if Flask can't find the HTML file in the frontend folder
         log.error("Missing file: index.html not found in frontend folder!")
         return "Sorry, index.html file is missing!"
         
     except Exception as error:
        # Final safety net for any other server crashes
        log.error(f"Unexpected Error: {error}")
        return "Sorry, something went wrong! Check back later."

# Production servers will completely ignore this block!
# It only triggers when running the app locally for development on your network.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True )