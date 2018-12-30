# Follow Unfollow

This is a simple driver script that uses the [InstaPy](https://github.com/timgrossmann/InstaPy) library to follow and unfollow users. It's based on one of the template scripts from the project. I've modified the script to include a config file so that I can easily spin up multiple instances for multiple accounts.

## Pre-requisites

I'm using pipenv and pyenv to manage my Python environments. You should have those installed first.
You also need Chrome Driver. I use homebrew to install it.

## Installation

Clone the repo and then run:

`pipenv install`

## Configuration

Copy the config.yml.example to config.yml and edit it accordingly

## Running 

`pipenv run python follow_unfollow.py`
