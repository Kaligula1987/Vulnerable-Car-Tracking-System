from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)

# Vulnerable API endpoint to return file contents (LFI)
@app.route('/api/cars', methods=['GET'])
def get_cars():
    file = request.args.get('file', default='cars.json', type=str)  # LFI here
    try:
        with open(file, 'r') as f:
            file_content = f.read()
        return jsonify({"data": file_content}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Frontend route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
