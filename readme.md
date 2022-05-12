# PVA2 - Programování a vývoj aplikací
## Cvičení 17: Týmové cvičení


### 1
Vytvořte třídu pro práci s rodným číslem.

a) Při inicializaci objektu ověřte pomocí regulárních výrazů vstup uživatele. Pokud rodné číslo nebude odpovídat tvaru rrmmdd/xxxy inicializujte výjimku. 

b) Ve třídě definujte metodu jeSpravne, která bude kontrolovat správnost rodného čísla. Návratová hodnota bude true je-li validní. V opačném případě false.

c) Definujte funkci pohlavi, která z rodné čísla vrátí pohlaví. Návratová hodnota M pro muže a Z pro ženy.

d) Definujte funkci datumNarození, která z rodného čísla vrátí datum narození. Návratová hodnota bude typu date.

e) Definujte libovolné dva objekty a ověřte funkčnost jednotlivých funkcí. Pro testovací účely nepoužívejte své rodné číslo!

c) Pomocí funkce getVek vypočítejte ze zadaného rodného čísla věk.

Požadavky na rodné číslo
* číslo má 10 znaků
* číslo je beze zbytku dělitelné 11
* první dvojčíslí je rok narození
* druhé dvojčíslí je měsíc narození, u žen se přičítá 50
* třetí dvojčíslí je den narození
* číslo za lomítkem je pořadí narození toho dne
* poslední číslo je kontrolní číslize přiřazená dle ostatních čísel

Příklad:
* 705425/1234 – jedná se o ženu narozenou 25.4.1970
* 700425/9876 – jedná se o muže narozeného 25.4.1970

Generátor rodných čísel: https://webdev.zaujimave.info/generator-rodneho-cisla

### 2
Pro aplikaci vytvořte GUI. Uživatelé budou po zadání rodného čísla zjišťovat:
* pohlaví
* datum narození
* věk

### 3
Každá správná aplikace musí mít dokumentaci. Připravte ji.
