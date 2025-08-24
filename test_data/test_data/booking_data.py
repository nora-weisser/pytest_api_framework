from datetime import timedelta, date
from faker import Faker

fake = Faker('nl_NL')

def valid_booking_data(room_id: str):
    """Generate valid booking data"""
    today = date.today()
    checkin_date = today + timedelta(days=fake.random_int(min=1, max=10))
    checkout_date = checkin_date + timedelta(days=fake.random_int(min=1, max=5))

    return {
        "roomid": room_id,
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": checkin_date.strftime("%Y-%m-%d"),
            "checkout": checkout_date.strftime("%Y-%m-%d")
        }
    }
