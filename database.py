# import mysql.connector
import sqlite3

# Verbindung zur Datenbank herstellen
# try:
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="morphy",
#         password="La3A_-Z5u3fQU]5",
#         database="morphy"
#     )
# except:
#     print("Connection Error")

connection = sqlite3.connect('discord.db')

# connection.cursor().execute('CREATE TABLE `economy` (`user_id` bigint,`coins` int);')


# Funktion zum Hinzufügen eines Benutzers mit Münzen
def add_user(user_id, coins):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO economy (user_id, coins) VALUES (?, ?)', (user_id, coins))
    connection.commit()
    cursor.close()

def delete_user(user_id):
    cursor = connection.cursor()
    cursor.execute('DELETE FROM economy WHERE user_id = ?', (user_id, ))
    connection.commit()
    cursor.close()


# Funktion zum Abrufen von Münzen für einen Benutzer
def get_coins(user_id):
    cursor = connection.cursor()
    cursor.execute("SELECT coins FROM economy WHERE user_id = ?", (user_id, ))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0]
    else:
        return None


# Funktion zum Setzen von Münzen für einen Benutzer
def set_coins(user_id, coins):
    cursor = connection.cursor()
    cursor.execute("UPDATE economy SET coins = ? WHERE user_id = ?", (coins, user_id))
    connection.commit()
