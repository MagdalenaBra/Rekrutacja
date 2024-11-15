!pip install openai

import openai

openai.api_key = "MY-API-KEY"

try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Hello, world!",
        max_tokens=5
    )
    print(response)
except openai.error.AuthenticationError as e:
    print(f"Authentication failed: {e}")
except Exception as e:
    print(f"Error occurred: {e}")

#Funkcja generująca kod HTML
def generate_html(article_text, prompt):
    # Wysyłanie zapytania do API OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Użycie modelu GPT-3.5
        messages=[
            {"role": "system", "content": "You are an HTML generator."},  # Definicja roli
            {"role": "user", "content": f"{prompt}\n\n{article_text}"}  # Artykuł jako użytkownik
        ]
    )
    return response['choices'][0]['message']['content']

# Wczytanie artykułu z pliku 'artykul.txt'
def load_article_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        article_text = file.read()
    return article_text

# Prompt do generowania HTML
html_prompt = """
Przekształć poniższy artykuł w strukturalny kod HTML.
Dodaj odpowiednie tagi <h1>, <h2>, <p> oraz inne strukturalne tagi HTML.
Zidentyfikuj miejsca, w których można dodać grafiki i oznacz je tagiem <img> z atrybutem alt, który zawiera prompt do wygenerowania grafiki.
"""

# Odczyt treści artykułu z pliku
article_text = load_article_from_file('artykul.txt')

# Generowanie HTML na podstawie artykułu
html_content = generate_html(article_text, html_prompt)

# Zapis wygenerowanego HTML do pliku podglad
with open('artykul.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)


print("HTML został zapisany do pliku 'artykul.html'.")

print("Wygenerowano plik artykul.html.")


#zablon html i podglad html


from jinja2 import Template

# Wczytanie artykułu z pliku
with open('artykul.txt', 'r', encoding='utf-8') as file:
    article_text = file.read()

# Szablon HTML (Jinja2) z uwzględnieniem obrazów i podpisów
html_template = """
<body>
    <h1>Podgląd Artykułu</h1>
    <div class="content">
        {{ article_text | safe }}
    </div>
    <!-- Placeholder dla grafiki -->
    <div class="images">
        {% for image in images %}
        <div class="image">
            <img src="{{ image.src }}" alt="{{ image.alt }}" />
            <p><strong>Opis grafiki:</strong> {{ image.caption }}</p>
        </div>
        {% endfor %}
    </div>
</body>
"""

# Przykładowe dane do wstawienia (możesz zastąpić je własnymi danymi)
images = [
    {
        'src': 'image_placeholder_1.jpg',
        'alt': 'Wygeneruj obrazek z krajobrazem z górskimi szczytami',
        'caption': 'Obrazek przedstawiający majestatyczne góry'
    },
    {
        'src': 'image_placeholder_2.jpg',
        'alt': 'Wygeneruj obrazek z plażą na zachodzie słońca',
        'caption': 'Piękna plaża podczas zachodu słońca'
    }
]

# Tworzenie obiektu Template
template = Template(html_template)

# Generowanie HTML z artykułem i miejscami na obrazy
html_content = template.render(article_text=article_text.replace("\n", "<br>"), images=images)

# Zapisanie wygenerowanego HTML do pliku
with open('artykul.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("Plik artykul.html został wygenerowany.")

from jinja2 import Template

# Wczytanie artykułu z pliku
with open('artykul.txt', 'r', encoding='utf-8') as file:
    article_text = file.read()

# Podzielmy tekst artykułu na linie
lines = article_text.split("\n")

# Pierwsza linia pliku testowego artykułu będzie tytułem artykułu
article_title = lines[0].strip()

# Reszta tekstu to treść artykułu
article_body = "\n".join(lines[1:]).strip()

# Szablon HTML (pusty, gotowy na wklejenie artykułu)
html_template = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Podgląd Artykułu</title>
    <style>
        /* Tło nawiązujące do sztucznej inteligencji */
        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, rgba(0, 255, 255, 0.8), rgba(0, 0, 128, 0.8)),
                        url('https://example.com/ai-background.jpg') no-repeat center center fixed;
            background-size: cover;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: #333; /* Ciemnoszary kolor tekstu */
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.4); /* Subtelny cień */
        }

        /* Styl dla kontenera artykułu */
        .container {
            width: 80%;
            max-width: 960px;
            background-color: rgba(255, 255, 255, 0.9); /* Przezroczyste tło */
            padding: 30px;
            margin: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(8px);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        /* Efekt powiększenia kontenera */
        .container:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 30px rgba(0, 0, 0, 0.15);
        }

        h1 {
            font-size: 2.2rem;
            text-align: center;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #6a3d3d; /* Delikatny ciemnoczerwony */
        }

        p {
            color: #555; /* Bardziej stonowany szary */
            font-size: 1.2rem;
            line-height: 1.8;
            margin-bottom: 25px;
            text-align: justify; /* Wyjustowanie tekstu */
        }

        /* Zmieniony kolor tekstu na ciemnoszary z mniejszym kontrastem */
        .article-content {
            color: #444; /* Ciemniejszy szary */
            font-size: 1.15rem;
            line-height: 1.7;
            text-align: justify; /* Wyjustowanie tekstu artykułu */
        }

        img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            transition: transform 0.3s ease;
        }

        /* Efekt na obrazkach */
        img:hover {
            transform: scale(1.05);
        }

        .image-caption {
            text-align: center;
            font-size: 1rem;
            color: #888;
            margin-bottom: 30px;
        }

        /* Dodanie subtelnych animacji */
        .article-content {
            opacity: 0;
            animation: fadeIn 2s forwards;
        }

        /* Animacja pojawiania się artykułu */
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        /* Dodatkowe efekty w tle */
        .background-effect {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('https://example.com/ai-pattern.jpg') repeat;
            opacity: 0.2;
            pointer-events: none;
            z-index: -1;
            animation: moveBackground 12s linear infinite;
        }

        /* Ruchome tło */
        @keyframes moveBackground {
            0% {
                background-position: 0 0;
            }
            100% {
                background-position: 100% 100%;
            }
        }
    </style>
