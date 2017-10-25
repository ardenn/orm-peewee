from dvdrentals import Film, Rental, Inventory, Customer

results = Rental.select().order_by(Rental.rental_date.desc()).limit(10)

for r in results:
    print(r.inventory.film.title)
