import pandas as pd

# Načtení dat z Excel souboru
data_path = '/klementinum.xlsx'  # Upravte cestu k vašemu souboru
data_sheet_name = 'data'
temperature_data = pd.read_excel(data_path, sheet_name=data_sheet_name)

# Definice třídy pro analýzu teplot
class TemperatureAnalytics:
    def __init__(self, data):
        self.data = data

    def get_average_temperature(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        return yearly_data['T-AVG'].mean()

    def get_max_temperature(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        max_temp = yearly_data['TMA'].max()
        date_of_max_temp = yearly_data[yearly_data['TMA'] == max_temp][['rok', 'měsíc', 'den']].iloc[0]
        return max_temp, date_of_max_temp

    def get_min_temperature(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        min_temp = yearly_data['TMI'].min()
        date_of_min_temp = yearly_data[yearly_data['TMI'] == min_temp][['rok', 'měsíc', 'den']].iloc[0]
        return min_temp, date_of_min_temp

    def get_monthly_averages(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        return yearly_data.groupby('měsíc')['T-AVG'].mean()

    def analyze_temperature_trends(self, start_year, end_year):
        trend_data = self.data[(self.data['rok'] >= start_year) & (self.data['rok'] <= end_year)]
        annual_average_temperatures = trend_data.groupby('rok')['T-AVG'].mean()
        return annual_average_temperatures

# Vytvoření instance třídy a provedení analýzy
temperature_analytics = TemperatureAnalytics(temperature_data)

# Příklad použití
average_temp_2022 = temperature_analytics.get_average_temperature(2022)
max_temp_2022, date_of_max_temp_2022 = temperature_analytics.get_max_temperature(2022)
min_temp_2022, date_of_min_temp_2022 = temperature_analytics.get_min_temperature(2022)

print(f"Průměrná teplota v roce 2022: {average_temp_2022}°C")
print(f"Maximální teplota v roce 2022: {max_temp_2022}°C, datum: {date_of_max_temp_2022['den']}.{date_of_max_temp_2022['měsíc']}.{date_of_max_temp_2022['rok']}")
print(f"Minimální teplota v roce 2022: {min_temp_2022}°C, datum: {date_of_min_temp_2022['den']}.{date_of_min_temp_2022['měsíc']}.{date_of_min_temp_2022['rok']}")
