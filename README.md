Projekt
=========

## Instalace projektu

Instalace se provádí pouze při pokusu o spuštění na cizím PC. Instalace předpokládá, že je na počítačí nainstalovaný yarn (node) a docker.

1. `yarn install`
2. `yarn build`
3. `docker-compose build`
4. `docker-compose up`
4. Naimportovat dump databáze ze souboru dump-postgres-202109131506 do databáze 

*pro připojení do databáze lze použít následující údaje*:

* host: localhost
* port: 5432
* user: postgres
* pass: 123456

## spuštění aplikace

1.  Otevřít CMD v kořenovém adresáři s projektem: `docker-compose up`

## Úpravy

Při úpravách obecně v python šablonách je nutné vždycky rebuildnout celý docker (aby se dostaly upravené šablony do dockeru). 

## Úpravy v reactu

Pokud budeme chtít dělat úpravy v reactu (modálu pro zobrazování notifikace), tak musíme dát vždycky následující sekvenci příkazů (hned po uložení souboru), aby se nám projevily změny (pozn.: Je možné, že prohlížeč může mít nacachované javascripty a tak je možná dobrý pak udělat hard reload stránky CTRL + SHIFT + R)

1. `yarn build` - vytvoří produkční minifikovaný a transpilovaný javascript, který se načítá na stránce
2. `docker-compose build` - přebuildí backend aplikace - tím se zkopíruje do dockeru ten zbuilděný soubor
3. `docker-compose up` - spustí aplikaci