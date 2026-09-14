from flask import Flask, render_template, request, redirect, url_for, session
import os
import time

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "change-this-in-production")

# Lab-only credentials. Never use a real password here.
LAB_USERNAME = os.environ.get("LAB_USERNAME", "labuser")
LAB_PASSWORD = os.environ.get("LAB_PASSWORD", "A11b12c13d14e15$")

# Deliberately vulnerable comparison for the controlled lab.
# The HTTP response itself contains no timing/debug information.
DELAY = float(os.environ.get("LAB_DELAY", "0.030"))

def check_password(candidate: str) -> bool:
    for supplied, expected in zip(candidate, LAB_PASSWORD):
        if supplied != expected:
            return False
        time.sleep(DELAY)
    return len(candidate) == len(LAB_PASSWORD)

@app.get("/")
def home():
    return render_template("login.html", error=None)

@app.post("/login")
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if username == LAB_USERNAME and check_password(password):
        session["user"] = username
        return redirect(url_for("dashboard"))

    # Normal-looking login failure. No timing/debug data is returned.
    return render_template("login.html", error="Invalid username or password"), 401

@app.get("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("dashboard.html", username=session["user"])

@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.get("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
