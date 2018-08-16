from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event, DDL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/real_estate_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from realestateapi import routes
from realestateapi.models import Tenant

event.listen(Tenant.__table__, 
            'after_create', 
                DDL(""" INSERT INTO tenants (email, account_holder, first_name, last_name, iban, rent, phone) VALUES                                         
                    ('malou_proper@hotmail.com', 'Mw M Proper', 'Malou', 'Proper', 'NL08INGB0001193558', 747.16, '0612345678'),
                    ('daphnevanede@hotmail.com', 'D D F VAN EDE', 'Daphne', 'van Ede', 'NL15ABNA0490096379', 720.64, '0612345678'),
                    ('bienbeijderwellen@gmail.com', 'BIEN BEIJDERWELLEN', 'Bien', 'Beijderwellen', 'NL58ABNA0535684053', 728.18, '0612345678'),
                    ('matine_eising@outlook.com', 'M. Eising eo', 'Matine', 'Eising', 'NL40RABO0184147433', 752.76, '0612345678'),
                    ('ninakatherinadejong@gmail.com', 'K.S.A. de Jong', 'Nina', 'de Jong', 'NL94RABO0354260308', 799.05, '0612345678'),
                    ('kris.stroeken@hotmail.com', 'Hr G L M Stroeken en?Mw A J M J Stroeken-Smeets', 'Kris', 'Stroeken', 'NL79INGB0003694783', 715.33, '0612345678'),
                    ('fennascharloo@outlook.com', 'F. Scharloo', 'Fenna', 'ScharLoo', 'NL08RABO0133380343', 588.37, '0612345678'),
                    ('stijn_bronzwaer@hotmail.com', 'M.E.S. Bronzwaer-Timmerm', 'Stijn', 'Bronzwaer', 'NL75RABO0140989757', 824.65, '0612345678'),
                    

                """))
