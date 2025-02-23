from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

#DB Connection: 
engine = create_engine("postgresql+psycopg2://postgres:(832354)Tm!!@localhost/postgres")

class Base(DeclarativeBase):
	pass

#Branch - 

class Branch(Base):
	__tablename__ = "Branch"

	branchID: Mapped[int] = mapped_column(Integer, primary_key=True)
	branch_name: Mapped[str] = mapped_column(String(50))
	branch_phone_num: Mapped[str] = mapped_column(String(50))
	branch_address: Mapped[str] = mapped_column(String(50))

	allocationarea: Mapped[List["AllocationArea"]] = relationship(back_populates="branch", cascade="all, delete-orphan")
	donor: Mapped[List["Donor"]] = relationship(back_populates="branch", cascade="all, delete-orphan")
	manager: Mapped[List["Manager"]] = relationship(back_populates="branch", cascade="all, delete-orphan")

#Donor - 

class Donor(Base):
	__tablename__ = "Donor"

	donorID: Mapped[int] = mapped_column(String(50), primary_key=True)
	donor_name: Mapped[str] = mapped_column(String(50), nullable=True)
	donor_email: Mapped[str] = mapped_column(String(50), nullable=True)
	donor_phone_num: Mapped[str] = mapped_column(String(50), nullable=True)

	branchID: Mapped[int] = mapped_column(Integer, ForeignKey("Branch.branchID")) 
	branch: Mapped["Branch"] = relationship(back_populates="donor")

	managerID: Mapped[str] = mapped_column(String(50), ForeignKey("Manager.managerID"), nullable=True)
	manager: Mapped["Manager"] = relationship(back_populates="donor")

	donation: Mapped[List["Donation"]] = relationship(back_populates="donor", cascade="all, delete-orphan")

#AllocationArea - 

class AllocationArea(Base):
	__tablename__ = "AllocationArea"

	areaID: Mapped[str] = mapped_column(String(50), primary_key=True)
	area_name: Mapped[str] = mapped_column(String(255), nullable=True)

	branchID: Mapped[int] = mapped_column(Integer, ForeignKey("Branch.branchID"))
	branch: Mapped["Branch"] = relationship(back_populates="allocationarea")

	donation: Mapped[List["Donation"]] = relationship(back_populates="allocationarea", cascade="all, delete-orphan")

#Manager - 

class Manager(Base):
	__tablename__ = "Manager"

	managerID: Mapped[str] = mapped_column(String(50), primary_key=True)
	manager_name: Mapped[str] = mapped_column(String(50), nullable=True)

	branchID: Mapped[int] = mapped_column(Integer, ForeignKey("Branch.branchID"))
	branch: Mapped["Branch"] = relationship(back_populates = "manager")

	donor: Mapped[List["Donor"]] = relationship(back_populates="manager", cascade="all, delete-orphan")

#Donation - 

class Donation(Base):
	__tablename__ = "Donation"

	donationID: Mapped[str] = mapped_column(String(50), primary_key=True)
	donation_date: Mapped[str] = mapped_column(String(50), nullable=True)
	donation_amt: Mapped[int] = mapped_column(Integer, nullable=True)

	areaID: Mapped[str] = mapped_column(String(50),ForeignKey("AllocationArea.areaID"), nullable=True)
	allocationarea: Mapped["AllocationArea"] = relationship(back_populates="donation")
	donorID: Mapped[str] = mapped_column(String(50),ForeignKey("Donor.donorID"), nullable=True)
	donor: Mapped["Donor"] = relationship(back_populates="donation")

Base.metadata.create_all(engine)

##INSERT DATA

