# ID BLOCK

- Eric Zair
- Gradient Descent (Singular)
- 02/03/2020

## Project Description

The goal of this project was to implement 3 different ways to do linear regression on a database that contains used car information. After collecting all of the data using turicreate, the goal was simple, given only the mileage of the car how can we estimate the expected cost for the car?

Note this program is built specifically for single feature gradient descent not multiple.

## The three different methods

1. Built in linear regression model in turicreate

2. Calculating the closed for for our gradient equations

3. Hand implementing gradient decent

## Using the built in linear regression model

Using the built in features was rather easy and yields a better answer than my implementation of gradient descent. Granted this hold true because...my implementation of gradient descent will generate `nan`s and loop for quite the long time due to not finding the correct step size. As it turns out if your step size and magnitude used are not sufficient, then your descent gradient never actually converges, which becomes quite the issue.

## Closed form

Closed form appears to be the way that linear regression should really be done (at least for a small amount of features). The closed form method provides you with a straightforward mathematical way of accomplish your linear regression. Since you do not have to worry about things like step size and all we are really doing are a few simple linear calculations (and later with more features matrix multiplications), we get straight to the point. The speed of doing this is arguably faster than that of gradient descent. We do not loop and loop until we find the estimated or close to perfect solution, but rather we know for a fact that the solution is 100% optimal, since it was mathematically calculated.

## My gradient descent

As it turns out, my implementation of gradient descent is truly flawed. When run, it may appear to be working, but then shortly after you will run into things such as an `inf` values, which clearly is a problem. I believe that the result of this has to do with having to find the proper step size or magnitude, but I could be wrong as well. Assuming that this implementation...worked properly, we should be receiving a number that is near similar to that of what is produced in the turicreate linear regression model.

## Setup

If you want to make sure that you have the proper python packages to run any of the implantation (that are stored in the `src/` folder) run the `dev_setup.py` script.

## Running each implementation

Each implementation is stored in it's own `.ipynb` file. Simply use something like anaconda, conda, jupyter notebook, or google collab in order to run the programs.

`closed_form.ipynb` contains the closed form implementation.

`my_gradient_implementation.ipynb` contains my implementation.

`turicreate_linear_regression_using.ipynb` contains the linear regression model implementation.
