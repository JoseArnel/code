
/* SQL 50  
Select */
/* Q1: 1757. Recyclable and Low Fat Products */
SELECT product_id
FROM Products
WHERE low_fats = 'Y' and recyclable = 'Y'

/* Q2: 584. Find Customer Referee */
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id is NULL

/* Q3: 595. Big Countries */
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >=25000000

/* Q4: 1148. Article Views I */
SELECT distinct author_id as id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC

/* Q5: 1683. Invalid Tweets */
SELECT tweet_id 
FROM Tweets
WHERE LENGTH(content) > 15

/* Basic Joins */
/* Q6: 1378. Replace Employee ID With The Unique Identifier */
SELECT EmployeeUNI.unique_id as unique_id, Employees.name as name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id

/* Q7: 1068. Product Sales Analysis I */
SELECT product_name, year, price
FROM Sales
LEFT JOIN Product ON Sales.product_id = Product.product_id

/* Q8: 1581. Customer Who Visited but Did Not Make Any Transactions */
SELECT customer_id, count(visit_id) as count_no_trans
FROM visits
WHERE visit_id not in(
    SELECT transactions.visit_id 
    FROM visits 
    INNER JOIN transactions on transactions.visit_id = visits.visit_id
)
GROUP BY customer_id

/* PSUEDO
Counting How many Transactions We're not made / Visits where no transactions were made
Output: customer_id, count_no_trans
Join Where Visit id equals
Count, Where */

/* Q9: 197. Rising Temperature */
SELECT w1.id 
FROM Weather w1, Weather w2 
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 and w1.temperature > w2.temperature

/* Q10: 1661. Average Time of Process per Machine */
SELECT a1.machine_id, round((avg(a1.timestamp - a2.timestamp)),3) as processing_time
FROM Activity a1
JOIN Activity a2 ON a1.machine_id = a2.machine_id and a1.process_id = a2.process_id 
and a2.activity_type = 'start' and a1.activity_type = 'end'
GROUP BY a1.machine_id

-- SELECT sum(DATADIFF(second, a1.timestamp, a2.timestamp))/count(# processes)
-- coun
-- SELECT customer_id, count(visit_id) as count_no_trans
-- FROM visits
-- WHERE visit_id not in(
--     SELECT transactions.visit_id 
--     FROM visits 
--     INNER JOIN transactions on transactions.visit_id = visits.visit_id
-- )
-- GROUP BY customer_id

/* Q11: 577. Employee Bonus */
SELECT name, bonus
FROM Employee
LEFT JOIN Bonus on Employee.empId = Bonus.empId
WHERE Bonus.bonus < 1000 or Bonus.bonus IS NULL

/* Q12: 1280. Students and Examinations */
SELECT Students.student_id, Students.student_name, Subjects.subject_name, COUNT(Examinations.student_id) as attended_exams
FROM Students
CROSS JOIN Subjects
-- CROSS JOIN
LEFT JOIN Examinations ON Students.student_id = Examinations.student_id and Subjects.subject_name = Examinations.subject_name
GROUP BY student_id, subject_name
ORDER BY student_id

/* Q13: 570. Managers with at Least 5 Direct Reports */
SELECT e.name
FROM Employee as e
INNER JOIN Employee AS m ON m.managerId = e.id
GROUP BY m.managerId
HAVING COUNT(m.managerId) >= 5

/* Basic Aggregate Functions */
/* Q1: Not Boring Movies*/
SELECT * 
FROM Cinema 
Where description != 'boring' AND id%2 
ORDER BY rating DESC

/* 1075. Project Employees I */
SELECT project_id, ROUND(AVG(experience_years),2) as average_years
FROM Project as P
INNER JOIN Employee as e ON e.employee_id = p.employee_id
GROUP BY project_id

/* 1633. Percentage of Users Attended a Contest */
SELECT contest_id, ROUND(COUNT(r.user_id) * 100/ (SELECT count(user_id) FROM Users), 2) as percentage 
FROM Register as r
LEFT JOIN Users as u on u.user_id = r.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id
1211. Queries Quality and Percentage
/* 1211. Queries Quality and Percentage */
SELECT query_name, ROUND(AVG(rating/position),2) as quality, ROUND((AVG(IF(rating<3,1,0)*100)),2) as poor_query_percentage 
FROM Queries
WHERE query_name is NOT NULL
GROUP by query_name
/* 1193. Monthly Transactions I */
SELECT SUBSTRING(trans_date, 1, 7) as month, country, COUNT(id) as trans_count, SUM(IF(state='approved',1,0)) as approved_count, SUM(amount) as trans_total_amount, SUM(IF(state='approved',amount,0)) as approved_total_amount
FROM Transactions 
GROUP BY month, country










595. Big Countries
SELECT name, population, area
FROM World
WHERE world.population >= 25000000 or world.area >= 3000000

# 596. Classes More Than 5 Students
SELECT class
FROM Courses
GROUP BY class
HAVING count(DISTINCT student) >= 5

# 1757. Recyclable and Low Fat Products
SELECT product_id
FROM products
WHERE low_fats = 'Y' and recyclable = 'Y'

# 183. Customers Who Never Order
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id is NULL

#1873. Calculate Special Bonus
SELECT name as Customers
FROM Customers 
WHERE Customers.id not IN (SELECT customerId from Orders)

1873. Calculate Special Bonus
SELECT employee_id,  salary * ( employee_id % 2) * (name not like 'M%') as bonus
FROM Employees
ORDER BY employee_id

627. Swap Salary
UPDATE Salary  
SET sex = CASE sex
    WHEN 'f' THEN 'm'
    ELSE 'f'
END

196. Delete Duplicate Emails
DELETE p1 
FROM Person p1, Person p2
WHERE p1.email = p2.email and p1.id > p2.id


1667. Fix Names in a Table
SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2, LENGTH(name)))) as name
FROM Users
ORDER BY user_id

