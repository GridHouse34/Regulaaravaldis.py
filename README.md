# Regulaaravaldis.py
Laeb https://kpkoda.ee/kohtutaiturid/kohtutaiturid-kontakt/ veebilehelt infot kasutades .py koodi

Koodi põhimõtte on kasutada .py-d, et laadida veebilehelt kohtutäiturite andmeid (nimed & e-mailid).

<pre>import re
import requests
</pre>
"requests" on vaja, et veebilehe sisu võtta all oleva koodi jaoks.

<pre>url = "https://kpkoda.ee/kohtutaiturid/kohtutaiturid-kontakt/"
response = requests.get(url)
html = response.text</pre>
url: veebilehe aadress

response: saadab HTTP-päringu sellele aadressile ja saab vastuseks kogu lehe sisu.

html: annab päringu vastuse HTML-teksti kujul (ehk kogu lehe koodi).

<pre>pattern = re.compile(r'([A-ZÕÄÖÜ][a-zõäöü]+ [A-ZÕÄÖÜ][a-zõäöü\-]+).*?([\w\.-]+@[\w\.-]+\.\w+)', re.S)</pre>
([A-ZÕÄÖÜ][a-zõäöü]+ [A-ZÕÄÖÜ][a-zõäöü\-]+)
Püüab nime kujul “Eesnimi Perenimi”:

[A-ZÕÄÖÜ] – algab suure tähega (ka eestikeelsed tähed on lubatud).

[a-zõäöü]+ – järgneb vähemalt üks väiketäht.

[A-ZÕÄÖÜ][a-zõäöü\-]+ – teine sõna (perekonnanimi), mis algab suure tähega ja võib sisaldada ka sidekriipsu.

.*? – “võimalikult vähe” suvalisi märke (et jõuda järgmise mustrini).
Seda kasutatakse selleks, et nimi ja e-post võivad HTML-is olla teineteisest eraldatud muu tekstiga.

([\w\.-]+@[\w\.-]+\.\w+)
Püüab e-posti aadressi kujul midagi@midagi.midagi.

re.S (ehk re.DOTALL)
Muudab . (punkti) käitumist nii, et see vastaks ka reavahetustele (tavaliselt mitte).

<pre>matches = pattern.findall(html)</pre>
pattern.findall(html): otsib kõik kohad, kus HTML vastab määratud mustrile.

<pre>seen = set()
for name, email in matches:
    if (name, email) not in seen:
        seen.add((name, email))
        print(f"{name};{email}")</pre>
seen = set() – luuakse tühi hulk (set), kuhu salvestatakse juba leitud (nimi, epost) paarid.
Hulk tagab, et duplikaadid ei korduks.

Tsükkel for name, email in matches: – käiakse kõik leitud vasted läbi.

if (name, email) not in seen: – kontrollib, kas seda paari pole varem leitud.

seen.add((name, email)) – lisab paari hulka, et see tulevikus enam ei korduks.

print(f"{name};{email}") – väljastab tulemuse formaadis

e
