import pandas as pd
import numpy as np
import os

def generate_soil_data(num_samples=10000):
    np.random.seed(42)
    
    # Generate random data for Soil parameters typical of Indian conditions
    # Nitrogen (mg/kg): typically 100 to 400
    nitrogen = np.random.uniform(50, 450, num_samples)
    
    # Phosphorus (mg/kg): typically 10 to 60
    phosphorus = np.random.uniform(5, 80, num_samples)
    
    # Potassium (mg/kg): typically 100 to 400
    potassium = np.random.uniform(50, 500, num_samples)
    
    # pH Level: typically 5.5 to 8.5
    ph_level = np.random.uniform(4.5, 9.0, num_samples)
    
    # Temperature (C): typically 20 to 40
    temperature = np.random.uniform(15, 45, num_samples)
    
    # Rainfall (mm): typical monsoon variations
    rainfall = np.random.uniform(100, 1500, num_samples)
    
    # Determine fertilizer recommendation based on simple agronomic rules
    recommendations = []
    
    for n, p, k, ph in zip(nitrogen, phosphorus, potassium, ph_level):
        if ph < 5.5:
            recommendations.append("Lime & Urea")
        elif ph > 8.5:
            recommendations.append("Gypsum & DAP")
        elif n < 150 and p > 30 and k > 200:
            recommendations.append("Urea (High N)")
        elif p < 20 and n > 200 and k > 200:
            recommendations.append("DAP (High P)")
        elif k < 150 and n > 200 and p > 30:
            recommendations.append("MOP (High K)")
        elif n < 150 and p < 20 and k < 150:
            recommendations.append("Complex NPK (19:19:19)")
        else:
            recommendations.append("Standard Balanced NPK")

    df = pd.DataFrame({
        'Nitrogen_mg_kg': nitrogen.round(2),
        'Phosphorus_mg_kg': phosphorus.round(2),
        'Potassium_mg_kg': potassium.round(2),
        'pH_Level': ph_level.round(2),
        'Temperature_C': temperature.round(1),
        'Rainfall_mm': rainfall.round(1),
        'Recommended_Fertilizer': recommendations
    })
    
    return df

if __name__ == "__main__":
    print("Generating Indian Soil Health Card synthetic dataset...")
    df = generate_soil_data()
    
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, 'soil_health_data.csv')
    
    df.to_csv(output_path, index=False)
    print(f"Dataset generated successfully! Saved to {output_path}")
    print(f"Total samples: {len(df)}")
    print("\nSample Preview:")
    print(df.head())
