
from flask import Flask, render_template


# ---------------------------------------------------------
# 1. APPLICATION CONFIGURATION
# ---------------------------------------------------------

app = Flask(__name__)


# ---------------------------------------------------------
# 2. HOME PAGE
# ---------------------------------------------------------

@app.route("/")
def home():
    return render_template("Diogo's Personal Site.html")


# ---------------------------------------------------------
# 3. RUN APPLICATION
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
