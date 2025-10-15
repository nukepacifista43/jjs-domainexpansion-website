from flask import Flask, render_template_string, abort

app = Flask(__name__)

# Data for Domain Expansions
domains = [
    {
        "id": 1,
        "name": "Malevolent Shrine",
        "user": "Ryomen Sukuna",
        "japanese": "伏魔御廚子 (Fukuma Mizushi)",
        "romaji": "Fukuma Mizushi",
        "power": "Creates a binding shrine that slashes anything within its radius with unstoppable slashing attacks.",
        "first": "Jujutsu Kaisen Chapter 119 (Manga), Episode 42 (Anime)",
        "image1": "https://i.pinimg.com/736x/be/b7/bf/beb7bfc44831fbc5f3563d043e3696ed.jpg",
        "image2": "https://www.dexerto.com/cdn-image/wp-content/uploads/2023/09/07/jujutsu-kaisen-mahito-domain-expansion-1024x576.jpeg?width=1200&quality=75&format=auto",
        "image3": "https://motionbgs.com/media/5134/sukuna-vs-mahoraga.jpg",
        "image4": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxHA9tqeTOVSmzbkI5n1f1pcMZuFn905Y3dw&s"
    },
    {
        "id": 2,
        "name": "Infinite Void",
        "user": "Satoru Gojo",
        "japanese": "無量空処 (Muryōkūsho)",
        "romaji": "Muryoukūsho",
        "power": "Traps the target in a limitless space filled with endless knowledge, overwhelming the mind.",
        "first": "Jujutsu Kaisen Chapter 15 (Manga), Episode 6 (Anime)",
        "image1": "https://wallpaperaccess.com/full/11264735.jpg",
        "image2": "https://www.dexerto.com/cdn-image/wp-content/uploads/2023/09/07/jujutsu-kaisen-gojo-domain-expansion-1024x576.jpeg?width=1200&quality=75&format=auto",
        "image3": "https://static0.cbrimages.com/wordpress/wp-content/uploads/2021/04/Jogo---Jujutsu-Kaisen---Infinite-Domain.jpg?q=50&fit=crop&w=825&dpr=1.5",
        "image4": "https://i.pinimg.com/736x/f2/63/7f/f2637ff12e70ca25f06adefdfaffc01f.jpg"
    },
    {
        "id": 3,
        "name": "Self-Embodiment of Perfection",
        "user": "Mahito",
        "japanese": "自閉円頓裹 (Jihei Endonka)",
        "romaji": "Jihei Endonka",
        "power": "Activates a barrier that guarantees his Idle Transfiguration hits the soul of anyone trapped inside.",
        "first": "Jujutsu Kaisen Chapter 30 (Manga), Episode 21 (Anime)",
        "image1": "https://i.pinimg.com/736x/e3/9f/fb/e39ffb6ac1e631627ee6b8f5b87fd351.jpg",
        "image2": "https://www.dexerto.com/cdn-image/wp-content/uploads/2023/09/07/jujutsu-kaisen-mahito-domain-expansion-1024x576.jpeg?width=1200&quality=75&format=auto",
        "image3": "https://i.ytimg.com/vi/tGyWCPionvk/sddefault.jpg",
        "image4": "https://i.pinimg.com/736x/ca/f8/5d/caf85d12606cf1d9e9990aa750ef3103.jpg"
    }
]

# Honorable mentions data
honorable_mentions = [
    {
        "name": "Boogie Woogie",
        "user": "Aoi Tōdō",
        "japanese": "不義遊戯 (Bugiyūgi)",
        "romaji": "Bugiyūgi",
        "power": "Allows Tōdō to swap places with anyone (or anything imbued with cursed energy) by clapping his hands.",
        "first": "Jujutsu Kaisen Chapter 35 (Manga), Episode 18 (Anime)",
        "image": "https://i1.sndcdn.com/artworks-DDeyzo1TejeHEOzz-r98LrQ-t500x500.jpg"
    },
    {
        "name": "Ratio Technique",
        "user": "Kento Nanami",
        "japanese": "比率術式 (Hiritsu Jutsushiki)",
        "romaji": "Hiritsu Jutsushiki",
        "power": "Divides his target into a 7:3 ratio, striking at the weak point to guarantee critical damage. His 'Overtime' state boosts his strength further.",
        "first": "Jujutsu Kaisen Chapter 18 (Manga), Episode 9 (Anime)",
        "image": "https://pbs.twimg.com/media/FMAatXXagAAC1Mk.jpg:large"
    }
]


