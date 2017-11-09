from dvdrentals import Film, Rental, Inventory, Customer, Payment, Staff
from peewee import fn

news = Film.select(
    Film.title,
    Rental.rental_date,
    Customer.last_name.concat(Customer.first_name).alias("name"))\
    .join(Inventory).join(Rental)\
    .join(Customer)\
    .order_by(Rental.rental_date)\
    .limit(10).naive()

results = Customer.select(
    Customer.last_name.concat(
        Customer.first_name).alias("name")).join(Rental).join(Payment).where(
            Payment.amount > 6).order_by(Rental.rental.desc()).limit(10).naive()

staff_amount = Rental.select(Staff.first_name, fn.sum(Payment.amount).alias("amt")).join(Payment).join(Staff).group_by(
    Staff.first_name).order_by(fn.sum(Payment.amount)).naive()

staff_count = Rental.select(Staff.first_name, fn.count(Rental.staff).alias("cnt")).join(Staff).group_by(
    Staff.first_name).order_by(fn.count(Rental.staff)).naive()
# for r in news:
#     print(r.name)
for result in results:
    print(result.name)
# for s in staff_amount:
#     print(s.first_name, s.amt)
# for staf in staff_count:
#     print(staf.first_name, staf.cnt)
