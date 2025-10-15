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
        "image3": "https://patient-coral-lpte5yn1co.edgeone.app/malevolent%20shrine.png"
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
        "image3": "https://static0.cbrimages.com/wordpress/wp-content/uploads/2021/04/Jogo---Jujutsu-Kaisen---Infinite-Domain.jpg?q=50&fit=crop&w=825&dpr=1.5"
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
        "image3": "https://i.ytimg.com/vi/tGyWCPionvk/sddefault.jpg"
    }
]

# Homepage template
home_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Jujutsu Kaisen Domains</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #111; color: #f5f5f5; }
        h1 { text-align: center; color: #ff5555;  margin-top: 30px;}
        .domain {
            border: 2px solid #444;
            border-radius: 10px;
            padding: 20px;
            margin: 20px auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            max-width: 800px;
            transition: transform 0.2s, box-shadow 0.2s;

        }
           /* Individual color themes */
        .domain.sukuna { background-color: #b30000; }   /* Red */
        .domain.gojo { background-color: #0099FF; }     /* Bright Gojo blue */
        .domain.mahito { background-color: #8A2BE2; }   /* Violet */

        .domain:hover { transform: translateY(-4px); box-shadow: 0 4px 10px rgba(255,255,255,0.3); }

        .domain.sukuna a { color: #000; }               /* Black for Sukuna */
        .domain.gojo a { color: #fff; }                 /* White for Gojo */
        .domain.mahito a { color: #D3D3D3; }            /* Light gray for Mahito */
        
        .images {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center; 
            margin-top: 10px; 
        }
        .images img {
            height: 180px;              /* Same height for all images */
            object-fit: contain;        /* Preserve aspect ratio for portrait or odd images */
            border-radius: 10px;
            background-color: #000;     /* fills behind transparent images */
        }
        a {  text-decoration: none;  }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Domain Expansions - Jujutsu Kaisen</h1>
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
        body { font-family: Arial, sans-serif; background-color: #111; color: #f5f5f5; }
        h1 { text-align: center; color: #ff5555; }
        .card {
            border: 2px solid #444;
            border-radius: 10px;
            padding: 20px;
            margin: 50px auto;
            background: #222;
            width: 60%;
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
        a { color: #66aaff; }
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
        <p><a href="/">⬅ Back to All Domains</a></p>
    </div>
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

if __name__ == "__main__":
    app.run(debug=True)
