from flask import Flask
import os

app = Flask(__name__)

html_design = """
<!DOCTYPE html>
<html lang="gu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GT OFFICER GUILD</title>
    <style>
        body { background-color: #0c0c0e; color: white; font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        .container { max-width: 500px; margin: auto; }
        .box { background-color: #16171b; border: 1px solid #333; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: left; }
        .btn { background: #ff1e27; color: white; padding: 15px; border: none; cursor: pointer; border-radius: 5px; font-weight: bold; width: 100%; margin-top: 15px; }
        input, select { width: 100%; padding: 12px; margin: 10px 0; border-radius: 5px; border: 1px solid #444; background: #1a1a1a; color: white; }
        .rule-list { list-style-type: decimal; padding-left: 20px; color: #ccc; font-size: 14px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>GT OFFICER GUILD</h1>
        
        <div class="box">
            <h3 style="color: #ff1e27; text-align: center;">🎯 ગિલ્ડના નિયમો</h3>
            <ul class="rule-list">
                <li>Player daily online</li>
                <li>Gujrati player only</li>
                <li>Weekly glori push 7/8 k</li>
                <li>Without guild test entry</li>
                <li>Koi pan problem hoi guild leder sate vat karo</li>
                <li>No hat other guild</li>
            </ul>
            <p style="text-align: center; font-weight: bold; margin-top: 10px;">THANK YOU FOR JOINING GT OFFICIAL 🤗</p>
        </div>

        <div class="box">
            <h2>📝 તમારી વિગતો ભરો</h2>
            <label>🎮 FREE FIRE U_ID:</label>
            <input type="text" id="ff_uid" placeholder="UID લખો">
            
            <label>💬 INSTAGRAM/WHATSAPP:</label>
            <input type="text" id="contact_info" placeholder="તમારું નામ/નંબર">
            
            <label>📩 કોનો સંપર્ક કરવો છે:</label>
            <select id="admin_select">
                <option value="918320894249">Leader (8320894249)</option>
                <option value="919023506977">Acting Leader (9023506977)</option>
            </select>
            
            <p style="font-size: 12px; color: #888;">*તમારો પ્રોફાઈલ ફોટો વોટ્સએપ પર સબમિટ કર્યા પછી મોકલવો.*</p>
            
            <button class="btn" onclick="submitRequest()">SUBMIT REQUEST</button>
        </div>
    </div>

    <script>
        function submitRequest() {
            var uid = document.getElementById("ff_uid").value;
            var contact = document.getElementById("contact_info").value;
            var adminNumber = document.getElementById("admin_select").value;
            
            if(uid == "" || contact == "") { alert("બધી વિગતો ભરો!"); return; }
            
            var message = "🔥 *GT OFFICER GUILD JOIN REQUEST* 🔥\\n\\n🎮 *UID:* " + uid + "\\n💬 *Name/Contact:* " + contact + "\\n\\n(અહીં તમારો પ્રોફાઈલ સ્ક્રીનશોટ મોકલો)";
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
