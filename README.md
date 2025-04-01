1) Forkkaa projekti omaan githubiisi. Jos haluat tehdä esim. parityönä, lisää projektille collaboratorit
2) Kloonaa forkattu projektisi koneellesi ja luo kloonattuun projektikansioon virtuaaliympäristö ja aktivoi se.
3) Asenna tarvittavat paketit requirements.txt -tiedostosta seuraavalla komennolla:
   pip install -r requirements.txt
4) Kun SAVE-napin toiminnallisuus on tehty (lisää uuden tehtävän), luo itsellesi uusi commit.
5) Luo omat branchit uusille toiminnallisuuksille:
   - file_as_db      (ohjelman auetessa haetaan tiedostosta kaikki taskit (jokainen esim. omalla rivillään),
                      ja ohjelman sulkiessa tallennetaan taskit tiedostoon
   - sqlite_db       (vastaava kuin file_as_db, mutta haetaan ja tallennetaan sqlite-kantaan (db-tiedostoon)
   - update_task     (Käyttäjä voi klikata taskia, jolloin aukeaa Update Task-ikkuna. Käyttäjä voi muuttaa taskin nimeä
                      ja painamalla UPDATE päivittää kyseisen taskin tekstikentän  
6) Kukin ryhmässä työstää omaa branchiaan (voitte valita itse kuka tekee mitäkin).
7) Kun toiminnallisuudet ovat valmiita, koittakaa yhdistää (eli gitillä mergetä) toiminnallisuudet yhteen!
