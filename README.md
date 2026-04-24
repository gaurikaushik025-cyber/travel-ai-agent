# AI Agent Project Report

## Topic: Universal AI Travel Planner (Travel Itinerary Builder)

### Group Members

**Role A – Architect & Integrator:**
**Soohani Gholse**
Roll No.: 55

**Role B – Builder & Deployer:**
**Gauri Kaushik**
Roll No.: 30

**Semester:** IV – B.Tech ECE-A
**Department:** Electronics and Communication Engineering
**Date:** 22/04/2026

**GitHub Repository:** **https://github.com/gaurikaushik025-cyber/travel-ai-agent**
**Live Demo:** **https://travel-ai-agent-bvxdntmzw8qrdcjhpyiqmf.streamlit.app/**


  Local URL: http://localhost:8501
  Network URL: http://10.112.219.65:8501
---

# PHASE 1: Problem Statement

## Problem

Travel itinerary planning across diverse Indian destinations requires users to coordinate multiple dynamic factors such as:

* Live flight prices
* Hotel availability
* Local transport
* Weather conditions
* Activity planning
* Budget management

These factors change frequently and are spread across 15+ fragmented platforms.

Traditional chatbots provide only static and generic suggestions without considering:

* Real-time availability
* Budget constraints
* Destination-specific logistics
* Practical feasibility

This makes trip planning slow, stressful, and often inaccurate.

---

## Agentic Solution

We developed a **Universal Multi-Agent AI Travel Planner** that creates complete travel itineraries for any destination within 30 seconds.

The system uses:

* **Flight Agent**
* **Logistics Agent**
* **Activity Agent**
* **Master Judge (LLM-as-Judge)**

along with:

* **Tavily Search API** for live internet data
* **Gemini API** for reasoning and decision-making
* **Streamlit** for interactive UI

The system generates:

* Day-wise itinerary
* Budget breakdown
* Live flight options
* Hotel recommendations
* Activities
* Quality score evaluation

---

# User Problem

## Why Trip Planning Feels Like a Nightmare

### Example: Andaman Trip

Problems faced:

* Flights change from ₹9,000 → ₹18,000 overnight
* Resorts show availability but are actually full
* Ferry timings are unclear
* Scuba permits require advance booking
* Weather risks affect travel plans

Users spend **10+ hours** checking:

* MakeMyTrip
* Goibibo
* Google
* Instagram
* Travel blogs
* Weather apps

for one single trip.

What they actually need is:

> “Give me a complete itinerary under ₹25,000 right now.”

---

# Why Simple Chatbots Fail

Example prompt:

> “Give me itinerary for Radhanagar Beach, Andaman”

Traditional chatbot problems:

* No live flight prices
* No ferry confirmation
* No hotel availability check
* No weather awareness
* No actual budget calculation

Result = beautiful but impractical output.

---

# Why Our Multi-Agent System Wins

## Example Input

> Mumbai → Andaman
> Feb 15 – Feb 20
> Budget: ₹25,000

---

## Multi-Agent Execution

### 1. Flight Agent

Uses Tavily live search:

* Finds cheapest direct flights
* Compares timings and prices

Example:

> IndiGo Mumbai → Port Blair
> ₹11,500 | Feb 15 – Feb 20

---

### 2. Logistics Agent

Performs 3 live searches:

* Weather forecast
* Hotels
* Local transport

Example:

> Sunny weather
> Wild Orchid Resort – ₹3,800/night
> Ferry available at 8:00 AM

---

### 3. Activity Agent

Finds top destination activities:

Example:

* Radhanagar Beach – Free
* Scuba Diving – ₹6,500

---

### 4. Master Judge (LLM-as-Judge)

Evaluates:

* Budget fit
* Completeness
* Feasibility
* Travel practicality

Final Output:

> Total Cost: ₹24,300
> Quality Score: 9.5/10

---

# Agentic Advantages

* Live real-time data
* Specialized independent agents
* LLM quality validation
* Works for any destination
* End-to-end complete planning

---

# User Persona

## Primary User: Priya Sharma

* Mumbai
* Age: 28
* Marketing Manager
* Budget: ₹25,000
* Vacation Duration: 5 Days

