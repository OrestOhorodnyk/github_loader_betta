# GttHub Loader

This application will create a new repository in a user's GitHub account and commits its code to the
repository.


## Requirements:
* This application can be deployed to any OS with docker installed 
* To create a new repository a user should have valid GitHub username and password

## Getting Started
```
git clone https://github.com/OrestOhorodnyk/github_loader.git
```

### Prerequisites

You need to build application with docker so install it and run:

```
cd github_loader
sudo docker build -t github_app .
```

### Installing

Wait until docker install all dependencies(it may take 5 min)

Then docker run all a container

```
sudo docker run -d -p 5000:5000 --name github_loader github_app
```

Wait until consumer app give you message like this :"connection with Kafka broker successfully established"


## Usage
1.  Open a browser and navigate to 
```
http://localhost:5000/login
```

2. Enter your GitHub **username** and **password**

3. Click the **'Create new repository'** button

Creation of new repository may take around one minute, after it dane you'll see 
confirmation  message.

4. After successful repository creation you can logout by clicking on the 
'Logout' button in top left corner

## Debuging
