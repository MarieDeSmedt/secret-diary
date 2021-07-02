# secret-diary

project management is done in kanban method

the evolution of the project in real time can be observed via:


https://docs.google.com/spreadsheets/d/1m2sT1Hc3ZxshAQQgosWXsNnj9f5wLl92FvwrM2SdfWo/edit?usp=sharing


there is: 

- the project architecture
- the uses cases
- the API map
- the MPD
- the task monitoring table




## Goals:


A web-app:

your client is a life coach, he helps people feel good about their daily lives.
To follow the morale of his clients in two coaching sessions, he asks them to write a short text every day.
He would like to automate his follow-up.
For it:

    creation of a database to store your coach's information
    a REST API to be able to interact with this database
    a web application used as a graphical interface.




## Content

  
-> api

    -> api.py (api using fastapi)
    -> crud.py (crud methods to ensure data persistence)
    -> models.py ( define antities for database)
    -> schemas.py (define entities shape to use pydantic)
       
      
 -> app

    -> app_utils (methods)
    -> my_app (front app with streamlit)
    -> page.py (class used for display pages on streamlit)
    
 -> src
    
    -> utils        
        
        -> __init__
        -> mysql_utils (method to connect to database)
        
    -> start
    
        -> __init__
        -> to_start (run first to create and connect database)
   


- requirements.txt (Contains libraries and versions)

## Getting Started

localy :

- run to_start.py 
- in terminal: uvicorn api.api:api --reload
- in terminal: streamlit run app/my_app.py



### Prerequisites

Nan

### Installing

Nan


## Running the tests

Nan

### Break down into end to end tests

Nan

### And coding style tests

Nan

## Deployment

Nan

## Built With

Nan 

## Contributing

Nan

## Versioning

Nan

## Authors

* **Marie De Smedt** - *Initial work* - [LinkedIn](www.linkedin.com/in/marie-desmedt)



## License

Nan

## Acknowledgments

Nan