#Branch -- 
with Session(engine) as session:
	one = Branch(
		branchID= 10001,
		branch_name= "Los Angeles",
		branch_phone_num= "4246567731",
		branch_address= "3438 San Marino Street",
    		allocationarea= [AllocationArea(areaID = "A1")],
		donor= [Donor(donorID = "11111")],
    		manager= [Manager(managerID = "M1")]
	)
	two = Branch(
		branchID = 10002,
		branch_name = "Las Vegas",
		branch_phone_num = "7023368547",
		branch_address = "10700 Space Odyssey Avenue",
		allocationarea = [AllocationArea(areaID = "A2")],
		donor= [Donor(donorID = "11112")],
		manager = [Manager(managerID = "M2")]
	)
	three = Branch(
		branchID = 10003,
		branch_name = "New York City",
		branch_phone_num = "2124962270",
		branch_address = "326 Theatre Drive",
		allocationarea = [AllocationArea(areaID = "A3")],
		donor= [Donor(donorID = "11113")],
		manager = [Manager(managerID = "M3")]
	)
	four = Branch(
		branchID = 10004,
		branch_name = "Philadelphia",
		branch_phone_num = "21564859012",
		branch_address = "801 North Bambrey Street",
		allocationarea = [AllocationArea(areaID = "A4")],
		donor= [Donor(donorID = "11114"), Donor(donorID = "11118")],
		manager = [Manager(managerID = "M4")]
	)
	five = Branch(
		branchID = 10005,
		branch_name = "Fort Wayne",
		branch_phone_num = "2606371994",
		branch_address = "914 West Gump Road",
		allocationarea = [AllocationArea(areaID = "A5")],
		donor= [Donor(donorID = "11115")],
		manager = [Manager(managerID = "M5")]
	)
	six = Branch(
		branchID = 10006,
		branch_name = "Washington D.C.",
		branch_phone_num = "2026541576",
		branch_address = "110 Maryland Avenue",
		allocationarea = [AllocationArea(areaID = "A6")],
			#can list more than one allocation area since this is the one branch to many AA relation
		donor= [Donor(donorID = "11116"), Donor(donorID = "11117")],
		manager = [Manager(managerID = "M6")]
	)
	session.add_all([one, two, three, four, five, six])
	session.commit()

#AllocationArea -- 

with Session(engine) as session:
	stmt = select(AllocationArea).where(AllocationArea.areaID == "A1")
	A1 = session.scalars(stmt).one()
	A1.area_name = "Area 1"

	stmt = select(AllocationArea).where(AllocationArea.areaID == "A2")
	A2 = session.scalars(stmt).one()
	A2.area_name = "Area 2"

	stmt = select(AllocationArea).where(AllocationArea.areaID == "A3")
	A3 = session.scalars(stmt).one()
	A3.area_name = "Area 3"

	stmt = select(AllocationArea).where(AllocationArea.areaID == "A4")
	A4 = session.scalars(stmt).one()
	A4.area_name = "Area 4"

	stmt = select(AllocationArea).where(AllocationArea.areaID == "A5")
	A5 = session.scalars(stmt).one()
	A5.area_name = "Area 5"

	stmt = select(AllocationArea).where(AllocationArea.areaID == "A6")
	A6 = session.scalars(stmt).one()
	A6.area_name = "Area 6"
	session.commit()

#Manager -- 

with Session(engine) as session:
	stmt = select(Manager).where(Manager.managerID == "M1")
	M1 = session.scalars(stmt).one()
	M1.manager_name = "Eliza Cohen"

	stmt = select(Manager).where(Manager.managerID == "M2")
	M2 = session.scalars(stmt).one()
	M2.manager_name = "Trina Vega"

	stmt = select(Manager).where(Manager.managerID == "M3")
	M3 = session.scalars(stmt).one()
	M3.manager_name = "Neha Singh"

	stmt = select(Manager).where(Manager.managerID == "M4")
	M4 = session.scalars(stmt).one()
	M4.manager_name = "Owen Cline"

	stmt = select(Manager).where(Manager.managerID == "M5")
	M5 = session.scalars(stmt).one()
	M5.manager_name = "Layla Dyson"

	stmt = select(Manager).where(Manager.managerID == "M6")
	M6 = session.scalars(stmt).one()
	M6.manager_name = "Carson Smith"
	session.commit()

#Donor -- 

