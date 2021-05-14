# Serverless-Performance-Comparison

Analyzing the performance of deep learning models on serverless computing platforms. For a detailed description, please refer to the report.pdf present in the repo    

## Project Structure     
The project code has been divided into 4 folders    
1. Combined Performance - Contains code as well as data files for Comparing all the 3 models    
2. idls-project-inception - Contains code as well as data files for our experiments with InceptionV3    
3. idls-project-mobilenet - Contains code as well as data files for our experiments with MobileNet    
4. idls project-Resnet - Contains code as well as data files for our experiments with Resnet50    
Each sub-folder has the following files and sub directories
1. data/ - Directory containing all the necessary pickle files which has the data as well as information to draw graphs     
2. Jupyter Notebook - Contains code as well as visualization for Warm start experiments, Cold start Experiments and Load testing experiments    
3. locustfile.py - Code for running the load tests on locusts    
4. lambda_function/ - Code for creating the lambda function. Details will be mentioned below    

## Running the code    
1. Creating the lambda function    
Inside the lamda_function sub-folder, include a directory named "packages" having the necessary runtime libraries required like tensorflow, pillow    
2. Create and Push the docker image to ECR    
Build your docker image    
docker build -t hello-world .   
    
Authenticate the Docker CLI to your Amazon ECR registry.    
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com    
    
Tag your image to match your repository name, and deploy the image to Amazon ECR using the docker push command.     
docker tag  hello-world:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest    
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest        
    
3. Create a REST endpoint using the API Gateway    
4. Connect APIGateway to Lambda    
5. Mention the endpoint in the notebook and run    


