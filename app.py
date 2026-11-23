from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/survey", methods=["POST", "GET"])
def survey():
    why_lovecat = request.form.get("why_lovecat", "")
    fav_cat = request.form.get("fav_cat", "")
    cats_name = request.form.get("cats_name", "")

    return render_template("survey.html", why_lovecat = why_lovecat, fav_cat = fav_cat, cats_name = cats_name)

# -- type higher --
if __name__ == "__main__":
    app.run(debug=True)
# -- end! --
