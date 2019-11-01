# Project 0

Web Programming with Python and JavaScript

About:
  This project contains multiple files that shows a website about Formula1.

  application.py contains functions with different routes that will direct you
  to the different webpages.

  In the folder "templates" you'll find five different html files, a style.css,
  a style.css.map and a style.scss file.
  Every webpage contains the five buttons that redirect you to the different
  pages. When you decrease the size of your page the top buttons and images
  will disappear and instead will show new buttons (red) under each other.

  Homepage.html contains:
    a bootstrap grid model that shows four columns, within the columns there are
    four buttons that also redirect you to the prefered webpage, the columns
    also contain a list with a small amount of information.
    down under the webpage you'll find the F1 logo.

  drivers.html contains:
    a table with three columns (driver number, name, team), on the right side of
    the page you'll see a picture of the 2019 driver line-up.

  Teams.html contains:
    a list of all the current F1 teams, and under it the chassis they use.
    when you click on the team's name, you'll be redirected to their website.

  Standings.html contains:
    a table with the current F1 standings, the table has four columns and on the
    right side of the page you'll see an image. It also has a .teams class that
    color the team's name in gray with a font-size of 60%.

  Calendar.html contains:
    a table with four columns (race number, GP, Circuit, Date). When you click
    on the grand prix track you'll be redirected to wikipedia where you can
    read information about the track.

  Style.scss and style.css:
    style.scss contains multiple variables, example of nesting and inheritance.
    the variables are used to determine the size, color and position of the
    html pages. here you can edit for example the size of the buttons used in
    the html files. For the buttons inheritance is used to give each button type
    its preferred size.
    @media is used to configurate the buttons and images when you make the page
    smaller. In one example nesting is used to align the text within the table.
    This file also contains a #id(#drivers_name) that is used to color the names
    in Dark Slate Gray and size 18px.
    when you run the style.scss file, style.css will contain the translated
    code that is implemented in every html file with the <link> function.
