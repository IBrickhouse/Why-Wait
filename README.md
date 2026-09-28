# Why Wait? Analyzing Theme Park Wait Times at Universal Studios Singapore

An ongoing data analytics project investigating which factors drive attraction wait times at Universal Studios Singapore (USS).

## Overview

Theme parks are complex operations, and much of what shapes a guest's day, especially how long they queue, is invisible from the outside. As a master's student in analytics at Nanyang Technological University (NTU), I am collecting my own data to study these dynamics, starting with USS, my local park.

## Research Questions

1. **What factors are associated with longer wait times?**
2. **By how much does each factor change the wait time?**

The second question is only addressed once the first has been answered.

## Data Collection

### Core attributes

Recorded for each attraction or show at each observation:

| Attribute | Description |
|---|---|
| Attraction / Show Name | Which attraction or show the observation is for |
| Date | Date of the observation |
| Time | Time of the observation |
| Wait Time | Posted wait time |
| Attraction Status | Whether the attraction is operating |

### Candidate factors

Factors hypothesized to influence wait times. These have not yet been investigated:

| Factor | Rationale |
|---|---|
| Weather conditions | Weather may change guest movement and attraction availability |
| Total park attendance | Higher daily attendance may lead to longer queues |
| Recent media tied to the attraction or show | New releases may increase interest in related attractions |
| Historical popularity of the property | Long-standing, well-known properties may attract consistently larger crowds |

## Data Source

Powered by [ThemeParks.wiki](https://www.themeparks.wiki/).

Attraction and wait-time data is retrieved from the ThemeParks.wiki API. Wait times originate from the park's own systems and are estimates.

## Approach

1. **Collect:** a Python script queries the ThemeParks.wiki API every 5 minutes for attractions and their wait times. Timestamps are stored in Singapore time (SGT), the park's local time.
2. **Explore:** a Jupyter notebook holds the initial analysis of the collected data.

**Tools:** Python, ThemeParks.wiki API, Jupyter Notebook

## Repository Structure

```
Why-Wait/
├── collector/    # Python script that collects attraction and wait-time data
├── analysis/     # Jupyter notebook with initial analysis
├── data/         # Collected CSV files (not tracked in git; generated locally)
├── .gitignore
└── README.md
```

Collected data files are excluded from version control via `.gitignore`.

## Status

Data collection is in progress and the analysis is at an early, exploratory stage.

## Disclaimer

This is an independent academic project. It is not affiliated with, endorsed by, or sponsored by Universal Studios Singapore, Resorts World Sentosa, or ThemeParks.wiki. Park and attraction names are used for identification only.

## Author

**Isaiah Peter Brickhouse**, MSc Analytics candidate, Nanyang Technological University
