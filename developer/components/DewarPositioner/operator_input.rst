.. highlight:: discos

.. _oi:

*********************
Guida per l'astronomo
*********************
In questa sezione viene descritto come interagire con il ``DewarPositioner``
tramite la sua console di *operator input*. Per avviare tale console, si esegua
il comando ``operatorIpunt`` specificando come target 
``RECEIVERS/DewarPositioner``::

    $ operatorInput RECEIVERS/DewarPositioner

.. _oisetup:

Esecuzione del setup
====================
Il ``DewarPositioner`` gestisce tutti i derotatori alla stessa maniera, 
per cui in fase di *setup* è necessario indicare il codice del derotatore
che si intende utilizzare. Il setup viene eseguito con il comando
``derotatorSetup``::

   > derotatorSetup=CODE

I codici sono i medesimi che vengono utilizzati per effettuare il setup 
dell'antenna.
Ad esempio, se si vuole utilizzare il derotatore del ricevitore
in banda K di SRT::

    > derotatorSetup=KKG

Al termine del *setup* il derotatore sarà pronto per essere utilizzato. Il
comando ``derotatorGetActualSetup`` restituisce il setup attuale, mentre il
comando ``derotatorIsReady`` ci dice se il derotatore è pronto per essere
movimentato::

    > derotatorGetActualSetup
    KKG
    > derotatorIsReady
    True

Durante il *setup* al derotatore viene comandata la posizione ``0``, che è 
quella scelta per l'allineamento iniziale. Ad esempio, per il il derotatore del
ricevitore in banda K di SRT, la posizione iniziale è quella in cui i tre feed
3, 0, 6 sono paralleli all'orizzonte, con il feed 3 a est.

Possiamo verificare la posizione con il comando ``derotatorGetPosition``::

    > derotatorGetPosition
    0.0084d

La ``d`` sta ad indicare che il valore numerico rappresenta un angolo 
espresso in gradi decimali.

.. note:: Il valore restituito potrebbe essere diverso da zero, per qualche 
   cifra decimale, come nell'esempio appena mostrato. Questo è normale, ed è 
   dovuto al fatto che il movimento del motore avviene a step, per cui i 
   valori di posizionamento sono discreti.

Il *setup* infine imposta i valori di default per la configurazione e la 
modalità di riavvolgimento::

    > derotatorGetConfiguration
    FIXED
    > derotatorGetRewindingMode
    AUTO

Parleremo delle configurazioni e del riavvolgimento nelle prossime sezioni.

.. _oiconfigurations:


Configurazione 
==============

Il ``DewarPositioner`` ha sette configurazioni:
:ref:`fixed <fixed>`,
:ref:`best space coverage <bsc>`, :ref:`bsc optimized <bsc_opt>`,
:ref:`custom <custom>`, :ref:`custom optimized <custom_opt>`, *aligned*
e *aligned optimized*.
Il comando ``derotatorSetConfiguration`` consente all'utente di impostare
la configurazione desiderata, mentre il comando ``derotatorGetConfiguration``
di leggerla::

    > derotatorSetConfiguration=FIXED
    > derotatorGetConfiguration
    FIXED
    > derotatorSetConfiguration=CUSTOM
    > derotatorGetConfiguration
    CUSTOM

Le configurazioni *aligned* e *aligned_opt* non sono al momento 
disponibili::

    > derotatorSetConfiguration=ALIGNED
    Error - configuration ALIGNED not available

Vediamo ora nel dettaglio le varie configurazioni, suddividendole in
:ref:`statiche <statics>` e :ref:`dinamiche <dynamics>`.


.. _statics:

Configurazioni *statiche*
-------------------------
Nelle configurazioni statiche la posizione del derotatore non cambia al
variare della posizione dell'antenna o dell'asse di scansione.


.. _fixed:

Configurazione *fixed*
~~~~~~~~~~~~~~~~~~~~~~
In questa configurazione, che è quella che viene impostata per default dal
*setup*, la posizione del derotatore viene mantenuta
fissa al variare della posizione dell'antenna, e questo è il motivo 
per cui le è stato assegnato il codice identificativo ``FIXED``. 

Nella configurazione ``FIXED`` è possibile impostare la posizione del
derotatore utilizzando il comando ``derotatorSetPosition``::

    > derotatorSetConfiguration=FIXED
    > derotatorSetPosition=30d
    > derotatorGetPosition
    30d

Se il derotatore si trova in una certa posizione :math:`P_x` e viene impostata
la modalità ``FIXED``, viene tenuta la posizione :math:`P_x`. Il derotatore quindi
non viene riportato in posizione di zero:

