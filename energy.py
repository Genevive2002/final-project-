import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample electricity consumption data (date, energy consumption in kWh)
data = {
    'Date': pd.date_range(start='2024-01-01', periods=30, freq='D'),
    'Energy Consumption (kWh)': np.random.randint(100, 300, size=30)
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display basic statistics
def display_statistics(df):
    print("Energy Consumption Statistics:")
    print(df.describe())

# Plot energy consumption over time
def plot_consumption(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Energy Consumption (kWh)'], marker='o', linestyle='-', color='b')
    plt.title('Energy Consumption Over Time')
    plt.xlabel('Date')
    plt.ylabel('Energy Consumption (kWh)')
    plt.grid(True)
    plt.show()

# Identify peak consumption days
def find_peak_days(df, threshold):
    peak_days = df[df['Energy Consumption (kWh)'] > threshold]
    return peak_days

# Provide energy-saving recommendations
def energy_saving_tips():
    tips = [
        "1. Use energy-efficient appliances.",
        "2. Turn off lights and electronics when not in use.",
        "3. Implement smart thermostats for better temperature control.",
        "4. Insulate your home to reduce heating and cooling needs.",
        "5. Use solar panels to generate clean energy."
    ]
    print("\nEnergy-Saving Tips:")
    for tip in tips:
        print(tip)

# Main function to analyze energy consumption
def energy_efficiency_analysis(df):
    display_statistics(df)
    plot_consumption(df)
    
    # Set a threshold for peak energy consumption
    threshold = 250
    peak_days = find_peak_days(df, threshold)
    if not peak_days.empty:
        print("\nPeak Consumption Days (above {} kWh):".format(threshold))
        print(peak_days[['Date', 'Energy Consumption (kWh)']])
    else:
        print("\nNo peak consumption days found.")
    
    energy_saving_tips()

# Run the analysis
energy_efficiency_analysis(df)
