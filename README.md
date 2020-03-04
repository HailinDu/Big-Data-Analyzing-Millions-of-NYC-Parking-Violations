# Analyzing millions of NYC Parking Violations
### STA9760 - Big Data Technologies
The purpose of this project is to conduct data visualization analysis to understand Parking and Camera Violation in NYC. We will be going through the process of containerization, terminal navigation, python scripting, artifact deployment and AWS EC2 provisioning. 

### Dataset
The Open Parking and Camera Violations dataset was initially loaded with all violations contained in the mainframe database as of May 2016 (Initial dataset loaded 05/14/2016.). New or open violations will be updated weekly (Sunday). [NYC Open Data](https://data.cityofnewyork.us/City-Government/O)

### Install & Quickstart
You will need to install [Docker](https://docs.docker.com/install/), [Docker Compose](https://docs.docker.com/compose/install/), register a [Docker Hub](https://hub.docker.com/) account, create a [Amazon EC2](https://aws.amazon.com/?nc1=h_ls) server account. create a [NYC App Token](https://data.cityofnewyork.us/login) from NYC Open Data.

### Overview
The project is broken into three parts. 
1. Part1: Python Scripting
2. Part2: Loading into ElasticSearch
3. Part3: Visualizing and Analysis on Kibana

## Part 1 
Develop a python command line interface that will connect to the OPCV API and demonstrate that the data is accessible via python. 

Build image from Dockerfile and push the image to Docker Hub. Lastly, run the image in AWS EC2 server.

### Using Dockerfile & Running AWS EC2 
1. Build an image from our dockerfile on your computer:

        $ docker build -t image_name . 
        
2. Create a container and run Python script locally. The command line is:

        $ docker run -v $(pwd):/app -e APP_KEY=API_Token -t image_name python main.py --page_size=1000 --num_page=4 --output=results.json
        
        #--page_size: This command line argument is required. It will ask for how many records to request from the API per call.
        #--num_pages: This command line argument is optional. If not provided, your script should continue requesting data until the entirety of the content has been exhausted. If this argument is provided, continue querying for data num_pages times.
        #--output: This command line argument is optional. If not provided, your script should simply print results to stdout. If provided, your script should write the data to the file (in this case, results.json).
        
3. Deploying via Docker Hub:

        $ docker push your_username/image_name
        
4. Pulling the image from dockerhub and running it in AWS EC2

        ~$ sudo docker pull image_name
        ~$ sudo docker run -it your_username/image_name /bin/bash
        ~$ sudo docker run -e APP_KEY=API_token -it your_username/image_name python main.py --page_size=1000 --num_page=4 --output=results.json

## Part 2:
Coming Soon
