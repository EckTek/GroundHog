# GroundHog

### Pre-requisites :
- python3
- pip3
- make

### Commands to run this project:
1. make
2. ./groundhog [INT]

The program, given a number of days (called period) as argument:
1. wait for the next value to be written on the standard input,
2. output, once enough data has been gathered, some technical indicators:
- a. the temperature increase average, g, observed on the last period (decrease in temperature are
not taken into account),
- b. the relative temperature evolution, r, between the last given temperature and the temperature
observed n-days ago,
- c. the standard deviation, s, of the temperatures observed during the last period,
- d. when appropriate, an alert as soon as it detects a switch in global tendency,
3. return to the first step, until the STOP keyword is read.