# Honorable Mentions template with Japanese pronunciation
honorable_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Honorable Mentions</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #111; color: #f5f5f5; margin: 0; }
        h1 { text-align: center; color: #ffcc00; margin-top: 40px; }
        .card {
            border: 2px solid #444; border-radius: 10px; padding: 20px;
            margin: 30px auto; background: #222; width: 90%; max-width: 700px;
        }
        .card img {
            width: auto; max-width: 100%; height: 300px; object-fit: contain;
            border-radius: 10px; display: block; margin: 10px auto; background-color: #000;
        }
        ul { list-style-type: square; padding-left: 20px; }
        a { color: #ffcc00; text-decoration: none; }
        a:hover { text-decoration: underline; }
        button {
            background-color: #ffcc00; border: none; color: #111;
            padding: 10px 20px; font-size: 1em; border-radius: 8px;
            cursor: pointer; display: block; margin: 15px auto;
        }
        button:hover { background-color: #ffe066; }
    </style>
</head>
<body>
    <h1>⭐ Honorable Mentions ⭐</h1>
    {% for c in mentions %}
    <div class="card">
        <img src="{{ c.image }}" alt="{{ c.name }}">
        <ul>
            <li><b>Technique:</b> {{ c.name }}</li>
            <li><b>User:</b> {{ c.user }}</li>
            <li><b>Japanese:</b> {{ c.japanese }}</li>
            <li><b>Romaji:</b> {{ c.romaji }}</li>
            <li><b>Power:</b> {{ c.power }}</li>
            <li><b>First Appearance:</b> {{ c.first }}</li>
        </ul>

        <button onclick="speakJapanese('{{ c.romaji }}')">🔊 '{{ c.romaji }}'</button>
    </div>
    {% endfor %}
    <p style="text-align:center;"><a href="/">⬅ Back to Main Page</a></p>

    <script>
    function speakJapanese(text) {
        const msg = new SpeechSynthesisUtterance(text);
        msg.lang = 'ja-JP';
        msg.rate = 1;
        msg.pitch = 1;
        msg.volume = 1;
        window.speechSynthesis.speak(msg);
    }
    </script>
</body>
</html>
"""


# Homepage template
home_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jujutsu Kaisen Domains</title>
    <style>
        html, body {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow-x: hidden;
            font-family: Arial, sans-serif;
            background-color: #111;
            color: #f5f5f5;
        }

        /* === Background Parallelograms === */
        .background-splits {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            overflow: hidden;
        }

        .background-splits .split {
            position: absolute;
            top: 0;
            bottom: 0;
            width: 40%;
            transform: skewX(-15deg);
            transform-origin: top left;
            opacity: 0.7;
            background-size: cover;
            background-position: center;
            filter: brightness(0.8) contrast(1.2);
        }

        /* Gojo (Center), Sukuna (Middle), Mahito (Right) */
        .gojo-split {
            left: -10%;
            background-image: url('https://i.pinimg.com/736x/b6/ee/01/b6ee01a797fe3553f25035b1a3163c7d.jpg');
        }

        .sukuna-split {
            left: 30%;
            background-image: url('https://i.pinimg.com/736x/f2/63/7f/f2637ff12e70ca25f06adefdfaffc01f.jpg');
        }

        .mahito-split {
            left: 70%;
            background-image: url('https://i.pinimg.com/736x/ca/f8/5d/caf85d12606cf1d9e9990aa750ef3103.jpg');
        }

        /* === Content Layer === */
        h1 {
            text-align: center;
            color: #ff5555;
            margin-top: 40px;
            position: relative;
            z-index: 1;
        }

        .container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
            position: relative;
            z-index: 1;
            max-width: 1200px;
            margin: auto;
        }

        /* === Domain Cards === */
        .domain {
            border: 2px solid #444;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .domain:hover {
            transform: translateY(-4px);
            box-shadow: 0 4px 10px rgba(255,255,255,0.3);
        }
        .honorable {
    position: relative;
    z-index: 2;
    text-align: center;
    margin: 40px 0;
}
        .honorable a {
    color: #ffcc00;
    background-color: rgba(0,0,0,0.3);
    padding: 10px 20px;
    border-radius: 10px;
    text-decoration: none;
}
        .honorable a:hover { background-color: #ffcc00; color: #111; }

        /* Individual color themes */
        .domain.sukuna { background-color: #b30000; }
        .domain.gojo { background-color: #0099FF; }
        .domain.mahito { background-color: #8A2BE2; }

        .domain.sukuna a { color: #000; }
        .domain.gojo a { color: #fff; }
        .domain.mahito a { color: #D3D3D3; }

        .images {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }

        .images img {
            height: 180px;
            object-fit: contain;
            border-radius: 10px;
            background-color: #000;
        }

        a { text-decoration: none; }
        a:hover { text-decoration: underline; }

        @media (max-width: 600px) {
            .images img { height: 150px; }
            h1 { font-size: 1.5em; }
        }
    </style>
</head>
<body>
    <!-- Background Layer -->
    <div class="background-splits">
        <div class="split gojo-split"></div>
        <div class="split sukuna-split"></div>
        <div class="split mahito-split"></div>
    </div>

    <!-- Foreground Content -->
    <h1>Domain Expansions - Jujutsu Kaisen</h1>
    <div class="container">
        {% for d in domains %}
            {% set domain_class = 'sukuna' if d.id == 1 else 'gojo' if d.id == 2 else 'mahito' %}
            <div class="domain {{ domain_class }}">
                <h2><a href="/domain/{{ d.id }}">{{ d.name }}</a></h2>
                <p><b>User:</b> {{ d.user }}</p>
                <div class="images">
                    <img src="{{ d.image1 }}" alt="{{ d.name }}">
                    <img src="{{ d.image2 }}" alt="{{ d.name }}">
                </div>
            </div>
        {% endfor %}
    </div>
     <div class="honorable">
        <a href="/honorable">⭐ Honorable Mentions: Tōdō & Nanami ⭐</a>
    </div>
</body>
</html>
"""

# Details page template
detail_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ domain.name }} - Details</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #111; color: #f5f5f5; margin: 0; }
        h1 { text-align: center; color: #ff5555; margin-top: 40px; }
        .card {
            border: 2px solid #444;
            border-radius: 10px;
            padding: 20px;
            margin: 50px auto;
            background: #222;
            width: 90%;
            max-width: 700px;
        }
        .card img {
            width: auto;
            max-width: 100%;
            height: 300px;
            object-fit: contain;
            border-radius: 10px;
            display: block;
            margin: 10px auto;
            background-color: #000;
        }
        ul { list-style-type: square; padding-left: 20px; }
        a { color: #66aaff; text-decoration: none; }
        a:hover { text-decoration: underline; }
                
        button {
            background-color: #ff5555; border: none; color: white;
            padding: 10px 20px; font-size: 1em; border-radius: 8px;
            cursor: pointer; display: block; margin: 15px auto;
        }
        button:hover { background-color: #ff7777; }
        
    </style>
</head>
<body>
    <h1>{{ domain.name }}</h1>
    <div class="card">
        <img src="{{ domain.image3 }}" alt="{{ domain.name }}">
        <ul>
            <li><b>User:</b> {{ domain.user }}</li>
            <li><b>Japanese:</b> {{ domain.japanese }}</li>
            <li><b>Romaji:</b> {{ domain.romaji }}</li>
            <li><b>Power:</b> {{ domain.power }}</li>
            <li><b>First Appearance:</b> {{ domain.first }}</li>
        </ul>
         <button onclick="speakJapanese('{{ domain.romaji }}')">🔊 '{{ domain.romaji }}'</button>
        <p><a href="/">⬅ Back to All Domains</a></p>
    </div>
    
     <script>
    function speakJapanese(text) {
        const msg = new SpeechSynthesisUtterance(text);
        msg.lang = 'ja-JP';
        msg.rate = 1;
        msg.pitch = 1;
        msg.volume = 1;
        window.speechSynthesis.speak(msg);
    }
    </script>
</body>
</html>
"""



@app.route("/")
def home():
    return render_template_string(home_template, domains=domains)

@app.route("/domain/<int:domain_id>")
def domain_detail(domain_id):
    domain = next((d for d in domains if d["id"] == domain_id), None)
    if not domain:
        abort(404)
    return render_template_string(detail_template, domain=domain)

@app.route("/honorable")
def honorable():
    return render_template_string(honorable_template, mentions=honorable_mentions)

if __name__ == "__main__":
    app.run(debug=True)

