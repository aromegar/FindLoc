
# FindLoc
IronHack week 4 project / Geolocation
# Finding the best place for your business using spatial data analysis and GeoLocation

![](https://media.istockphoto.com/photos/modern-office-interior-picture-id1136436814)


FindLoc is a data-driven analytical consultant firm with expertise in finding the office that fits exactly for each client. We have been hired to help locate the new headquarters for a tech start-up. According to a list of requirements, we will use geospatial data techniques to propose and evaluate a list of potential candidates.

## Workflow

First of all, we will propose an array of candidate locations across the US, based on clusterization of similar tech-companies based on the ZIP-code of their location. We shortlist them to 10 final candidates located in San Francisco, Silicon Valley, New York and Seattle.

Second, for each location, we create a database with the interesting venues for our client in a radius of 800m. Then we query to this database wich venues are located closer than 500m and build a total score according to a previous weight distribution. The final output is a total score and a map where the proposed location and near venues are displayed.

## What is in this repo

In this repository you will find:

 - A readmi.md file with information about the project (this document).
 
 - A "0 - Finding candidates" Jupyter notebook in wich we extract 10 candidates for further analysis.
 
 - A subsequent series of Jupyter notebooks called "1-First candidate", "2-Second candidate", etc with particular analysis for each candidate.
 
 - A "DATA" folder with a csv with the candidates info (including a map) and a specific json file with the venues around each candidate analyzed.
 
  - A "src" folder with cleaning functions and API functions for calling Google and zip codes service.
 
## Libraries

In this project we have used the following libraries:

 - [pandas](https://pandas.pydata.org/docs/)
 
 - [pymongo](https://pymongo.readthedocs.io/)
 
 - [json](https://docs.python.org/3/library/json.html)
 
 - [folium](https://python-visualization.github.io/folium/)

