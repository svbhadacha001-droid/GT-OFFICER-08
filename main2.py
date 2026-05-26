from flask import Flask
import os

app = Flask(__name__)

# તમારો ઓરિજિનલ ડિઝાઇન કોડ
html_design = """
<!DOCTYPE html>
<html lang="gu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GT OFFICER GUILD</title>
    <style>
        body { font-family: 'Arial', sans-serif; background-color: #0c0c0e; color: #ffffff; margin: 0; padding: 0; text-align: center; }
        .btn { background: linear-gradient(180deg, #ff1e27, #b30006); color: white; border: none; padding: 15px 40px; font-size: 18px; font-weight: bold; border-radius: 8px; cursor: pointer; text-decoration: none; display: inline-block; box-shadow: 0 4px 15px rgba(255,30,39,0.4); transition: 0.3s; }
        .btn:hover { transform: scale(1.05); background: #ff1e27; }
        #page1 { display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; background: radial-gradient(circle, #2a080a 0%, #0c0c0e 100%); }
        .container { max-width: 500px; margin: auto; padding: 20px; display: none; }
        header { background: linear-gradient(180deg, #ff1e27, #800c10); padding: 30px 20px; border-bottom-left-radius: 20px; border-bottom-right-radius: 20px; }
        .box { background-color: #16171b; border: 2px solid #ff1e27; border-radius: 12px; padding: 20px; margin: 20px 0; text-align: left; }
        .rule-item { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #2a2c33; font-weight: bold; }
        .rule-val { color: #ff1e27; }
        label { display: block; margin-top: 15px; font-weight: bold; color: #ffb400; text-align: left; }
        input[type="text"] { width: 100%; padding: 12px; margin-top: 5px; border: 2px solid #ff1e27; border-radius: 6px; background-color: #0c0c0e; color: white; box-sizing: border-box; }
    </style>
</head>
<body>
    <div id="page1">
        <h1>🔥 WELCOME TO<br>GT OFFICER GUILD 🔥</h1>
        <button class="btn" onclick="showPage2()">👉 ENTER 👈</button>
    </div>
    <div id="page2" class="container">
        <header><h1>📜 GUILD RULES MENU</h1></header>
        <div class="box">
            <h2>🎯 JOINING REQUIREMENTS</h2>
            <div class="rule-item"><span>WEEK GLORY:</span> <span class="rule-val">10000+ GLORY</span></div>
            <div class="rule-item"><span>BEHAVIOR:</span> <span class="rule-val">RESPECT ALL PLAYERS 🤝</span></div>
            <div class="rule-item"><span>MIN LEVEL:</span> <span class="rule-val">LEVEL 50+</span></div>
        </div>
        <button class="btn" onclick="showPage3()">📩 ENTER FOR JOIN REQUEST</button>
    </div>
    <div id="page3" class="container">
        <header><h1>📩 JOIN REQUEST FORM</h1></header>
        <div class="box">
            <h2>📝 તમારી વિગતો ભરો</h2>
            <label>🎮 FREE FIRE U_ID:</label>
            <input type="text" id="ff_uid">
            <label>💬 INSTAGRAM/WHATSAPP:</label>
            <input type="text" id="contact_info">
            <button class="btn" style="width: 100%; margin-top: 25px;" onclick="submitRequest()">🚀 SUBMIT REQUEST</button>
        </div>
    </div>
    <script>
        var MY_NUMBER = "919023506977"; 
        function showPage2() { document.getElementById("page1").style.display = "none"; document.getElementById("page2").style.display = "block"; }
        function showPage3() { document.getElementById("page2").style.display = "none"; document.getElementById("page3").style.display = "block"; }
        function submitRequest() {
            var uid = document.getElementById("ff_uid").value;
            var contact = document.getElementById("contact_info").value;
            var message = "🔥 *GT OFFICER GUILD JOIN REQUEST* 🔥\\n\\n🎮 *ID:* " + uid + "\\n💬 *Contact:* " + contact;
            window.location.href = "https://wa.me/" + MY_NUMBER + "?text=" + encodeURIComponent(message);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return html_design

if __name__ == '__main__':
    # આ લાઈન Render માટે ખૂબ જરૂરી છે
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