1484. Group Sold Products By The Date
/* Algorithm: 
Output: Distnct sell_date, num_sold, products
Interate thought table, find dates that match, count/increment!
make a list of products, concat product names from activities list */
SELECT sell_date, COUNT(DISTINCT product) as num_sold, GROUP_CONCAT(DISTINCT product) as products
FROM activities
GROUP BY sell_date

1527. Patients With a Condition
/* Algorithm
Find matching DIAB100, condition
Output: patient_id, patient_name, conditions
Interate conditions column and find matching string
REGEX
*/
SELECT patient_id, patient_name, conditions
FROM patients
WHERE conditions like 'DIAB10%'
OR conditions like '% DIAB10%'

SELECT * FROM patients WHERE conditions REGEXP '\\bDIAB1'

1795. Rearrange Products Table
SELECT T.employee_id
FROM (SELECT * FROM employees LEFT JOIN salaries USING(employee_id)
        UNION
        SELECT * FROM employees RIGHT JOIN salaries USING(employee_id))
AS T
WHERE T.salary is NULL
OR T.name IS NULL
ORDER BY employee_id

# Not working
SELECT employees.employee_id
FROM employees
FULL JOIN salaries ON  employees.employee_id = salaries.employee_id
WHERE employees.employee_id is NULL 
OR salaries.employee_id is NULL

SELECT employees.employee_id
FROM employees
LEFT JOIN salaries on employees.employee_id = salaries.employee_id
UNION ALL
SELECT employees.employee_id
FROM employees
RIGHT JOIN salaries on employees.employee_id = salaries.employee_id
WHERE salaries.salary IS NULL
OR employees.name IS NULL


1795. Rearrange Products Table
mysql>create table data(id int, a varchar(255), b varchar(255), c varchar(255));
mysql>insert into data(id,a,b,c) values(1,'a1','b1','c1'),(2,'a1','b1','c1');
mysql>select * from data;

+------+------+------+------+
| id   | a    | b    | c    |
+------+------+------+------+
|    1 | a1   | b1   | c1   |
|    2 | a1   | b1   | c1   |
+------+------+------+------+

mysql> select id, 'a' col, a value
      from data
      union all
      select id, 'b' col, b value
      from data
      union all
      select id, 'c' col, c value
      from data;
+------+-----+-------+
| id   | col | value |
+------+-----+-------+
|    1 | a   | a1    |
|    2 | a   | a1    |
|    1 | b   | b1    |
|    2 | b   | b1    |
|    1 | c   | c1    |
|    2 | c   | c1    |
+------+-----+-------+

SELECT product_id, 'store1' store, store1 price
FROM products
UNION ALL
SELECT product_id, 'store2' store, store2 price 
FROM products
UNION ALL
SELECT product_id, 'store3' store, store3 price
FROM products

/* Algorithm
Turn store column  in rows
unpivot table
*/
SELECT t.product_id, t.store, t.price
FROM (
    SELECT product_id, 'store1' store, store1 price FROM products
    UNION ALL
    SELECT product_id, 'store2' store, store2 price FROM products
    UNION ALL
    SELECT product_id, 'store3' store, store3 price FROM products
) t
WHERE t.price is not Null

