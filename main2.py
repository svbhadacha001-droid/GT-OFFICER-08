from flask import Flask
import os

app = Flask(__name__)

html_design = """
<!DOCTYPE html>
<html lang="gu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GT OFFICIAL 08 - Premium</title>
    <style>
        body { background: linear-gradient(135deg, #0c0c0e 0%, #1a1a1c 100%); color: white; font-family: 'Segoe UI', sans-serif; text-align: center; padding: 20px; min-height: 100vh; }
        .container { max-width: 500px; margin: auto; }
        .box { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 20px; margin-bottom: 20px; text-align: left; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8); }
        .btn { background: linear-gradient(45deg, #ff1e27, #ff6b6b); color: white; padding: 15px; border: none; cursor: pointer; border-radius: 50px; font-weight: bold; width: 100%; margin-top: 20px; transition: 0.3s; box-shadow: 0 4px 15px rgba(255, 30, 39, 0.4); }
        .btn:hover { transform: scale(1.02); box-shadow: 0 6px 20px rgba(255, 30, 39, 0.6); }
        input, select { width: 100%; padding: 14px; margin: 10px 0; border-radius: 12px; border: 1px solid #444; background: rgba(0,0,0,0.3); color: white; box-sizing: border-box; }
        .rule-list { list-style-type: none; padding-left: 0; color: #eee; }
        .rule-list li { margin: 10px 0; padding-left: 25px; position: relative; }
        .rule-list li::before { content: '✓'; color: #ff1e27; position: absolute; left: 0; font-weight: bold; }
        .hidden { display: none; }
        h1 { background: linear-gradient(to right, #ff1e27, #fff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    </style>
</head>
<body>
    <div class="container">
        <div id="welcome_screen">
            <h1 style="margin-top: 100px;">WELCOME<br>GT OFFICIAL 08</h1>
            <button class="btn" onclick="showRules()">ENTER NOW</button>
        </div>

        <div id="main_content" class="hidden">
            <div class="box">
                <h3 style="color: #ff1e27; text-align: center; margin-bottom: 20px;">🎯 ગિલ્ડના નિયમો</h3>
                <ul class="rule-list">
                    <li>Player daily online</li>
                    <li>Gujrati player only</li>
                    <li>Weekly glori push 7/8 k</li>
                    <li>Without guild test entry</li>
                    <li>Koi pan problem hoi guild leder sate vat karo</li>
                    <li>No hat other guild</li>
                </ul>
            </div>

            <div class="box">
                <h2 style="text-align: center;">📝 Join Form</h2>
                <label>🎮 FREE FIRE U_ID:</label>
                <input type="text" id="ff_uid" placeholder="UID લખો">
                <label>💬 INSTAGRAM/WHATSAPP:</label>
                <input type="text" id="contact_info" placeholder="તમારું નામ/નંબર">
                <label>📩 કોનો સંપર્ક કરવો છે:</label>
                <select id="admin_select">
                    <option value="917990843839">Leader (7990843839)</option>
                    <option value="919023506977">Acting Leader (9023506977)</option>
                </select>
                <button class="btn" onclick="submitRequest()">SUBMIT REQUEST</button>
            </div>
        </div>
    </div>

    <script>
        function showRules() {
            document.getElementById('welcome_screen').style.display = 'none';
            document.getElementById('main_content').classList.remove('hidden');
        }
        function submitRequest() {
            var uid = document.getElementById("ff_uid").value;
            var contact = document.getElementById("contact_info").value;
            var adminNumber = document.getElementById("admin_select").value;
            if(uid == "" || contact == "") { alert("બધી વિગતો ભરો!"); return; }
            var message = "🔥 *GT OFFICER GUILD JOIN REQUEST* 🔥\\n\\n🎮 *UID:* " + uid + "\\n💬 *Name/Contact:* " + contact;
            window.location.href = "https://wa.me/" + adminNumber + "?text=" + encodeURIComponent(message);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return html_design

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
