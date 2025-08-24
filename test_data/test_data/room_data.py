from test_data.schemas.room_payload import RoomPayload
from faker import Faker
from random import randint, sample, choice

fake = Faker()
room_type = ['Single', 'Twin', 'Double', 'Suite', 'Family']
features = ['WiFi', 'TV', 'Refreshments', 'Safe', 'Radio', 'Views']

def generate_room():
    """Generate valid room data"""
    return {
        'roomName': str(randint(100, 999)),
        'type': choice(room_type),
        'description': fake.sentence(),
        'accessible': fake.boolean(),
        'image': fake.image_url(),
        'features': sample(features, k=randint(1, 6)),
        'roomPrice': randint(100, 500)
    }
