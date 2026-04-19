<!-- BUTTON Github Codespaces Assignment-2 -->
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23293846)
<!-- BUTTON -->

### Harald Hammershaug
- Studentnummer: S374171
- E-post: S374171@oslomet.no

# DAFE1000 – Innlevering 2
Programmet finner Maksimum av f(x) = e^{-x/4} · arctan(x). Viser at toppunktet bestemmes av likningen
arctan(x) − 4/(1+x^2) = 0, finner toppunktet numerisk og plotter funksjonen.

## Analytisk (kort)
- f(x) = e^{-x/4} · arctan(x)
- f'(x) = e^{-x/4}[ -¼·arctan(x) + 1/(1+x^2) ]
- f'(x)=0 ⇔ arctan(x) − 4/(1+x^2) = 0 (dette gir toppunktets x-verdi)

## Numerisk (kort)
- Løser g(x) = arctan(x) − 4/(1+x^2) = 0 (biseksjon + Newton).
- Plotter f(x) og markerer toppunktet (x*, f(x*)).

## Kjøring
- Krever Python 3.8+
- Installer: `pip install -r requirements.txt`
- Kjør: `python main.py`
- Bildet lagres som `toppunkt.png`.

## Filer
- `main.py`: beregner x* og f(x*), og lager plottet
- `requirements.txt`: nødvendige Python-pakker
- `README.md`: denne beskrivelsen
- `toppunkt.png`: plott med toppunkt (opprettes ved kjøring)

## Resultater
```text
python main.py
x* = 1.6908
f(x*) = 0.6791
