# Programmeerplatform<br><small>Studiewijzer Fulltime, lente 2022</small>

In dit vak maak je kennis met verschillende platforms om programmeerproblemen aan te pakken. Dit is een breed vak met een focus op het gebruiken tools en technieken uit de professionele wereld. De platforms zijn geschikt om uiteenlopende problemen te benaderen, van dataverwerking tot aan webprogrammeren. Soms gebruik je één platform voor een probleem en soms kun je er meerdere samen gebruiken. Daarnaast word je bekend met Unix en allerlei verschillende command-line tools zodat je steeds beter grip hebt op jouw ontwikkelomgeving. Gedurende het hele vak bouw je ervaring op met versiebeheer via git en kom je in aanraking met allerlei tools en technieken om betere code te schrijven, zoals linters, unit testing, type checkers en profilers.

## Voorkennis

Programmeren 1 en Programmeren 2 moet je helemaal gehaald hebben vóór je deze cursus start.

## Onderwerpen en deadlines

Er komen modules voorbij met uiteenlopende onderwerpen. Dit vak start razendsnel, dus zorg dat je die eerste deadline niet mist! Er is geen mogelijkheid tot verder uitlopen dan de genoemde datums.

| Onderwerp | **Uiterste deadline**{: style="hyphens: none; white-space: nowrap; font-weight: bold;"} |
| - | -: |
| **Git, Web en SQL**, het opzetten van een ontwikkelomgeving, het gebruik van git, het opzetten van een webpagina en het gebruik van SQL | 5 april 2022 |
| **Datastructuren**, afwegingen maken tussen het gebruik van verschillende datastructuren en de invloed op de computationele complexiteit | 8 april 2022 |
| **Data & Scraping**, data verwerken in Python met Pandas; en geautomatiseerd data vergaren vanaf het web | 12 april 2022 |
| **Data Processing**, automatisch data vergaren vanaf het web en deze transformeren en visualiseren | 15 april 2022 |
| **Codekwaliteit**, stijl op orde krijgen met linters, type checkers; en run-time performance analyseren en verbeteren met profilers | 19 april 2022 |
| **Testing**, geautomatiseerd testen van de correcte werking van je eigen programma's | 22 april 2022 |

## Docenten en contact

Je docent is Jelle van Assema.

- Er zijn iedere week twee **werkcolleges op locatie**. De tijden en locatie vind je op <https://datanose.nl/103382.course>. Het is _verplicht_ één van beide bij te wonen, behalve in uitzonderlijke situaties (het volgen van andere vakken is geen uitzonderlijke situatie). Deze bijeenkomsten zijn verreweg je beste mogelijkheid voor hulp; zowel voor moeilijke bugs als "ik weet niet hoe te beginnen".
- Voor **vragen over regeltjes**, het maken van persoonlijke afspraken en het op de hoogte houden van de docenten over je voortgang stuur je een mail naar <help@mprog.nl>.

## Minimumeisen

Een flink deel van de opdrachten netjes af en werkend inleveren is de eerste eis om het vak te halen. Daarnaast is het nodig dat je _zichtbaar_ actief meedoet en leert van het vak. Dat doe je onder andere op de volgende manieren:

1. meedoen aan minimaal één werkcollege per week
2. actief vragen stellen en hulp vragen
3. het bijhouden van een procesboek
4. laag scoren op de "plagiaatschaal"

Op die manier kunnen we een goed beeld vormen van jouw voortgang en constateren dat je aan de leerdoelen van het vak hebt voldaan. Er is daarom ook niet voorzien in een schriftelijk tentamen. Dat is natuurlijk een prettig einde van het vak, maar legt wel meer verantwoordelijkheid bij jou om zichtbaar te leren.

## Cijfers

Voordat je een eindcijfer kunt krijgen moet je alle opdrachten werkend hebben ingeleverd en aan alle bovengenoemde verwachtingen hebben voldaan, tenzij je een _schriftelijke_ uitzondering hebt gekregen van de examinator of coördinator. Voel je vrij om te overleggen of jouw omstandigheden een uitzondering rechtvaardigen (via een mail naar help@mprog.nl). We denken graag mee!

De cursus bestaat uit modules (weken). Alle modules tellen even zwaar mee voor het eindcijfer. Als je een module niet volledig en correct werkend inlevert op de bovenvermelde deadline krijg je *geen* punten voor die week. Er is geen mogelijkheid om het werk nog in te halen voor punten.

| Week 1a               |             |
| --------------------- | ------------|
| Homepage              | 1--2 punten |
| Movies                | 1 punt      |
| Fiftyville            | 1 punt      |

Homepage: 1 punt als *precies* aan alle eisen in de opdracht is voldaan. 2 punten bij een exceptionele website. Exceptioneel is significant meer moeite in de opdracht gestoken en duidelijk verder gegaan dan de geboden stof.

