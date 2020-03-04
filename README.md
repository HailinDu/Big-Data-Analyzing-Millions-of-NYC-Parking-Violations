# Analyzing millions of NYC Parking Violations
# (STA9760 - Big Data Technologies)
The project is broken into three parts. 
1. Part1: Python Scripting
2. Part2: Loading into ElasticSearch
3. Part3: Visualizing and Analysis on Kibana

## Dataset
The Open Parking and Camera Violation dataset is coming from NYC Open Data. 

# Part 1 
Develop a python command line interface that will connect to the OPCV API and demonstrate that the data is accessible via python. 

Build image from Dockerfile and push the image to Docker Hub. Lastly, run the image in AWS EC2 instance.

## Using Dockerfile
1. Build an image from our dockerfile on your computer:

        $ docker build -t image_name . 
        
2. Create a container and run Python script locally. The command line is:

        $ docker run -v $(pwd):/app -e APP_KEY=API_Token -t image_name python main.py --page_size=1000 --num_page=4 --output=results.json
        
        #--page_size: This command line argument is required. It will ask for how many records to request from the API per call.
        #--num_pages: This command line argument is optional. If not provided, your script should continue requesting data until the entirety of the content has been exhausted. If this argument is provided, continue querying for data num_pages times.
        #--output: This command line argument is optional. If not provided, your script should simply print results to stdout. If provided, your script should write the data to the file (in this case, results.json).
        
3. Deploying via Docker Hub:

        $ docker push your_username/image_name
        
4. Pulling this image from dockerhub and runing it in AWS EC2 instance:

        ~$ sudo docker pull image_name
        ~$ sudo docker run -it your_username/image_name /bin/bash
        ~$ sudo docker run -e APP_KEY=API_token -it your_username/image_name python main.py --page_size=1000 --num_page=4 --output=results.json

## Part2:
Coming Soon
