from flask import Flask, render_template, request
import database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home_page.html')


@app.route('/view_notes')
def view_notes():
    notes_data = database.fetch_data()
    return render_template('notes.html', notes_data=notes_data)


@app.route('/add_note', methods=['POST', 'GET'])
def add_note():
    if request.method == 'POST':
        data = request.form
        print(data['date'])
        print(data['message'])
        insert_data = database.insert_data({"date": data["date"], "message": data["message"]})
        print(insert_data)
        notes_data = database.fetch_data()
        return render_template('notes.html', notes_data=notes_data)
    else:
        return render_template('add_note.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
