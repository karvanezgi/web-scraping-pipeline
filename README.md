# Data Engineering test assignment

## Intro
Hello and thank you for applying for the Data Engineer position at Quandoo! 
We do hope the work on the task will be interesting for you and help us to know each other better.

In the nutshell a small system to collect and process restaurant data should be built.

The completion of the whole task could be challenging. Hence, it's split on the mandatory(A) and the extra parts(B&C).

## The motivation:
In general the motive of the task is to get a vision of the candidate's ability to:
1. Demonstrate problem solving skills
2. Demonstrate ability of the candidate not only to build pipelines but also think set up the deployment and CI/CD processes 
3. Let the candidate catch a glimpse of what work at Quandoo looks like
4. Get a closer look at the coding/documenting skills of the candidate  

## Points to consider:
1. Below a frame of the system can be found. There are mandatory parts and extra ones
3. If the full solution that you have in mind is too complex or time-consuming to implement, describe your idea and provide a diagram if it makes sense for you
4. Please do a proper documentation of what was done and why

## The mandatory part(A)
### The sourcer
* Build an app to scrape/fetch data from a website which contains restaurants data and publishes the data to the DB
* An API can be used to get the data as well as scraping process
* The app should be able to fetch restaurant's data of Berlin(or certain zone of Berlin)

**Suggestions**:
* To use this data API [source](https://location.foursquare.com/). `Place search` route can be used to retrieve restaurants and `Get Place Details` route to get place details
* To scrape data using geo_id. For retrieving pages https://www.tripadvisor.com/RestaurantSearch?Action=PAGE&geo=187323&sortOrder=relevance&o=a{page_number} url can be used

Any other open data sources could be used to fetch data.

**Extra improvements suggestions**:
* To have a schedule for the sourcer to run(daily/hourly/monthly)
* Think how to fetch only new data 
* Think how to fetch other cities 


### The database
* Deploy a database. The database is expected to be supported by [DBT](https://docs.getdbt.com/docs/supported-data-platforms)
* Build the initial database layer to store the sourcer data
* Build Datamarts layer to store calculated data
* Add more layers if it's needed

**Suggestions**:
* Use PostgreSQL, Greenplum, Clickhouse, Hive
* Datamarts should contain possibly valuable insights 

### The DWH
* [Use DBT](https://getdbt.com) to process data from the raw to the Datamarts layers
* Consider how to update Datamarts on a certain schedule(hourly, daily)
* Up to the candidate to suggest which marts could be built and the structure of the tables

**Extra improvements suggestions**:
* Use extra features of DBT. Like metrics, exposures, ..

### The deployment
* Dockerize all the pipelines

**Suggestions**:
* To deploy a K8s cluster locally and use Helm charts releases
* Use Docker Composer to run all the containers

### All jobs notes
* Please provide the proper documentation and description how to run the test assignment and see how it works
* The deployment of all the components should be easy to use. Like a pushing a 1-2 buttons. Feel free to use Bash if it's needed
* The solution is expected to be runnable on Mac and Linux
* Please consider the database to be the DWH. The data can be denormalized
* It would be great to think about scaling the system

## The extra part

### BI visualisation tool(B)
Add a visualisation tool to have dashboards

**Suggestions**:
* Use Tableau
* Use PowerBI

### Add Data Lake layer(C)
Add a raw data storage to store scraper data and add a pipeline to deliver the raw data to the DB

**Suggestions**:
* Use S3 minio

### Any extra components
Feel free to suggest any extra components you probably have experience with(adding a queue, monitoring, more DBs)
In this case please provide a diagram alongside with the description to justify your chooses

The described part of the test task can be seen on the diagram
![test_task.png](./test_task.png)

## Submitting your solutions

* Fork it to a [!]private[!] gitlab repository (go to Settings -> General -> Visibility, project features, permissions -> Project visibility).
* Commit&Push your solutions(including all the diagrams, descriptions and code)
* Share the project with the gitlab users: @martin.marx @sachin.nair2 @tamizhselvan.kandasamy @elmehdi.elkhayati (go to Settings -> Members -> Invite member, find the user in Select members to invite and set Choose a role permission to Developer)
* Send us an ssh clone link to the repository.

We are looking forward to discussing your solutions with you. Good luck!
