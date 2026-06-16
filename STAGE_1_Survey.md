# STAGE 1 (Weeks 1–4) – Literature Survey & Research Gap

## Deliverables

### 1. Literature Table

| Paper Title with Year | Methodology & Algorithm / Technique | Dataset | Limitation | Future Scope | Source / Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[Magnetotactic Bacteria Optimized K-Nearest Neighbour-Tuned Tree Algorithm in Digital Twins (2026)](https://www.eajournals.org/)** | Hybrid AI Framework (MBO-KNN-TA) + Digital Twin | Multi-modal IoT, UAV, and Remote Sensing (Sentinel-2) | High reliance on continuous cloud connectivity and bandwidth for synchronization. | Transition to "Cloud-Fog-Edge" infrastructure to handle high data latency. | [EA Journals](https://www.eajournals.org/) |
| **[Explainable AI in Soil Property Prediction Models (2025)](https://www.soilfuturejournal.com/)** | LSTM & Deep Learning + XAI (SHAP & LIME) | Real-time IoT soil sensors (NPK, pH, moisture) | Computationally heavy, making it difficult to run on low-power edge devices. | Optimization of XAI models for edge computing in rural environments. | [Soil Future Journal](https://www.soilfuturejournal.com/) |
| **[AgroMind+: An Intelligent Multi-Crop Recommendation System (2025)](https://www.impactfactor.org/)** | LSTM-Attention Architectures | Meteorological forecasts and historical yield data | Lacks the ability to simulate "what-if" future climate and irrigation scenarios. | Integration of predictive simulation for dynamic environmental changes. | [Impact Factor / Discover Robotics](https://www.impactfactor.org/) |
| **[Machine learning based recommendation of agricultural and horticultural crop farming (2024)](https://www.etasr.com/)** | Ensemble Models (Random Forest, XGBoost) | Regional soil health and historical climate datasets | Acts as a "black-box" model, reducing farmer trust; predicts based on static data. | Implementation of XAI to improve transparency and explainability. | [ETASR / Heliyon](https://www.etasr.com/) |
| **[Precision Irrigation Scheduling using IoT and AI (2023)](https://www.mdpi.com/journal/sensors)** | Multi-layer Perceptron (MLP) + IoT feedback loop | In-situ moisture sensors and local weather stations | Primarily focused on current state prediction without long-term scenario forecasting. | Expansion into holistic resource efficiency including automated nutrient recommendation. | [MDPI Sensors](https://www.mdpi.com/journal/sensors) |

---

### 2. Research Gap

*   **Current Systems:** Focus primarily on **Predict Only** paradigms. They analyze historical and current data (like NPK levels, moisture, and weather) to recommend a crop or predict the immediate yield, but they operate as static or "black-box" models without simulating long-term outcomes.
*   **Proposed System:** **Predict + Simulate Future Scenarios**. By combining **Explainable AI (XAI)** and **Digital Twin** technology, the proposed system will not only predict yield and recommend nutrients but also simulate dynamic "what-if" scenarios (e.g., "What happens to the yield if drought occurs for 10 days?" or "How will a 15% reduction in fertilizer affect the soil in 3 months?").

---

## Output: Survey Paper Draft

### 1. Introduction
The agricultural sector is undergoing a massive transformation driven by Precision Agriculture (PA) and Artificial Intelligence (AI). With a growing global population and escalating climate unpredictability, traditional farming methods are proving insufficient. Recent advancements from 2023 to 2026 have seen the introduction of Digital Twin (DT) technology and Explainable AI (XAI) to optimize yield prediction, irrigation, and nutrient recommendation. While current models boast high accuracy in forecasting agricultural outputs, the challenge of user trust and static prediction remains. This survey explores the state-of-the-art in agricultural AI, examining methodologies, datasets, and limitations to propose a framework that bridges the gap between static prediction and dynamic simulation.

### 2. Related Work
Recent literature emphasizes the shift towards data-driven agricultural management. Studies in 2024 demonstrated the efficacy of ensemble learning techniques, such as XGBoost and Random Forest, in providing accurate crop and nutrient recommendations based on historical datasets [4]. By 2025, the focus shifted towards addressing the "black-box" nature of these algorithms [2]. Researchers began integrating XAI tools like SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) to provide transparent reasoning behind fertilizer dosages and crop selections [2][3]. Concurrently, in 2026, Digital Twin technology emerged as a powerful tool for precision agriculture, creating virtual replicas of physical farm environments using multi-modal data from IoT sensors and Sentinel-2 satellites [1]. 

### 3. Comparative Analysis
A critical comparison of recent methodologies reveals a trade-off between predictive accuracy, model interpretability, and simulation capability. 
*   **Traditional ML vs. Deep Learning:** While traditional ML models (e.g., Random Forest) are easier to deploy, deep learning frameworks (e.g., LSTM-Attention) offer superior accuracy for yield prediction but suffer from a lack of transparency.
*   **Black-box vs. XAI:** Systems employing XAI (SHAP/LIME) significantly improve stakeholder trust by detailing feature importance (e.g., the exact impact of nitrogen levels on yield). However, they often demand higher computational resources.
*   **Static vs. Dynamic (Digital Twins):** Most current recommendation systems are static—they output a single decision based on input data. Conversely, Digital Twins provide a continuous, real-time feedback loop, though they currently struggle with edge-computing constraints and high latency.

### 4. Research Gap
Despite significant progress in agricultural AI, a substantial research gap persists. **Current systems are strictly predictive.** They successfully recommend nutrients or predict yields based on existing datasets but fail to provide interactive, forward-looking simulations. Stakeholders cannot easily test hypotheses or visualize the long-term impacts of their decisions under varying climatic conditions. 

The proposed solution must evolve from a **"Predict Only"** model to a **"Predict + Simulate Future Scenarios"** framework. By synergizing Digital Twins with Explainable AI, the proposed system will not only offer transparent nutrient and irrigation recommendations but also allow users to simulate "what-if" scenarios, ensuring sustainable and resilient farming practices in the face of environmental uncertainty.

### 5. References
1. [Magnetotactic Bacteria Optimized K-Nearest Neighbour-Tuned Tree Algorithm in Digital Twins (EA Journals, 2026)](https://www.eajournals.org/)
2. [Explainable AI in Soil Property Prediction Models (Soil Future Journal, 2025)](https://www.soilfuturejournal.com/)
3. [AgroMind+: An Intelligent Multi-Crop Recommendation System (Impact Factor / Discover Robotics, 2025)](https://www.impactfactor.org/)
4. [Machine learning based recommendation of agricultural and horticultural crop farming (ETASR / Heliyon, 2024)](https://www.etasr.com/)
5. [Precision Irrigation Scheduling using IoT and AI (MDPI Sensors, 2023)](https://www.mdpi.com/journal/sensors)
