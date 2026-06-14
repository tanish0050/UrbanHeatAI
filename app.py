import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import random

st.set_page_config(
    page_title="AI Powered Urban Heat Island Detection",
    layout="wide"
)
st.markdown("""
<div style="
background:linear-gradient(90deg,#0f172a,#2563eb);
padding:25px;
border-radius:15px;
text-align:center;
color:white;">
<h1>🌍 AI Powered Urban Heat Island Detection System</h1>
<p>Analyze Temperature, NDVI and Urban Heat Hotspots</p>
</div>
""", unsafe_allow_html=True)
st.sidebar.title("🌍 Urban Heat AI")

st.sidebar.info("""
AI Powered Urban Heat
Island Detection System
""")

city = st.text_input(
    "Enter City Name",
    "Jaipur"
)

if st.button("Analyze"):

    # ==========================
    # CITY DATA
    # ==========================

    try:

        df = pd.read_csv("city_data.csv")

        city_row = df[
            df["City"].str.lower() == city.lower()
        ]

        if not city_row.empty:

            temperature = float(
                city_row["Temperature"].values[0]
            )

            ndvi = float(
                city_row["NDVI"].values[0]
            )

            vegetation = float(
                city_row["Vegetation"].values[0]
            )

            builtup = float(
                city_row["Builtup"].values[0]
            )

        else:

            temperature = 40
            ndvi = 0.40
            vegetation = 30
            builtup = 60

    except:

        temperature = 40
        ndvi = 0.40
        vegetation = 30
        builtup = 60

    # ==========================
    # HEAT SCORE
    # ==========================

    heat_score = round(
        (temperature * 0.5)
        + (builtup * 0.3)
        + ((100 - vegetation) * 0.2),
        2
    )

    priority_score = round(
        heat_score * 1.5,
        2
    )

    cooling = round(
        ndvi * 10,
        2
    )

    if heat_score >= 55:
        risk = "High 🔴"

    elif heat_score >= 40:
        risk = "Medium 🟠"

    else:
        risk = "Low 🟢"

    st.success(
        f"Analysis Generated Successfully For {city}"
    )

    st.info(
        f"Selected City : {city}"
    )

    st.divider()

    # ==========================
    # KPI CARDS
    # ==========================

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div style='background:#ff4b4b;padding:20px;border-radius:15px;text-align:center;color:white'>
        <h4>🌡 Temperature</h4>
        <h2>{temperature} °C</h2>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div style='background:#00c853;padding:20px;border-radius:15px;text-align:center;color:white'>
        <h4>🌿 NDVI</h4>
        <h2>{ndvi}</h2>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div style='background:#2962ff;padding:20px;border-radius:15px;text-align:center;color:white'>
        <h4>🎯 Priority Score</h4>
        <h2>{priority_score}</h2>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div style='background:#ff9800;padding:20px;border-radius:15px;text-align:center;color:white'>
        <h4>❄ Cooling Potential</h4>
        <h2>{cooling} °C</h2>
        </div>
        """, unsafe_allow_html=True)

    c5, c6 = st.columns(2)

    with c5:
        st.metric(
            "Vegetation %",
            f"{vegetation}%"
        )

    with c6:
        st.metric(
            "Built-up %",
            f"{builtup}%"
        )

    st.metric(
        "Heat Risk",
        risk
    )
    if "High" in risk:
        st.error(f"🔥 Heat Risk : {risk}")
    elif "Medium" in risk:
        st.warning(f"⚠️ Heat Risk : {risk}")
    else:
        st.success(f"✅ Heat Risk : {risk}")

    st.metric(
        "AI Predicted Risk",
        risk
    )

    st.divider()

        # ==========================
        # HEAT RISK GAUGE
        # ==========================

    st.subheader(
            "🔥 Heat Risk Index"
        )

    fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=heat_score,
                title={
                    "text": "Heat Risk Index"
                },
                gauge={
                    "axis": {
                        "range": [0, 100]
                    }
                }
            )
        )

    st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

        # ==========================
        # MAP IMAGES
        # ==========================

    col1, col2 = st.columns(2)
    with col1:

            st.subheader(
                f"{city} Surface Temperature"
            )

            if os.path.exists(
                "temperature_map.png"
            ):
                st.image(
                    "temperature_map.png",
                    use_container_width=True
                )

    with col2:

            st.subheader(
                f"{city} NDVI Map"
            )

            if os.path.exists(
                "ndvi_map.png"
            ):
                st.image(
                    "ndvi_map.png",
                    use_container_width=True
                )

    st.subheader(
            f"{city} Urban Heat Hotspots"
        )

    if os.path.exists(
            "urban_heat_hotspots.png"
        ):
            st.image(
                "urban_heat_hotspots.png",
                use_container_width=True
            )

    st.divider()

        # ==========================
        # LAND COVER
        # ==========================

    st.subheader(
            "🌿 Land Cover Distribution"
        )

    chart_df = pd.DataFrame(
            {
                "Category": [
                    "Vegetation",
                    "Built-up",
                    "Water"
                ],
                "Percentage": [
                    vegetation,
                    builtup,
                    100 - vegetation - builtup
                ]
            }
        )

    st.bar_chart(
            chart_df.set_index(
                "Category"
            )
        )

    st.divider()

        # ==========================
        # FUTURE PREDICTION
        # ==========================

    st.subheader(
            "📈 2030 Heat Prediction"
        )

    future_temp = temperature + 4

    prediction_df = pd.DataFrame(
            {
                "Year": [
                    "2025",
                    "2030"
                ],
                "Temperature": [
                    temperature,
                    future_temp
                ]
            }
        )

    st.line_chart(
            prediction_df,
            x="Year",
            y="Temperature"
        )
    st.divider()

    st.subheader(
            "🌱 Mitigation Simulator"
        )

    strategy = st.selectbox(
            "Select Mitigation Strategy",
            [
                "Tree Plantation",
                "Cool Roofs",
                "Green Corridors"
            ]
        )

    if strategy == "Tree Plantation":
            reduction = 3

    elif strategy == "Cool Roofs":
            reduction = 5

    else:
            reduction = 4

    new_temp = temperature - reduction

    mc1, mc2 = st.columns(2)

    with mc1:
            st.metric(
                "Temperature After Mitigation",
                f"{new_temp} °C"
            )

    with mc2:
            st.metric(
                "Temperature Reduction",
                f"{reduction} °C"
            )

    st.divider()

    st.subheader(
            "🏆 Priority Ranking"
        )

    ranking_df = pd.DataFrame(
            {
                "Zone": [
                    "Zone A",
                    "Zone B",
                    "Zone C",
                    "Zone D",
                    "Zone E"
                ],
                "Risk Score": [
                    92,
                    85,
                    78,
                    65,
                    55
                ]
            }
        )

    st.dataframe(
            ranking_df,
            use_container_width=True
        )
    st.subheader("📄 Project Summary")

    st.info(
        f"""
    City: {city}

    Temperature: {temperature} °C

    NDVI: {ndvi}

    Heat Score: {heat_score}

    Risk Level: {risk}
    """
    )

        # ==========================
        # AI RECOMMENDATIONS
        # ==========================


    st.subheader(
            "🤖 AI Recommendations"
        )

    if "High" in risk:

            st.warning(
                """
    • Increase Tree Plantation

    • Install Cool Roof Systems

    • Reduce Asphalt Coverage

    • Create Green Corridors

    • Increase Urban Forest Cover
                """
            )

    elif "Medium" in risk:

            st.info(
                """
    • Improve Green Spaces

    • Expand Water Bodies

    • Promote Reflective Roof Paint
                """
            )

    else:

            st.success(
                """
    • Maintain Existing Green Cover

    • Continue Environmental Monitoring
                """
            )
    
    st.divider()

    report = f"""
    Urban Heat Island Detection Report
 
    City: {city}
    Temperature: {temperature} °C 
    NDVI: {ndvi}
    Heat Score: {heat_score}
    Priority Score: {priority_score}
    Cooling Potential: {cooling}
    Risk Level: {risk}
    """
def create_pdf_report(
    city,
    temperature,
    ndvi,
    heat_score,
    priority_score,
    cooling,
    risk
):

    pdf_file = f"{city}_urban_heat_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Urban Heat Island Detection Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1,12))

    content.append(
        Paragraph(f"City: {city}", styles["Normal"])
    )

    content.append(
        Paragraph(f"Temperature: {temperature} °C", styles["Normal"])
    )

    content.append(
        Paragraph(f"NDVI: {ndvi}", styles["Normal"])
    )

    content.append(
        Paragraph(f"Heat Score: {heat_score}", styles["Normal"])
    )

    content.append(
        Paragraph(f"Priority Score: {priority_score}", styles["Normal"])
    )

    content.append(
        Paragraph(f"Cooling Potential: {cooling}", styles["Normal"])
    )

    content.append(
        Paragraph(f"Risk Level: {risk}", styles["Normal"])
    )

    doc.build(content)

    return pdf_file
st.markdown("---")

st.markdown("""
<div style='text-align:center'>
<h4>🚀 Developed by CHAMPIONFOREVER</h4>
<p>AI Powered Urban Heat Island Detection System</p>
</div>
""", unsafe_allow_html=True)
 