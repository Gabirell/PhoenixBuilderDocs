# Phoenix Engine + How Not To Die
# Consolidated Project Context, Ideas, Instructions and Current State

## 1. CORE VISION
There are two distinct products:
1. Phoenix Engine - Reusable, game-agnostic simulation technology.
2. How Not To Die - First actual game powered by Phoenix.

Core philosophy:
> Phoenix is the technology that powers the games. The game is the product.

## 2. DEVELOPMENT DISCIPLINE
> STOP ARCHITECTING. START IMPLEMENTING.
The current development loop is:
IMPLEMENT → RUN → OBSERVE → MEASURE → IDENTIFY ONE REAL PROBLEM → FIX → RUN AGAIN

## 3. CURRENT MOST IMPORTANT RULE
The game already has enough foundation to begin iterative development (citizens, movement, hunger, thirst, day/night, death, scarcity).
The immediate work is: SPRINT 5 — OBSERVATION & BALANCING.

Goal: Measure what is already happening. No new mechanics. No Phoenix redesign. No new architecture.

## 4. SPRINT 5 REQUIRED METRICS
At simulation end or after 5 minutes:
- Population Start / End
- Deaths by Hunger / Thirst
- Average Lifetime
- Food / Water Consumed
- Average Hunger / Thirst at Death

Timeline events:
- 00:00 Simulation Started
- First Citizen Hungry
- First Death
- Resource Exhausted
- Population below 50%

Resource Heat Map:
- Track how often each source is used to determine distribution efficiency.
- Survivor Analysis (longest survivors, meals/drinks taken).

Collapse Cause:
At the end determine from actual data if the collapse was due to food shortage, water shortage, poor distribution, poor behavior, or other.
