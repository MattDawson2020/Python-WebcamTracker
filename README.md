## 🐍 Python-Motion tracker app

- Seventh example project from [Udemy course](https://www.udemy.com/course/the-python-mega-course/)
- Uses OpenCV and Pandas to track motion from a webcam, and then Bokeh to plot the motion timestamps to a Dataframe, and render that dataframe as a hime series graph with Bokeh hovertools data


## 📓 Comments

- OpenCV and Pandas are possibly two of the most powerful Python libraries, letting you very quickly create complex programs using minimal code
- Tracking is not as accurate as I would like, often applying multiple boxes to the same object, but it is suprisingly accurate for the time taken
- 


## 💻 Running the app

- Clone this repo to your local machine, navigate to the directory, and then use ``` python plotting.py  ``` to run the graph plotting script, which will run the motion_detector script by importing the resulting Dataframe
- The window will popup on your screen, which will then track your movements, highlighting them in a green box
- When you are done with the video section, press ``` q ``` to quit the video program, and the graph will load in a browser window