### Goals

* Beach trip (Andaman)
* Trek trip (Spiti Valley)
* City trip (Delhi)

Needs:

* Flights + Stay + Activities under budget
* Minimum planning effort
* Reliable complete itinerary

---

## Current Pain Points

* Too many apps and websites
* Prices keep changing
* No single source for complete planning
* Time-consuming manual comparisons

---

## Our Solution

### Input

> “Andaman | Feb 15–20 | ₹25,000”

### Output

> IndiGo ₹11.5k + Resort ₹3.8k/night + Scuba ₹6.5k
> Final Budget: ₹24.3k
> Quality Score: 9.5/10

---

# PHASE 2: Task Decomposition

| Step | Agent           | Input                              | Tavily Search Used           | Output          | Logic                      |
| ---- | --------------- | ---------------------------------- | ---------------------------- | --------------- | -------------------------- |
| 1    | Flight Agent    | Origin, Destination, Dates, Budget | Cheapest flights             | Flight JSON     | Cheapest + Direct          |
| 2    | Logistics Agent | Destination, Dates                 | Weather + Hotels + Transport | Logistics JSON  | Budget-safe + Weather-safe |
| 3    | Activity Agent  | Destination, Budget                | Top activities               | Activities JSON | Affordable + Popular       |
| 4    | Master Judge    | All agent outputs                  | No direct search             | Final itinerary | Quality Score > 8/10       |

---

# PHASE 3: Architecture Diagram

The system follows a multi-agent architecture:

### Flow

User Input
→ Gemini LLM Orchestrator
→ Flight Agent + Logistics Agent + Activity Agent
→ Tavily Live Search
→ Result Combiner
→ Master Judge (LLM-as-Judge)
→ Final Itinerary + Quality Score
→ Streamlit UI Output

*(Insert architecture diagram image here)*

---

# PHASE 4: Implementation

## Technology Stack

### Backend

* Python

### LLM Provider

* Gemini API

### Search Tool

* Tavily Search API

### Frontend

* Streamlit

### Visualization

* Plotly

### Deployment

* Streamlit Community Cloud

---

# Key Features Implemented

## API Connection

Connected Gemini API for:

* reasoning
* itinerary generation
* evaluation

---

## Tool Integration

Integrated Tavily Search for:

* live flights
* hotels
* transport
* activities
* weather

---

## LLM-as-Judge

Master Judge evaluates:

* budget optimization
* completeness
* practicality
* final quality score

---

## Working End-to-End Agent

The system:

* accepts user input
* performs live searches
* reasons using LLM
* generates final optimized travel plan

---

# UI (Streamlit)

## Features

* Origin and destination input
* Date selection
* Budget input
* Generate itinerary button
* Quality score dashboard
* Budget breakdown graph
* Flight options
* Hotels
* Activities
* Day-wise itinerary tabs

---

# Example Outputs

## Example 1: Mumbai → Andaman

* Quality Score: 8.5/10
* Total Cost: ₹24,000
* Budget Left: ₹1,000

Includes:

* flights
* hotels
* activities
* recommendations

---

## Example 2: Mumbai → Delhi

* Dynamic destination support
* Customizable for any location
* Flexible budget planning

---

# PHASE 5: Deployment

The application is deployed publicly using:

## Streamlit Community Cloud

This provides:

* live public URL
* easy access for evaluation
* real-time demonstration capability

Live Demo Link:

https://travel-ai-agent-bvxdntmzw8qrdcjhpyiqmf.streamlit.app/

---

# PHASE 6: Loom Video

A 5-minute Loom walkthrough includes:
https://travel-ai-agent-bvxdntmzw8qrdcjhpyiqmf.streamlit.app/
* problem statement
* architecture explanation
* code implementation
* live demo
* technical decisions

---

# Conclusion

This project demonstrates a complete production-style AI Agent system using:

* Multi-Agent Architecture
* Real-Time Tool Integration
* LLM-as-Judge
* End-to-End Deployment

It solves a real-world problem with practical usability and strong scalability potential.

The system can be extended further using:

* real booking APIs
* payment gateways
* automatic PDF itinerary generation
* full production deployment
