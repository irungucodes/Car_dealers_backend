from config import app, db, bcrypt
from models import User, Inventory, Importation, Customer, Sale, Invoice, Report, Notification, Receipt,GalleryImage

def seed_data():
    with app.app_context():
        # Delete all existing records
        db.session.query(User).delete()
        db.session.query(Inventory).delete()
        db.session.query(Importation).delete()
        db.session.query(Customer).delete()
        db.session.query(Sale).delete()
        db.session.query(Invoice).delete()
        db.session.query(Report).delete()
        db.session.query(Notification).delete()
        db.session.query(Receipt).delete()
        db.session.query(GalleryImage).delete()
        db.session.commit()

        # Add users
        password_hash = bcrypt.generate_password_hash('mypassword').decode('utf-8')
        password_hash2 = bcrypt.generate_password_hash('password').decode('utf-8')

        user1 = User(first_name='Dennis', last_name='Irungu',status ="active", email='irungud220@gmail.com', image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScNc6oZl7o7MuTWxfNXnWIiqzzCRmQg8sjBp59ZBZpFg&s', role='admin', contact=1234567890,_password_hash=password_hash)
        user3 = User(first_name='dennis', last_name='irungu',status ="active" , email='dennisnganga7148@gmail.com', image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2bPWPwj6jFqpAFm7q02z4hQ2Uwt4vYEueQzkzpq7dfg&s', role='super admin', contact=345678765, _password_hash=password_hash2)
        user2 = User(first_name='Maurine', last_name='wambui',status ="active" , email='maurinewambui@gmail.com', image='https://imgv3.fotor.com/images/blog-cover-image/a-pink-barbie-doll-with-a-pink-background.jpg', role='admin', contact=9876543210, _password_hash=password_hash2)
        user4 = User(first_name='Stanley', last_name='Muiruri',status ="active" , email='stanleywanjau@gmail.com', image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScNc6oZl7o7MuTWxfNXnWIiqzzCRmQg8sjBp59ZBZpFg&s', role='admin', contact=9876567,_password_hash=password_hash)
        user5 = User(first_name='Beatrice', last_name='Mwangi',status ="active" , email='bbeatricemwangi@gmail.com', image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2bPWPwj6jFqpAFm7q02z4hQ2Uwt4vYEueQzkzpq7dfg&s', role='seller', contact=2345098, _password_hash=password_hash2)
        user7 = User(first_name='Samuel', last_name='Mwangi',status ="active" , email='samwelmwangi@gmail.com', image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScNc6oZl7o7MuTWxfNXnWIiqzzCRmQg8sjBp59ZBZpFg&s', role='seller', contact=98765678,_password_hash=password_hash)
        user8 = User(first_name='James', last_name='Kinyanjui',status ="active" , email='jameskinyanjui@gmail.com', image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2bPWPwj6jFqpAFm7q02z4hQ2Uwt4vYEueQzkzpq7dfg&s', role='seller', contact=987678, _password_hash=password_hash2)


        db.session.add(user1)
        db.session.add(user3)
        db.session.add(user2)
        db.session.add(user4) 
        db.session.add(user5)
        # db.session.add(user6)
        db.session.add(user7)
        db.session.add(user8)

        # Add inventories
        inventory1 = Inventory(make='Toyota', image='https://images.pexels.com/photos/3311574/pexels-photo-3311574.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', price=15000, currency='USD', model='SUV', year='2022', VIN=12345678901234567, color='Black', mileage=5000, body_style='SUV', transmission='Automatic', fuel_type='Gasoline', engine_size='3.5L', drive_type='AWD', trim_level='XLE', condition='New', availability='Available', cylinder=6, doors=4, stock_number=1001, purchase_cost=12000, profit=3000, user_id=1)
        inventory2 = Inventory(make='Honda', image='https://images.pexels.com/photos/712618/pexels-photo-712618.jpeg?auto=compress&cs=tinysrgb&w=600', price=20000, currency='USD', model='Sedan', year='2021', VIN=98765432109876543, color='White', mileage=10000, body_style='Sedan', transmission='Automatic', fuel_type='Gasoline', engine_size='2.0L', drive_type='FWD', trim_level='Touring', condition='Used', availability='Available', cylinder=4, doors=4, stock_number=1002, purchase_cost=15000, profit=5000, user_id=2)
        
        inventory3 = Inventory(make='Toyota', image='https://images.pexels.com/photos/3786091/pexels-photo-3786091.jpeg?auto=compress&cs=tinysrgb&w=600', price=25000, currency='USD', model='SUV', year='2022', VIN=98767898, color='Black', mileage=5000, body_style='SUV', transmission='Automatic', fuel_type='Gasoline', engine_size='3.5L', drive_type='AWD', trim_level='XLE', condition='New', availability='Pending', cylinder=6, doors=4, stock_number=1001, purchase_cost=12000, profit=3000, user_id=3)
        inventory4 = Inventory(make='Honda', image='https://images.pexels.com/photos/2676096/pexels-photo-2676096.jpeg?auto=compress&cs=tinysrgb&w=600', price=2700000, currency='KSH', model='Sedan', year='2021', VIN=23456789, color='White', mileage=10000, body_style='Sedan', transmission='Automatic', fuel_type='Gasoline', engine_size='2.0L', drive_type='FWD', trim_level='Touring', condition='Used', availability='Available', cylinder=4, doors=4, stock_number=1002, purchase_cost=15000, profit=5000, user_id=2)
        
        inventory5 = Inventory(make='Toyota', image='https://images.pexels.com/photos/3166786/pexels-photo-3166786.jpeg?auto=compress&cs=tinysrgb&w=600', price=780, currency='USD', model='SUV', year='2022', VIN=876543459976, color='Black', mileage=5000, body_style='SUV', transmission='Automatic', fuel_type='Gasoline', engine_size='3.5L', drive_type='AWD', trim_level='XLE', condition='New', availability='Pending', cylinder=6, doors=4, stock_number=1001, purchase_cost=12000, profit=3000, user_id=1)
        inventory6 = Inventory(make='Honda', image='https://images.pexels.com/photos/2920064/pexels-photo-2920064.jpeg?auto=compress&cs=tinysrgb&w=600', price=9000, currency='USD', model='Sedan', year='2021', VIN=3456789856899, color='White', mileage=10000, body_style='Sedan', transmission='Automatic', fuel_type='Gasoline', engine_size='2.0L', drive_type='FWD', trim_level='Touring', condition='Used', availability='Available', cylinder=4, doors=4, stock_number=1002, purchase_cost=15000, profit=5000, user_id=2)
        
        inventory7 = Inventory(make='Toyota', image='https://images.pexels.com/photos/15253379/pexels-photo-15253379/free-photo-of-off-road-car-standing-on-a-snowed-side-road.jpeg?auto=compress&cs=tinysrgb&w=600', price=1500000, currency='KSH', model='SUV', year='2022', VIN=4567890654457994, color='Black', mileage=5000, body_style='SUV', transmission='Automatic', fuel_type='Gasoline', engine_size='3.5L', drive_type='AWD', trim_level='XLE', condition='New', availability='Not Available', cylinder=6, doors=4, stock_number=1001, purchase_cost=12000, profit=3000, user_id=2)
        inventory8 = Inventory(make='Honda', image='https://images.pexels.com/photos/733745/pexels-photo-733745.jpeg?auto=compress&cs=tinysrgb&w=600', price=1000, currency='USD', model='Sedan', year='2021', VIN=86458974333, color='White', mileage=10000, body_style='Sedan', transmission='Automatic', fuel_type='Gasoline', engine_size='2.0L', drive_type='FWD', trim_level='Touring', condition='Used', availability='Available', cylinder=4, doors=4, stock_number=1002, purchase_cost=15000, profit=5000, user_id=3)
        
        inventory9 = Inventory(make='Toyota', image='https://images.pexels.com/photos/1805053/pexels-photo-1805053.jpeg?auto=compress&cs=tinysrgb&w=600', price=4500000, currency='KSH', model='SUV', year='2022', VIN=9864211009765, color='Black', mileage=5000, body_style='SUV', transmission='Automatic', fuel_type='Gasoline', engine_size='3.5L', drive_type='AWD', trim_level='XLE', condition='New', availability='Available', cylinder=6, doors=4, stock_number=1001, purchase_cost=12000, profit=3000, user_id=3)
        inventory10 = Inventory(make='Honda', image='https://images.pexels.com/photos/1402787/pexels-photo-1402787.jpeg?auto=compress&cs=tinysrgb&w=600', price=4800000, currency='KSH', model='Sedan', year='2021', VIN=96211234567986445, color='White', mileage=10000, body_style='Sedan', transmission='Automatic', fuel_type='Gasoline', engine_size='2.0L', drive_type='FWD', trim_level='Touring', condition='Used', availability='Not Available', cylinder=4, doors=4, stock_number=1002, purchase_cost=15000, profit=5000, user_id=3)
        gallery1=GalleryImage(url='https://images.pexels.com/photos/244818/pexels-photo-244818.jpeg?auto=compress&cs=tinysrgb&w=600', inventory_id=1)
        gallery2=GalleryImage(url='https://images.unsplash.com/photo-1592570714618-15e2d4719c6c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8Y2FyJTIwaW50ZXJpb3J8ZW58MHx8MHx8fDA%3D', inventory_id=1)
        gallery3=GalleryImage(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU-OSqoHtlalct0ZPJVrO8dPz4Ce3L6y7QfoY4G-L5bJNBpP25LF4S4nfgDe9_Bg4P_94&usqp=CAU', inventory_id=2)
        gallery4=GalleryImage(url='https://images.unsplash.com/photo-1629280878139-038999084e23?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Y2FyJTIwaW50ZXJpb3J8ZW58MHx8MHx8fDA%3D', inventory_id=2)
        gallery5=GalleryImage(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlXtj5mczW8mpdca163lEL96So5vVkj0cGxOL_vnMj6f0czbctGYk0ocungF5UkkFcBRc&usqp=CAU', inventory_id=3)
        gallery6=GalleryImage(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvuD7avGsbX7pPJMx5wXlShRlS0HyQDkNcL__x8s5wOuylMiGBzT4IeRYgw2Q1sZajAdA&usqp=CAU', inventory_id=3)
        gallery7=GalleryImage(url='https://media.istockphoto.com/id/1407904356/photo/rear-back-passenger-car-seat.webp?b=1&s=170667a&w=0&k=20&c=8e0oHMxOt_aoyH7FlF2TfrsKreUvVbRvPiT6WgxmvgY=', inventory_id=4)
        gallery8=GalleryImage(url='https://media.istockphoto.com/id/1287914899/photo/car-inside-part-of-interior.webp?b=1&s=170667a&w=0&k=20&c=nN2BmX-BRMStC_9Jln_cCEVAgAszTJ6ubEYep8ZtF20=', inventory_id=4)
        gallery9=GalleryImage(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvuD7avGsbX7pPJMx5wXlShRlS0HyQDkNcL__x8s5wOuylMiGBzT4IeRYgw2Q1sZajAdA&usqp=CAU', inventory_id=5)


        db.session.add(inventory1)
        
        db.session.add(inventory3)
        db.session.add(inventory4)
        db.session.add(inventory5)
        db.session.add(inventory6)
        db.session.add(inventory7)
        db.session.add(inventory8)
        db.session.add(inventory9)
        db.session.add(inventory10)
        db.session.add(gallery1)
        db.session.add(gallery2)
        db.session.add(gallery3)
        db.session.add(gallery4)
        db.session.add(gallery5)
        db.session.add(gallery6)
        db.session.add(gallery7)
        db.session.add(gallery8)
        db.session.add(gallery9)
        db.session.add(inventory2)

        # Add importations
        importation1 = Importation(country_of_origin='Japan', transport_fee=1000, currency='USD', import_duty=500, import_date='2023-01-01', import_document='import_doc.pdf', car_id=1)
        importation2 = Importation(country_of_origin='USA', transport_fee=800, currency='USD', import_duty=400, import_date='2023-02-01', import_document='import_doc.pdf', car_id=2)
        importation3 = Importation(country_of_origin='Japan', transport_fee=1000, currency='USD', import_duty=500, import_date='2023-01-01', import_document='import_doc.pdf', car_id=3)
        importation4 = Importation(country_of_origin='Japan', transport_fee=1000, currency='USD', import_duty=500, import_date='2023-01-01', import_document='import_doc.pdf', car_id=4)
        importation5 = Importation(country_of_origin='Japan', transport_fee=1000, currency='USD', import_duty=500, import_date='2023-01-01', import_document='import_doc.pdf', car_id=4)
        importation6 = Importation(country_of_origin='Japan', transport_fee=1000, currency='USD', import_duty=500, import_date='2023-01-01', import_document='import_doc.pdf', car_id=6)
        importation7 = Importation(country_of_origin='Japan', transport_fee=1000, currency='USD', import_duty=500, import_date='2023-01-01', import_document='import_doc.pdf', car_id=7)
        importation8 = Importation(country_of_origin='Japan', transport_fee=1000, currency='USD', import_duty=500, import_date='2023-01-01', import_document='import_doc.pdf', car_id=8)
        importation9 = Importation(country_of_origin='Japan', transport_fee=1000, currency='USD', import_duty=500, import_date='2023-01-01', import_document='import_doc.pdf', car_id=9)
        importation10 = Importation(country_of_origin='Japan', transport_fee=1000, currency='USD', import_duty=500, import_date='2023-01-01', import_document='import_doc.pdf', car_id=10)
        db.session.add(importation1)
        db.session.add(importation2)
        db.session.add(importation3)
        db.session.add(importation4)
        db.session.add(importation5)
        db.session.add(importation6)
        db.session.add(importation7)
        db.session.add(importation8)
        db.session.add(importation9)
        db.session.add(importation10)

        # Add customers
        customer1 = Customer(first_name='Alice', last_name='Johnson', email='alice@example.com', address='123 Main St', phone_number=1234567890, image='https://static.wikia.nocookie.net/cartoons/images/e/ed/Profile_-_SpongeBob_SquarePants.png/revision/latest/thumbnail/width/360/height/360?cb=20230305115632', seller_id=6)
        customer2 = Customer(first_name='Bob', last_name='Smith', email='bob@example.com', address='456 Oak St', phone_number=9876543210, image='https://upload.wikimedia.org/wikipedia/en/2/2f/Jerry_Mouse.png', seller_id=5)
        customer3 = Customer(first_name='Alice', last_name='Johnson', email='alice@example.com', address='123 Main St', phone_number=809976566, image='https://static.wikia.nocookie.net/cartoons/images/e/ed/Profile_-_SpongeBob_SquarePants.png/revision/latest/thumbnail/width/360/height/360?cb=20230305115632', seller_id=5)
        customer4 = Customer(first_name='Alice', last_name='Johnson', email='alice@example.com', address='123 Main St', phone_number=34598655, image='https://static.wikia.nocookie.net/cartoons/images/e/ed/Profile_-_SpongeBob_SquarePants.png/revision/latest/thumbnail/width/360/height/360?cb=20230305115632', seller_id=7)
        customer5 = Customer(first_name='Alice', last_name='Johnson', email='alice@example.com', address='123 Main St', phone_number=1234567890, image='https://static.wikia.nocookie.net/cartoons/images/e/ed/Profile_-_SpongeBob_SquarePants.png/revision/latest/thumbnail/width/360/height/360?cb=20230305115632', seller_id=6)
        customer6 = Customer(first_name='Alice', last_name='Johnson', email='alice@example.com', address='123 Main St', phone_number=1234567890, image='https://static.wikia.nocookie.net/cartoons/images/e/ed/Profile_-_SpongeBob_SquarePants.png/revision/latest/thumbnail/width/360/height/360?cb=20230305115632', seller_id=5)
        customer7 = Customer(first_name='Alice', last_name='Johnson', email='alice@example.com', address='123 Main St', phone_number=1234567890, image='https://static.wikia.nocookie.net/cartoons/images/e/ed/Profile_-_SpongeBob_SquarePants.png/revision/latest/thumbnail/width/360/height/360?cb=20230305115632', seller_id=7)
        customer8 = Customer(first_name='Alice', last_name='Johnson', email='alice@example.com', address='123 Main St', phone_number=1234567890, image='https://static.wikia.nocookie.net/cartoons/images/e/ed/Profile_-_SpongeBob_SquarePants.png/revision/latest/thumbnail/width/360/height/360?cb=20230305115632', seller_id=5)
        # customer9 = Customer(first_name='Alice', last_name='Johnson', email='alice@example.com', address='123 Main St', phone_number=1234567890, image='https://static.wikia.nocookie.net/cartoons/images/e/ed/Profile_-_SpongeBob_SquarePants.png/revision/latest/thumbnail/width/360/height/360?cb=20230305115632', seller_id=7)






        db.session.add(customer1)
        db.session.add(customer2)
        db.session.add(customer3)
        db.session.add(customer4)
        db.session.add(customer5)
        db.session.add(customer6)
        db.session.add(customer7)
        db.session.add(customer8)

        # Add sales
        sale1 = Sale(commision=500, status='completed', history='No issues', discount=1000, sale_date='2023-03-01', customer_id=1, seller_id=5, inventory_id=1, promotions='Discount on next purchase')
        sale2 = Sale(commision=700, status='completed', history='Minor scratches', discount=1500, sale_date='2023-04-01', customer_id=2, seller_id=5, inventory_id=2, promotions='Extended warranty')
        sale3 = Sale(commision=700, status='completed', history='Minor scratches', discount=1500, sale_date='2023-04-01', customer_id=3, seller_id=6, inventory_id=3, promotions='Extended warranty')
        sale4 = Sale(commision=700, status='completed', history='Minor scratches', discount=1500, sale_date='2023-04-01', customer_id=4, seller_id=7, inventory_id=4, promotions='Extended warranty')
        sale5 = Sale(commision=700, status='completed', history='Minor scratches', discount=1500, sale_date='2023-04-01', customer_id=5, seller_id=6, inventory_id=5, promotions='Extended warranty')
        sale6 = Sale(commision=700, status='completed', history='Minor scratches', discount=1500, sale_date='2023-04-01', customer_id=6, seller_id=7, inventory_id=6, promotions='Extended warranty')
        sale7 = Sale(commision=700, status='completed', history='Minor scratches', discount=1500, sale_date='2023-04-01', customer_id=7, seller_id=5, inventory_id=7, promotions='Extended warranty')
        sale8 = Sale(commision=700, status='completed', history='Minor scratches', discount=1500, sale_date='2023-04-01', customer_id=8, seller_id=6, inventory_id=8, promotions='Extended warranty')
        db.session.add(sale1)
        db.session.add(sale2)
        db.session.add(sale3)
        db.session.add(sale4)
        db.session.add(sale5)
        db.session.add(sale6)
        db.session.add(sale7)
        db.session.add(sale8)
        # db.session.add(sale9)

        # Add invoices
        invoice1 = Invoice(date_of_purchase='2023-03-01', method='credit card', amount_paid=14000, fee=500, tax=1000, currency='USD', seller_id=5, sale_id=1, balance=1000, total_amount=15000, installments=1, pending_cleared='no', customer_id=1, vehicle_id=1, signature='signature.jpg', warranty='1 year', terms_and_conditions='Terms', agreement_details='Details', additional_accessories='Accessories', notes_instructions='Instructions', payment_proof='proof.jpg')
        invoice2 = Invoice(date_of_purchase='2023-04-01', method='cash', amount_paid=18500, fee=700, tax=1500, currency='USD', seller_id=6, sale_id=2, balance=500, total_amount=20000, installments=1, pending_cleared='no', customer_id=2, vehicle_id=2, signature='signature.jpg', warranty='2 years', terms_and_conditions='Terms', agreement_details='Details', additional_accessories='Accessories', notes_instructions='Instructions', payment_proof='proof.jpg')
        invoice3 = Invoice(date_of_purchase='2023-04-01', method='cash', amount_paid=18500, fee=700, tax=1500, currency='USD', seller_id=7, sale_id=3, balance=500, total_amount=5667, installments=4, pending_cleared='no', customer_id=3, vehicle_id=3, signature='signature.jpg', warranty='1 years', terms_and_conditions='Terms', agreement_details='Details', additional_accessories='Accessories', notes_instructions='Instructions', payment_proof='proof.jpg')
        invoice4 = Invoice(date_of_purchase='2023-04-01', method='cash', amount_paid=18500, fee=700, tax=1500, currency='USD', seller_id=6, sale_id=4, balance=500, total_amount=20000, installments=2, pending_cleared='no', customer_id=4, vehicle_id=4, signature='signature.jpg', warranty='3 years', terms_and_conditions='Terms', agreement_details='Details', additional_accessories='Accessories', notes_instructions='Instructions', payment_proof='proof.jpg')
        invoice5 = Invoice(date_of_purchase='2023-04-01', method='cash', amount_paid=18500, fee=700, tax=1500, currency='USD', seller_id=5, sale_id=5, balance=500, total_amount=20000, installments=1, pending_cleared='no', customer_id=5, vehicle_id=5, signature='signature.jpg', warranty='1 years', terms_and_conditions='Terms', agreement_details='Details', additional_accessories='Accessories', notes_instructions='Instructions', payment_proof='proof.jpg')
        invoice6 = Invoice(date_of_purchase='2023-04-01', method='cash', amount_paid=18500, fee=700, tax=1500, currency='USD', seller_id=7, sale_id=6, balance=500, total_amount=20000, installments=1, pending_cleared='no', customer_id=6, vehicle_id=6, signature='signature.jpg', warranty='2 years', terms_and_conditions='Terms', agreement_details='Details', additional_accessories='Accessories', notes_instructions='Instructions', payment_proof='proof.jpg')
        invoice7 = Invoice(date_of_purchase='2023-04-01', method='cash', amount_paid=18500, fee=700, tax=1500, currency='USD', seller_id=6, sale_id=7, balance=500, total_amount=20000, installments=1, pending_cleared='no', customer_id=7, vehicle_id=7, signature='signature.jpg', warranty='2 years', terms_and_conditions='Terms', agreement_details='Details', additional_accessories='Accessories', notes_instructions='Instructions', payment_proof='proof.jpg')
        invoice8 = Invoice(date_of_purchase='2023-04-01', method='cash', amount_paid=18500, fee=700, tax=1500, currency='USD', seller_id=5, sale_id=8, balance=500, total_amount=20000, installments=1, pending_cleared='no', customer_id=8, vehicle_id=8, signature='signature.jpg', warranty='2 years', terms_and_conditions='Terms', agreement_details='Details', additional_accessories='Accessories', notes_instructions='Instructions', payment_proof='proof.jpg')
        db.session.add(invoice1)
        db.session.add(invoice2)
        db.session.add(invoice3)
        db.session.add(invoice4)
        db.session.add(invoice5)
        db.session.add(invoice6)
        db.session.add(invoice7)
        db.session.add(invoice8)

        # Add reports
        report1 = Report(company_profit=3000, sale_id=1, expenses=500, inventory_id=1, sale_date='2023-03-01', customer_id=1, seller_id=5, importation_id=1)
        report2 = Report(company_profit=5000, sale_id=2, expenses=700, inventory_id=2, sale_date='2023-04-01', customer_id=2, seller_id=6, importation_id=2)
        report3 = Report(company_profit=5000, sale_id=3, expenses=700, inventory_id=3, sale_date='2023-04-01', customer_id=3, seller_id=7, importation_id=3)
        report4 = Report(company_profit=5000, sale_id=4, expenses=700, inventory_id=4, sale_date='2023-04-01', customer_id=4, seller_id=6, importation_id=4)
        report5 = Report(company_profit=5000, sale_id=5, expenses=700, inventory_id=5, sale_date='2023-04-01', customer_id=5, seller_id=5, importation_id=5)
        report6 = Report(company_profit=5000, sale_id=6, expenses=700, inventory_id=6, sale_date='2023-04-01', customer_id=6, seller_id=6, importation_id=6)
        report7 = Report(company_profit=5000, sale_id=7, expenses=700, inventory_id=7, sale_date='2023-04-01', customer_id=7, seller_id=7, importation_id=7)
        report8 = Report(company_profit=5000, sale_id=8, expenses=700, inventory_id=8, sale_date='2023-04-01', customer_id=8, seller_id=7, importation_id=8)
        db.session.add(report1)
        db.session.add(report2)
        db.session.add(report3)
        db.session.add(report4)
        db.session.add(report5)
        db.session.add(report6)
        db.session.add(report7)
        db.session.add(report8)

        # Add notifications
        notification1 = Notification(user_id=1, customer_id=1, message='Notification 1', notification_type='email')
        notification2 = Notification(user_id=2, customer_id=2, message='Notification 2', notification_type='sms')
        notification3 = Notification(user_id=3, customer_id=3, message='Notification 2', notification_type='sms')
        notification4 = Notification(user_id=4, customer_id=4, message='Notification 2', notification_type='sms')
        notification5 = Notification(user_id=5, customer_id=5, message='Notification 2', notification_type='email')
        notification6= Notification(user_id=6, customer_id=6, message='Notification 2', notification_type='sms')
        notification7 = Notification(user_id=7, customer_id=7, message='Notification 2', notification_type='email')
        notification8 = Notification(user_id=8, customer_id=8, message='Notification 2', notification_type='sms')
        notification9 = Notification(user_id=2, customer_id=1, message='Notification 2', notification_type='email')
        db.session.add(notification1)
        db.session.add(notification2)
        db.session.add(notification3)
        db.session.add(notification4)
        db.session.add(notification5)
        db.session.add(notification6)
        db.session.add(notification7)
        db.session.add(notification8)
        db.session.add(notification9)

        # Add receipts
        receipt1 = Receipt(user_id=7, customer_id=1, invoice_id=1, amount_paid=14000)
        receipt2 = Receipt(user_id=6, customer_id=2, invoice_id=2, amount_paid=18500)
        receipt3 = Receipt(user_id=5, customer_id=3, invoice_id=3, amount_paid=18500)
        receipt4 = Receipt(user_id=5, customer_id=4, invoice_id=4, amount_paid=18500)
        receipt5 = Receipt(user_id=5, customer_id=5, invoice_id=5, amount_paid=18500)
        receipt6 = Receipt(user_id=6, customer_id=6, invoice_id=6, amount_paid=18500)
        receipt7 = Receipt(user_id=7, customer_id=7, invoice_id=7, amount_paid=18500)
        receipt8= Receipt(user_id=6, customer_id=8, invoice_id=8, amount_paid=18500)
        db.session.add(receipt1)
        db.session.add(receipt2)
        db.session.add(receipt3)
        db.session.add(receipt4)
        db.session.add(receipt5)
        db.session.add(receipt6)
        db.session.add(receipt7)
        db.session.add(receipt8)

        db.session.commit()

if __name__ == '__main__':
    seed_data()
