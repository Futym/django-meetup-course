# DjangoMeetup course application

## Disclaimer!
This project is heavily based on the "Python Django - The Practical Guide" course by Maximilian Schwarzmüller on Udemy. 
The purpose of this repository is for personal learning and reference. 
If you're interested in the original course materials and detailed explanations, I highly recommend checking out the course here:
https://www.udemy.com/course/python-django-the-practical-guide/?couponCode=KEEPLEARNING.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Futym/django-meetup-course.git
$ cd django-meetup-course
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m virtualenv --no-site-packages env
$ source env/bin/activate
```

Or

```sh
$ pyenv virtualenv <python_version>=3.12.7> <env_name>
$ pyenv activate <env_name>
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies create superuser for admin panel:

```shell
(env)$ ./manage.py createsuperuser
```

and follow the instructions in the shell. This is necessary to access the admin panel and manage db data.

Now the only thing to remain is to start the server:

```sh
(env)$ ./manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.

## Walkthrough

Before you will be able to view any meetings, go to admin page, log in using created earlier superuser,
and create some sample meetings. (It may be required to also create some locations.)
After that you are good to go back to the main page and see the list of created meetings.

<img width="1920" alt="image" src="https://github.com/user-attachments/assets/a300e90a-b1a0-4dc7-8668-34e1c87f8e0a" />


### Meetup details

In the main meetups view you can view details for each separate meetup by pressing the `More Details` button.

<img width="1905" alt="image" src="https://github.com/user-attachments/assets/45fbdb92-b650-4173-b29e-4e832824e858" />


### Meetup Registration

In order to register user to the chosen meetup all you need to do is put your email in the registration box and press `Register`.
After successfull registration you will be presented with registration confirmation screen from which you can get in contact
with organizer or go back to the main view of all meetups.

<img width="1920" alt="image" src="https://github.com/user-attachments/assets/8fdee79b-91cd-4322-b7d5-2f55fe2aa7da" />

## Tests

To run the tests, `cd` into the directory where `manage.py` is:

```sh
there are not tests yet
```
