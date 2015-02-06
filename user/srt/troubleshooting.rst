***************
Troubleshooting
***************

Stato dei servo minori *unknown*
================================

.. index:: minor servo, servoSetup, actualSetup, setupCCB, setupKKG, setupLLP
   unknown, emergency stop, failure, reset, GRF, M3R, SRP, PFP, MSCU

Problema
--------
Dalla console *OperatorInput* è stato eseguito il setup (comando ``setupXXX`` oppure ``servoSetup=XXX``)
ma dopo qualche minuto nella console *MinorServo* il flag ``starting`` è passato da verde a rosso ed il campo 
``actualSetup`` risulta ``unknown``.

.. note:: Inserire una immagine della console sei servo minori che mostra la situazione descritta.

Soluzione
---------
Su *acsCommandCenter* (macchina *nuraghe-mng*), controllare la finestra di log del container dei servo minori.

.. note:: Inserire immagine di tale finestra di log.

Ci sono quattro possibili soluzioni, a seconda del messaggio di errore riportato nella finestra di log: 

* se è riportato "**GFR (o SRP o M3R o PFP) in failure**", non ci si può far nulla, se non contattare il 
  responsabile degli impianti (G.Paolo Vargiu) per avvisarlo del malfunzionamento. Questo è un problema
  ricorrente, che spesso si risolve riarmando il differenziale nel quadro elettrico del servo minore
  in avaria
* se è riportato "**GFR (o SRP o M3R o PFP) in emergency stop**", si vada alla sezione :ref:`ms-emergency-stop`
* se è riportato un messaggio diverso dai precedenti, si vada alla sezione :ref:`mscu-restart`

.. _ms-emergency-stop:

Fare il reset delle emergenze
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prima di espletare questa procedura bisogna accertarsi che vi siano le condizioni di sicurezza
per fare il reset, ovvero che nessuno si trovi nei pressi dei servo minori (GRF, M3R, SRP, PFP).
Se vi sono le condizioni di sicurezza, si proceda con il reset. 

Il reset da remoto viene fatto...

Il reset può essere fatto anche in antenna, tramite l'appostito *push buttom* presente nel fronte 
quadro del servo minore.

.. note:: Inserire immagine del pulsante in questione.

Una volta fatto il reset, si può procedere eseguendo da *OperatorInput* il setup globale (``setupXXX``), 
oppure si può fare il setup del solo sistema dei servo minori, eseguendo il comando ``servoSetup=XXX``. In
questo ultimo caso, prima di procedere con l'osservazione si verifichi che tutti gli altri sottosistemi
siano configurati correttamente.


.. _mscu-restart:

Riavviare la MSCU
-----------------
Indicare come riavviare la MSCU. Fatto ciò, stoppare i container dei servo minori, chiudere la console dei
servo minori, riavviare i container dei servo minori, riavviare la console dei servo minori, fare il setup.

Problemi di puntamento
======================

.. index:: minor servo, SRP, MSCU

Problema
--------
Descrivere l'anomalia... La console deve riportare il setup corretto.

Soluzione
---------
Possibilita':

* container servo giu'
* failure SRP
* messaggio errore differente da failure, in questo caso :ref:`mscu-restart`
