We will explore two network motifs: toggle switch and toggle triad. 

## Toggle Switch

>A = !B
; B = !A

With toggle switch, the aim is to understand the time taken to reach a steady state. At every time step, you will make two choices:

1. Whether to make an update to the system or not. This choice will be made with a probability 'p'.
2. If you chose to update, which node to update (asynchronous update basically).

A simulation will be defined as a sequence of updates starting from the initial condition 11, till a steady state is reached. The number of updates that are needed to reach the steady state will be defined as the convergence time. You are to calculate the mean and standard deviation of convergence time by conducting multiple (100) simulations for a given value of p. 

Vary p between 0.1 to 1 with steps of 0.1 (0.1, 0.2 and so on). Plot the mean convergence time against p and represent the standard deviation as error bars.

## Toggle Triad

There are two forms of toggle triad that we will consider

### Form 1
>A = !B & !C
; B = !C & !A
; C = !A & !B

### Form 2
>A = !B | !C
; B = !C | !A
; C = !A | !B

Each form gives rise to different types of steady states. First, simulate both forms asynchronously and obtain the steady states and the corresponding frequencies. The frequency of a steady state is the number of times a simulation converges to that steady state. Simulation here should start from a random initial condition. Then, construct a PBN such that, Form 1 takes probability p and Form 2 takes probability 1-p. Simulate the PBN and obtain the steady state frequency distribution for different values of p. How does the frequency distribution change as p changes? Simulate each BN for 100 random initial conditions atleast and get the frequency distributions.

## Trajectories for toggle switch with perturbation probability

We now define a new probability called the perturbation probability. At every time point, we make a choice of whether or not to perturb a node. If yes, we flip the level of a chosen node. Use the perturbation probability in conjunction with update probability and simulate the toggle switch for 1000 time steps. Repeat for 100 times to get a mean expression level trajectory of node A of the toggle switch (similar to the figure you reproduced from Reka's paper). For update probability of 0.1, calculate the trajectories for perturbation probability of 0.1, 0.3, 0.5, 0.7 and 0.9 and plot them together. Repeat for update probability of 0.9.

## Analysis for toggle triad and asymmetric 3-node network

Perform the update probability and perturbation probability analysis for toggle triad and the networks below:

### Netowrk 1

>A = !B & !C
; B = C & !A
; C = !A & B

### Network 2

>A = !B & !C
; B = C & !A
; C = !A

### Network 3

>A = !B & !C
; B = !C & !A
; C = !A

### Network 4

>A = !B & A
; B = !A

### Network 5

>A = !B & A
; B = !A & B


