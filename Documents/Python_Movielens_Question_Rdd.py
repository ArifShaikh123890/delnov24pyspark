1) Extract rating as float and count no of occurences of each number in reverse order of ratings?
Output:-
(5.0, 13211)	--> Verified data in ratings csv file
(4.5, 8551)
(4.0, 26818)
(3.5, 13136)
(3.0, 20047)

2) Create a function mapToTuple and map String rows to tuples and selected attributes?
mapToTuple function converts a String row into a key-value pair movieId → (rating, count) where the initial value of count is 1.
Find the sum of ratings and number of ratings of each movie (movieId, (totalRatings, count))
Output:-
(6, (402.5, 102))	--> Verified data in ratings csv file
(50, (864.5, 204))	
(70, (193.0, 55))
(110, (955.5, 237))
(216, (163.0, 49))

3) Given the totalRating and count (number of ratings), we can find the average rating by dividing totalRating by the count.
Output:-

(6, 3.946078431372549)	--> Verified data in ratings csv file
(50, 4.237745098039215)
(70, 3.5090909090909093)
(110, 4.031645569620253)
(216, 3.326530612244898)
OR
(6, 3.95)	--> After Rounding Up
(50, 4.24)
(70, 3.51)
(110, 4.03)
(216, 3.33)

4) From above movieIDs mapped to the average ratings. Sort the result by average ratings in descending order.
(131724, 5.0)	--> Verified data in ratings csv file
(5746, 5.0)
(92494, 5.0)
(67618, 5.0)
(8804, 5.0)

5) From the movies file display 1st & 2nd column & split 2nd column value by ('|') and repeat on every row.
Hint: .flatMapValues(x => x.split('|))
Output:-
(Toy Story (1995),Adventure)
(Toy Story (1995),Animation)
(Toy Story (1995),Children)
(Toy Story (1995),Comedy)
(Toy Story (1995),Fantasy)

6) From movies file split the data based of 2nd column and display only Action data & remove the tuple.
Output:
Sudden Death (1995),Action
Fair Game (1995),Action
Under Siege 2: Dark Territory (1995),Action
Bloodsport 2 (a.k.a. Bloodsport II: The Next Kumite) (1996),Action
Best of the Best 3: No Turning Back (1995),Action

7) From movies file split the data based of 2nd column and display only Comedy data & sort it.
Output:
Father of the Bride Part II (1995),Comedy
Four Rooms (1995),Comedy
Ace Ventura: When Nature Calls (1995),Comedy
Bio-Dome (1996),Comedy
Friday (1995),Comedy

8) Create a function loadMovieNames() to read the movies.csv file and to create Key-Value pairs of movieIds and titles.
Find the average ratings on movieId & sort in reverse order of average ratings and then call the loadMovieNames() 
to fetch the below result.
Output:
('Lamerica (1994)', 5.0)
('Sandpiper', 5.0)
('My Man Godfrey (1957)', 5.0)
('Black Tar Heroin: The Dark End of the Street (2000)', 5.0)
('Moscow Does Not Believe in Tears (Moskva slezam ne verit) (1979)', 5.0)

9) Fetch only CLOSED orders & format date into mm/dd/yyyy format from orders data.
Output:-
1,07/25/2013,11599,CLOSED
4,07/25/2013,8827,CLOSED
12,07/25/2013,1837,CLOSED
18,07/25/2013,1205,CLOSED
24,07/25/2013,11441,CLOSED

10) Join Orders & Order_Items and display output of these two dataset?
Output:
(4926,((2013-08-12 00:00:00.0,3224,PENDING_PAYMENT),(12324,1014,49.98,4,199.92)))
After that flatten the data & display only columns: 
order_id, order_date, order_item_subtotal, order_item_product_price, order_status
('4', '2013-07-25 00:00:00.0', '24.99', '49.98', 'CLOSED')
('4', '2013-07-25 00:00:00.0', '59.99', '299.95', 'CLOSED')
('4', '2013-07-25 00:00:00.0', '50.0', '150.0', 'CLOSED')
('4', '2013-07-25 00:00:00.0', '49.98', '199.92', 'CLOSED')
('10', '2013-07-25 00:00:00.0', '199.99', '199.99', 'PENDING_PAYMENT')

11) Find the employee count & cost to company for each group consisting of dept, cadre, and state?
Output:
dept,cadre,sate,TotalEmployeeCount,costToCompany
(('Sales', 'Lead', 'AUS'), (64000, 2))
(('Sales', 'Lead', 'NY'), (96000, 3))
(('Sales', 'Trainee', 'UK'), (12000, 1))
(('Sales', 'Lead', 'IND'), (64000, 2))
(('Marketing', 'Associate', 'IND'), (36000, 2))
