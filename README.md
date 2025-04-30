# Message-Analyzer

A Django project that uses Google's **Gemini Pro API** to analyze the **tone** and **intent** of user-submitted messages. The analysis is stored in a PostgreSQL database, and relevant action suggestions are returned based on the message context.

---

## ⚙️ Features

- 🔍 Analyze user input with Google Gemini LLM
- 🧠 Detect **tone** and **intent** from natural language messages
- 💾 Store analysis results in PostgreSQL
- 💡 Generate action suggestions based on detected intent

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 1. Install requirements.txt
```
pip install -r requirements.txt
```
### 3. Set Up Environment Variables
```
GOOGLE_API_KEY=your_google_ai_studio_api_key
```
### 4. Run Migrations
```
python manage.py migrate
```

### 5. Run Server
```
python manage.py runserver
```

## API Endpoint
```
POST /api/analyze/
```
## LLM Provider
Google Gemini API

