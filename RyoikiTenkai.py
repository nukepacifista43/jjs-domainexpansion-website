from flask import Flask, render_template_string

app = Flask(__name__)

# Data for Domain Expansions
domains = [
    {
        "name": "Malevolent Shrine",
        "user": "Ryomen Sukuna",
        "japanese": "伏魔御廚子 (Fukuma Mizushi)",
        "romaji": "Fukuma Mizushi",
        "power": "Creates a binding shrine that slashes anything within its radius with unstoppable slashing attacks.",
        "first": "Jujutsu Kaisen Chapter 119 (Manga), Episode 42 (Anime)",
        "image": "https://64.media.tumblr.com/c7ac5679680acaaccc82e3d7b28e8d5a/f4539acb036fdffe-ec/s1280x1920/09d3c20c5e1b19a851b33e01a33a43ca2ac2d447.jpg",

    },

    {
        "name": "Infinite Void",
        "user": "Satoru Gojo",
        "japanese": "無量空処 (Muryōkūsho)",
        "romaji": "Muryoukūsho",
        "power": "Traps the target in a limitless space filled with endless knowledge, overwhelming the mind.",
        "first": "Jujutsu Kaisen Chapter 15 (Manga), Episode 6 (Anime)",
        "image": "https://wallpaperaccess.com/full/11264735.jpg"
    },
    {
        "name": "Self-Embodiment of Perfection",
        "user": "Mahito",
        "japanese": "自閉円頓裹 (Jihei Endonka)",
        "romaji": "Jihei Endonka",
        "power": "Activates a barrier that guarantees his Idle Transfiguration hits the soul of anyone trapped inside.",
        "first": "Jujutsu Kaisen Chapter 30 (Manga), Episode 21 (Anime)",
        "image": "https://cdna.artstation.com/p/assets/images/images/069/384/762/large/muhammed-kayacan-muhammed-kayacan-mha-render-02.jpg?1700001018"
    }
]

# HTML Template (inline for simplicity)
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Jujutsu Kaisen Domain Expansions</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #111; color: #f5f5f5; }
        .domain { border: 2px solid #444; border-radius: 10px; padding: 20px; margin: 20px; background: #222; }
        img { width: 300px; border-radius: 10px; margin-top: 10px; }
        h1 { text-align: center; color: #ff5555; }
        ul { list-style-type: square; }
    </style>
</head>
<body>
    <h1>Jujutsu Kaisen Domain Expansions</h1>
    {% for d in domains %}
    <div class="domain">
        <h2>{{ d.name }}</h2>
        <img src="{{ d.image }}" alt="{{ d.name }}">
        <ul>
            <li><b>User:</b> {{ d.user }}</li>
            <li><b>Japanese:</b> {{ d.japanese }}</li>
            <li><b>Romaji:</b> {{ d.romaji }}</li>
            <li><b>Power:</b> {{ d.power }}</li>
            <li><b>First Appearance:</b> {{ d.first }}</li>
        </ul>
    </div>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template, domains=domains)

if __name__ == "__main__":
    app.run(debug=True)
