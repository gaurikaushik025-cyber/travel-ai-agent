import streamlit as st
import json
import pandas as pd
from agents import generate_complete_itinerary
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AI Travel Planner", layout="wide")

# Custom CSS
st.markdown("""
<style>
.main {padding: 2rem;}
h1 {color: #1f77b4; text-align: center;}
.metric-card {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
              padding: 1rem; border-radius: 10px; color: white;}
</style>
""", unsafe_allow_html=True)

st.title("✈️ Universal AI Travel Planner")
st.markdown("**Get complete itineraries in 30 seconds** - Live flights, hotels, activities!")

# Sidebar
st.sidebar.header("⚙️ Settings")
origin = st.sidebar.text_input("🛫 From", value="Mumbai")
destination = st.sidebar.text_input("🏖️ To", value="Andaman")
dates = st.sidebar.text_input("📅 Dates", value="Feb 15-20 2026")
budget = st.sidebar.number_input("💰 Budget (₹)", value=25000, min_value=10000)

col1, col2 = st.columns([1, 3])

with col1:
    if st.button("🚀 Generate Itinerary", type="primary", use_container_width=True):
        with st.spinner("Planning your dream vacation..."):
            result = generate_complete_itinerary(origin, destination, dates, budget)
            st.session_state.result = result
            st.session_state.budget = budget
            st.rerun()

if 'result' in st.session_state:
    result = st.session_state.result
    
    # Quality Score Card
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Quality Score</h3>
            <h2>{result['final_plan'].get('quality_score', 0):.1f}/10</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col_b:
        total_cost = result['final_plan'].get('budget_breakdown', {}).get('total_cost', 0)
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Cost</h3>
            <h2>₹{total_cost:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col_c:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Budget Left</h3>
            <h2>₹{st.session_state.budget - total_cost:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # Tabs for detailed view
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Itinerary", "💸 Budget", "🛫 Flights", "🏨 Logistics & Activities"])
    
    with tab1:
        st.subheader("📅 Complete Itinerary")
        itinerary = result['final_plan'].get('itinerary', {})
        for day, plan in itinerary.items():
            st.markdown(f"**{day.upper()}**: {plan}")
        
        recommendations = result['final_plan'].get('recommendations', [])
        if recommendations:
            st.subheader("💡 Recommendations")
            for rec in recommendations:
                st.success(rec)
    
    with tab2:
        breakdown = result['final_plan'].get('budget_breakdown', {})
        df = pd.DataFrame(list(breakdown.items()), columns=['Category', 'Amount'])
        fig = px.pie(df, values='Amount', names='Category', 
                    title="Budget Breakdown")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("✈️ Live Flight Options")
        flights = result['flight']['flights']
        for flight in flights:
            st.markdown(f"**{flight['airline']}** - {flight['price']}")
            st.markdown(f"[Book Now]({flight['url']})")
    
    with tab4:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🏨 Hotels")
            hotels = result['logistics']['hotels']
            for hotel in hotels[:3]:
                st.write(f"• {hotel.get('title', 'N/A')}")
        
        with col2:
            st.subheader("🎯 Top Activities")
            activities = result['activities']['activities']
            for activity in activities:
                st.write(f"• {activity['name']} - {activity['cost']}")

# Footer
st.markdown("---")
st.markdown("*Built with ❤️ using Tavily + Gemini + Streamlit*")