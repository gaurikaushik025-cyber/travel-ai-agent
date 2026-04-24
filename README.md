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

## PROBLEM: Travel itinerary planning across diverse Indian destinations requires coordinating live flight prices, local transport, accommodations, weather risks, and activities - all changing hourly across 15+ fragmented sources. Simple chatbots deliver static, generic advice ignoring real-time availability, budget constraints, and location-specific logistics.
## AGENT SOLUTION: Universal 3-agent system (FlightAgent + LogisticsAgent + ActivityAgent) with Tavily live search + Gemini reasoning + MasterJudge quality scoring creates personalized, budget-accurate multi-day itineraries for ANY destination (beach/mountain/city) in 30 seconds.

## USER PROBLEM:
"User  wants dream vacation but planning = NIGHTMARE:
**ANDAMAN:**
 Flights ₹9k→₹18k overnight
 Resort ₹8k but empty off-season
 Scuba permits 48hrs advance
 SPITI VALLEY:
 Roads closed Nov-May
 Homestays book out June
 Extreme weather -10°C
 **DELHI:**
Metro + Uber costs unclear
Street food safety unknown
Peak traffic timings
Priya spends 10+ HOURS across 15 websites.
She needs: 'Give me  COMPLETE itinerary under ₹25k NOW'.
## WHY SIMPLE CHATBOT FAILS:
 **ChatGPT:** " Give me Itinerary Radhanagar Beach, Andaman"
 NO FLIGHT PRICES (₹11.5k IndiGo?)
 WRONG FERRY (8AM Port Blair→Havelock?)
 NO RESORT (Wild Orchid ₹3.8k available?)
 NO WEATHER (Monsoon risk?)
 NO BUDGET BREAKDOWN
WHY OUR MULTI-AGENT WINS :
4 Specialized Agents + Master Judge = PRODUCTION-GRADE:
 User: "Andaman Feb15-20 ₹25k"
Agent:
1️. FlightAgent (Tavily Live):
"IndiGo Mumbai-Port Blair: ₹11,500 | Feb15 6AM → Feb20 8PM"
2️. LogisticsAgent (3 Tavily Searches):
"Weather: Sunny 28°C | Wild Orchid Resort: ₹3,800/night | Ferry: 8AM Port Blair→Havelock"
3️. ActivityAgent (Tavily Live):
"Day3: Radhanagar Beach (₹0) | Day4: Scuba Dive (₹6,500)"
4️.  MasterJudge:
" Flights ✓ |  Ferry ✓ |  Resort ✓ |  Activities ✓ |  Weather-safe ✓" TOTAL: ₹24,300 | QUALITY: 9.5/10 
AGENTIC ADVANTAGE:
• LIVE DATA (Tavily updates every run)
• SPECIALIZATION (3 expert agents)
• QUALITY GATE (Judge rejects bad output)
• UNIVERSAL (Andaman → Spiti → Delhi)

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
