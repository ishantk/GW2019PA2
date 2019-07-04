"""

    Linear Regression:
    To predict the output for an unseen input

    ML Model
    1. We need data for Presentation
    2. We need evaluation
    3. We need to optimize model

    Supervised Learning

    Given DataSet
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 5]

    If X is 1, Y is 2
    If X = 2.75, Y = ?

    Find Mean of X and Mean of Y

    mean of x : MX -> 3
    mean of y : MY -> 4

    Step 1:
    ------------------------------------------------
    X   Y   X-MX    Y-MY    Sq(X-MX)    (X-MX)(Y-MY)
    ------------------------------------------------
    1   2   -2      -2      4           4
    2   4   -1       0      1           0
    3   5    0       1      0           0
    4   4    1       0      1           0
    5   5    2       1      4           2
    -------------------------------------------------

    Step 2:
    -------
    Sum of Sq(X-MX)     :   10
    Sum of (X-MX)(Y-MY) :   6

    Y = b0 + b1X | y = mx + c
    b0: interceptor
    b1: slope

    We must find slope of Line
    b1 = [Sum of (X-MX)(Y-MY)] / [Sum of Sq(X-MX)]
    b1 = 6/10
    b1 = 0.6

    Eqn of Line : Y = b0 + (0.6)X

    Substitute mean of x and mean of y to calculate value of b0

    4 = b0 + (0.6)*3
    b0 = 2.2

    =================
    EQUATION OF LINE
    =================
    Y = 2.2 + (0.6)X
    =================

    For any value of x now we can know value of y

    BUT, we don't know if equation will be able to predict perfectly :P

    Step 3:
    -------

    Calculate Errors so that we can know equation of line will work or not !!


    =================
    EQUATION OF LINE
    =================
    Y = 2.2 + (0.6)X
    =================

    Y' is predicted output on the basis of original input

    mean of x : MX -> 3
    mean of y : MY -> 4

    ------------------------------------------------
    X   Y   Y'     (Y-MY) Sq(Y-MY) (Y'-MY) Sq(Y'-MY)
    ------------------------------------------------
    1   2   2.8     -2    4         -1.2    1.44
    2   4   3.4      0    0         -0.6    0.36
    3   5   4        1    1            0       0
    4   4   4.6      0    0          0.6    0.36
    5   5   5.2      1    1          1.2    1.44
    -------------------------------------------------

    Error : [Sum of Sq(Y'-MY)] / [Sum of Sq(Y-MY)]
    Error : 3.6 / 6
    Error : 0.6

    If Error is 0 it means regression line is perfect :)
    Our Error is 0.6 which is close to 0

    In case error will keep on increasing we thereafter will optimize our model


"""

import numpy as np

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

MX = np.mean(X)
MY = np.mean(Y)

print(MX)
print(MY)