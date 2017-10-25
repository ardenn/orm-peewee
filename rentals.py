import psycopg2
import psycopg2.extras


class Rental:

    def __init__(self, film, rental_date, renter):
        self.film = film
        self.rental_date = rental_date
        self.renter = renter

    def __repr__(self):
        return self.renter

    def run_query(raw_query):
        conn = psycopg2.connect(dbname="dvdrental", user="rodgers")
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(raw_query)
        results = cur.fetchall()
        return results

if __name__ == '__main__':
    Rental.run_query("""
        SELECT title AS movie_name, r.rental_date,
        CONCAT(first_name,' ', last_name)
        AS renter_name FROM rental r
        JOIN inventory i ON (i.inventory_id=r.inventory_id)
        JOIN film f ON (f.film_id=i.film_id)
        JOIN customer c ON (c.customer_id=r.customer_id)
        ORDER BY r.rental_date DESC LIMIT 10;""")