.. code-block:: discos


    > derotatorGetPosition
    50d
    > derotatorSetConfiguration=FIXED
    > derotatorGetConfiguration
    FIXED
    > derotatorGetPosition
    50d
    > derotatorSetPosition=10d
    > derotatorGetPosition
    10d

.. _dynamics:

Configurazioni dinamiche
------------------------
Nelle configurazioni *dinamiche*, a differenza di quelle statiche,
il ``DewarPositioner`` aggiorna la posizione del derotatore in funzione
della posizione dell'antenna, al fine di compensare l'angolo parallatico
(più un eventuale contributo del *galactic parallactic angle*, 
a seconda dell'asse di scansione). 

Nelle configurazioni dinamiche la posizione del derotatore è data dalla 
seguente equazione:

.. math::

    P(az, el) = P_{is} + P_{ip}(az_0, el_0) + P_{dp}(az, el) 

dove ``az`` ed ``el`` sono rispettivamente l'azimuth e l'elevazione 
dell'antenna, mentre:

* :math:`P_{is}` è la *initial static position*, ovvero una posizione 
  (letta dal Configuration Data Base, CDB) che non dipende dall'azimuth ed
  elevazione dell'antenna ma solamente dall'asse di scansione

* :math:`P_{ip}` è la *initial parallactic position*, ovvero il valore
  dell'angolo parallatico ad inizio scansione: questo dipende sia dall'asse 
  di scansione (vale 0 per gli assi ``HOR_LON`` e ``HOR_LAT``) sia dal
  dal puntamento (azimuth, elevazione e settore)

* :math:`P_{dp}` è il delta di angolo parallatico rispetto a :math:`P_{ip}`

Nelle configurazioni ottimizzate (``BSC_OPT`` e ``CUSTOM_OPT``) 
si ha :math:`P_{ip} = 0`. Queste configurazioni sono utili quando si
utilizza un derotatore con un limitato range di escursione (ad esempio,
quello del ricevitore S-Band di SRT).

Oltre al fatto che sia ottimizzata o meno, ciò che differenzia una 
configurazione dinamica dall'altra è il valore della posizione iniziale 
:math:`P_{ip}`, perchè la funzione di compensazione dell'angolo parallatico
non cambia, e vale 0 quando l'asse di scansione è ``HOR_LAT`` o ``HOR_LON``,
è il risultato della funzione ``getParallacticAngle()`` quando 
l'asse di scansione è ``TRACK``, ``EQ_LON``, ``EQ_LAT`` o ``GCIRCLE``:

.. code-block:: python

   def getParallacticAngle(latitude, az, el):
       p = atan2(-sin(az), tan(latitude)*cos(el) - sin(el)*cos(az))
       return degrees(p)

mentre è dato dalla funzione ``getGalacticParallacticAngle()`` quando l'asse è
``GAL_LON`` o ``GAL_LAT``:

.. code-block:: python

   def getGalacticParallacticAngle(latitude, az, el, ra, dec):
       p = PosGenerator.getParallacticAngle(latitude, az, el) 
       g = PosGenerator.getGalacticAngle(ra, dec)
       return p + g 

   def getGalacticAngle(ra, dec):
       # North celestial pole coordinates - (j2000)
       # ncp = ('12 51 26.28', '27 07 41.7') 
       ra0 = 3.3660332687500043
       dec0 = 0.47347728280415174
       g = atan2(sin(ra-ra0), cos(dec)*tan(dec0) - sin(dec)*cos(ra-ra0))
       return degrees(g)

Quando viene impostata una configurazione, la posizione del derotatore non 
viene aggiornata, visto che non è ancora noto l'asse di scansione. 
L'aggiornamento viene comandato nel momento in cui DISCOS avvia lo scan.


.. _bsc:

Configurazione *best space coverage*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Il codice associatò a questa configurazione è ``BSC``::

    > derotatorSetConfiguration=BSC
    > derotatorGetConfiguration
    BSC

In questa configurazione il valore della posizione iniziale :math:`P_{ip}` 
viene letto da un database di configurazione ed è tale da garantire che
i feed vengano disposti in modo da avere la miglior copertura spaziale della 
sorgente durante la scansione.

.. note:: Tipicamente la miglior copertura viene ottenuta equispaziando, quando
   possibile, i beam nella direzione ortogonale a quella di scansione (se 
   si sta facendo una scansione in azimuth i feed vengono equispaziati in 
   elevazione, in modo da ottimizzare la scansione dell'area osservata).

Quando è impostata la modalità ``BSC``, all'utente non è consentito il 
posizionamento del derotatore::

    > derotatorSetConfiguration=BSC
    > derotatorSetPosition=50d
    Error - setPosition() not allowed in BSC configuration

In questa modalità l'insieme dei feed posizionati in modo da garantire la
massima copertura spaziale sono stabiliti a priori (ad esempio per il
banda K sono i feed 3, 0 e 6, con il 3 a est).

.. _bsc_opt:

Configurazione BSC *optimized*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Questa configurazione è analoga alla :ref:`best space coverage <bsc>` ma a 
differenza di quest'ultima, come abbiamo detto nella sezione :ref:`dynamics`,
il valore dell'angolo parallatico iniziale :math:`P_{ip}` non viene preso in 
considerazione. Questa configurazione è identificata dal codice ``BSC_OPT``::

    > derotatorSetConfiguration=BSC_OPT
    > derotatorGetConfiguration
    BSC_OPT

Analogamente alla ``BSC``, all'utente non è consentito il posizionamento
del derotatore::

    > derotatorSetConfiguration=BSC_OPT
    > derotatorSetPosition=50d
    Error - setPosition() not allowed in BSC_OPT configuration


..
    .. _aligned:
    Configurazione *aligned*
    ~~~~~~~~~~~~~~~~~~~~~~~~
    In questa configurazione, il cui codice identificativo è ``ALIGNED``,
    viene scelto il set di feed che si vuole allineare con l'asse di scansione.
    In DISCOS/ESCS vi sarà una tabella che riporterà, per ogni derotatore,
    i possibili set. La posizione del derotatore è data da::
    
       Pa = Pia(AXIS) + D(AZ, EL, AXIS) 
    
    .. attention:: Se il derotatore non compre un angolo di almento 360°, non
       è detto che sia possibile allineare un certo set di feed con un dato
       asse. In generale però se non è possibile allinearli con un asse, è 
       probabile che li si possa allineare con quello ortogonale.
    
    Rispetto alle altre configurazioni dinamiche, nella configurazione *aligned*
    vi è un ulteriore comando da utilizzare, chiamato ``derotatorSetAlignment``,
    che prende come argomento una stringa identificativa dei feed che si 
    vuole allineare.
    Nella stringa i feed devono essere separati da un segno meno::
    
        > derotatorSetConfiguration=ALIGNED
        > derotatorSetAlignment=0-4
    
    In questo caso viene scelto il set a cui appartengono
    i feed 0 e 4 (ad esempio, nel caso del banda K verrebbe scelto il set 
    ``{1, 0, 4}``).
    
    .. note:: Se non viene scelto un allineamento, allora viene utilizzato
       un allineamento di default (nel caso del banda K è quello ``{1, 0, 4}``).
    
    Concludiamo dicendo che così come per la configurazione ``BSC`` e 
    ``OPTIMIZED``, anche la ``ALIGNED`` non consente l'utilizzo del comando 
    ``derotatorSetPosition``.

.. _custom:

Configurazione *custom*
~~~~~~~~~~~~~~~~~~~~~~~
In questa configurazione la posizione iniziale statica :math:`P_{is}`
viene impostata dall'utente, e per tale motivo a questa configurazione è 
stato assegnato il codice identificativo ``CUSTOM``.

.. _custom_opt:

Configurazione *custom* optimized
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Analogamente a quanto abbiamo visto per la configurazione ``BSC_OPT``, anche
in questo caso ciò che differezia la ``CUSTOM_OPT`` dalla ``CUSTOM`` è la 
mancanza del contributo dell'angolo parallattico iniziale :math:`P_{ip}`.


Interrompere l'aggiornamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Se si vuole interrompere l'aggiornamento della posizione, si deve 
impostare la configurazione :ref:`fixed <fixed>`. In questo caso il derotatore
si fermerà all'ultima posizione comandata.

Riavvolgimento
~~~~~~~~~~~~~~
Il derotatore ha una corsa limitata, per cui la sua posizione ha un limite
massimo e uno minimo. Ad esempio, per il derotatore del ricevitore in banda K 
di SRT la massima posizione raggiungibile è 125.23 gradi, mentre la  minima 
è di -85.77 gradi::

    > derotatorSetup=KKG
    > derotatorGetMaxLimit
    125.2300d
    > derotatorGetMinLimit
    -85.7700d

Quando il derotatore sta aggiornado la sua posizione per tener conto
dell'angolo parallattico, è quindi possibile che si arrivi a fine corsa.
In questo caso, per default il derotatore viene riavvolto in modo automatico,
e l'effetto del riavvolgimento è che il feed più vicino al fine corsa viene
rimpiazzato da un altro, in modo da garantire che il derotatore abbia (durante
il proseguo dello scan) la massima corsa.

Durante il riavvolgimento, la console dei ricevitori indicherà che il
derotatore è in fase di riavvolgimento, e il campo *rewindingOffset* della
medesima console riporterà l'offset che avrà la posizione al termine del
riavvolgimento.
