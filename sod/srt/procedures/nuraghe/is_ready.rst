.. _nuraghe-is-ready:

********************************
Verificare che Nuraghe sia ready
********************************
La situazione è questa: il SoD ha avviato Nuraghe, seguendo l'attuale *Nuraghe from
scratch* o qualcosa di simile. Fatto ciò, non siamo ancora sicuri che il
sistema sia ready. Infatti il SoD a questo punto potrebbe verificare che tutti 
i container siano su e anche avviare le console, ma tutto questo non garantirebbe 
che il setup vada a buon fine. Alcuni motivi:

* c'è un reset globale delle emergenze (non previsto nel setup)
* c'è un reset da fare nei servo minori
* un servo minore è in failure
* le schede dei ricevitori non sono raggiungibili perché ci si è dimenticati
  di chiudere il tool di diagnostica
* il backend che si dovrebbe utilizzare è spento

Se siete d'accordo, ho in mente un check che risolva buona parte di tutto questo
in un unico comando da lanciare da shell prima di ``nuragheConsole``. Ad esempio,
se chiamiamo questo comando ``telescopeCheck``, nel caso in cui tutto sia OK::

    $ telescopeCheck
    OK

Se c'è da fare un ``antennaReset`` (leverei il comando dalla *OperatorInput*, e
lo metterei in carico al SoD --posso fare in modo che venga lanciato da shell-- in
modo da separare ancora meglio i ruoli)::

    $ telescopeCheck
    ERROR
    An emergency stop reset is required.
    You should execute antennaReset (please, be careful)
    $ antennaReset
    Reset successfully sent

Ora abbiamo risolto questo primo problema, però ci sono altre condizioni
che potrebbero non consentire un setup corretto. Non possiamo fare un check del
backend, perchè ancora non sappiamo quale vorrà usare l'utente. Possiamo però
avvisare il SoD::

    $ telescopeCheck
    WARNING
    The total power backend is not online. 
    Fix the problem if you have to use it.

