from flask import Flask, request, jsonify
from youtube_dl import YoutubeDL

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'hello': 'data'}), 200

@app.route('/download_url', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return jsonify({'error':'Use POST and pass video-url'}), 200
    if request.method == 'POST':
        video = request.form['video-url']
        data = {}
        with YoutubeDL(youtube_dl_opts) as ydl:
            info_dict = ydl.extract_info(video, download=False)
            for i in info_dict['formats']:
                data[i['format_id']] = i['url']
        print(data["22"])
        return jsonify(data),200

if __name__ == "__main__":
    app.run()