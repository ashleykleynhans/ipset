#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

PIE_CHART_IMAGE_FILE = 'abuse-pie-chart.png'

if __name__ == '__main__':
    # Load data from CSV with error handling
    try:
        df = pd.read_csv('ipv4.csv', on_bad_lines='skip')
    except pd.errors.ParserError as e:
        print(f"Error reading the CSV file: {e}")

    # Check if DataFrame is created
    if 'df' in locals():
        # Group by 'Country' and count occurrences
        country_counts = df['Country'].value_counts()

        # Sorting and selecting top 10
        top_countries = country_counts.nlargest(10)
        others_count = country_counts.iloc[10:].sum()
        final_counts = pd.concat([top_countries, pd.Series([others_count], index=['Others'])])

        # Define colors for each segment
        colors = [
            '#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD',
            '#FF69B4', '#00FA9A', '#800080', '#FFA500', '#20B2AA', '#A52A2A'
        ]  # 11 colors including one for 'Others'

        # Labels for the pie chart, only showing labels for top 10
        labels = [f'{index}: {value:.1f}%' for index, value in (top_countries * 100 / final_counts.sum()).items()]
        labels.append('Others')  # Simple label for 'Others'

        # Plotting the pie chart
        plt.figure(figsize=(12, 9))
        wedges, texts, autotexts = plt.pie(final_counts, labels=None, colors=colors, autopct=lambda pct: f'{pct:.1f}%' if pct > 3 else '', startangle=140, pctdistance=0.85)

        # Add a legend
        plt.legend(wedges, labels, title="Country", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        plt.title('Abuse Reports by Country: Top 10 and Others')
        plt.axis('equal')

        # Save the figure to a file
        plt.savefig(PIE_CHART_IMAGE_FILE, bbox_inches='tight')
        plt.close()
        print(f'Pie chart saved to: {PIE_CHART_IMAGE_FILE}')
    else:
        print('Data could not be loaded. Please check the CSV file format.')
