import re
import sys
import os

def print_help():
    print("Uzycie: python make_oneliner.py <input_file> [output_file]")
    print("  <input_file>: Sciezka do pliku HTML (wymagane)")
    print("  [output_file]: Nazwa pliku wynikowego (opcjonalne, domyslnie: oneliner_out.txt)")

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "oneliner_out.txt"

    if not os.path.exists(input_path):
        print(f"Blad: Plik '{input_path}' nie istnieje.")
        sys.exit(1)

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = f.read()

        # Usuwanie znakow nowej linii i nadmiarowych spacji
        content = re.sub(r'\s+', ' ', data)
        # Usuwanie spacji miedzy tagami
        content = re.sub(r'>\s+<', '><', content)
        content = content.strip()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Wygenerowano: {output_path}")

    except Exception as e:
        print(f"Blad procesowania: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()