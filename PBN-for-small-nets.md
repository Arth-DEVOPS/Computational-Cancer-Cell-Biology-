We will explore two network motifs: toggle switch and toggle triad. 

## Toggle Switch

A = !B
B = !A

With toggle switch, the aim is to understand the time taken to reach a steady state. At every time step, you will make two choices:

1. Whether to make an update to the system or not. This choice will be made with a probability 'p'.
2. If you chose to update, which node to update (asynchronous update basically).

A simulation will be defined as a sequence of updates starting from the initial condition 11, till a steady state is reached. The number of updates that are needed to reach the steady state will be defined as the convergence time. You are to calculate the mean and standard deviation of convergence time by conducting multiple (100) simulations for a given value of p. 

Vary p between 0.1 to 1 with steps of 0.1 (0.1, 0.2 and so on). Plot the mean convergence time against p and represent the standard deviation as error bars.

## Toggle Triad

There are two forms of toggle triad that we will consider

### Form 1
A = !B & !C
B = !C & !A
C = !A & !B

### Form 2
A = !B | !C
B = !C | !A
C = !A | !B

Each form gives rise to different types of steady states. First, simulate both forms asynchronously and obtain the steady states and the corresponding frequencies. The frequency of a steady state is the number of times a simulation converges to that steady state. Simulation here should start from a random initial condition. Then, construct a PBN such that, Form 1 takes probability p and Form 2 takes probability 1-p. Simulate the PBN and obtain the steady state frequency distribution for different values of p. How does the frequency distribution change as p changes? Simulate each BN for 100 random initial conditions atleast and get the frequency distributions.
