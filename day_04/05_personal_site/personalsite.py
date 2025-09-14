from flask import Flask, render_template

app = Flask(__name__)
todo_items = ['do laundry', 'eat cereal', 'throw milk']

@app.route("/")
def index():
    #return "Index Page"
    # Introduce yourseld
    return render_template("index.html")

@app.route("/hobby/")
@app.route("/hobbies/")
def Hobby():
    return "Hobby Page"


@app.route("/opinion/")
@app.route("/opinions/")
def Opinion():
    return "/opinion/"

@app.route("/food/")
def Food():
    #return "/opinion/"

    foods = ["dumpling", "chocolate", "Ebi Tempura"]
    return render_template("food.html", foods=foods)

@app.route("/skill/")
def Skill():
    skill_level = {
        "Speaking English": "Average",
        "Writing English": "Average",
        "Driving": "Will make sure you will arrive alive and in complete body parts",
        "Manual Installation": "Great",
    }

    return render_template("skill.html", skills=skill_level )

@app.get("/todo/")
def get_todo()
    return render_template('todo_list'
                           '')

app.run()