608. Tree Node
/* Algorithm
Output: id Type,
Case 1. Null = Root
Case 2.They do not have child nodess, Leaf
Case 3. They have child nodes and not null, Inner
*/ 
SELECT id, 'Root' as type
FROM tree
WHERE p_id is null
UNION
SELECT id, 'Leaf' as type
FROM tree
WHERE id not IN(SELECT p_id from tree WHERE p_id is not null) 
and p_id is not NULL
UNION
SELECT id, 'Inner' as type
FROM tree
WHERE p_id is not NULL
and id IN (SELECT p_id from tree WHERE p_id is not null) 

176. Second Highest Salary
/* Algorithm
Output: Second Highest Salary
Return Id 2?
*/
SELECT MAX(salary) as SecondHighestSalary
FROM employee
WHERE salary NOT IN(SELECT MAX(salary) FROM employee)
AND (SELECT COUNT(id) FROM employee) >= 1

175. Combine Two Tables
SELECT person.firstName, person.lastName, address.city, address.state
FROM person 
LEFT JOIN address ON person.personID = address.personID

1741. Find Total Time Spent by Each Employee
SELECT event_day as day, emp_id, (SUM(out_time) - SUM(in_time)) as total_time
FROM employees
GROUP BY event_day, emp_id

1581. Customer Who Visited but Did Not Make Any Transactions
SELECT customer_id, count(visit_id) as count_no_trans
FROM visits
WHERE visit_id not in(
    SELECT transactions.visit_id 
    FROM visits 
    INNER JOIN transactions on transactions.visit_id = visits.visit_id
)
GROUP BY customer_id

1148. Article Views I
SELECT DISTINCT viewer_id as id 
FROM views
WHERE author_id = viewer_id

607. Sales Person
/* Algorithm
Q: Return salesperson who did not have orders with the name "Red"
JOIN 3 tables
GET sales salesID where com

Work Backwords
GET sales_id from 1 
*/
SELECT DISTINCT name
FROM SalesPerson
LEFT JOIN orders ON SalesPerson.sales_id = orders.sales_id
WHERE SalesPerson.sales_id NOT IN(  
    SELECT sales_id
    FROM orders
    LEFT JOIN company ON orders.com_id = company.com_id
    WHERE company.name = "RED")

1141. User Activity for the Past 30 Days I
/* Algorithm
Output: activity of users: Day, active_users 
Count, using Where in range, Group By 
*/ 
SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM activity
WHERE activity_date > '2019-06-27' and activity_date < '2019-07-27'
GROUP BY activity_date

1693. Daily Leads and Partners
/*
 as unique_leads, distinct partner_id as unique_partners
 COUNT Group BY, 
 data_id, make_name, 
*/

SELECT date_id, make_name, COUNT(DISTINCT lead_id) as unique_leads, COUNT(DISTINCT partner_id) as unique_partners
FROM DailySales
GROUP BY date_id, make_name

1729. Find Followers Count
SELECT user_id, COUNT(DISTINCT follower_id) as followers_count
FROM followers
GROUP BY user_id

586. Customer Placing the Largest Number of Orders
/* Algorithm
Output: Customer_number, 
Return Count of order(nums)
*/

SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY count(customer_number) DESC
LIMIT 1 

511. Game Play Analysis I
SELECT player_id, MIN(event_date) as first_login
FROM activity  
GROUP BY player_id

1890. The Latest Login in 2020
SELECT user_id, MAX(time_stamp) as last_stamp
FROM logins
WHERE YEAR(time_stamp) <= 2020 and YEAR(time_stamp) > 2019
GROUP BY user_id

1407. Top Travellers
SELECT name, COALESCE(SUM(distance),0) as travelled_distance
FROM rides
RIGHT JOIN users ON rides.user_id = users.id
GROUP BY user_id
ORDER BY sum(distance) DESC, name ASC

FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY ,
so, it removes the records for which no orders were placed in 2019 way before you can perform a GROUP BY or SELECT(COUNT).

182. Duplicate Emails
SELECT email as Email 
FROM person
Group By email
HAVING Count(email) > 1

1050. Actors and Directors Who Cooperated At Least Three Times
SELECT actor_id, director_id
FROM actordirector
GROUP BY actor_id, director_id
HAVING Count(director_id) > 2

