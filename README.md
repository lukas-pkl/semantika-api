# semantika-api
An API to make using Lithuanian lemmatizer from [semantika.lt](https://semantika.lt/Help/Info/Solutions) easier.

## Using 

* Bring up the application

```bash
[sudo] docker-compose up
```

* Use the API to lemmatize texts

```python
import requests 
import json

text = """
Vilniaus universitetas (trumpiau – VU) – seniausias ir didžiausias Lietuvos universitetas. Įkurtas 1579 m. Vilniuje jėzuitų po Lietuvos Didžiosios Kunigaikštystės kunigaikščio Stepono Batoro privilegijos suteikimo.

Būdamas vienu seniausių ir žymiausių Vidurio ir Rytų Europos aukštųjų mokyklų, universitetas darė didelę įtaką ne tik Lietuvos, bet ir kaimyninių šalių kultūriniam gyvenimui, išugdė ne vieną mokslininkų, poetų, kultūros veikėjų kartą. Universitete profesoriavo ir mokėsi daug garsių asmenybių: medikai vokiečiai Johanas Frankas ir jo sūnus Jozefas Frankas, istorikas Joachimas Lelevelis, poetai Adomas Mickevičius ir Julius Slovackis, istorikas Simonas Daukantas, rašytojas, poetas ir literatūros mokslininkas Česlovas Milošas.

XVI a. VU įkurtas sklindant renesanso, reformacijos ir katalikiškosios reformos idėjoms. Už VU anksčiau Rytų Europoje įkurti tik Prahos, Krokuvos, Pečo, Budapešto, Bratislavos ir Karaliaučiaus universitetai.


Šiuo metu VU yra Europos universitetų Magna Charta signataras, Tarptautinės universitetų asociacijos, Europos universitetų asociacijos, Baltijos universitetų rektorių konferencijos, tarptautinių Utrechto, UNICA ir Baltijos jūros regiono universitetų tinklo narys. Nuo 2016 m. sausio 1 d. VU pakviestas į prestižinių universitetų tinklą – Koimbros grupę, o nuo 2019 m. priklauso Europos universitetų aljansui „ARQUS“. 2021 m. sausio 1 d., reorganizavus Šiaulių universitetą, įkurtas kamieninis akademinis padalinys – Šiaulių akademija.


"""

data = {"text":text}
url = "http://localhost/lemmatize"
result = requests.post(url, data=data)

prnt(json.loads(result.text))
```
