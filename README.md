# Hillary-Trump-First-Debate-Twitter-Analysis

This repo includes everything I needed to make and use to eventually publish this analysis of Hillary and Trump's first debate [here](http://andresavalos.com/hillary-and-trump-the-debate-through-twitter.html).

- **fetchprogram.py** is the Twitter scraping script. It connects to the Twitter API and outputs the live stream of Tweets. Check the final line of this code for the keyword filter.
- **tweets.db** is the SQLite database that stores all the captured tweets. 
- **convertcsv.py** is the Python script used to convert the SQL database to *.csv* format.
- **Hillary Trump Debate Analysis.ipynb** is the IPython (or Jupyter) notebook used to explore the .csv file and generate the charts.
- The **images** folder contains all the charts I made in .png format.
- The **website** folder contains the only necessary files for creating [the webpage](http://andresavalos.com/hillary-and-trump-the-debate-through-twitter.html). The main thing to see here is the HTML file.

- **Hillary Trump Debate Analysis+get_meme.ipynb** a fun little detour

Enjoy!