1587. Bank Account Summary II
SELECT name, SUM(t.amount) as balance
FROM users u 
RIGHT JOIN transactions t ON u.account = t.account 
GROUP BY u.account=
HAVING SUM(t.amount) > 10000

1084. Sales Analysis III
SELECT p.product_id, product_name 
FROM product p 
RIGHT JOIN sales s ON s.product_id = p.product_id
WHERE s.product_id NOT IN (
SELECT product_id from sales WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31')
GROUP BY p.product_id

1393. Capital Gain/Loss
SELECT stock_name, 
SUM(CASE WHEN operation = 'Buy' THEN -price ELSE price END) as capital_gain_loss
FROM stocks 
GROUP BY stock_name 

197. Rising Temperature
SELECT weather.id
FROM weather
JOIN weather w ON DATEDIFF(weather.recordDate, w.RecordDate) = 1
WHERE weather.temperature > w.temperature


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums

    def sleep_in(weekday, vacation):
  if (weekday == False or vacation == True):
    return True
  else:
    return False

    def monkey_trouble(a_smile, b_smile):
  if(a_smile == b_smile):
    return True
  else:
    return False

    123 

    345

    678

  def sum_double(a, b):
  if a and b and a == b:
    return 2*(a+b)
  else:
    return a+b

  def diff21(n):
  if (n > 21):
    return (n-21)*2
  else:
    return (21-n)

  def parrot_trouble(flag, h):
  if(flag != False and (h < 7 or h > 20)):
    return True
  else: 
    return False

  def makes10(a, b):
  if((a == 10 or b == 10) or ((a + b) == 10)):
    return True
  else:
   return False

  def near_hundred(n):
  if (n < 150):
    x = 100 - n 
  else: 
    x = 200 - n
  if ((abs(x) <= 10) or (abs(n) == 100)):
    return True
  else: 
    return False


  def near_hundred(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

  def string_times(text, n):
    return(text*n

def front_times(txt, n):
  if(len(txt) > 4):
    return(txt[:3] *n)
  else:
    return(txt*n)

def string_bits(txt):
  string = ""
  for i in range(0, len(txt), 2):
    string += txt[i]
  return string

def string_splosion(txt):
  result = ""
  for i in range(0, len(txt)):
    result += txt[:i+1]
  return result
def last2(txt):
  string = txt[-2:]
  count = 0
  for i in range(0, len(txt)-2):
    if (txt[i:i+2] == string):
      count += 1
  return count

def array_count9(n):
  count = 0 
  for i in range(len(n)):
    if n[i] == 9:
      count += 1
  return count

def array_front9(n): 
  l = 4
  if (len(n) < 4):
    l = len(n)    
  for i in range(0, l):
    if (n[i] == 9):
      return True
  return False

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums [i+2]==3:
      return True
  return False
            
def array123(n):
  for i in range(0, len(n)-2):
    if n[i] == 1:
      if n[i+1] == 2:
        if n[i+2] == 3:
          return True
  return False

def string_match(a, b):
  count = 0
  for i in range(0, len(a)-1):
    if (a[i:i+2] == b[i:i+2]):
      count += 1
  return count


def double_char(txt):
  string = ""
  for i in range(len(txt)):
    string += txt[i]*2
  return string

def count_hi(txt): 
  count = 0
  for i in range(0, len(txt)-1):
    if txt[i] == 'h' and txt[i+1] == 'i':
      count += 1
  return count

  def cat_dog(txt): 
  count1 = 0
  count2 = 0 
  for i in  range(0, len(txt)-2):
    if txt[i] == 'c' and txt[i+1] == 'a' and txt[i+2] == 't':
      count1 += 1
    elif txt[i] == 'd' and txt[i+1] == 'o' and txt[i+2] == 'g':
      count2 += 1
  return (count1 == count2)

def cat_dog(str):
  a = str.split('cat')
  b = str.split('dog')
  if len(a) == len(b):
    return True 
  else: 
    return False

def count_code(str):
  count = 0
  for i in range(0, len(str)-3):
    if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
      count += 1
  return count

def end_other(str1, str2):
  x = str1.lower()
  if (len(str1) >= len(str2)):
    x = str2.lower()
  if (x == str2[-len(x):].lower()):
    return True
  return False

  def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if a.endswith(b) or b.endswith(a):
    return True
  return False

def xyz_there(str):
  str = str.replace('.xyz', ' ')
  if 'xyz' in str:
    return True
  else:
    return False