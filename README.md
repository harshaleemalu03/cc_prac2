# ☁️ Cloud Computing Practical 2

## Installation and Configuration of Google App Engine

---

## 🎯 Aim

To install and configure Google App Engine (GAE) and deploy a simple Python web application on the cloud platform.

---

## 🛠 Tools & Technologies Used

* Python 3.11
* Flask Framework
* Gunicorn
* Google Cloud Platform (GCP)
* Google App Engine (Standard Environment)

---

## 📁 Project Structure

```
building-an-app/
│
├── app.yaml
├── main.py
├── requirements.txt
│
├── static/
│   ├── script.js
│   └── style.css
│
└── templates/
    └── index.html
```

---

## 📋 Prerequisites

Before starting the practical, ensure:

* Python (3.10 or above) is installed
* Google account is available
* Internet connection
* Basic knowledge of terminal/command prompt

---

## 🔽 Step 1: Install Google Cloud SDK

1. Download Google Cloud SDK from:
   https://cloud.google.com/sdk/docs/install

2. Install it according to your operating system.

3. Verify installation:

```bash
gcloud --version
```

---

## 🔑 Step 2: Initialize Google Cloud

Login to your Google account:

```bash
gcloud auth login
```

Initialize configuration:

```bash
gcloud init
```

Select:

* Your Google account
* Create a new project or select existing project
* Choose region

---

## ☁️ Step 3: Enable App Engine

Create App Engine application:

```bash
gcloud app create
```

Select region (example: asia-south1 for India).

---

## 🐍 Step 4: Install Python Dependencies

Navigate to project folder:

```bash
cd building-an-app
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Step 5: Run Application Locally

```bash
python main.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🚀 Step 6: Deploy to Google App Engine

Deploy application:

```bash
gcloud app deploy
```

After deployment, open app in browser:

```bash
gcloud app browse
```

---

## 📄 Description of Files

* **main.py** → Flask backend application
* **app.yaml** → Configuration file for App Engine
* **requirements.txt** → Python dependencies
* **templates/index.html** → Frontend HTML page
* **static/** → Contains CSS and JavaScript files

---

## ✅ Result

The Flask web application was successfully deployed on Google App Engine and accessed through a public URL.

---

## 📚 Conclusion

Google App Engine simplifies cloud deployment by automatically managing infrastructure, scaling, and server configuration. This practical demonstrated installation, configuration, and deployment of a Python web application on GAE.

---

## 👩‍💻 Author

Name: Harshalee Malu
Class: TE Computer Engineering
University: Savitribai Phule Pune University
Pattern: 2019
