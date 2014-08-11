yali
====

Yet another language library

=================================================================
Add french synonyms and antonyms functions with http://www.crisco.unicaen.fr/des/synonymes/ like data sources

Example:

    from yali.fr import synonyms

    crisco = synonyms.Crisco()\n
    _iter_sy = crisco.synonyms_of("manger")
    _iter_an = crisco.antonyms_of("manger")

=================================================================