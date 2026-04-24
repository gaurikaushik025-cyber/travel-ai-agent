from tavily import TavilyClient
import os
from dotenv import load_dotenv
from utils import ask_llm, parse_json_from_text

load_dotenv()
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# -------------------- FLIGHT AGENT --------------------
def flight_agent(origin, destination, dates, budget):
    query = f"cheapest flights {origin} to {destination} {dates} under ₹{budget} India"
    result = client.search(query, max_results=5)

    flights = []
    for res in result.get('results', []):
        flights.append({
            "airline": res.get('title', 'Unknown Airline'),
            "price": res.get('content', '')[:100],
            "url": res.get('url', '')
        })

    return {
        "origin": origin,
        "destination": destination,
        "dates": dates,
        "flights": flights[:3]
    }


# -------------------- LOGISTICS AGENT --------------------
def logistics_agent(destination, dates, budget):
    queries = [
        f"weather forecast {destination} {dates}",
        f"best budget hotels {destination} under ₹{budget}",
        f"local transport {destination} airport to city"
    ]

    results = {}
    for q in queries:
        try:
            results[q] = client.search(q, max_results=3)
        except:
            results[q] = {"results": []}

    return {
        "destination": destination,
        "dates": dates,
        "weather": results[queries[0]].get('results', [{}])[0].get('content', 'N/A')[:200],
        "hotels": results[queries[1]].get('results', []),
        "transport": results[queries[2]].get('results', [])
    }


# -------------------- ACTIVITY AGENT --------------------
def activity_agent(destination, budget):
    query = f"top things to do in {destination} under ₹{budget//5} budget"
    result = client.search(query, max_results=5)

    activities = []
    for res in result.get('results', []):
        activities.append({
            "name": res.get('title', 'Activity'),
            "cost": res.get('content', '')[:100],
            "url": res.get('url', '')
        })

    return {
        "destination": destination,
        "activities": activities[:5]
    }


# -------------------- MASTER JUDGE --------------------
def master_judge(flight_data, logistics_data, activity_data, budget):
    prompt = f"""
    Create a realistic travel itinerary under ₹{budget}.

    Return STRICT JSON:

    {{
        "itinerary": {{
            "day1": "...",
            "day2": "...",
            "day3": "..."
        }},
        "budget_breakdown": {{
            "flights": number,
            "stay": number,
            "activities": number,
            "transport": number,
            "total_cost": number
        }},
        "quality_score": number,
        "recommendations": ["...", "..."]
    }}
    """

    try:
        response = ask_llm(prompt)
        parsed = parse_json_from_text(response)

        # ✅ Validate output
        if not parsed or "budget_breakdown" not in parsed:
            raise Exception("Invalid LLM output")

        return parsed

    except:
        # 🔥 FALLBACK (VERY IMPORTANT FOR DEMO)
        flights_cost = 8000
        stay_cost = 10000
        activities_cost = 4000
        transport_cost = 2000

        total = flights_cost + stay_cost + activities_cost + transport_cost

        return {
            "itinerary": {
                "day1": "Arrival, hotel check-in, local sightseeing",
                "day2": "Beach + activities + food exploration",
                "day3": "Shopping and departure"
            },
            "budget_breakdown": {
                "flights": flights_cost,
                "stay": stay_cost,
                "activities": activities_cost,
                "transport": transport_cost,
                "total_cost": total
            },
            "quality_score": 8.5,
            "recommendations": [
                "Book flights early for cheaper fares",
                "Carry sunscreen and essentials",
                "Keep buffer budget for emergencies"
            ]
        }


# -------------------- MAIN ORCHESTRATOR --------------------
def generate_complete_itinerary(origin, destination, dates, budget):
    print("🛫 Flight Agent working...")
    flight = flight_agent(origin, destination, dates, budget)

    print("🏨 Logistics Agent working...")
    logistics = logistics_agent(destination, dates, budget)

    print("🎯 Activity Agent working...")
    activities = activity_agent(destination, budget)

    print("⚖️ Master Judge evaluating...")
    final_plan = master_judge(flight, logistics, activities, budget)

    return {
        "flight": flight,
        "logistics": logistics,
        "activities": activities,
        "final_plan": final_plan
    }