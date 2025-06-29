# EVA Sentinel – Problem Statement

## Scenario
Imagine a secure airbase that is experiencing frequent low-altitude drone incursions that are very disruptive. They delay flight schedules, disrupt runway operations, and cause emergency response protocols. These drones exploit blind spots that lie below usual radar coverage, such as in approach corridors. The base is equipped with perimeter infrared (IR) sensors, RF signal detectors, acoustic arrays, and short-range surveillance radars, but lacks cohesive integration for rapid response. Incursions have increased threefold over the past month, suggesting deliberate probing. The operational tempo is compromised, and security confidence is eroding. A multi-modal detection and deterrent system is urgently needed to restore safety, and airspace integrity!

## No-Fly Zone Coordinates
- NW corner: 37.415 N, 126.953 E
- NE corner: 37.415 N, 126.965 E
- SE corner: 37.405 N, 126.965 E
- SW corner: 37.405 N, 126.953 E

## Available Sensors
- Laptop replay of CSV telemetry (Week 1)
- ADS-B network feed (Week 3)
- Pi-mounted camera + radar (Hardware phase)

## Success Criteria
1. Detect low-altitude (<120 m) intrusions inside polygon.
2. Raise alert ≤1 s after packet arrival.
3. Log events for forensics.

