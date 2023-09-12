# Computational-Cancer-Cell-Biology
Refer to the document "IISC Summer Report.pdf" in the repository for a brief overview on the results that have been collected for various gene networks.

The conclusions/results for the EMT circuits were:
1. Independence from the initial states: The final states of the circuits seemed to be independent of their initial conditions for the cases that I studied.
2. Continuity and Discreteness with Increase in Delay: The mean expression level graphs tend to become more consistent and continuous as the time interval between the updation of noises increases but tend to become more discretised when the intervals between perturbation probability are increased in the circuits. As perturbation probability increases, we had expected the mean expression level to vary a lot, yet the system remained stable for AND cases. 
3. Stability in the system: Despite the addition of noise and perturbation components, the circuits which feature AND showed extremely stable behaviour, which was not initially expected since the states are supposed to switch. Consider a case where you are at 011. You flip one node and get to 010. Since it is AND formalism, you stay at 010 in the next step, particularly since it is the AND formalism; the dominant states should have been one of the mono-positive ones. States not switching was a surprising result. 
