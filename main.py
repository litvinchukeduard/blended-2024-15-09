import json
import asyncio
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__, static_folder='static')

workout_file = 'data.json'

lock = asyncio.Lock()

async def write_workouts_to_file():
    with open(workout_file, 'w', encoding='utf-16') as file:
        json.dump(workouts, file)

async def read_workouts_from_file():
    with open(workout_file, 'r', encoding='utf-16') as file:
        return json.load(file)

workouts = asyncio.run(read_workouts_from_file())

@app.route("/")
async def index():
    return render_template('index.html', available_workouts=workouts)

@app.route("/add-workout", methods=['GET', 'POST'])
async def add_workout():
    if request.method == 'GET':
        return render_template('add_workout.html')
    elif request.method == 'POST':
        title = request.form['title']
        calories = request.form['calories']
        new_workout = {'title': title, 'calories': calories, 'exercises': []}
        workouts.append(new_workout)

        await lock.acquire()
        try:
            await write_workouts_to_file()
        finally:
            lock.release()
            
        # return render_template('index.html', available_workouts=workouts) # TODO: Fix to redirect
        return redirect(url_for('index'))
    
