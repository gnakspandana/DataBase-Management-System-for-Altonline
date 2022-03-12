CREATE TABLE users
(
userid int NOT NULL primary key ,
Username varchar(225),
Email varchar(255),
PhoneNumber bigint(20),
UserPassword varchar(225),
Newsletter varchar(225),
FullName varchar(225)
);
CREATE TABLE Address
(
Addressid int NOT NULL primary key,
usersid int,
FOREIGN KEY (usersid) REFERENCES users(usersid),
userid int,
City varchar(225),
Zipcode varchar(225)
);

CREATE TABLE Address_StreeName
(
StreetName int NOT NULL primary key,
Addressid int,
usersid int,
FOREIGN KEY (Addressid) REFERENCES Address(Addressid),
FOREIGN KEY (usersid) REFERENCES users(usersid),
Street1 varchar(25),
Street2 varchar(25)
);

CREATE TABLE Product
(
Productid int NOT NULL primary key,
Discount varchar(225),
Product_Description varchar(225),
Tax decimal(13,4),
Featured varchar(225),
Stock int,
Price_without_tax decimal(13,4)
);

CREATE TABLE Department
(
Deptid int NOT NULL primary key,
Title varchar(225),
URL varchar(225),
Description varchar(225),
Productid int,
FOREIGN KEY (Productid) REFERENCES Product(Productid)
);

CREATE TABLE Review
(
 Review_ID int NOT NULL primary key,
 FOREIGN KEY (usersid) REFERENCES users(usersid),
 FOREIGN KEY (Productid) REFERENCES Product(Productid),
 Stars varchar(20),
 Review_Text varchar(225)
);

CREATE TABLE Ordered_Products
(
Ordered_Products int NOT NULL primary key,
FOREIGN KEY (usersid) REFERENCES users(usersid),
FOREIGN KEY (Productid) REFERENCES Product(Productid),
Product_Quantity int,
Tax int,
Price_without_tax int,
Discount int
);

CREATE TABLE Keyword
(
Productid int,
FOREIGN KEY (Productid) REFERENCES Product(Productid),
Keyword_desp varchar(225)
);


CREATE TABLE Orders
(
Ordersid int NOT NULL primary key,
FOREIGN KEY (usersid) REFERENCES users(usersid),
OrderDate varchar(10) Not Null,
Lastupdate_date varchar(10) Not Null,
Tracking_Number varchar(10),
Payement_Information varchar(225),
Quantity int,
Order_Status varchar(10)
);


