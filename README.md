# Aermetric testing task
### Testing task
There is a CSV file with aircraft data and their errors.
It is necessary to upload a CSV file to the database and make an endpoint that returns statistics for each aircraft (column aircraft), for each status (column status), for each type (column type). For statistics, it is necessary to calculate the sum of info_count, the sum of errors_count and the number of each type (there are 9 types) for the above columns
### Technical requirements
The job can be implemented in any framework (preferably Django), Postgresql database, wrapped in Docker and published to a repository.
### Expected output example:
[
  {
    "aircraft": "AN835",
    "status": null,
    "type": null,
    "info_count": 47,
    "errors_count": 786,
    "pre_legend": 2,
    "warning": 0,
    "paired_b": 0,
    "legend": 12,
    "lower_b": 0,
    "repeat_legend": 0,
    "upper_a": 8,
    "lower_a": 25,
    "paired_a": 6
    },

  {
    "aircraft": null,
    "status":”Suspend”,
    "type": null,
    "info_count": 32,
    "errors_count": 24,
    "pre_legend": 12,
    "warning": 7,
    "paired_b": 8,
    "legend": 12,
    "lower_b": 0,
    "repeat_legend": 0,
    "upper_a": 8,
    "lower_a": 25,
    "paired_a": 6
    },

  {
    "aircraft": null,
    "status": null,
    "type":”Warning”,
    "info_count": 1,
    "errors_count": 678,
    "pre_legend": 0,
    "warning": 0,
    "paired_b": 12,
    "legend": 2,
    "lower_b": 0,
    "repeat_legend": 0,
    "upper_a": 8,
    "lower_a": 5,
    "paired_a": 6
    },
]
### The project used:
- python = 3.8
- Django = 4.0.4
- psycopg2 = 2.9.3
- djangorestframework = 3.13.1
- factory-boy = 3.2.1
### Installation:
1. create folder where you want expand project and go there 
2. write a command: git clone https://github.com/emilrakaev/aermetric_testing_task
3. write a command: docker-compose build
4. write a command: docker-compose up
### Endpoints documentation
- **Upload csv file data in model**
   - Path: [http://localhost:8000/api/v1/upload_file/](http://localhost:8000/api/v1/upload_file/))
   - Method: POST
   - Body
      - file: csv file
 - **Get aircraft statistic**
   - Path: [http://localhost:8000/api/v1/get_statistic/](http://localhost:8000/api/v1/get_statistic/))
   - Method: GET
### Run test
- run command: docker-compose run --rm web python manage.py test
