from email.message import EmailMessage
from flask import Flask, render_template, request


import requests
import smtplib
import ssl

posts = requests.get("https://api.npoint.io/5434fb065ea9bbad37bc").json()
OWN_EMAIL = "YOUR OWN EMAIL"
OWN_PASSWORD = "YOUR OWN PASSWORD"
app = Flask(__name__) 


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    em = EmailMessage()
    em['From'] = OWN_EMAIL
    em['To'] = OWN_EMAIL
    em['Subject'] = "New Message"
    em.set_content(email_message)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, em.as_string())


if __name__ == "__main__":
    app.run(debug=True)
