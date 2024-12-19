from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data Dummy untuk Simulasi
logs = [
    {"id": 1, "time": "2024-12-13 10:30:00", "attack": "SQL Injection", "source": "192.168.1.10", "action": "Blocked"},
    {"id": 2, "time": "2024-12-12 14:22:00", "attack": "DDoS", "source": "203.0.113.5", "action": "Mitigated"},
]
config = {
    "signatures": ["SQL Injection", "DDoS", "Cross-Site Scripting"],
    "sensitivity": "Medium",
}
stats = {
    "total_attacks": 56,
    "detection_speed": "0.5 seconds",
    "accuracy": "98.5%",
}

@app.route('/')
def main_menu():
    return render_template('main_menu.html', stats=stats)

@app.route('/logs')
def view_logs():
    return render_template('logs.html', logs=logs)

@app.route('/config', methods=['GET', 'POST'])
def configure_ids():
    if request.method == 'POST':
        config['sensitivity'] = request.form.get('sensitivity')
        new_signature = request.form.get('new_signature')
        if new_signature:
            config['signatures'].append(new_signature)
        return redirect(url_for('configure_ids'))
    return render_template('config.html', config=config, stats=stats)

@app.route('/stats')
def view_stats():
    return render_template('stats.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
