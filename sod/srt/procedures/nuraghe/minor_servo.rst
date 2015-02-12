************
Servo Minori
************

.. _ms-emergency-stop:

Fare il reset degli emergency stop
==================================
Prima di espletare questa procedura bisogna accertarsi che vi siano le 
condizioni di sicurezza per fare il reset, ovvero che nessuno si trovi 
nei pressi dei servo minori (GRF, M3R, SRP, PFP).
Se vi sono le condizioni di sicurezza, si proceda con il reset. 

Il reset da remoto viene fatto...

Se per qualche motivo non è possibile fare il reset da remoto, lo 
si faccia in antenna tramite l'apposito *push buttom* presente nel fronte 
quadro del servo minore.

.. note:: Inserire immagine del pulsante in questione.

.. _ms_setup:

Fare il setup dei soli servo minori
===================================
Eseguire da *OperatoInput* il comando ``servoSetup=XXX``. Ad esempio, se si
vuole mettere in fuoco il ricevitore in banda C::

    > servoSetup=CCB

Nella console dei servo minori il flag ``starting`` dovrebbe diventare
verde, come mostrato in figure.

.. note:: Inserire immagine console servo con flag starting verde

Il setup termina quando il flat ``starting`` passa da verde a rosso (sono
necessari dai 2 ai 4 minuti, a seconda del setup). Se il setup è
andato a buon fine, nella console dei servo minori il campo 
``actualSetup`` riporta il codice del setup appena effettuato, e il flag
``ready`` diventa verde. Ad esempio, in figura X è mostrata la console
dei servo minori dopo che è stato concluso con successo un ``servoSetup=CCB``.

.. note:: Inserire immagine console servo con servoSetup=CCB done

Se il flag ``starting`` è diventato rosso ma il flag ``ready`` non
è diventato verde, allora c'é stato un problema con il setup. In questo
caso si consulti la sezione :ref:`ms-setup-problem`.

.. _mscu-restart:

Riavviare la MSCU
-----------------
Indicare come riavviare la MSCU. Fatto ciò, stoppare i container dei servo minori, chiudere la console dei
servo minori, riavviare i container dei servo minori, riavviare la console dei servo minori, fare il setup.


