from flask import Flask, render_template, request, url_for
import qrcode
import os
from datetime import datetime

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/qrcodes"


os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code_path = None
    if request.method == "POST":
        data = request.form.get("data")
        if data:
            
            filename = f"qr_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            
           
            img = qrcode.make(data)
            img.save(filepath)
            
            qr_code_path = url_for("static", filename=f"qrcodes/{filename}")
    return render_template("index.html", qr_code=qr_code_path)

if __name__ == "__main__":
    app.run(debug=True)
