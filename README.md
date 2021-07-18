## Inspiration
For those of us who live in India have been stuck inside our homes for a long time. Only recently a glimmer of hope has emerged and people are planning their vacations away from their homes. I have developed this project to help them. There are two parts to this project. Both of them geared to help and educate the people of what places to visit and what is the situation on the outside.  
## What it does
There are two sides to this project:
>The first side to the project is the Flutter and Python application. The Flutter is the frontend for a DiagFlow ES bot and a server hosted on Replit written in python handles the webhooks for the bot. The bot is trained to handle queries like "Is is safe to travel to ___" where ___ can be filled by any country. It will return the latest CDC data on that country and their recommendation. It also will tell you the number of COVID cases of any country if you as "How many cases are there in ___" , ___ again being any county of your choosing. These were the international travel help. For domestic travel (inside India) you can ask things like "Help me plan a Daycation", or " I want to go to Noida Should I do so?" or "I want to travel to Noida from silchar. Should I?" Depending on your question it will ask you all the necessary information and provide you with some data. 
> The second Part to this project is the one which took major chunk of my time. It is a filter developed using Spark AR and Blender for modelling. It is a 3D interactable map of India, wherein you can tap on any state to see some really cool tourist spots along with a few pictures. (The Filter along with data went over the 4MB limit of Ig and Fb hence I wasnt able to upload it there) You can also scale and move around the map as your liking. It have over 32 materials and 20 patches. 

## How I built it
I used Spark AR for the filter, I used Flutter for the frontend, Python for the Backend, Used GCP for Diagflow and an API based on GMaps distance Matrix API to help out with the Domestic Travels. I also used Cockroach DB for my DB use and also used Replit for hosting my Flask server. I used Blender for modelling my map of India

## Challenges I ran into
There were a lot of challenges I had to face. This was my first time working with Spark AR and Blender for modelling. I had never even used Visual Scripting (Patch Editor of Spark AR) so everything felt new to me. Finding the right idea to make into an AR filter was also very difficult. A lot of attempts and time also went into optimization and size reduction such that I could put it on instagram and facebook however that was not possible in the end. There were also issues with blender as I have next to none experience using the tool. All in all it was a fun and challenging weekend

## Accomplishments that I am proud of
The fact that I was able to convert my vision into the reality. I wanted to have a good AR experience and make something really cool. The fact that after over a day's worth of work on the filter alone I was able to get it to do exactly what I wanted it to do. Getting a bot together and finding the right element to scrape data from is always a difficult task.  

## What I learned
I learned a lot about Spark AR, about Visual Scripting, about Blender, about Backend, about Flutter, about Diagflow, about Cockroach DB.

## What's next for Travelisory
I plan on making a lot of these filters. That is hoping to extend India to the world. Adding more visual flare and making the app look a lot cleaner.
