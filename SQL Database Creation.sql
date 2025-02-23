CREATE TABLE AllocationArea(areaID varchar(50) PRIMARY KEY, area_name varchar(255));

INSERT INTO AllocationArea (areaID, area_name)
VALUES 
('A1', 'Area A'),
('A2', 'Area B'),
('A3', 'Area C'),
('A4', 'Area D'),
('A5', 'Area E');

CREATE TABLE Manager(managerID varchar(50) PRIMARY KEY, manager_name varchar(50), );

INSERT INTO Manager(managerID, manager_name)
VALUES
('M1', 'Eliza Cohen'),
('M2', 'Trina Vega'),
('M3', 'Neha Singh'),
('M4', 'Owen Cline'),
('M5', 'Layla Dyson'),
('M6', 'Carson Smith');

CREATE TABLE Branch(branchID varchar(50) PRIMARY KEY, branch_name varchar(50), branch_address varchar(50), branch_phone_num varchar(50), areaID varchar(50), FOREIGN KEY (areaID) REFERENCES AllocationArea(areaID), managerID varchar(50), FOREIGN KEY (managerID) REFERENCES Manager(managerID));

INSERT INTO Branch(branchID, branch_name, branch_address, branch_phone_num, areaID , managerID)
VALUES
('10001', 'Los Angeles', '3438 San Marino Street' , '4246567731', 'A1', 'M1'),
('10002', 'Las Vegas', '10700 Space Odyssey Avenue' ,  '7023368547','A2', 'M2'),
('10003', 'New York City', '326 Theatre Drive', '2124962270','A3', 'M3'),
('10004', 'Philadelphia', '801 North Bambrey Street', '21564859012','A3', 'M4'),
('10005', 'Fort Wayne', '914 West Gump Road', '2606371994','A4', 'M5'),
('10006', 'Washington D.C', '110 Maryland Avenue', '2026541576','A5', 'M6');

CREATE TABLE Donor(donor_name varchar(50), donorID varchar(50) PRIMARY KEY, donor_email varchar(50), donor_phone_num varchar(50), branchID varchar(50), FOREIGN KEY (branchID) REFERENCES Branch(branchID), managerID varchar(50), FOREIGN KEY (managerID) REFERENCES Manager(managerID));

insert into Donor(donor_name, donorID, donor_email, donor_phone_num, branchID, managerID)
values
('Todd Smith', '11111', 'tsmithy@hotmail.com', '7089895446', '10001', 'M1'),
('Elena Baker','11112', 'bakersman@gmail.com', '7089387495', '10002', 'M2'),
('Riley MacBeth', '11113', 'whereartthou@yahoo.com', '2698499847', '10003', 'M2'),
('John Macafee', '11114', 'macafeematters@gmail.com', '7080394495', '10004', 'M3'),
('Jack Ripper', '11115', 'beware@outlook.com', '7084549983', '10005', 'M4'),
('Ginny George', '11116', 'ggeorge@gmail.com', '5159389948', '10006', 'M5'),
('John Doe', '11117', 'jdoe@outlook.com', '7083455555', '10004', 'M5'),
('Jane Doe', '11118', 'janedoe@gmail.com', '5159037485', '10002', 'M6');

CREATE TABLE Donation(donationID varchar(50) PRIMARY KEY, donation_date date, donation_amt integer, area_ID varchar(50), donorID varchar(50), areaID varchar(50), FOREIGN KEY (areaID) REFERENCES AllocationArea(areaID), FOREIGN KEY (donorID) REFERENCES Donor(donorID));

INSERT INTO Donation(donationID, donation_date, donation_amt, areaID, donorID)
VALUES
('D1', to_date( '2023/10/20', 'YYYY/MM/DD'), 50, 'A1',  '11111'),
('D2', to_date( '2023/10/21', 'YYYY/MM/DD'), 100, 'A2',  '11112'),
('D3', to_date( '2023/10/20', 'YYYY/MM/DD'), 25, 'A3',  '11113'),
('D4', to_date( '2023/10/22', 'YYYY/MM/DD'), 50, 'A4',  '11114'),
('D5', to_date( '2023/10/23', 'YYYY/MM/DD'), 150, 'A5',  '11115'),
('D6', to_date( '2023/10/24', 'YYYY/MM/DD'), 15, 'A2',  '11112'),
('D7', to_date( '2023/10/23', 'YYYY/MM/DD'), 10, 'A2',  '11116'),
('D8', to_date( '2023/10/20', 'YYYY/MM/DD'), 150, 'A5',  '11112'),
('D9', to_date( '2023/10/19', 'YYYY/MM/DD'), 120, 'A3',  '11111');

CREATE TABLE goes_to(donationID varchar(50) references Donation(donationID) on update cascade, areaID varchar(50) references AllocationArea(areaID) on update cascade);

ALTER TABLE goes_to
ADD CONSTRAINT PK_donationarea
PRIMARY KEY (donationID, areaID);

INSERT INTO goes_to(donationID,areaID)
VALUES
('D1','A1'),
('D2','A2'),
('D3','A3'),
('D4', 'A4'),
('D5', 'A5'),
('D6', 'A2'),
('D7', 'A2'),
('D8', 'A5'),
('D9', 'A3');

CREATE TABLE donates_money_to(branchID varchar(50) references Branch(branchID) on update cascade, areaID varchar(50) references AllocationArea(areaID) on update cascade);

INSERT INTO donates_money_to(branchID, areaID)
VALUES 
('10001', 'A1'),
('10002', 'A2'),
('10003', 'A3'),
('10004', 'A4'),
('10005', 'A5'),
('10006', 'A2');

ALTER TABLE donates_money_to
ADD CONSTRAINT PK_brancharea
PRIMARY KEY (branchID, areaID);

CREATE TABLE donates(donorID varchar(50) REFERENCES Donor(donorID) on update cascade, donationID varchar(50) REFERENCES Donation(donationID) on update cascade);

INSERT INTO donates(donorID, donationID)
VALUES
('11111', 'D1'),
('11112', 'D2'),
('11113', 'D3'),
('11114', 'D4'),
('11115', 'D5'),
('11116', 'D6'),
('11117', 'D7'),
('11118', 'D8');

ALTER TABLE donates
ADD CONSTRAINT PK_donordonation
PRIMARY KEY (donorID, donationID);
