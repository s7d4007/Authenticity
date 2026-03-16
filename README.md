# Authenticity

A modern web application for checking the safety and authenticity of URLs using Google's Safe Browsing API.

## Overview

Authenticity helps users evaluate whether a link is safe to visit by scanning it against multiple security databases in real-time. It detects malware, phishing scams, unwanted software, and other potential threats.

## Tech Stack

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Font Awesome](https://img.shields.io/badge/Font%20Awesome-339AF0?style=flat&logo=fontawesome&logoColor=white)
![Google Fonts](https://img.shields.io/badge/Google%20Fonts-4285F4?style=flat&logo=google&logoColor=white)

### Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Flask-CORS](https://img.shields.io/badge/Flask--CORS-000000?style=flat&logo=flask&logoColor=white)

### APIs & Services
![Google Safe Browsing v5](https://img.shields.io/badge/Google%20Safe%20Browsing%20v5-4285F4?style=flat&logo=google&logoColor=white)

## Features

- **Malware Detection**: Scans links for known malware, viruses, and trojans
- **Anti-Phishing**: Identifies phishing scams designed to steal credentials
- **Privacy Check**: Detects excessive trackers and data breach history
- **Real-time Analysis**: Checks links against multiple security databases
- **Simple Interface**: User-friendly design for quick URL verification
- **Dynamic UI**: Responsive result cards with clear threat indicators

## Project Structure

```
Authenticity/
├── index.html           # Main HTML file with UI structure
├── style.css            # Styling and responsive design
├── script.js            # Frontend logic and API communication
├── backend/
│   ├── app.py           # Flask backend server
│   └── requirements.txt  # Python dependencies
├── LICENSE              # Project license
└── README.md            # Project documentation
```

## Installation & Setup

### Prerequisites
- Python 3.x
- pip package manager
- Google Safe Browsing API Key

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your Google Safe Browsing API key:
   ```
   GOOGLE_SAFE_BROWSING_API_KEY=your_api_key_here
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```
   The server will start on `http://localhost:5000`

### Frontend Setup

1. Open `index.html` in a web browser or serve it using a local server:
   ```bash
   # Using Python's built-in server
   python -m http.server 8000
   ```

2. Access the application at `http://localhost:8000`

## How It Works

1. **User Input**: Paste a URL into the search box
2. **API Request**: Frontend sends the URL to the Flask backend
3. **Google Safe Browsing Check**: Backend checks the URL against Google's threat database
4. **Response Processing**: Backend processes the threat data and returns results
5. **Display Results**: Frontend displays a clear report with threat indicators

## API Endpoints

### POST `/api/check-url`
Checks a URL for threats

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "status": "safe|dangerous|error",
  "title": "Result Title",
  "message": "Detailed message about the URL"
}
```

## Dependencies

### Python Packages
- `requests` - HTTP library for API communication
- `flask` - Web framework for backend server
- `flask-cors` - Enable CORS for cross-origin requests
- `python-dotenv` - Load environment variables from `.env` file

## Browser Support

- Chrome (Latest)
- Firefox (Latest)
- Safari (Latest)
- Edge (Latest)

## License

This project is licensed under the terms specified in the LICENSE file.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Author

Created by Souvik Dutta

## Disclaimer

This tool is for informational purposes only. Always use caution when visiting unfamiliar websites and maintain up-to-date security practices.
