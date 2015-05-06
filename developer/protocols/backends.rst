.. highlight:: cpp

.. _backend_protocols:

.. danger::
   This protocol is still a draft and is subject to potentially disruptive changes

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
**Status**           DRAFT
==================== ===============

Introduction
============

*DISCOS BACKEND PROTOCOL* consits of newline separated
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

Messaging Protocol
==================

Communication consists of a number of messages, each message consisting of a
line of text.  The protocol supports requests and replies messages.
Requests are indicated by "?", replies by "!". Each request should be
acknowledged by a reply. 
Replies should not be sent except in response to a request.
A reply is necessary for every request, however the nature of the reply may
change depending on the request.
The reply message should have the same name as the request message.
The first parameter of a reply message should always be a return code. A return
code of *ok* indicates successful
processing of the request, while anything else indicates failure. 
The recommended failure strings are
*invalid* (for malformed requests) and
*fail* (for valid requests which could not be processed) but backends may return
other failure strings. On success, further parameters are specific to the type
of request made while in the case of
failure a second parameter should describe the failure in more detail and in
human-readable form:

+-----------+---------------------------------------------------------------+
|Return Code|Description                                                    |
+===========+===============================================================+
|ok         |Request successfully processed. Further arguments are request  |
|           |specific.                                                      |
+-----------+---------------------------------------------------------------+
|invalid    |Request  malformed. Second argument is a human-readable        |
|           |description of the error.                                      |
+-----------+---------------------------------------------------------------+
|fail       |Valid request that could not be processed. Second argument is a|
|           |human-readable description of the error.                       |
+-----------+---------------------------------------------------------------+

Message Grammar
~~~~~~~~~~~~~~~

The message grammar is described in extended BNF [EBNF]_ where:

  * Optional items are enclosed in square brackets
  * Items repeating 0 or more times are suffixed with a *
  * Items repeating 1 or more times are suffixed with a +
  * Alternative choices in a production are separated by the '|' symbol
  * Set difference is indicated by the '/' symbol

The grammar is defined as::

    <message> ::= <type> <name> <arguments> <eol>
       <type> ::= "?" | "!"
       <name> ::= alpha (alpha | digit | "-")*
  <arguments> ::= ("" | <separator> <argument>) [<arguments>]
        <eol> ::= newline
  <separator> ::= ","
   <argument> ::= (<plain> | <escape>)+
      <plain> ::= character / <special>
    <special> ::= backslash | null | newline | carriage-return | escape | tab
     <escape> ::= "\" <escapecode>
  <escapecode>::= "\" | "t" | <separator>

Note that arguments can contain spaces and tabs and are limited only by commas
and newlines at the end of the message.

Data Types
==========

Being the protocol string based, whenever we need to transmit other data types
they must be encoded into strings in an unequivocable manner. This is defined
as per the table below:

  * **integer** as formatted by printf("%d",i). i.e. 10 -15
  * **float** as formatted by printf("%f",f) i.e. -1209087123.234234 1.0
  * **boolean** True as 1 and False as 0 i.e. 1, 0
  * **timestamp** XXXX.YYYYYYYY where XXXX is the number of seconds since epoch 
    and YYYYYYYY is the remaining fraction of seconds with centinanosecond 
    precision i.e. 1430922782.97088300

Request and Reply Messages
==========================

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

Considerations
==============

The proposed protocol is intentionally very simple and little powerful; this
choice is derived from the specs given in the meeting held the 13 / 04 / 2015 at
OaC. 
More complex interactions would require a different protocol resulting in a more
complex definition and different technologies involved. In particular the actual
definition does **not** : 

 * Version the protocol in the protocol itself
 * Permit to send asynchronous messages
 * Permit biderectional requests
 * Permit to send the same message to multiple recipients

References
==========

.. [EBNF] http://www.cl.cam.ac.uk/~mgk25/iso-14977.pdf
.. [KAT] https://casper.berkeley.edu/wiki/images/1/11/NRF-KAT7-6.0-IFCE-002-Rev4.pdf

