# Data Engineering Challenge

Hello and thank you for applying for the Data Engineer position at Quandoo!

To help us better assess your technical skills, we have prepared a set of tasks for you.

In order to succeed, it is not 100% necessary to finish all the tasks. Quality is more important than quantity.

These tasks attempt to mimic the 3 most common types of problems that our data engineers encounter at Quandoo: 

* designing data pipelines
 
* writing SQL
 
* writing scalable, maintainable Python/Scala code 

If you're not sure whether you can make certain assumptions (for example, about the input data) you can either make up your own reasonable assumptions(in which case make sure to communicate them when submitting your work), or discuss it with us (aleksandr.kurilov@quandoo.com or create an Issue here).

The preferred way to submit your work is described at the end of this readme. If you would like to use a different method, write to us and let's discuss it.

Now, the tasks!


## Task 1 - Data pipeline architecture 
We want to help our salespeople find new clients who might be interested in our products. 
In order to do that, we want to crawl around 10 million web pages that contain info about these potential clients.
The data should be stored in(or readable as), the JSON format, and should satisfy a specific schema(let's say something like `{"name", "phone", "email"}`).
The end result should be some type of a DB table/Kafka topic/some other storage that contains this data.
We want to minimize data latency and avoid unnecessary financial costs as well.
In other words, the data should be updated as often as possible and as cheaply as possible.
How would you design such a system? 
You might consider, for example
* which programming language to use
* which distributed computing engine to use
* which cloud services to use
* which algorithms, broadly speaking, to use 

No need to go too deep: you don’t have to decide on specific libraries, language/engine/service-specific tools or super-precise configurations for the aforementioned products or cloud services.

Please, compose an architecture diagram or a description - in any format you want - as a solution for the task. 

## Task 2 - SQL 
We have a table that contains our “merchants”(restaurants).
For each merchant we might have more than one row, where each row represents the state of the merchant at the time indicated by the timestamp field.
Write an SQL query that returns the last state of each merchant. 
 
| Field Name | Data Type  |  Description |
|---|---|---|
| merchant_id  |  STRING |  Merchant Identifier |
| timestamp  |  INTEGER |  Merchant state timestamp|
| createdAt  |  INTEGER |  Merchant creation timestamp |
| cuisines_additional | STRING | Merchant’s additional cuisines |
| priceRange| INTEGER | Price range category | 
 
Write two(or more) SQL queries that both return the last state of each of the merchants and outline their advantages and disadvantages(for example, how many times is the source table scanned)?

You can find some sample data in sql_challenge_dataset.csv.

## Task 3 - Data Processing with Python/Scala

You can complete the challenge using either Python or Scala.

The goal here is to analyze our 2020 reservations. 

The first step is to create a program that would reliably work with the given inputs(reservation_dataset.csv and merchant_dataset.csv).

The second step is to consider scaling issues.

### Making it work with the given inputs

The input for this challenge are reservation_dataset.csv and merchant_dataset.csv(you can find them in this repo).

* Exclude all the reservations with badly formatted email addresses. Note that the email addresses have been anonymized on purpose.
* Print the average number of seated guests
* Display the name of the merchant with the highest amount of seated guests from the merchant_csv dataset. Reservations with only 1 seated guest shouldn’t be considered for this analysis.
* Display the name of the merchant with the highest amount of reservations for each quarter of the year (January, February, March;  April, May, June ...).

Please provide a dockerized program that can execute all 3 tasks sequentially.  

Bonus points if it comes with a script that allows us to use a different set of files as the input(with the same structure, of course).


### Scaling 

Does your solution scale for any/all of the subtasks(1-3)? 

In other words, would it still work if reservation_dataset.csv and merchant_dataset.csv were both 500G+ files? 

If not, try to come up with an upgraded version of the program that would handle bigger inputs.

If the solution that you have in mind is too complex or time-consuming to implement, describe what you would use and how it would fit together, or provide a diagram. 


## Submitting your solutions

* Fork it to a [!]private[!] gitlab repository (go to Settings -> General -> Visibility, project features, permissions -> Project visibility).
* Commit&Push your solutions(including all the diagrams, descriptions and code)
* Share the project with the gitlab user quandoo_recruitment_task (go to Settings -> Members -> Invite member, find the user in Select members to invite and set Choose a role permission to Developer)
* Send us an ssh clone link to the repository.

We are looking forward to discussing your solutions with you. Good luck!
