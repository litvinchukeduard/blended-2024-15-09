from flask import Flask, render_template

app = Flask(__name__)

workouts = [

    {'id': 1, 'title': 'Workout One', 'calories': 2000, 'exercises': [
        {'title': 'Присідання', 'sets': 2, 'reps': 4},
        {'title': 'Віджимання', 'sets': 4, 'reps': 8}
    ]},


    {'id': 2, 'title': 'Workout Two', 'calories': 1000, 'exercises': [
        {'title': 'Віджимання', 'sets': 3, 'reps': 6},
        {'title': 'Присідання', 'sets': 4, 'reps': 8}
    ]}

]

@app.route("/")
def index():
    return render_template('index.html', available_workouts=workouts)
