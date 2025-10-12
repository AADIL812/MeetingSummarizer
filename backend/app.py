from flask import Flask,request,jsonify
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
from whisper_utils import transcribe_audio
from gpt_utils import analyze_meeting
app=Flask(__name__)
CORS(app)
upload_folder='uploads'
os.makedirs(upload_folder,exist_ok=True)

@app.route('/upload',methods=['POST'])
def upload_audio():
    file=request.files['file']
    filename=secure_filename(file.filename)
    filepath=os.path.join(upload_folder,filename)
    file.save(filepath)
    transcript=transcribe_audio(filepath)
    result=analyze_meeting(transcript)

    return jsonify({
        "transcript":transcript,
        "analysis":result
    })

if __name__=='__main__':
    app.run(debug=True)