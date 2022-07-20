# Computational-Cancer-Cell-Biology
Ranked asynchronous simulation of RTK signalling. Need to process nodes one at a time to generate a smoother curve.

TT + 1 SA: A = !B & !C & A, B = !A & !C, C = !A & !B  //  A = !B | !C | A, B = !A | !C, C = !A | !B
TT + 2 SA: A = !B & !C & A, B = !A & !C &B, C = !A & !B  //  A = !B | !C | A, B = !A | !C | B, C = !A | !B
TT + 3 SA: A = !B & !C & A, B = !A & !C &B, C = !A & !B & C  //  A = !B | !C | A, B = !A | !C | B, C = !A | !B | C
