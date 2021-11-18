from application import app, db
from application.models import Tasks
from datetime import date, timedelta



@app.route('/tasks')

def view():
    tasks = Tasks.query.all()
    return '<br>'.join([f'Task {task.id}: ' + task.name +'||' + task.desc + '||' + str(task.due) + '||' + task.status] for task in tasks)



@app.route('/add/<name>&<desc>')

def add(name, desc):
    duedate = date.today() + timedelta(days=14)
    newtask = Tasks(name=name.lower(), desc=desc, status = 'todo', due = duedate)
    db.session.add(newtask)
    db.session.commit()
    return "New task added"

@app.route('/update/<id>&<ustatus>')

def upd(id, ustatus):
    task = Tasks.query.get(id)
    task.status = ustatus 
    db.session.commit()
    return "Task status updated"


