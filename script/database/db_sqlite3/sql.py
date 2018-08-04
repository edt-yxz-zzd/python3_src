import sqlite3

def f():
    class MySum:
        def __init__(self):
            self.count = 0

        def step(self, value):
            self.count += value

        def finalize(self):
            return self.count

    con = sqlite3.connect(":memory:")
    con.create_aggregate("mysum", 1, MySum)
    cur = con.cursor()
    cur.execute("create table test(i PRIMARY KEY)")
    cur.execute("insert into test(i) values (1)")
    cur.execute("insert into test(i) values (1)")
    cur.execute("select mysum(i) from test")
    print(cur.fetchone()[0])


con = sqlite3.connect(":memory:")

stats = r'''
CREATE TABLE customer
    (customer_id VARCHAR(6),
    customer_name VARCHAR (24),
    customer_street_no NUMBER(3),
    customer_address VARCHAR (36),
    customer_postcode VARCHAR(6),
    date_entered (DATE));

CREATE TABLE stock_item
    (code VARCHAR(13),
    item_description VARCHAR (24) NOT NULL,
    price NUMBER (7,2) NOT NULL,
    vat NUMBER (2) NOT NULL,
    master_item VARCHAR(15),
    CONSTRAINT stock_item_pk PRIAMRY KEY (code),
    CONSTRAINT stock_item_fk FOREIGN KEY master_item REFER-ENCES stock_item(code),
    CONSTRAINT item_description_uk UNIQUE (item_description));

CREATE TABLE invoice
    (invoice_id NUMBER (8),
    invoice date DATE NOT NULL,
    order_date DATE NOT NULL,
    customer_id VARCHAR(6)
    CONSTRAINT invoice_id_pk PRIMARY KEY (invoice_id),
    CONSTRAINT customer_id_fk FOREIGN KEY (customer_id)
    REFERENCES customer (customer_id));
    
CREATE TABLE line_item
    (invoice_id NUMBER (8),
    code VARCHAR(13),
    qty NUMBER (4),
    CONSTRAINT line_item_pk PRIMARY KEY (invoice_id, code),
    CONSTRAINT invoice_id_fk FOREIGN KEY (invoice_id)
    REFERENCES invoice (invoice_id),
    CONSTRAINT code_fk FOREIGN KEY (code)
    REFERENCES stock_item (code));
'''
#DROP TABLE customer;

stats = [r'''

CREATE TABLE customer
    (customer_id BLOB(6),
    customer_name TEXT (24),
    customer_street_no INTEGER(3),
    customer_address TEXT (36),
    customer_postcode TEXT(6),
    date_entered DATE);
    ''',
         r'''
    
CREATE TABLE stock_item
    (code TEXT(13),
    item_description TEXT (24) NOT NULL,
    price REAL (7,2) NOT NULL,
    vat REAL (2) NOT NULL,
    master_item TEXT(15),
    CONSTRAINT stock_item_pk PRIMARY KEY (code),
    CONSTRAINT stock_item_fk FOREIGN KEY (master_item) REFERENCES stock_item(code),
    CONSTRAINT item_description_uk UNIQUE (item_description));
''',
         r'''
CREATE TABLE invoice
    (invoice_id INTEGER (8),
    invoice_date DATE NOT NULL,
    order_date DATE NOT NULL,
    customer_id TEXT(6),
    CONSTRAINT invoice_id_pk PRIMARY KEY (invoice_id),
    CONSTRAINT customer_id_fk FOREIGN KEY (customer_id)
    REFERENCES customer (customer_id));
    ''',
         r'''
CREATE TABLE line_item
    (invoice_id INTEGER (8),
    code TEXT(13),
    qty INTEGER (4),
    CONSTRAINT line_item_pk PRIMARY KEY (invoice_id, code),
    CONSTRAINT invoice_id_fk FOREIGN KEY (invoice_id)
    REFERENCES invoice (invoice_id),
    CONSTRAINT code_fk FOREIGN KEY (code)
    REFERENCES stock_item (code));
''',
         '''INSERT INTO customer VALUES ('OS3457',
    'Warren Felsky', 8, 'Mien Place, Sheffield', 'S7 4GH', '20-APR-13');
    ''',
         '''SELECT * FROM customer 
    WHERE customer_name = 'Warren Felsky' AND date_entered > '01-JAN-2010';
    ''',
         
         '''
SELECT customer_name, invoice_id, invoice_date
    FROM customer, invoice
    WHERE customer.customer_id = invoice.customer_id AND
    customer_name = 'Warren Felsky' AND
    date_entered > '01-JAN-2010';
''',
         '''
SELECT customer_name, invoice_id, invoice_date
    FROM customer
    INNER JOIN invoice
    ON customer.customer_id=invoice.customer_id;

''',
         '''
SELECT customer_name, invoice_id, invoice_date
    FROM customer
    LEFT OUTER JOIN invoice
    ON customer.customer_id=invoice.customer_id;
''',
         '''
SELECT m.item_description, i.item_description 
    FROM stock_item AS m LEFT JOIN stock_item AS i
    ON m.master_item=i.item_description;
''',
         '''
SELECT code, item_description, price
    FROM stock_item
    WHERE item_description LIKE '%Paris%'
    ORDER BY price DESC, item_description;
''',
         
         '''
SELECT COUNT(invoice_id)
    FROM invoice
    GROUP BY customer_id;
    ''',
         '''
SELECT invoice.invoice_id, COUNT (line_item.code), SUM (price)
    FROM invoice JOIN line_item JOIN stock_item
    ON invoice.invoice_id=line_item.invoice_id AND
       line_item.code=stock_item.code
    GROUP BY invoice.invoice_id;
''',
         '''
UPDATE customer
    SET customer_street_no=6,
    customer_address='McGregor St, Sheffield',
    customer_postcode='S11 1OD'
    WHERE customer_id='OS3457';

''',
         '''
DELETE FROM customer
    WHERE customer_name='Warren Felsky';
''',]

cur = con.cursor()
#con.execute(stat)
for i, stat in enumerate(stats):
    cur.execute(stat)
e = con.execute
f = cur.fetchall

