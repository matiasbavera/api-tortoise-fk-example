# FastApi-Tortoise-fk-example

I'm creating this because I had issues with FKs from the way I have structured my project in the past. With this proposed structure, initializing the models first before they are created, should solve the problem. I hope it helps someone who has the same problem.

To simplify this example it is contemplated that we want to save a house phone. So several people can have the same phone. But a person cannot have more than one.


## Pre-requisites

* python 3.8
* [pipenv](https://pypi.org/project/pipenv/)

## Install

``` bash
pipenv install --dev
```

## Run

``` bash
pipenv run dev
```

On your browser go to http://127.0.0.1:8000.



## Test that the FK are returning

Go to http://127.0.0.1:8000/docs

1. Create a phone record.
2. Create a user with the `phone_id: 1`

E.g: 

``` json
{
  "username": "John",
  "name": "John",
  "family_name": "John",
  "category": "misc",
  "phone_id": 1
}
{
  "username": "John2",
  "name": "John2",
  "family_name": "John2",
  "category": "misc",
  "phone_id": 1
}
```

On your browser `http://127.0.0.1:8000/users/user/John` you should see the user record + the phone information.