from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import validates
from config import db,bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ ='user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String,nullable=False)
    email = db.Column(db.String,nullable=False )
    image = db.Column(db.String,nullable=False)
    status = db.Column(db.String,nullable=False)
    role = db.Column(db.String,nullable=False)
    contact = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String,nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    inventory = db.relationship("Inventory", backref='user')
    sale = db.relationship("Sale", backref='user')
    invoice = db.relationship("Invoice", backref='user')
    report = db.relationship("Report", backref='user')
    notifications = db.relationship("Notification", backref='user')
    receipt = db.relationship("Receipt", backref='user')
    customer =db.relationship("Customer", backref='user')
    
    
        # validates email format
    @validates('email')
    def validate_email(self, key, value):
        if '@' not in value and '.com' not in value:
            raise ValueError("Invalid email")
        return value
    
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    # sets the password encryption using bycrpt
    @password_hash.setter
    def password_hash(self,password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    # used t authenticate if teh password provided is 
    def authenticate(self,password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    
    
    
    

    def __repr__(self):
        return f"User('{self.first_name}', '{self.email}, '{self.role}'')"
class Inventory(db.Model, SerializerMixin):
    __tablename__ ='inventories'   

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    VIN = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    body_style = db.Column(db.String, nullable=False)
    transmission = db.Column(db.String, nullable=False)
    fuel_type = db.Column(db.String, nullable=False)
    engine_size = db.Column(db.String, nullable=False)
    drive_type = db.Column(db.String, nullable=False)
    trim_level = db.Column(db.String, nullable=False)
    gallery = db.Column(db.String)
    condition = db.Column(db.String, nullable=False)
    availability = db.Column(db.String, nullable=False)
    cylinder = db.Column(db.Integer)
    doors = db.Column(db.Integer, nullable=False)
    features = db.Column(db.String)
    stock_number = db.Column(db.Integer, nullable=False)
    purchase_cost = db.Column(db.Integer, nullable=False)
    profit = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    importation = db.relationship("Importation", backref='inventories')
    sale = db.relationship("Sale", backref='inventories')
    invoice = db.relationship("Invoice", backref='inventories')
    report = db.relationship("Report", backref='inventories')
    gallery = db.relationship('GalleryImage', backref='inventories')

    
    def serializer(self):
        return{
            'id':self.id,
            'make':self.make,
            'price':self.price,
            'currency':self.currency,
            'image':self.image,
            'model':self.model,
            'year':self.year,
            'VIN':self.VIN,
            'color':self.color,
            'mileage':self.mileage,
            'body_style':self.body_style,
            'transmission':self.transmission,
            'fuel_type':self.fuel_type,
            'engine_size':self.engine_size,
            'drive_type':self.drive_type,
            'trim_level':self.trim_level,
            'gallery':self.gallery,
            'condition':self.condition,
            'availability':self.availability,
            'cylinder':self.cylinder,
            'doors':self.doors,
            'features':self.features,
            'stock_number':self.stock_number,
            'purchase_cost':self.purchase_cost,
            'profit':self.profit,
            'user_id':self.user_id
        }

class Importation(db.Model, SerializerMixin):
    __tablename__ ='importations'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    country_of_origin = db.Column(db.String, nullable=False)
    transport_fee = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String, nullable=False)
    import_duty = db.Column(db.Integer, nullable=False)
    import_date = db.Column(db.String, nullable=False)
    import_document = db.Column(db.String, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey("inventories.id"), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def serializer(self):
        return{
            'id':self.id,
            'country_of_origin':self.country_of_origin,
            'transport_fee':self.transport_fee,
            'currency':self.currency,
            'import_duty':self.import_duty,
            'import_date':self.import_date,
            'import_document':self.import_document,
            'car_id':self.car_id
        }
class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("user.id", name="fk_customer_seller_id")) 
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    sale = db.relationship("Sale", backref='customer')
    invoice = db.relationship("Invoice", backref='customer')
    report = db.relationship("Report", backref='customer')
    notification = db.relationship("Notification", backref='customer')
    receipt = db.relationship("Receipt", backref='customer')

    def serializer(self):
        return{
            'id':self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'email':self.email,
            'address':self.address,
            'phone_number':self.phone_number,
            'image':self.image
        }
class Sale(db.Model, SerializerMixin):
    __tablename__ = 'sales'
    
    id = db.Column(db.Integer, primary_key=True)
    commision = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    history = db.Column(db.String, nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    sale_date = db.Column(db.String, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    seller_id = db.Column(db.String, db.ForeignKey("user.id"), nullable=False)
    inventory_id = db.Column(db.String, db.ForeignKey("inventories.id"), nullable=False)
    promotions = db.Column(db.String, nullable=False)
    
    invoice = db.relationship("Invoice", backref='sales')

    def serializer(self):
        return{
            'id':self.id,
            'commision':self.commision,
            'status':self.status,
            'history':self.history,
            'discount':self.discount,
            'sale_date':self.sale_date,
            'customer_id':self.customer_id,
            'seller_id':self.seller_id,
            'inventory_id':self.inventory_id,
            'promotions':self.promotions
        }
class Invoice(db.Model, SerializerMixin):
    __tablename__ ='invoices'

    id = db.Column(db.Integer, primary_key=True)
    date_of_purchase = db.Column(db.String, nullable=False)
    method = db.Column(db.String, nullable=False)
    amount_paid = db.Column(db.Integer, nullable=False)
    fee = db.Column(db.Integer, nullable=False)
    tax = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String, nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    sale_id = db.Column(db.Integer, db.ForeignKey("sales.id"), nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.Integer, nullable=False)
    installments = db.Column(db.Integer, nullable=False)
    pending_cleared = db.Column(db.String, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("inventories.id"), nullable=False)
    signature = db.Column(db.String, nullable=False)
    warranty = db.Column(db.String, nullable=False)
    terms_and_conditions = db.Column(db.String, nullable=False)
    agreement_details = db.Column(db.String, nullable=False)
    additional_accessories = db.Column(db.String, nullable=False)
    notes_instructions = db.Column(db.String, nullable=False)
    payment_proof = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def serializer(self):
        return{
            'id':self.id,
            'date_of_purchase':self.date_of_purchase,
            'method':self.method,
            'amount_paid':self.amount_paid,
            'fee':self.fee,
            'tax':self.tax,
            'customer_id':self.customer_id,
            'seller_id':self.seller_id,
            'currency':self.currency,
            'sale_id':self.sale_id,
            'balance':self.balance,
            'total_amount':self.total_amount,
            'installments':self.installments,
            'pending_cleared':self.pending_cleared,
            'vehicle_id':self.vehicle_id,
            'signature':self.signature,
            'warranty':self.warranty,
            'terms_and_conditions':self.terms_and_conditions,
            'agreement_details':self.agreement_details,
            'additional_accessories':self.additional_accessories,
            'notes_instructions':self.notes_instructions,
            'payment_proof':self.payment_proof
            
        }
class Report(db.Model, SerializerMixin):
    __tablename__ ='reports'
    
    id = db.Column(db.Integer, primary_key=True)
    company_profit = db.Column(db.Integer, nullable=False)
    sale_id = db.Column(db.Integer, nullable=False)
    expenses = db.Column(db.Integer, nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey("inventories.id"), nullable=False)
    sale_date = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    importation_id = db.Column(db.Integer, nullable=False)

    def serializer(self):
        return{
            'id':self.id,
            'company_profit':self.company_profit,
            'sale_id':self.sale_id,
            'expenses':self.expenses,
            'importation_id':self.importation_id,
            'sale_date':self.sale_date,
            'customer_id':self.customer_id,
            'seller_id':self.seller_id,
            'inventory_id':self.inventory_id
            
        }
class Notification(db.Model, SerializerMixin):
    __tablename__ ='notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    message = db.Column(db.String, nullable=False)
    notification_type = db.Column(db.String, nullable=False)

    def serializer(self):
        return{
            'id':self.id,
            'user_id':self.user_id,
            'message':self.message,
            'notification_type':self.notification_type,
            'customer_id':self.customer_id,
            
        }
class Receipt(db.Model, SerializerMixin):
    __tablename__ ='receipts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    invoice_id = db.Column(db.Integer, nullable=False)
    amount_paid = db.Column(db.Integer, nullable=False)
    commission = db.Column(db.Integer, nullable=False)
    time_stamp = db.Column(db.DateTime, server_default=db.func.now())

    def serializer(self):
        return{
            'id':self.id,
            'user_id':self.user_id,
            'invoice_id':self.invoice_id,
            'amount_paid':self.amount_paid,
            'customer_id':self.customer_id,
            'commission':self.commission,
            'time_stamp':self.time_stamp
            
        }
        
class GalleryImage(db.Model,SerializerMixin):
    __tablename__ = 'gallery_image'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey("inventories.id"))
    

    def __init__(self, url, inventory_id):
        self.url = url
        self.inventory_id = inventory_id
        
    def serializer(self):
        return{
            'id':self.id,
            'url':self.url,
            'inventory_id':self.inventory_id,
            
        }