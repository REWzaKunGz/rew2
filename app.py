from flask import Flask, request, render_template
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1430032843664392285/jSQpCp6bVM-p1Yz12wzBB0F_yqmAz70G1G3MRO9hpcTHoimaimkUSvvmX99OzpGYH8_O"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    # ส่งไฟล์ไปยัง webhook
    files = {'file': (file.filename, file.stream, file.mimetype)}
    response = requests.post(WEBHOOK_URL, files=files)

    if response.status_code == 200 or response.status_code == 204:
        return "Uploaded successfully!"
    else:
        return f"Failed to upload. Status code: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
