# ICTA_Python_Osnovni_public

## Osnovne informacije

Trajanje: 10 tednov, 1x na tedn 
<br>
Izpit: Zadnji teden

Predavatelja: 
* **Gregor Balkovec** (<gregor.balkovec@fe1.uni-lj.si>)
* **Anže Glušič** (<anze.glusic@fe1.uni-lj.si>)

1 termin poteka 4 ure, 16:15 - 20:00. Vmes bomo imel nekaj pavzic, po potrebi.

## Termini

| Zaporedje | Datum      | Dan   | Tip |
| :-------: | :--------: | :---: | :---: |
| 1.        | 17.10.2022 | Pon   | Termin 1 |
| 2.        | 24.10.2022 | Pon   | Termin 2 |
| 3.        | 03.11.2023 | Čet   | Termin 3 |
| 4.        | 07.11.2022 | Pon   | Termin 4 |
| 5.        | 14.11.2022 | Pon   | Termin 5 |
| 6.        | 21.11.2022 | Pon   | Termin 6 |
| 7.        | 28.11.2022 | Pon   | Termin 7 |
| 8.        | 05.12.2022 | Pon   | Termin 8 |
| 9.        | 12.12.2022 | Pon   | Termin 9 |
| 10.       | 19.10.2022 | Pon   | Izpit    |


## Domače naloge

Vsak teden bomo imeli domače naloge iz tematik katere smo obravnavali na tečaju.

Namen domačih nalog je, da sami doma poizkušate rešiti problem, nato jih pošljete in jih mi pogledamo in vam povemo kje točno delate napake. Domače naloge so tudi nam indikator, kje se še kaj zatika in kaj bi bilo za ponoviti oziroma dodatno razložiti.

Naloge najdete v mapi DN pod posameznim poglavjem.

Naloge oddate preko email-a, kjer priložite datoteko z rešeno nalogo.

Zadeva email-a: \[DN-Python\] \<Termin\>\_Ime\_Priimek
> Primer: \[DN-Python\] Termin\_01\_Luka_Novak

Email pošljete na <gregor.balkovec@fe1.uni-lj.si> in <anze.glusic@fe1.uni-lj.si>.

## Izpit

Izpit bo potekal zadnji termin. Časa boste imeli vse 4 ure, vendar povprečno participanti potrebujejo približno 2 uri.

Na izpitu vam je dovoljeno vse - internet, lastni zapiski, naši zapiski, itd. Le komunikacija (pogovarjanje, ...) ni odvoljena.

Za uspešno opravljen izpit boste potrebovali vsaj 80% vseh točk. Po koncu tečaja dobite certifikat.

## Teorija in Zapiski predavanj
  
Zapiski predavanj bodo dostopni na GitHub-u, dodatna teorija pa je dostopna na potralu NetAcad.

### GitHub

Notri boste našli naše zapiske in razlage snovi, navodila za vaje in rešitve, domača naloga itd.

### NetAcad

Dodatna gradiva lahko najdete na NetAcad.

Vsi boste na emaile dobili povabilo k tečju. Predno lahko dostopate do gradiv morate izpolniti njihov "terms and services" in formo.


# Uporaba linterja in code formaterja
`flake` je Python linter. To pomeni, da nam omogoča hiter pregled kode in izpostavi kje so morebitne napake (syntax errors, pomoč pri styling-u kode po priporočilih PEP8, itd.)
Za inštalacijo flake v terminal vpišemo ukaz `pip install flake8`.
* [Flake dokumentacija](https://flake8.pycqa.org/en/latest/)

`black` je Python code formater. Black nam samodejno odstrani prazne vrstice na koncu kode, samodejno naredi razmake med matematičnimi operacijami (po priporočilih PEP8), samodejno naredi razmake med funkcijami, itd. Načeloma nam formatira kodo po PEP8 priporočilih, kar pomeni, da vsi pišemo v istem stilu. To pa naredi kodo bolj berljivo za druge programerje.
Za inštalacijo black v terminal vpišemo ukaz `pip install black`.
* [Black dokumentacija](https://pypi.org/project/black/)

**Za uporabo v VisualStudio Code**:

Da nam VS Code avtomatično uporabi naši novo-inštalirani knjižnjici moramo dodati te nastavitve v naš VS Code.

Znotraj mape kjer se nahaja naš projekt (kjer kliknemo *open with Code*) ustvarimo mapo `.vscode` in znotraj te mape ustvarimo datoteko `settings.json`.
```
new_folder/
├─ .vscode/
│  ├─ settings.json
├─ Termin01/
├─ Termin02/
├─ main.py
```

Znotraj `settings.json` definiramo naše nastavitve:
```
{
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true,
    "python.linting.flake8Args": [
        "--max-line-length=130",
    ],
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```
