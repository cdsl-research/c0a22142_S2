from flask import Flask, render_template_string, request, redirect
from datetime import datetime
import csv
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>出席管理システム（日付別）</title>
</head>
<body>
    <h1>出席管理システム（日付別）</h1>
    <h3>{{ today }} の出席登録</h3>

    <form action="/submit" method="post">
        <label>名前：</label>
        <input type="text" name="name" required>
        <button type="submit">出席</button>
    </form>

    <h2>本日の出席一覧</h2>
    <ul>
        {% for name, time in records %}
            <li>{{ name }} - {{ time }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

def get_csv_filename():
    date_str = datetime.now().strftime('%Y%m%d')
    return f"attendance_{date_str}.csv"

def load_records():
    filename = get_csv_filename()
    if not os.path.exists(filename):
        return []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        return list(reader)

def save_record(name):
    filename = get_csv_filename()
    time_str = datetime.now().strftime('%H:%M:%S')
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, time_str])

@app.route('/')
def index():
    records = load_records()
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template_string(HTML, records=records, today=today)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    save_record(name)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
