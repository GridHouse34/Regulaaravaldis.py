import re
import requests

# Lae lehe sisu
url = "https://kpkoda.ee/kohtutaiturid/kohtutaiturid-kontakt/"
response = requests.get(url)
html = response.text

# Regulaaravaldis, mis püüab nime ja e-posti
# Nimed on kujul "Eesnimi Perenimi" ja e-post midagi@midagi
pattern = re.compile(r'([A-ZÕÄÖÜ][a-zõäöü]+ [A-ZÕÄÖÜ][a-zõäöü\-]+).*?([\w\.-]+@[\w\.-]+\.\w+)', re.S)

# Leia kõik vasted
matches = pattern.findall(html)

# Eemaldame duplikaadid ja vormindame
seen = set()
for name, email in matches:
    if (name, email) not in seen:
        seen.add((name, email))
        print(f"{name};{email}")
