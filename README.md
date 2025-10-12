🧠 AI Meeting Summarizer \n
This is a full-stack application designed to transcribe and summarize your meeting audio files using the power of AI. Simply upload an audio file, and the application will provide you with a complete transcript, a concise summary, a list of action items, and even a draft for a follow-up email.

✨ Features
Audio File Upload: Easily upload your meeting recordings in various audio formats.

Automatic Transcription: Utilizes OpenAI's Whisper to generate an accurate and detailed transcript of your meeting.

AI-Powered Analysis: Leverages Google's FLAN-T5 model to provide a comprehensive analysis, including:

A summary of the key discussion points.

A list of all action items and assigned individuals.

A summary of all decisions made during the meeting.

A concise follow-up email draft to send to all participants.

User-Friendly Interface: A clean and intuitive interface built with React to make the process seamless and straightforward.

🚀 Tech Stack
Frontend:

React

Vite

Axios

Backend:

Flask

Python

OpenAI Whisper

Hugging Face Transformers

🛠️ Setup and Installation
To get the project up and running on your local machine, follow these steps:

Backend
Navigate to the Backend Directory:

Bash

cd backend
Install Python Dependencies:
It is recommended to use a virtual environment to manage your dependencies.

Bash

pip install Flask Flask-Cors whisper transformers
Run the Flask Server:

Bash

python app.py
The backend server will now be running on http://localhost:5000.

Frontend
Navigate to the Frontend Directory:

Bash

cd frontend
Install Node.js Dependencies:

Bash

npm install
Start the Development Server:

Bash

npm run dev
The frontend application will now be running on http://localhost:5173.

Usage
Open the Application: Open your web browser and navigate to http://localhost:5173.

Upload an Audio File: Click on the "Choose File" button to select the audio file of the meeting you want to analyze.

Analyze the Meeting: Click the "Upload & Analyze" button to begin the transcription and analysis process.

View the Results: Once the analysis is complete, the full transcript and the AI-generated summary will be displayed on the screen.
