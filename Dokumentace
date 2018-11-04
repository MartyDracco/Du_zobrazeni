# Kartografické zobrazení - domácí úkol 1

### Zadání
---
Úkolem je vytvořit program, který na základě zadaných parametrů vypočítá vzdálenosti poledníků a rovnoběžek od středu tak, jak bychom je zaznamenávali při kartografickém cvičení na papír.
Program obsahuje volitelné parametry jako je poloměr Země a měřítko mapy.
Všechna výsledná čísla budou vypočtena v cm s přesností na mm, tedy s jedním desetinným číslem.
Program vypočítá vzdálenosti poledníků a rovnoběžek pro následující válcová zobrazení:
- Lambertovo zobrazení
- Marinovo zobrazení
- Braunovo zobrazení
- Mercatorovo zobrazení
 
 ### Popis programu
---
Do programu je možné zadat tyto povinné parametry:

- Měřítko mapy
- Typ zobrazení
- Poloměr Země

Dále obsahuje volitelné parametry:

- Interval souřadnic mezi poledníky a rovnoběžkami
- Počet poledníků a rovnoběžek

Pokud uživatel zadá 0 do vstupu volitelných parametrů, budou použity jejich základní hodnoty, tedy program vypočítá 18 poledníků a 9 rovnoběžek v intervalu 10° v obou směrech od středu.

Výpočet souřadnic probíhá vždy podle stanoveného vzorce pro dané zobrazení.
- Pro Lambertovo zobrazení je výpočet pro poledníky x = R * v , pro rovnoběžky y = R * sin u
- Marinovo zobrazení x = R * v, y = R * u
- Braunovo zobrazení x = R * v, y = 2 * R * tg(u/2)
- Mercatorovo zobrazení x = R * v, y =  1/2 * ln ((1+sin(u))/(1-sin(u)))

### Nekorektní vstupy
---
Program se ukončí, jestliže uživatel zadá hodnotu, se kterou v dalších výpočtech nelze počítat, nebo která by znamenala kartograficky nekorektní výstupy v dalších výpočtech.
Program se ukončí, pokud uživatel zadá záporné číslo pro následující parametry:
- Měřítko mapy
- Poloměr Země
- Interval mezi poledníky a rovnoběžkami
- Počet poledníků a rovnoběžek

Program se také ukončí, pokud uživatel zadá nulu do měřítka mapy.
Pokud výsledek výpočtu zobrazení přesáhne 1 metr, program vypíše - (pomlčku) místo výsledné vzdálenosti.
### Použitý programovací jazyk
---
Program na výpočet zobrazení byl vytvořen v Pythonu 3.4 a k jeho vytvoření sloužilo prostředí programu Pycharm.
### Licence programu
---
Program byl vytvořen pouze pro studijní účely, jakékoli obohacení na základě komerčního použití tohoto programu je zamítnuto autorem.
