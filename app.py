from flask import Flask, render_template, request, redirect
import hashlib
from datetime import datetime

app = Flask(__name__)

tasks = []


def hash_task(text):
    return hashlib.sha256(text.encode()).hexdigest()


@app.route('/')
def index():
    total_tasks = len(tasks)
    latest_task = tasks[-1]['text'] if tasks else "No tasks yet"

    return render_template(
        'index.html',
        tasks=tasks,
        total_tasks=total_tasks,
        latest_task=latest_task
    )


@app.route('/add', methods=['POST'])
def add():
    task_text = request.form['task']

    task = {
        "text": task_text,
        "hash": hash_task(task_text),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(task)
    return redirect('/')


@app.route('/delete/<int:index>')
def delete(index):
    if index < len(tasks):
        tasks.pop(index)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
