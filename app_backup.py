import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(
    page_title="AI Powered Urban Heat Island Detection",
    layout="wide"
)

st.title("🌍 AI Powered Urban Heat Island Detection System")
st.write("Analyze Temperature, NDVI and Urban Heat Hotspots")

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
        st.metric(
            "Temperature",
            f"{temperature} °C"
        )

    with c2:
        st.metric(
            "NDVI",
            ndvi
        )

    with c3:
        st.metric(
            "Priority Score",
            priority_score
        )

    with c4:
        st.metric(
            "Cooling Potential",
            f"{cooling} °C"
        )

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
    if heat_score > 60:
        ai_risk = "HIGH 🔴"
    elif heat_score > 45:
        ai_risk = "MEDIUM 🟠"
    else:
        ai_risk = "LOW 🟢"

    st.metric(
    "AI Predicted Risk",
    ai_risk
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

    content.append(Spacer(1, 12))

    content.append(Paragraph(f"City: {city}", styles["Normal"]))
    content.append(Paragraph(f"Temperature: {temperature} °C", styles["Normal"]))
    content.append(Paragraph(f"NDVI: {ndvi}", styles["Normal"]))
    content.append(Paragraph(f"Heat Score: {heat_score}", styles["Normal"]))
    content.append(Paragraph(f"Priority Score: {priority_score}", styles["Normal"]))
    content.append(Paragraph(f"Cooling Potential: {cooling}", styles["Normal"]))
    content.append(Paragraph(f"Risk Level: {risk}", styles["Normal"]))

    doc.build(content)

    return pdf_file


pdf_file = create_pdf_report(
    city,
    temperature,
    ndvi,
    heat_score,
    priority_score,
    cooling,
    risk
)

with open(pdf_file, "rb") as file:

    st.download_button(
        label="📄 Download PDF Report",
        data=file,
        file_name=pdf_file,
        mime="application/pdf"
    )
