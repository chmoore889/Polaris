# Polaris: A Smart Cane
## Won *Best Health Hack* at SBUHacks 2019
### Team Members: Elyas Masrour, Chris Moore, Abdullah Nauman, and Rohan Nagavardhan

A novel smart accessory to help the visually impaired navigate to any given destination. 

Many blind people can still live normally with their disability. They have jobs, friends, and places to be. Like the rest of us, in order to get to where they need to be, they need navigation. However, often times, people with disabilities are simply an afterthought in phone and software design. Not anymore. We wanted to create a device that is designed primarily with the visually impaired in mind.

So, we decided to create a smart speaker that can be clipped onto a cane, an everyday necessity for the blind). This speaker uses a singular button and voice commands to bring the conveniences of GPS to the blind.

## The Front End: 

Upon pressing a large conveniently located button at the top of the device, Polaris uses a combination of C and Python to fluently converse with the user using the about their desired destination and finds the most optimal route for their journey.

## Integrating with API's:

Polaris uses the Google Speech API to carry a seamless conversation with the user and uses powerful machine learning techniques to locate specific key phrases regarding the destination and ignores background noise. Using the key phrases, Polaris finds the best route for the user through the Google Maps API, guiding them through conversation based on coordinate values from the Raspberry Pi.

## What we learned 

*Elyas* - I learned so much during this project. I handled the product design and hardware. Creating physical hardware that matches up to the needs of our software was very difficult. I went through many phases of the design, revising constantly to match up what was needed, what looked the best, and what was available. Additionally, I helped with project management and helped make sure everyone on the team had everything they needed to do their job. I tried to facilitate communication between team members and encouraged healthy decisions (such as sleeping and eating).

*Rohan* - I came into this competition-ready and confident. I had experience with API requests before and thought I was ready for any challenge that came my way. However, this project really stretched my experience with Python. Not only did I have to extract data from certain APIs, but I also had to process the data to make it ready for the user. This proved a formidable challenge, but I worked very hard, and eventually accomplished my goal.

*Abdullah* - I also tackled a difficult task. I primary woked with input and output data for the Raspberry Pi. At first, I designed a solution with NodeJS that could do the things we needed to do. It worked initially, but later, due to certain network errors, the system did not work reliably, and it soon became clear it would not be possible. I did not give up, however. I adapted and started from scratch on another program. By the end of the competition, I had it working with the Google Speech API using the Python library. My knowledge of all things Raspberry Pi has multiplied.

*Christopher* - I collaborated with Rohan and Abdullah on making the code that ran on the Raspberry Pi. I made software that allowed both Rohan and Abdullah's Python code to more easily interface with lower level systems of the Pi. We had to adapt to many problems, like a browser that was behaving weird, screwed up permissions, SSL certificates, and SSH permissions. For each one, we brainstormed a solution, decided on it, and implemented it. It was certainly a learning experience. I learned not to get my mind set on one way- we had to improvise so many times I can't even count.
