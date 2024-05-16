from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SerializerMixin(object):
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    user_type = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    phone_number = db.Column(db.String(15))
    intasend_wallet_id = db.Column(db.String(100), nullable=True, unique=True)
    wallet = db.relationship('Wallet', backref='user', uselist=False)

class Wallet(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=[True])
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    balance = db.Column(db.Numeric(10, 2))
    currnecy = db.Column(db.String(3))
    last_updated = db.Column(db.DateTime, default=db.func.now())

class Transaction(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    wallet_id = db.Column(db.Integer, db.ForeingKey('wallet'))
    transaction_type = db.Column(db.String(10))
    amount = db.Column(db.Numeric(10, 2))
    description = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=db.func.now())

class PaymentMethod(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    payment_type = db.Column(db.String(20))
    details = db.Column(db.Text)

class Route(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    route_name = db.Column(db.String(100))
    start_location = db.Column(db.String(100))
    end_location = db.Column(db.String(100))
    distance = db.Column(db.Numeric(10, 2))
    price = db.Column(db.Numeric(10, 2))

class Vehicle(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Ineger, db.ForeignKey('route.id'))
    vehicle_number = db.Column(db.String(20), unique=True)
    driver_name = db.Column(db.String(150))
    conductor_name = db.Column(db.String(150))
    capacity = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=True)

