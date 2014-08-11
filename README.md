yali
====

Yet another language library

Add french synonyms and antonyms functions with http://www.crisco.unicaen.fr/des/synonymes/ like data sources

=================================================================
from yali.fr import synonyms

crisco = synonyms.Crisco()\n
_iter_sy = crisco.synonyms_of("manger")\n
_iter_an = crisco.antonyms_of("manger") \n

=================================================================