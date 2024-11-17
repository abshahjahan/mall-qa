from flask import Flask, render_template
print(" * staring app "+ __name__)
app = Flask(__name__)

@app.route("/")
def home():
    data="Cool!!!"
    return render_template("index.html", data=data)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    print(" * hello")
    app.run(debug=True)