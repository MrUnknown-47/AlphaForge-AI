import factory
from faker import Factory as FakerFactory
from app.modules.auth.models import UserModel
from app.modules.portfolio.models import PortfolioModel

faker = FakerFactory.create()

class UserFactory(factory.Factory):
    class Meta:
        model = UserModel

    id = factory.LazyFunction(faker.uuid4)
    email = factory.LazyAttribute(lambda o: faker.email())
    username = factory.LazyAttribute(lambda o: faker.user_name())
    password_hash = "hashed_password_placeholder"
    is_active = True
    is_verified = True

class PortfolioFactory(factory.Factory):
    class Meta:
        model = PortfolioModel

    id = factory.LazyFunction(faker.uuid4)
    user_id = factory.LazyFunction(faker.uuid4)
    name = factory.LazyAttribute(lambda o: f"Portfolio {faker.word()}")
    cash_balance = 100000.00\n