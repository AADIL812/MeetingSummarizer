import React, { useState } from "react";
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) return alert("Please upload a file");

    setLoading(true);
    setResult(null); // Clear previous results
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:5000/upload", formData);
      // Assuming the backend returns an object like: { transcript: "...", summary: "..." }
      setResult(res.data);
    } catch (error) {
      alert("Analysis failed. Please check the console for details.");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>🧠 AI Meeting Extractor</h1>
      <p>Upload your meeting audio and get an instant transcript, summary, and action items.</p>
      
      <div className="upload-section">
        <input 
          type="file" 
          accept="audio/*" 
          onChange={(e) => {
            setFile(e.target.files[0]);
          }} 
        />
        <button onClick={handleUpload} disabled={!file || loading}>
          {loading ? "Analyzing..." : "Upload & Analyze"}
        </button>
      </div>
      
      {loading && <div className="loader"></div>}
      
      {result && (
        <div className="results-container">
          {/* --- Transcript Section --- */}
          <section className="result-section">
            <h2>Transcript</h2>
            <div className="result-content transcript-box">
              <p>{result.transcript}</p>
            </div>
          </section>

          {/* --- Summary Section --- */}
          <section className="result-section">
            <h2>AI Summary & Analysis</h2>
            <div className="result-content summary-box">
              {/* Using <pre> for better formatting of multi-line AI output */}
              <pre>{result.analysis}</pre>
            </div>
          </section>
        </div>
      )}
    </div>
  );
}

export default App;