Aplikacja do generowania podglądu artykułu

Opis
Aplikacja pozwala na generowanie podglądu artykułu w formacie HTML, gdzie tekst artykułu jest automatycznie przekształcany na stronę internetową. Aplikacja umożliwia dynamiczne wczytywanie artykułu z pliku tekstowego, wyświetlanie go w estetycznym formacie z tłem nawiązującym do sztucznej inteligencji oraz efektami wizualnymi. Strona zawiera również możliwość wstawiania placeholderów dla obrazków w artykule, co pozwala na przyszłe generowanie grafik.

Funkcjonalności:
1. **Wczytywanie artykułu** - Aplikacja wczytuje artykuł z pliku tekstowego (`artykul.txt`).
2. **Szablon HTML** - Aplikacja generuje pusty szablon HTML (`szablon.html`), gotowy do wklejenia artykułu.
3. **Podgląd artykułu** - Na podstawie artykułu generowany jest pełny plik podglądu HTML (`podglad.html`), który zawiera odpowiednią strukturę i formatowanie.
4. **Efekty wizualne** - Na stronie artykułu zastosowano różne efekty CSS, takie jak tło związaną z AI, subtelne animacje, powiększanie obrazków po najechaniu kursorem, oraz animację pojawiania się treści.

Wymagania:
- Python 3.x
- Zainstalowane biblioteki:
  - `jinja2`

Instrukcja uruchomienia

1. **Pobierz repozytorium:**
   Jeśli jeszcze tego nie zrobiłeś, pobierz repozytorium na swoje lokalne urządzenie:
   ```bash
   git clone https://github.com/TwojeRepozytorium.git
   cd TwojeRepozytorium
