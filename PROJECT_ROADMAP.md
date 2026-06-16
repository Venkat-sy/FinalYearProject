# Final Year Project: Complete Roadmap

**Project Title:** AI-Driven Nutrient Recommendation System with Digital Twin & XAI Capabilities  
**Domain:** Precision Agriculture / Artificial Intelligence  
**Target Context:** Indian Agriculture (Smallholder Farms, Monsoonal Climate)

As your guide, I have structured this roadmap to take you from the theoretical research phase all the way to a fully deployed software application. Use this as your master checklist.

---

## Stage 1: Literature Survey & Problem Definition (Weeks 1–4) ✅ *COMPLETED*
*   **Tasks:** Study existing systems, identify the research gap (Predict Only vs. Predict + Simulate).
*   **Deliverables:** Literature Table, Research Gap Identification, Survey Paper Draft.

---

## Stage 2: System Architecture & Requirements (Weeks 5–8)
Before writing any code, you must define the "blueprint" of your project.

*   **Software Requirements Stack (Recommended):**
    *   **Machine Learning:** Python, Scikit-Learn, XGBoost, SHAP (for Explainable AI).
    *   **Backend / API:** FastAPI or Flask (Python-based, easy to connect to your ML models).
    *   **Frontend (User Interface):** HTML/CSS/JavaScript or a modern framework like React/Next.js.
    *   **Database:** SQLite (for development) or PostgreSQL.
*   **Data Requirements:**
    *   Gather agricultural datasets. Look for Kaggle datasets specific to Indian soil (e.g., "Crop Recommendation Dataset India" containing N, P, K, Temperature, Humidity, pH, Rainfall).
    *   Identify a Weather API (like OpenWeatherMap) to pull real-time climate data for the simulation part.
*   **Deliverable:** A System Architecture Diagram showing how the User Interface talks to the Backend, which queries the ML Model and Weather API.

---

## Stage 3: Data Preprocessing & EDA (Weeks 9–11)
AI is only as good as the data you feed it.

*   **Tasks:**
    *   Load your dataset into Python using Pandas.
    *   **Clean the Data:** Handle missing values, remove duplicates.
    *   **Exploratory Data Analysis (EDA):** Create graphs to see how Nitrogen levels correlate with crop yield or how Rainfall affects soil pH.
    *   **Feature Engineering:** Combine or modify data columns to make them more useful for the AI.
*   **Deliverable:** A Jupyter Notebook (`.ipynb`) containing all your data cleaning steps and visual graphs.

---

## Stage 4: Core Machine Learning Development (Weeks 12–16)
This is where you build the "Brain" of your project.

*   **Tasks:**
    *   **Baseline Model:** Train a simple Random Forest and an XGBoost model on your data to predict the required fertilizer dose based on input soil parameters.
    *   **Evaluation:** Check your model's accuracy (using metrics like RMSE or F1-Score).
    *   **The XAI Integration:** Write the Python code using the `shap` library to generate visual explanations (waterfall plots) showing *why* the model made its prediction.
*   **Deliverable:** A trained `.pkl` (pickle) model file and a script that outputs SHAP explanations.

---

## Stage 5: The "Digital Twin" Simulation Module (Weeks 17–20)
This is your unique selling point (USP) that separates your project from generic calculators.

*   **Tasks:**
    *   Build a Python module that takes the base ML prediction and modifies it based on hypothetical "what-if" scenarios.
    *   *Example Scenario Engine:* If the user selects "What if it doesn't rain for 15 days?", the code mathematically adjusts the predicted nutrient efficiency and outputs a new, adjusted fertilizer recommendation.
*   **Deliverable:** The Simulation logic/script integrated into your main backend.

---

## Stage 6: Full-Stack Web Application Integration (Weeks 21–24)
Making your AI usable for a farmer or end-user.

*   **Tasks:**
    *   **Backend:** Wrap your Python ML code and Simulation engine in API endpoints.
    *   **Frontend:** Build a clean, professional web interface. It should have forms for the user to input their NPK values and a dashboard to display the XAI charts (why the decision was made) and the Simulation toggles ("What if...").
*   **Deliverable:** A fully functioning local web application (running via `localhost`).

---

## Stage 7: Testing, Validation & Final Thesis (Weeks 25–28)
Polishing the diamond before final submission.

*   **Tasks:**
    *   Test the web app with extreme "edge case" inputs (e.g., zero nitrogen, extreme heat) to ensure it doesn't crash.
    *   Write the Final Project Report / Thesis.
    *   Prepare the final PowerPoint presentation, ensuring you have screenshots of your XAI dashboards.
*   **Deliverable:** Final Thesis Document, Final Presentation, and potentially deploying the app live on a free platform like Vercel or Render.
