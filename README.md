# Why Wait? Analyzing Theme Park Wait Times at Universal Studios Singapore

An ongoing data analytics project investigating which factors are associated with attraction wait times at Universal Studios Singapore (USS).

## Overview

Theme parks are complex operations, and much of what shapes a guest's day, especially how long they queue, is invisible from the outside. As a master's student in analytics at Nanyang Technological University (NTU), I am collecting my own data to study these dynamics, starting with USS.

## Research Questions

1. **What factors are associated with longer wait times?**
2. **How large is the association between each factor and wait time?**

The second question will be investigated after identifying relevant factors in the exploratory analysis. Associations will not necessarily imply causation.

## Data Collection

### Core attributes

The collector records attraction-level observations in daily CSV files under `data/production/`.

| Column | Description |
|---|---|
| `timestamp` | Date and time of the observation, in Singapore time |
| `attraction` | Attraction name |
| `wait_time` | Posted standby wait time in minutes (empty if no standby wait is reported) |
| `status` | Operating status of the attraction |

Each observation represents a snapshot of an attraction's reported conditions at the time of collection.

### Candidate factors

Factors hypothesized to be associated with wait times. These have not yet been investigated and may require additional data sources.

| Factor | Rationale |
|---|---|
| Weather conditions | Weather may affect guest movement and attraction availability |
| Total park attendance | Higher daily attendance may lead to longer queues |
| Recent media tied to the attraction or show | New releases may increase interest in related attractions |
| Historical popularity of the property | Long-standing, well-known properties may attract consistently larger crowds |

## Data Source

Powered by [ThemeParks.wiki](https://www.themeparks.wiki/).

Attraction and wait-time data is retrieved from the ThemeParks.wiki API. Wait times are estimates originating from the park's own systems.

## Approach

1. **Collect:** A Python script queries the ThemeParks.wiki API every 5 minutes for attraction information and wait times. Collection is skipped when no attractions are reported as operating. Timestamps use Singapore time (SGT).
2. **Explore:** A Jupyter notebook is used for initial exploratory analysis and data-quality checks.
3. **Analyze:** Relevant candidate factors will be investigated and, where suitable, modeled against reported wait times.

**Tools:** Python, ThemeParks.wiki API, CSV, Jupyter Notebook

## Repository Structure

```text
Why-Wait/
├── collector/        # Python script for live data collection
├── analysis/         # Jupyter notebook for exploratory analysis
├── data/             # Collected CSV files (not tracked in Git)
│   ├── production/   # Output from live data collection
│   └── test/         # Output from test runs
├── .gitignore
└── README.md
```

Production and test data are excluded from version control via `.gitignore`. The collector creates `data/production/` automatically when it runs. Production files are organized by collection date.

## Status

Data collection is in progress. Initial exploratory analysis and data-quality assessment are at an early stage.

## Disclaimer

This is an independent academic project. It is not affiliated with, endorsed by, or sponsored by Universal Studios Singapore, Resorts World Sentosa, or ThemeParks.wiki. Park and attraction names are used for identification only.

## Author

**Isaiah Peter Brickhouse**, MSc Analytics candidate, Nanyang Technological University