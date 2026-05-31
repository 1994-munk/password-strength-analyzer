markdown# 🔐 Password Strength Analyzer

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-teal?style=flat-square&logo=flask)
![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=flat-square&logo=render)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Live-success?style=flat-square)

> Entropy-based password evaluation + cryptographically secure password generator built with Flask.

🌐 **Live Demo**: [https://your-app.onrender.com](https://password-strength-analyzer-k0yn.onrender.com/)

---

## ✨ Features

- 🔢 **Entropy Estimation** — calculates bits of entropy using `L × log₂(N)`
- 📊 **Visual Strength Meter** — color-coded bar from weak to strong
- ⚡ **Password Generator** — cryptographically secure via Python's `secrets` module
- 💬 **Smart Feedback** — specific, actionable tips to improve any password
- 📋 **One-click Copy** — instantly copy generated passwords to clipboard

---

## 🧠 How Entropy Works
Entropy (bits) = L × log₂(N)
L = password length | N = character pool size

| Entropy     | Rating      |
|-------------|-------------|
| < 28 bits   | Very Weak   |
| 28–36 bits  | Weak        |
| 36–60 bits  | Moderate    |
| 60–128 bits | Strong      |
| 128+ bits   | Very Strong |

> 💰 **quote:**
> *"The application evaluates password strength using character class detection and Shannon entropy estimation, providing users with a quantitative security rating alongside qualitative feedback."*

---

## 🛠️ Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python 3.11, Flask 3.0  |
| Security   | `secrets` module (cryptographically secure RNG) |
| Frontend   | HTML, CSS, Vanilla JS   |
| Server     | Gunicorn (WSGI)         |
| Deployment | Render                  |

---

## 📁 Project Structure
password-strength-analyzer/
├── app.py              ← Flask app, entropy logic, password generator
├── requirements.txt    ← Flask + Gunicorn
├── render.yaml         ← Render deployment config
├── templates/
│   └── index.html      ← Jinja2 UI template
└── static/
└── style.css       ← Styling

---

## ⚙️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/password-strength-analyzer
cd password-strength-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python app.py

# 4. Visit
# http://127.0.0.1:5000
```

---

## 🌍 Deploy on Render

1. Push code to GitHub
2. Go to [render.com](https://render.com) → **New + → Web Service**
3. Connect your GitHub repo
4. Set start command: `gunicorn app:app`
5. Click **Deploy** — your live URL will be:
https://your-app.onrender.com

---

## 🔒 Cybersecurity Concepts Demonstrated

- **Shannon entropy estimation** — quantifying password unpredictability in bits
- **Character class analysis** — detecting use of uppercase, lowercase, digits, symbols
- **Cryptographically secure generation** — using `secrets` instead of `random`
- **Security UX** — actionable feedback rather than just pass/fail ratings

---

## 👩‍💻 Author

**Shirleen Gatu**
[GitHub](https://github.com/1994-munk) · [LinkedIn](https://www.linkedin.com/in/shirleengatu/)

---

## 📄 License

MIT — fork it, use it, make it yours.