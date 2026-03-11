# Informacja
Template na pewno wykorzystywany w mailach wysyłanych do kursantów poprzez panel instruktora kursu.

# Korzystanie
1. Modyfikujemy og_template_2013/modified/plain-hmtl.txt zgodnie z potrzebami.
2. Kopiujemy plik do scripts/ 
3. Uruchamiamy 
"python convert_html_to_one_line.html plain-text.html"
4. Kopiujemy plik stworzony przez skrypt do **Bulk_Email/Course email templates** do pola **Html template** pożądanego obiektu w panelu django.

# Skład repozytorium
## og_template_2013/original
Tutaj oryginalne pliki z kontenera jako źródłowy przykład
## og_template_2013/modified
Pliki zmodyfikowane - tak naprawdę podczas pracy nad szablonem modyfikujemy tylko plain-html.txt
## scripts
Katalog ze skryptem python który zmienia *plain-text.html* na jednoliniowy plik .html który następnie można wkleić jako template do panelu
administratora w zakładce **Bulk_Email/Course email templates** do obiektu, pola **Html template**. Skrypt posiada małe readme (wystarczy podać nazwę pliku wejściowego)
