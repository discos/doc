.. _nuraghe-is-configured:

****************************************************
Verificare che Nuraghe sia configurato correttamente
****************************************************
La situazione è questa: è stato eseguito ``setupXXX`` da
*OperatorInput*. Il SoD dovrebbe guardare tutte le varie
console per capire se il setup è andato a buon fine. 
Se siete d'accordo, implemento un check veloce che può essere
eseguito da *OperatorInput*, ad esempio con il comando
*systemCheck*. Se tutto è OK::

    > systemCheck
    OK 
    System configured (setupCCB)

Se ad esempio il sistema è in ``setupCCB``, ma è scattato il
differenziale del SRP o è andato giù un container, ma è previsto
che ci sia tracking in funzione dell'elevazione::

   > systemCheck
   ERROR 
   The SRP is in power off

Quando l'utente ha dei sospetti su qualcosa, può sempre eseguire
un systemCheck da *OperatorInput*, per verificare al volo che
tutto stia andando bene, senza dover passare su *nuraghe-mng* o
altre eventuali macchine per contare che tutti i container siano
attivi, o verificare i log di ciascun container.
