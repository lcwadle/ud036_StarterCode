# Upcoming Movie Trailers

This is the code to generate a webpage using **The Movie Database** to display up coming movies, their titles, release dates, and trailers.

## Structure

The code is written in python with three class files: **Movie**, **Website**, and **fresh_tomatoes**.

* Each movie is an instance of the **Movie** class.
* The **Website** class connects to **The Movie Database** and requests all upcoming movies including their movie information.  Next it uses the **fresh_tomatoes** class to output that information to the user via a web browser.
* Finally, when clicked, each movie plays the first video for the movie, often the trailer.

## Todo
Remove **The Movie Database** API key from code.  Only included so that Udacity can test the webpage.  Once evaluation is complete it will be removed and the user will have to replace dummy API key with their own.

## License

The content of this repository is licensed under a [Creative Commons Attribution License](http://creativecommons.org/licenses/by/3.0/us/)