| Week 1b                |                                        |
| ---------------------- | -------------------------------------- |
| Complexity questions 1 | 1 punt voor (vrijwel) goede antwoorden |
| Complexity questions 2 | 1 punt voor (vrijwel) goede antwoorden |
| Jaccard                | 1 punt voor een goede implementatie    |
| Indexing Words         | 1--2 punten                            |

Indexing Words: 1 punt als het programma werkt, maar de runtime complexiteit verder omlaag kan, 2 punten als het programma werkt en de runtime complexiteit niet verder omlaag kan.

| Week 2a               |             |
| --------------------- | ----------- |
| Pandas                | 2 punten    |
| Scraping              | 2--3 punten |

Scraping: 2 punten voor een goede (correcte en redelijk nette) implementatie, 3 punten voor een excellente implementatie (uitgebreid gedocumenteerd, consistente stijl).

| Week 2b               |                                          |
| --------------------- | ---------------------------------------- |
| Transforming          | 1 punt                                   |
| Visualizing           | 2 punten                                 |
| Crawling              | 4 punten (2 correctness, 2 design/style) |

Bij deze module geldt dat alle code op een Pandas-achtige manier moet zijn geschreven. Hierbij schrijf je relatief weinig loops maar laat je operaties over aan Pandas. Voorwaarde voor het geven van punten bij deze module is dat gebruik is gemaakt van de mogelijkheden die Pandas biedt (omdat de module hier over gaat).

Crawling: 2 punten voor een goede (correcte en redelijk nette) implementatie, 4 punten voor een excellente implementatie (uitgebreid gedocumenteerd, consistente stijl).

| Week 3a                        |          |
| ------------------------------ | -------- |
| Linters: style                 | 2 punt   |
| Linters: cyclomatic complexity | 2 punt   |
| Type Checkers                  | 2 punt   |
| Profilers: Sudoku              | 6 punten |

Linters en Type Checkers worden alleen op correctheid (en eventuele uitleg) nagekeken, maar een zekere minimum netheid wordt altijd vereist. Profilers: 1 punt voor iedere goed onderbouwde aanpassing.

| Week 3b  |          |
| -------- | -------- |
| Rotate   | 3 punten |
| Tennis   | 5 punten |
| Cash     | 5 punten |

Opdrachten worden alleen op correctheid nagekeken, maar een zekere minimum netheid wordt altijd vereist. Rotate: 3 punten bij 7 correcte tests. Tennis: 4 punten voor correcte voorgeschreven tests, 5 punten als ook een zinvolle extra test is toegevoegd (met uitleg). Cash: 0.5 punt per goed onderbouwd antwoord.

**Herhaling: alle modules tellen even zwaar mee voor het eindcijfer.** Dus het heeft geen zin om alle punten van alle modules bij elkaar op te tellen!

## Procesboek

Tijdens het volgen van het vak hou je een procesboek bij, waarin je per opdracht documenteert welke dingen je hebt geleerd die jou opvielen, maar ook welke bronnen je hebt gebruikt en wat voor soort hulp je hebt gevraagd: opstarten, nare bugs, ideeën opdoen? Allemaal vermelden!

## Samenwerken

Je mag met je medestudenten (en anderen) communiceren in het Nederlands of Engels over je werk in deze cursus, maar niet in de vorm van meer dan een paar regels Python, JavaScript, HTML en dergelijke talen. Als je twijfelt of je manier van werken in deze correct is, neem gerust contact op met de docenten.

### Citeren en hulpbronnen

Je mag gerust op het web zoeken naar uitleg die verder gaat dan de colleges en andere materialen die in de cursus bijgeleverd zijn, en je mag op zoek naar oplossingen voor technische problemen waar je tegenaan loopt, maar je mag zeker geen oplossingen voor onderdelen van de opdrachten overnemen om aan de eisen te voldoen. Daarnaast moet je bij het geheel of gedeeltelijk overnemen van codefragmenten of werken via tutorials en dergelijke altijd een precieze bronvermelding doen.

### Officiële regels

Wat betreft fraude en plagiaat volgen we in deze cursus de richtlijnen van de Universiteit van Amsterdam en de werkwijze van de bachelor Informatica. De richtlijnen kun je [hier vinden].

[hier vinden]: http://student.uva.nl/az/a-z-lijst/a-z-lijst/content/folder/fraude-plagiaat-en-bronvermelding/plagiaat-en-fraude.html

## Herkansen

Bij dit vak gaat herkansen vooral over de situatie waarin je stopt met opdrachten maken of erg gaat achterlopen. Het is niet mogelijk opdrachten nog in te leveren na de deadlines die genoemd zijn in deze studiewijzer.

Herkansen kan daarom de eerstvolgende keer dat het vak wordt gegeven in het **volgende semester**. Dit vak wordt echter vanaf september 2022 vervangen door een ander vak. Je kunt dus niet zomaar alle opdrachten meenemen.
