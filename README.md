# Match Analyzer

Match Analyzer är ett Python-projekt för att analysera fotbollsmatcher baserat på CSV-data.
Projektet fokuserar på enkla men meningsfulla analyser av matchutfall, såsom målstatistik
och frekvenser för olika typer av resultat.

Syftet är både att träna på systematisk Python-utveckling och att bygga ett tydligt,
utbyggbart analysverktyg.

---

## Funktionalitet (nuvarande och planerad)

Projektet är uppdelat i tydliga steg och moduler.


### Nuvarande funktionalitet
- Läsa matchdata från CSV-filer
- Skriva analyserade resultat till nya CSV-filer
- Centraliserad logging (konsol + fil)
- Tydlig projektstruktur med separata moduler


### Planerad funktionalitet
- Analys av:
  - Snittmål per liga
  - Andel matcher över / under 2.5 mål
  - Hur ofta båda lagen gör mål (BTTS)
  - Home vs Away-mål
- Kommando-rad-gränssnitt (CLI)
- Tydligare rapportering av analysresultat

---

## Datamodell

Varje rad i CSV-filen representerar **en match** och ska innehålla följande kolumner:

```text
league,date,home_team,away_team,home_goals,away_goals



## Projektstruktur
....


## Installation
....


## Versionshantering
- Projektet använder Git
- Utveckling sker via feature branches
- Main branch är den version som innehåller stabil kod
- Varje funtion utvecklas och mergas separat


## Mål med projektet
- Lära sig bygga ett strukturerat Python-projekt
- Träna på Git, branches och commits
- Skriva tydlig, läsbar och testbar kod
- Bygga analyser baserade på verklig data


## Status
Projektet är under aktiv utveckling
