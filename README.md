# Vulnerable-Car-Tracking-System
A deliberately insecure Flask web app that simulates a car tracking system — built for learning, testing, and practicing **web app pentesting**.

# 🔧 Vulnerable Car Tracking System (Flask)

A deliberately insecure Flask web app that simulates a car tracking system — built for learning, testing, and practicing **web app pentesting**.

![screenshot](https://via.placeholder.com/600x300.png?text=Car+Tracking+System+Simulation)

---

## 🚀 Features

- Fake car location data in JSON format
- Vulnerable LFI (Local File Inclusion) endpoint
- HTML frontend that fetches backend data
- Minimal styling with simulated UI

---



---

## 🛠 Installation

### 1. Clone or Download


git clone https://github.com/yourusername/car-tracking-lab.git
cd car-tracking-lab

pip install flask

python app.py


Then open your browser and go to:


http://127.0.0.1:5000



🧪 Vulnerability Testing with Burp Suite




1. Open Burp Suite
Go to Proxy > Options and confirm it's listening on 127.0.0.1:8080


http://127.0.0.1:5000


4. Intercept a Request to the API
Intercept and modify this request:


GET /api/cars?file=../../../../etc/passwd HTTP/1.1
Try other payloads to explore LFI or extend it for XSS.


car-tracking-lab/



https://buymeacoffee.com/lukassimun