with Session(engine) as session:
	stmt = select(Donor).where(Donor.donorID == "11111")
	D1 = session.scalars(stmt).one()
	D1.donor_name = "Todd Smith"
	D1.donor_email = "tsmithy@hotmail.com"
	D1.donor_phone_num = "7089895446"
	D1.managerID = "M1"

	stmt = select(Donor).where(Donor.donorID == "11112")
	D2 = session.scalars(stmt).one()
	D2.donor_name = "Elena Baker"
	D2.donor_email = "bakersman@gmail.com"
	D2.donor_phone_num = "7089387495"
	D2.managerID = "M2"

	stmt = select(Donor).where(Donor.donorID == "11113")
	D3 = session.scalars(stmt).one()
	D3.donor_name = "Riley MacBeth"
	D3.donor_email = "Whereartthou@yahoo.com"
	D3.donor_phone_num = "2698499847"
	D3.managerID = "M2"

	stmt = select(Donor).where(Donor.donorID == "11114")
	D4 = session.scalars(stmt).one()
	D4.donor_name = "John Macafee"
	D4.donor_email = "macafeematters@gmail.com"
	D4.donor_phone_num = "7080394495"
	D4.managerID = "M3"

	stmt = select(Donor).where(Donor.donorID == "11115")
	D5 = session.scalars(stmt).one()
	D5.donor_name = "Jack Ripper"
	D5.donor_email = "beware@outlook.com"
	D5.donor_phone_num = "7084549983"
	D5.managerID = "M4"

	stmt = select(Donor).where(Donor.donorID == "11116")
	D6 = session.scalars(stmt).one()
	D6.donor_name = "Ginny George"
	D6.donor_email = "ggeorge@gmail.com"
	D6.donor_phone_num = "5159389948"
	D6.managerID = "M5"

	stmt = select(Donor).where(Donor.donorID == "11117")
	D7 = session.scalars(stmt).one()
	D7.donor_name = "John Doe"
	D7.donor_email = "jdoe@outlook.com"
	D7.donor_phone_num = "7083455555"
	D7.managerID = "M5"

	stmt = select(Donor).where(Donor.donorID == "11118")
	D8 = session.scalars(stmt).one()
	D8.donor_name = "Jane Doe"
	D8.donor_email = "janedoe@gmail.com"
	D8.donor_phone_num = "5159037485"
	D8.managerID = "M6"
	session.commit()

#Donation -- 

with Session(engine) as session:
	D1 = Donation(
		donationID = "D1",
		donation_date= "2023/10/20",
		donation_amt = 50,
	)
	D2 = Donation(
		donationID = "D2",
		donation_date= "2023/10/21",
		donation_amt = 100,
	)
	D3 = Donation(
		donationID = "D3",
		donation_date= "2023/10/20",
		donation_amt = 25,
	)
	D4 = Donation(
		donationID = "D4",
		donation_date= "2023/10/22",
		donation_amt = 50,
	)
	D5 = Donation(
		donationID = "D5",
		donation_date= "2023/10/23",
		donation_amt = 150,
	)
	D6  = Donation(
		donationID = "D6",
		donation_date= "2023/10/24",
		donation_amt = 15,
	)
	D7 = Donation(
		donationID = "D7",
		donation_date= "2023/10/23",
		donation_amt = 10,
	)
	D8 = Donation(
		donationID = "D8",
		donation_date= "2023/10/20",
		donation_amt = 150,
	)
	D9 = Donation(
		donationID = "D9",
		donation_date= "2023/10/19",
		donation_amt = 120,
		#areaID = [AllocationArea(areaID = "A3")],
		#donorID = [Donor(donorID = "11111")]
	)
	session.add_all([D1, D2, D3, D4, D5, D6, D7, D8, D9])

	stmt = select(Donation).where(Donation.donationID == "D1")
	D1 = session.scalars(stmt).one()
	D1.areaID = "A1"
	D1.donorID = "11111"

	stmt = select(Donation).where(Donation.donationID == "D2")
	D2 = session.scalars(stmt).one()
	D2.areaID = "A2"
	D2.donorID = "11112"

	stmt = select(Donation).where(Donation.donationID == "D3")
	D3 = session.scalars(stmt).one()
	D3.areaID = "A3"
	D3.donorID = "11113"

	stmt = select(Donation).where(Donation.donationID == "D4")
	D4 = session.scalars(stmt).one()
	D4.areaID = "A4"
	D4.donorID = "11114"

	stmt = select(Donation).where(Donation.donationID == "D5")
	D5 = session.scalars(stmt).one()
	D5.areaID = "A5"
	D5.donorID = "11115"

	stmt = select(Donation).where(Donation.donationID == "D6")
	D6 = session.scalars(stmt).one()
	D6.areaID = "A2"
	D6.donorID = "11112"

	stmt = select(Donation).where(Donation.donationID == "D7")
	D7 = session.scalars(stmt).one()
	D7.areaID = "A2"
	D7.donorID = "11116"

	stmt = select(Donation).where(Donation.donationID == "D8")
	D8 = session.scalars(stmt).one()
	D8.areaID = "A5"
	D8.donorID = "11112"

	stmt = select(Donation).where(Donation.donationID == "D9")
	D9 = session.scalars(stmt).one()
	D9.areaID = "A3"
	D9.donorID = "11111"

	session.commit()














