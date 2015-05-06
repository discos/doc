.. highlight:: cpp

.. _backend_protocols:

*****************
Backend protocols
*****************

This section describes the protocol used by DISCOS to communicate with external
backends. You can find reported the protocol definition, the grammar definition
and a simple example implementation of the protocol server as a twisted
protocol. This definition is liberally inspired by the one used by KAT telescope
for device communication ([KAT]_) as we found that work of really good quality.

==================== ===============
**Protocol Version** 1.0
**Last revision**    06/05/2015
==================== ===============

Introduction
============

*DISCOS BACKEND PROTOCOL* (from here called **BDP**) consits of newline separated
text messages sent synchronously over a TCP/IP connection. Messages can be of
two kinds: request and reply. Requests are sent from a client to a server,
while replies are sent from the server in response to a client's request. Each
request must receive one and only one reply message back. In this kind of
topology the client will be tipically represented by a DISCOS component, while
the server is represented by the backend controller. This version of the
protocol does not impose any constraint to the number of clients connecting to a
server but leaves to the clients the responsibility of orchestrating their
requests in a consistent way. Implementations consisting of a single client will
be the first and foremost ones.

Here you can find a quick list of the requests defined by the protocol, which
will be better described in next sections:

======================== =======================================
Request                  Description
======================== =======================================
:ref:`status`            get the backend status code
:ref:`version`           get the server protocol version
:ref:`configuration`     get the backend actual configuration
:ref:`set-configuration` set a new backend configuration
:ref:`time`              get the backend time
:ref:`start`             start the acquisition [at a given time]
:ref:`stop`              stop the acquisition [at a given time]
======================== =======================================

Messages
========

.. _status:

status
~~~~~~

Get status ask the DBE to return a status

.. _version:

version
~~~~~~~

.. _configuration:

configuration
~~~~~~~~~~~~~

.. _set-configuration:

set-configuration
~~~~~~~~~~~~~~~~~

.. _time:

time
~~~~

.. _start:

start
~~~~~

.. _stop:

stop
~~~~


Bibliography
============

.. [EBNF] http://www.cl.cam.ac.uk/~mgk25/iso-14977.pdf
.. [KAT] https://casper.berkeley.edu/wiki/images/1/11/NRF-KAT7-6.0-IFCE-002-Rev4.pdf

Introduzione
============
Lo scopo è definire un protocollo per comunicare con il *sistema ROACH2*
(d'ora in avanti SR2), ovvero il sistema che prende in ingresso delle 
richieste, esegue delle azioni sulla ROACH2 e da indietro una risposta.

La comunicazione non prevede uno scambio di grandi quantità di informazioni. I dati
infatti abbiamo detto che verranno scritti direttamente dal SR2, il quale
recupera le informazioni dell'antenna e il relativo timestamp da un 
FITS appositamente scritto da DISCOS. Cio' significa che possiamo utilizzare
un protocollo testuale line-based.

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
