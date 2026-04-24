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

### Phase 1: Problem Statement
### Project Title: Travel Itinerary Builder
### Problem Statement

Travel itinerary planning across diverse Indian destinations is a complex and time-consuming process. Travelers must coordinate live flight prices, local transport, accommodations, weather risks, and activities, all of which change frequently across 15+ fragmented platforms.

Traditional chatbots and simple travel assistants often provide only static and generic suggestions. They fail to consider:

Real-time flight availability and pricing
Hotel availability and seasonal demand
Local transport and ferry schedules
Weather conditions and travel risks
Budget constraints
Destination-specific logistics and activity planning

As a result, users spend hours manually checking multiple websites like MakeMyTrip, Goibibo, hotel booking platforms, weather apps, and travel blogs just to create one complete trip plan.

### User Problem

The user wants a dream vacation, but travel planning becomes a nightmare.

Example Scenarios
Andaman
Flight prices change from ₹9,000 to ₹18,000 overnight
Resorts may be expensive or unavailable during peak season
Scuba diving permits often require 48-hour advance booking
Spiti Valley
Roads remain closed from November to May
Homestays get fully booked during summer
Extreme weather conditions can reach -10°C
Delhi
Metro + Uber travel costs are unclear
Street food safety information is difficult to verify
Peak traffic timings affect daily planning

A typical traveler like Priya spends 10+ hours across 15 different websites.

What she really needs is:

“Give me a complete travel itinerary under ₹25,000 right now.”

Why Simple Chatbots Fail

Example:

### User Prompt:
“Give me an itinerary for Radhanagar Beach, Andaman”

Traditional Chatbot Response Problems
No live flight prices (Is IndiGo really ₹11,500?)
Wrong ferry timing (Is the 8 AM Port Blair → Havelock ferry available?)
No real hotel availability (Is Wild Orchid Resort available at ₹3,800?)
No weather awareness (Is there monsoon risk?)
No proper budget breakdown

This makes the itinerary incomplete and unreliable for real travel decisions.
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

### Needs:

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
