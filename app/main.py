# main.py

from flask import Flask, render_template, request
from alert_system import generate_alerts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alerts', methods=['POST'])
def alerts():
    current_location = request.json['current_location']
    data = request.json['data']
    alerts = generate_alerts(current_location, data)
    return {'alerts': alerts}

if __name__ == '__main__':
    app.run(debug=True)
