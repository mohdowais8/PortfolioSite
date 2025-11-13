from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Backend console me message print hoga
    print(f"Message from {name} ({email}): {message}")

    # Agar chahe, yaha email bhejne ka code add kar sakte ho
    return jsonify({"status": "success", "msg": "Message sent successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
