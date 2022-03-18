# EMAT10006COURSE (Daniel Joinson, Kate E, Tim A. , Adetutu S. )
This repository contains a simulation titled , 'THE PROGRESSIVE ACCEPTANCE OF VACCINATIONS DURING THE COVID-19 CRISES IN THE UK'.
The codes for the simulation have been tested using PyCharm and the video was downloaded. Ensure you have the required encoder to view and download the created simulation.
The ffmpeg encoder is one of the most popular. Else, please run the code on PyCharm so as to get the exact same results that we did.

**FIRST PART**
//
**SIMULATION: THE PROGRESSIVE ACCEPTANCE OF VACCINATIONS DURING THE COVID-19 CRISES IN BRISTOL:**
1. A class containing several reusable functions was created
2. Population was set to 10,000 and it could be extrapolated to fit a larger population (The population density in the raw dataset was extremely heavy and led to RunTime errors and poor indexing, hence the choice for an arbitrary figure)
3. Parameters representing infected persons, as well as the first, second and third dose of the vaccine were set
4. The first_wave() function is responsible for depicting how the infections spread through iterations, after it had been initialized to zero. It initializes our plot with the set population of 10,000. 
The **GOLDEN SPIRAL METHOD** discussed on stackoverflow: https://stackoverflow.com/questions/9600801/evenly-distributing-n-points-on-a-sphere was the principle behind the sections witnessed in the polar plot. 
It generates a 2D-spiral algorithm.
6. The Vaccine_share() function would calculate the number of newly infected people while vaccinations are out, a serial interval of 7days was used, however, this value can be changed/adjusted. 
7. The Doses() function calculates the doses given during each wave of the infection.
8. The updates() function would update the color of plot points when infections occur, whether or not they have been vaccinated
9. The update_annotation() function would make changes to the annotations created at the beginning on the polar plot, so that each data would change and reflect on the plot. Formatted strings were used to make changes.
10.The animate() function would show the plot while the program is running.
11.The generator function acts as short cut to build iterations as frames for the plot. It is totally dependent on the number of vaccinated persons being less than infectious persons.
12.The class was assigned to a variabe covid, after the COVID_19 parameter had been passed, the animate function was called. And the simulation appeared


**SECOND PART**


**RESPONSIBILITIES**


















