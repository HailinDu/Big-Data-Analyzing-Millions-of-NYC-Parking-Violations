# Analyzing millions of NYC Parking Violations
### STA9760 - Big Data Technologies
The purpose of this project is to conduct data visualization analysis to understand Parking and Camera Violation in NYC. We will be going through the process of containerization, terminal navigation, python scripting, artifact deployment and AWS EC2 provisioning. 

![NYC Open Data](https://data.cityofnewyork.us/api/assets/3FF54443-CD9C-4E56-8A20-8D2BD245BD1A?nyclogo300.png)

### Dataset
The Open Parking and Camera Violations dataset was initially loaded with all violations contained in the mainframe database as of May 2016 (Initial dataset loaded 05/14/2016.). New or open violations will be updated weekly (Sunday). [NYC Open Data](https://data.cityofnewyork.us/City-Government/O)

### Install & Quickstart
You will need to install [Docker](https://docs.docker.com/install/), [Docker Compose](https://docs.docker.com/compose/install/), register a [Docker Hub](https://hub.docker.com/) account, create a [Amazon EC2](https://aws.amazon.com/?nc1=h_ls) server account and set up a AWS EC2 instance. create a [NYC App Token](https://data.cityofnewyork.us/login) from NYC Open Data.

### Overview
The project is broken into three parts. 
1. [Part1: Python Scripting (Docker & AWS EC2)](#Part1) 
2. [Part2: Loading into ElasticSearch](#Part2) 
3. [Part3: Visualizing and Analysis on Kibana](#Part3) 

## Part1: Python Scripting
Develop a python command line interface that will connect to the OPCV API and demonstrate that the data is accessible via python. 

Build image from Dockerfile and push the image to Docker Hub. Lastly, run the image in AWS EC2 server.

**Docker Architecture**
![Credit to https://devopedia.org/docker](https://devopedia.org/images/article/101/8323.1565281088.png "credit to devopedia.org")
### Using Dockerfile & Running AWS EC2 
1. Build an image from our dockerfile on your computer:

        $ docker build -t image_name . 
        
2. Create a container and run Python script locally. The command line is:

        $ docker run -v $(pwd):/app -e APP_KEY=API_Token -t image_name python main.py --page_size=1000 --num_page=4 --output=results.json

**Key Arguments**
- --page_size: This command line argument is required. It will ask for how many records to request from the API per call.
- --num_pages: This command line argument is optional. If not provided, your script should continue requesting data until the entirety of the content has been exhausted. If this argument is provided, continue querying for data num_pages times.
- --output: This command line argument is optional. If not provided, your script should simply print results to stdout. If provided, your script should write the data to the file (in this case, results.json).
        
3. Deploying via Docker Hub:

        $ docker push your_username/image_name

4. Pulling the image from dockerhub and running it in AWS EC2

        ~$ sudo docker pull image_name
        ~$ sudo docker run -it your_username/image_name /bin/bash
        ~$ sudo docker run -e APP_KEY=API_token -it your_username/image_name python main.py --page_size=1000 --num_page=4 --output=results.json

## Part2: Loading into ElasticSearch
In this part, you will leverage docker-compose to bring up a service that encapsulates your bigdata1 container and an elasticsearch container and ensures that they are able to interact. 

You must update your original script (from Part_1) to now not only download the data but also load it into the elasticsearch instance.

### Updating the Script:
**Under Part_2/bigdata1 folder**
1. create docker-compose.yml - include three images/servcies (python, elasticsearch, kibana) to interact with your container 
1. requirements.txt - add elasticsearch
1. main.py - add 'push_elastic' arugement and pass it to the `call_api function`

**Under Part2/bigdata1/src/bigdata1 folder** 
* callapi.py add:
   * import `Elasticsearch` and `datetime, date`  
   * add `create_update_index()` function - create an elasticsearch index to store data
   * add `format_push_data()` function - format python data type and push to elasticsearch
   * update `call_api` function - takes argument from the interface (main.py)

### Use Docker-Compose to Run ElasticSearch and Kibana Locally
1. Build ElasticSearch and Kibana (Create Images):

        $ docker-compose build pyth

2. Run ElasticSearch and Kibana (Run Services):

        $ docker-compose up -d
        
3. Interact at Interface

        $ docker-compose run -e APP_KEY=API_token -v ${PWD}:/app pyth python -m main --page_size=100 --num_pages=10 --output=results.json --push_elastic=True

You have successfully pushed to ElasticSearch

## Part3: Visualizing and Analysis on Kibana
You now can visualize and analyze data in Kibana by accessing http://localhost:5601/app/kibana

Then you will go to the `Management` tab, define your Index pattern using `indices`, and use Time Filter using `issue_data`

### `Discover` Tab to See Your Data
![Discover Tab](/Part_3/Discover.png)

### `Visualize` Tab to Create Visualization
Here are some data visualization examples:

**Horizontal Bar Chart - Average Reduction Amount By County**
![Horizontal Bar Chart](/Part_3/Horizontal_Bar_Chart.png)

**Pie Chart - Top 10 Violation Type**
![Pie Chart](/Part_3/Pie_Chart.png)

**Bar Chart - Number of Violation By County**
![Bar Chart](/Part_3/Bar_Chart.png)

**Line Chart - Number of Violation Per Monthly**
![Line Chart](/Part_3/Line_Chart.png)

### `Dashboard` Tab to Combine Your Data Visualization
**Dashboard**
![Dashboard](/Part_3/Dashboard.png)

