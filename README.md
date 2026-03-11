# Informacja
Template na pewno wykorzystywany w mailach wysyłanych do kursantów poprzez panel instruktora kursu.

# Korzystanie
1. Modyfikujemy og_template_2013/modifying/plain-hmtl.txt zgodnie z potrzebami.
2. Uruchamiamy 
"python convert_html_to_one_line.html plain-text.html"
3. Kopiujemy plik stworzony przez skrypt do **Bulk_Email/Course email templates** do pola **Html template** pożądanego obiektu w panelu django.

# Skład repozytorium
## og_template_2013/original
Tutaj oryginalne pliki z kontenera jako źródłowy przykład
## og_template_2013/modified
Pliki zmodyfikowane i skrypt pomocniczy zamieniajacy plik .html na odpowiedni format (jednoliniowy)
