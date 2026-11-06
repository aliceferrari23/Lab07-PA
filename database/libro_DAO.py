from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor()
        query = "SELECT DISTINCT genere FROM libro ORDER BY genere"
        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        cnx.close()
        return result

    def get_libri_filtrati(self, nome_biblioteca=None, genere=None):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor(dictionary=True)

        query = """
                SELECT l.* 
                FROM libro l, biblioteca b
                WHERE l.id_biblioteca = b.id
                """
        params = []

        if nome_biblioteca and nome_biblioteca != "Tutte":
            query += " AND b.nome = %s"
            params.append(nome_biblioteca)

        if genere and genere != "Tutti":
            query += " AND l.genere = %s"
            params.append(genere)

        cursor.execute(query, tuple(params))

        for row in cursor:
            result.append(Libro(
                id=row["id"],
                titolo=row["titolo"],
                autore=row["autore"],
                genere=row["genere"],
                anno_pubblicazione=row["anno_pubblicazione"],
                id_biblioteca=row["id_biblioteca"]
            ))

        cursor.close()
        cnx.close()
        return result
