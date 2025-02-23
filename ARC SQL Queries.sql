Query DonorSum():
SELECT D.donorID, SUM(D.donation_amt)
FROM Donation D, Donor O 
WHERE D. donorID = O.donorID 
GROUP BY D.donorID
ORDER BY SUM(D.donation_amt) DESC

Query AreaDonationAmount():
SELECT A.areaID, A.area_name, SUM(D.donation_amt) AS total_donation_amt
FROM AllocationArea A, Donation D
WHERE A.areaID = D.areaID 
GROUP BY A.areaID, A.area_name
ORDER BY total_donation_amt DESC

Query AllocationAreaDonations):
SELECT A.area_name, Count(D.donationID) AS donationsPerArea
FROM AllocationArea A, Donation D
WHERE D.areaID = A.areaID
GROUP BY A.areaID
ORDER BY donationsPerArea DESC

Query DonorsNotDonating():
SELECT O.donorID, O.donor_email, B.branchID, SUM(D.donation_amt) as total_donation_for_area
FROM Donor O, Branch B, Donation D
WHERE B.branchID = O.branchID AND B.areaID = D.areaID
AND O.donorID NOT IN (SELECT donorID FROM Donation)
GROUP BY B.branchID, O.donorID, O.donor_email
ORDER BY O.donor_name;

Query AvgBranchDonations():
SELECT B.branchID, B.branch_name, avg(D.donation_amt) as AvgBranchDonation
FROM AllocationArea A
JOIN Donation D
ON A.areaID = D.areaID
JOIN Branch B
ON A.areaID = B.areaID
GROUP BY B.branchID
ORDER BY AvgBranchDonation desc