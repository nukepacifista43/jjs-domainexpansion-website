from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
        <html>
        <head><title>Domain Expansions - Jujutsu Kaisen</title></head>
        <body>
            <h1>Domain Expansions in Jujutsu Kaisen</h1>
            <ul>
                <li><b>Name:</b> Unlimited Void<br>
                    <b>User:</b> Satoru Gojo<br>
                    <b>Kanji:</b> 無量空処 (Muryōkūsho)<br>
                    <b>Power:</b> Traps opponents in infinite knowledge<br>
                    <b>First Appearance:</b> Season 1, Episode 7
                            <div style="display: flex; gap: 10px;">
            <img src="https://i.pinimg.com/736x/dc/76/ea/dc76ea3747e218611d382508cbcea810.jpg" width="200">
            <img src="https://vast-gray-183q3iybwq.edgeone.app/Gojo%20domain.png" width="200">
        </div>
                </li>
                <br>
                <li>
                <div style="margin-top: 100px;">
                </div>
                <b>Name:</b> Malevolent Shrine<br>
                    <b>User:</b> Ryomen Sukuna<br>
                    <b>Kanji:</b> 伏魔御厨子 (Fukuma Mizushi)<br>
                    <b>Power:</b> Slashes everything in a 200m radius<br>
                    <b>First Appearance:</b> Season 1, Episode 19
                    <div style="display: flex; gap: 10px;">
            <img src="https://i.pinimg.com/736x/be/b7/bf/beb7bfc44831fbc5f3563d043e3696ed.jpg" width="100", height="200">
            <img src="https://healthy-turquoise-pzbgnzcgfv.edgeone.app/Malevolent%20Shrine%20Hand%20Sign.png" width="200", height="200">
                </li>
            </ul>
        </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
