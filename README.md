# Chef AI – Smart Cooking Assistant

Chef AI is an AI-powered cooking assistant that generates meal suggestions based on available ingredients. The project uses LangChain with an API jey from groq.com and provides a Flask-based web interface for interaction.

The system allows users to input ingredients they have at home and receive structured recipe suggestions including meal names, preparation time, and step-by-step instructions.

---

## Features

- AI-generated meal suggestions based on user-provided ingredients
- Flask-based backend API
- Clean and responsive web interface
- Markdown-formatted AI responses rendered in the browser
- Automatic RTL/LTR language detection support
- Structured recipe output including tables and instructions

---

## Technology Stack

- Python
- Flask
- LangChain
- groq
- HTML, CSS, JavaScript

---

## Project Structure


project/
├── app.py

├── agents/

   └── CookingAgent.py

├── templates/
   └── index.html

├── static/
   ├── style.css
   
   └── script.js

├── venv/

├── requirements.txt

└── README.md


---

## How It Works

1. The user enters a list of available ingredients in the web interface.
2. The Flask backend sends the input to a LangChain agent.
3. The agent uses an API key from groq to generate meal suggestions.
4. The response is returned in Markdown format.
5. The frontend renders the response as structured HTML.

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chef-ai.git
cd chef-ai
2. Create virtual environment
python -m venv venv

Activate the environment:

Windows:

venv\Scripts\activate

Linux / Mac:

source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt

4. Start Flask server
python app.py

Then open:

http://127.0.0.1:5000
Environment Variables

If needed, create a .env file for configuration. This file should not be committed to version control.

Future Improvements
Add voice input support
Save favorite recipes
Add user authentication
Deploy the application to cloud platforms
Improve prompt engineering for more accurate recipes
License

This project is open-source and available under the MIT License.