</head>
<body>

    <!-- Ruchome tło AI -->
    <div class="background-effect"></div>

    <div class="container">
        <h1>{{ article_title }}</h1>
        <div class="article-content">
            {{ article_body | safe }}
        </div>
    </div>

</body>
</html>
"""

# Przykład danych artykułu (np. wstawienie placeholderów obrazków)
article_body = article_body.replace("\n", "<br>")  # Zamiana nowych linii na <br>
article_body += """
<p><img src="image_placeholder_1.jpg" alt="Generuj obrazek przedstawiający pejzaż górski" /></p>
<p class="image-caption"><strong>Opis obrazka:</strong> Pejzaż górski z zielonymi wzgórzami i ośnieżonymi szczytami.</p>
<p><img src="image_placeholder_2.jpg" alt="Generuj obrazek przedstawiający zachód słońca nad morzem" /></p>
<p class="image-caption"><strong>Opis obrazka:</strong> Zachód słońca nad spokojnym morzem, z widokiem na plażę.</p>
"""

# Zapisanie pustego szablonu HTML (szablon.html)
with open('/content/szablon.html', 'w', encoding='utf-8') as file:
    file.write(html_template)

# Generowanie podglądu artykułu (podglad.html)
template = Template(html_template)
html_preview = template.render(article_title=article_title, article_body=article_body)

# Zapisanie pełnego podglądu artykułu (podglad.html)
with open('/content/podglad.html', 'w', encoding='utf-8') as file:
    file.write(html_preview)

print("Pliki 'szablon.html' i 'podglad.html' zostały wygenerowane.")
