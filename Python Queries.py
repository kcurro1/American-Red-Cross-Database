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

## BranchDonation
session = Session(engine)
branch = session.query(Branch)
for B in branch:
    stmt = (
        select(AllocationArea)
        .where(AllocationArea.branchID == B.branchID))
    AA = session.scalars(stmt).one()
    branch_AA = str(AA.areaID)
    stmt2 = (
    select(Donation.donation_amt)
    .where(Donation.areaID == branch_AA)
    )
    DD = session.scalars(stmt2).all()
    total = sum(DD)
    num = len(DD)
    print(str(B.branch_name) + " Donation Total: $" + str(total) + " with "+ str(num) + " donation(s)")
    if num != 0:
       avg = total / num
        print(str(B.branch_name) + " Average Donation: $" + str(avg))
    else:
        print(str(B.branch_name) + " Average Donation: $0")

## DonorsPerAllocationArea

# Create a session
session = Session (engine) 
# Construct a query to get allocation areas with donor counts, ordered by donor count descending
stmt =  session.query (
AllocationArea.areaID,
        	AllocationArea.area_name,
      	func.count (Donation.donorID).label ('donor_count'))
# Query to get a list of all allocation areas in descending order of donors count
    .outerjoin (Donation, Donation.area_ID == AllocationArea.areaID)
    .group_by (AllocationArea.areaID, AllocationArea.area_name)
    .order_by (func.count (Donation.donorID).desc ()) 
    .all () 
 # Retrieve all results
)
# Printing the list of allocation areas with the most donors in descending order
print("The Allocation Areas ranked by the highest number of donors in descending order are as follows") 
for area in stmt:
    print(f"Area ID: {area.areaID}, Area Name: {area.area_name}, Donor Count: {area.donor_count}") 


Taylor’s Query (AllDonors)
session = Session(engine)
donors = session.query(Donor)
print("There are "+str(donors.count())+" donors.")  
for donor in donors:  
	print("Name: ")
	print(donor.donor_name)
	print("ID: ")
	print(donor.donorID)
	print("Email: ")	
	print(donor.donor_email)
	print()

## DonationInfo
session = Session(engine)
donation = session.query(Donation)
print("These are the current donations in the database:")  
for dono in donation:  
	print("Donation ID: ", dono.donationID, "Donation Amount: ", dono.donation_amt, "Donation Date: ", dono.donation_date, "Donation Area", dono.areaID)


##ManagerOfDonor
# Using the Select.join() method) Find the name and ID of the managers for donors "Jack Ripper" and "Ginny George"

session = Session(engine)

stmt1 = (
	select(Manager)
	.join(Manager.donor)
	.where(Donor.donor_name =="Jack Ripper"))
stmt2 = (
	select(Manager)
	.join(Manager.donor)
	.where(Donor.donor_name =="Ginny George"))
ManagerDonorJack = session.scalars(stmt1).one()
ManagerDonorGinny = session.scalars(stmt2).one()

print("The manager of Jack Ripper is " + ManagerDonorJack.manager_name + "with manager ID: " + ManagerDonorJack.managerID)
print("The manager of Ginny George: " + ManagerDonorGinny.manager_name+ "with manager ID: " + ManagerDonorGinny.managerID)
