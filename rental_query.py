from rental_db import DvdRental
from rentals import Rental

if __name__ == "__main__":
    for result in Rental.run_query("""
		SELECT title AS movie_name, r.rental_date,
        CONCAT(first_name,' ', last_name)
        AS renter_name FROM rental r
        JOIN inventory i ON (i.inventory_id=r.inventory_id)
        JOIN film f ON (f.film_id=i.film_id)
        JOIN customer c ON (c.customer_id=r.customer_id)
        ORDER BY r.rental_date DESC LIMIT 10;"""):
        new = DvdRental(**result)
        new.save()
