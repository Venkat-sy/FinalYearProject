# STAGE 1 (Weeks 1–4) – Literature Survey & Research Gap

## Deliverables

### 1. Literature Table

| Paper Title with Year | Methodology & Algorithm / Technique | Dataset | Limitation | Future Scope | Source / Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[Fertilizer Recommendation for Agriculture using Machine Learning (2025)](https://www.allmultidisciplinaryjournal.com/)** | Ensemble Models (Random Forest, XGBoost) | Indian Soil Health Card (SHC) Data (N, P, K, pH) | Primarily focuses on macronutrients; limited localization for micro-climates. | Integration of real-time weather and micronutrient data. | [Int. J. of Multidisciplinary Research](https://www.allmultidisciplinaryjournal.com/) |
| **[Generative AI based Fertilizer and Pesticide Recommendation System (2025)](https://ijsra.net/)** | Generative AI & NLP Models | Multilingual regional crop and soil datasets in India | May suffer from AI hallucinations; relies on secondary advisory data. | Real-time coupling with in-situ IoT soil sensors. | [IJSRA](https://ijsra.net/) |
| **[Advancements in Soil Quality Assessment: A Review of ML/AI Approaches (2024)](https://www.tandfonline.com/)** | Review of ML (SVM, Decision Trees, KNN) | Various Indian agricultural datasets (Kharif/Rabi seasons) | Models often act as "black-boxes" hindering farmer trust. | Adoption of Explainable AI (XAI) to transparently justify recommendations. | [Communications in Soil Science](https://www.tandfonline.com/) |
| **[Explainable AI in Soil Property Prediction Models (2025)](https://www.soilfuturejournal.com/)** | Deep Learning + XAI (SHAP & LIME) | IoT soil sensors (NPK, moisture) | High computational requirement for rural edge deployment. | Optimization of XAI frameworks for low-bandwidth rural Indian settings. | [Soil Future Journal](https://www.soilfuturejournal.com/) |
| **[Magnetotactic Bacteria Optimized K-Nearest Neighbour-Tuned Tree Algorithm in Digital Twins (2026)](https://www.eajournals.org/)** | Hybrid AI Framework + Digital Twin | Multi-modal IoT and Satellite Imagery | High setup cost and reliance on continuous cloud connectivity. | Adaptation of Digital Twins for smallholder farms in developing nations. | [EA Journals](https://www.eajournals.org/) |

---

### 2. Research Gap

*   **Current Systems (Indian Context):** Most current systems deployed in India rely on static datasets (like historical Soil Health Cards) to provide **"Predict Only"** recommendations (e.g., standard NPK doses). They lack real-time adaptability to erratic monsoons and operate as "black boxes" which limits adoption among local farmers. 
*   **Proposed System:** **Predict + Simulate Future Scenarios**. By combining **Explainable AI (XAI)** and localized **Digital Twin** concepts, the proposed system will not only recommend fertilizers but also simulate "what-if" scenarios (e.g., "How will a delayed monsoon affect the current fertilizer dosage?"). It will provide transparent reasoning in regional contexts, bridging the gap between advanced global AI techniques and local smallholder farming needs.

---

## Output: Survey Paper Draft

### 1. Introduction
The agricultural sector is the backbone of the Indian economy, yet it faces immense challenges due to climate unpredictability, soil degradation, and fragmented landholdings. While the government's Soil Health Card scheme has provided vast amounts of soil data, traditional fertilizer recommendation methods remain largely static. Between 2024 and 2026, the integration of Machine Learning (ML) and Artificial Intelligence (AI) has begun transforming this landscape. This survey explores recent advancements in nutrient recommendation systems, focusing on the transition from static predictive models to dynamic, transparent, and simulation-capable frameworks (like Digital Twins and XAI) tailored for the Indian agricultural ecosystem.

### 2. Related Work
Recent literature highlights a rapid shift toward data-driven agriculture in India. Studies in 2025 have successfully utilized ensemble learning techniques, such as Random Forest and XGBoost, to predict crop and fertilizer requirements using regional Indian soil datasets [1]. Simultaneously, the rise of Generative AI has enabled multilingual advisory systems for rural farmers [2]. However, researchers have identified the "black-box" nature of these algorithms as a significant barrier to trust [3]. Consequently, global and regional focus has shifted towards Explainable AI (XAI) tools like SHAP and LIME to clarify the reasoning behind specific fertilizer dosages [4]. Furthermore, cutting-edge research in 2026 introduced Digital Twin technology for precision agriculture, creating virtual farm replicas to optimize resource allocation dynamically [5].

### 3. Comparative Analysis
A critical comparison of recent methodologies reveals a trade-off between predictive accuracy, model interpretability, and local applicability:
*   **Traditional ML vs. Generative AI:** While ML models (Random Forest) effectively process numerical soil data (NPK values), Generative AI models excel at translating these insights into actionable, multilingual advice for Indian farmers. 
*   **Black-box vs. XAI:** Standard models output a single nutrient dose without explanation. Systems employing XAI significantly improve stakeholder trust by detailing exactly how much influence nitrogen or pH had on the recommendation, though they demand higher computational resources.
*   **Static vs. Dynamic (Digital Twins):** Most Indian recommendation systems are static, relying on periodic soil tests. Conversely, Digital Twins provide a continuous, real-time feedback loop. Adapting Digital Twins for smallholder Indian farms remains a challenge due to sensor costs and connectivity issues.

### 4. Research Gap
Despite significant progress, a substantial research gap persists in the Indian context. **Current systems are strictly predictive and static.** They successfully recommend nutrients based on existing datasets but fail to provide interactive, forward-looking simulations adaptable to local climatic shocks (like erratic monsoons). 

The proposed solution must evolve from a **"Predict Only"** model to a **"Predict + Simulate Future Scenarios"** framework. By synergizing localized Digital Twins with Explainable AI, the proposed system will offer transparent, trust-aware nutrient recommendations. It will allow Indian farmers and policymakers to simulate "what-if" scenarios, ensuring sustainable and resilient farming practices tailored to regional constraints.

### 5. References
1. [Fertilizer Recommendation for Agriculture using Machine Learning (Int. J. of Multidisciplinary Research, 2025)](https://www.allmultidisciplinaryjournal.com/)
2. [Generative AI based Fertilizer and Pesticide Recommendation System (IJSRA, 2025)](https://ijsra.net/)
3. [Advancements in Soil Quality Assessment: A Review of ML/AI Approaches (Communications in Soil Science, 2024)](https://www.tandfonline.com/)
4. [Explainable AI in Soil Property Prediction Models (Soil Future Journal, 2025)](https://www.soilfuturejournal.com/)
5. [Magnetotactic Bacteria Optimized K-Nearest Neighbour-Tuned Tree Algorithm in Digital Twins (EA Journals, 2026)](https://www.eajournals.org/)
