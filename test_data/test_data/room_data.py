from test_data.schemas.roompayload import RoomPayload
from faker import Faker
from random import randint, sample, choice

faker = Faker()
room_type = ['Single', 'Twin', 'Double', 'Suite', 'Family']
features = ['WiFi', 'TV', 'Refreshments', 'Safe', 'Radio', 'Views']

def generate_room() -> RoomPayload:
    return RoomPayload(
        roomName=str(randint(100, 999)),
        type=choice(room_type),
        description=faker.sentence(),
        accessible=faker.boolean(),
        image=faker.image_url(),
        features=sample(features, k=randint(1, 6)),
        roomPrice=randint(100, 500)
    )