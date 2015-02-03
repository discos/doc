.. highlight:: cpp

.. _backend_protocols:

*****************
Backend protocols
*****************

Scrivo in italiano che facciamo prima, poi quando ci siamo accordati traduco e
scrivo il documento finale.

Introduzione
============
Lo scopo è definire un protocollo per comunicare con il *sistema ROACH2*
(d'ora in avanti SR2), ovvero il sistema che prende in ingresso delle 
richieste, esegue delle azioni sulla ROACH2 e da indietro una risposta.

La comunicazione non prevede uno scambio di grandi quantità di informazioni. I dati
infatti abbiamo detto che verranno scritti direttamente dal SR2, il quale
recupera le informazioni dell'antenna e il relativo timestamp da un 
FITS appositamente scritto da Nuraghe. Cio' significa che possiamo utilizzare
un protocollo testuale.

Detto ciò, l'idea è qualla di definire un protocollo generico, in modo
da scrivere la libreria una volta, e utilizzarla anche per futuri backend
o altri dispositivi che lo implementano. Ci occorre:

1. impostare qualcosa (*set*)
2. leggere qualcosa (*get*)


Request-response socket
=======================
Possiamo definire dei caratteri di inizio e fine comando. In più potrebbe
essere utile indicare anche un ID del comando. Con un esempio ci capiamo
meglio. Consideriamo il metodo ``.setSection()``::

   void setSection(
       in long input,
       in double freq,
       in double bw,
       in long feed,
       in long pol,
       in double sr,
       in long bins
   );

Supponiamo di chiamare questo metodo nel seguente modo::

    setSection(11, 22, 33, 44, 55, 66, 77);

Questa chiamata viene tradotta nel seguente comando, da inviare al
sistema backend::

    #set:99:section:11,22,33,44,55,66,77\n

Dove ``99`` è l'ID del comando. La risposta relativa potrebbe essere::

    #set:99:OK\n
    #set:99:KO:Error message here\n

.. note:: Può essere utile definire gruppi di parametri? Ad esempio, nel caso
   in cui un metodo nella IDL definisca una sequenza, come in questo caso::

       setPosition(doubleSeq position, time);

   se la posizione è ``(1, 1, 1)``, e il tempo è ``0``::

       #set:100:position:[1,1,1],0\n


Se vogliamo ottenere una richiesta, usiamo un comando ``getSomethig(t)``
che restituisce il valore della grandezza *something* al tempo ``t``::

    #get:101:something:t\n

La risposta potrebbe esser::

    #get:101:timestamp,par1,par2,par3\n

Dove ``timestamp`` è il tempo di processamento della risposta da parte
del sistema backend.


HTTP
====
Oppure, visto che in questo modo stiamo praticamente reinventando la ruota,
che dite se usiamo direttamente qualcosa di pronto, come HTTP?
In questo caso abbiamo un sacco di opzioni e tutto pronto (anche lato 
server, ci sarebbe solo da mappare le API REST agli script eseguiti dal SR2).

Inoltre avremo multiclient, e potremmo scambiare anche informazioni complesse,
di più alto livello, come ad esempio un content-type application/json.
Lo svantaggio rispetto al primo caso è che è più pesante.



