# SchoolHub

This is a simple student planner that is used to keep track of your couses, grades and events.
check out the web application *[here](http://web-02.reinhardservices.tech/)*.

## installation

it's pretty straight forward to set up, the MVC architecture is what was used,
and flask is used to implement the controller for the web application,
So the models are kept in the models directory and the flask controller logic is kept
in the web_dynamic directory, and test are kept in the test directory.
python unittest and pytest was used for testing and can be ran using ```pytest```.
the flask app contains two blueprints, the api and the pages blueprint.
and the template and static files are located in the ```web_dynamic/pages/``` directory.
python dependencies are in the ```requirments.txt``` and can be installed using
```pip3 install -r requirments.txt``` and system level dependencies are in the ```apt.txt```
file.

## contributing

the web application is open for contributions.
always feel free to raise an issue if you find one or contribute to add changes.
