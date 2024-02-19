import pandas as pd
import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data_path = 'data/klementinum.xlsx'
data_sheet_name = 'data'
temperature_data = pd.read_excel(data_path, sheet_name=data_sheet_name)

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

    def get_monthly_averages(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        return yearly_data.groupby('měsíc')['T-AVG'].mean()

    def analyze_temperature_trends(self, start_year, end_year):
        trend_data = self.data[(self.data['rok'] >= start_year) & (self.data['rok'] <= end_year)]
        annual_average_temperatures = trend_data.groupby('rok')['T-AVG'].mean()
        return annual_average_temperatures

    def plot_daily_temperature_trends(self, start_year, end_year):
        filtered_data = self.data[(self.data['rok'] >= start_year) & (self.data['rok'] <= end_year)]
        annual_average_temperatures = filtered_data.groupby('rok')['T-AVG'].mean()
        plt.figure(figsize=(10, 6))
        plt.plot(annual_average_temperatures.index, annual_average_temperatures.values, marker='o', linestyle='-', color='b')
        plt.title(f'Denní teplotní trendy mezi lety {start_year} - {end_year}')
        plt.xlabel('Rok')
        plt.ylabel('Průměrná teplota (C)')
        plt.grid(True)
        plt.show()

    def plot_anual_temperature_averages(self, start_year, end_year):
        filtered_data = self.data[(self.data['rok'] >= start_year) & (self.data['rok'] <= end_year)]
        annual_avg_temps = filtered_data.groupby('rok')['T-AVG'].mean()
        plt.figure(figsize=(10, 6))
        plt.plot(annual_avg_temps.index, annual_avg_temps.values, marker='o', linestyle='-', color='b')
        plt.title(f'Průměrné roční teploty mezi lety {start_year} a {end_year}')
        plt.xlabel('Rok')
        plt.ylabel('Průměrná teplota (C)')
        plt.grid(True)
        plt.show()

    def plot_day(self, day, month, year):
        filtered_data = self.data[
            (self.data['den'] == day) & (self.data['měsíc'] == month) & (self.data['rok'] == year)]
        annual_max_temps = filtered_data['TMA']
        annual_min_temps = filtered_data['TMI']

        X = np.array([annual_min_temps.index,annual_max_temps.index])
        Y = np.array([annual_min_temps.values,annual_max_temps.values])
        plt.figure(figsize=(10, 6))
        plt.scatter(X, Y)
        plt.title(f'Maximální a minimální teplota v tento den: {day}.{month}.{year}')
        plt.xlabel('den')
        plt.ylabel('Maximální a minimální teplota (°C)')
        plt.grid(True)
        plt.show()

def vyber():
    print("1 - Zobrazit průměrnou teplotu pro zadaný rok")
    print("2 - Zobrazit minimální a maximální teplotu pro zadaný rok")
    print("3 - Zobrazit měsíční průměry pro zadaný rok")
    print("4 - Analyzovat teplotní trendy")
    print("5 - Detekovat teplotní anomálie")
    print("6 - Vykreslit denní teplotní trendy")
    print("7 - Vykreslit minimální a maximální teploty pro konkrétní den")
    print("0 - Konec")
    vybrano = input("Zvolte akci:")
    return vybrano

def validacniFunkce(typ, cislo):
    cislo = int(cislo)
    if (typ == "rok"):
        if (cislo > 1970 and cislo < 2024):
            return cislo
        else:
            return "2020"
    elif (typ == "mesic"):
        if (cislo < 12 and cislo > 0):
            return cislo
        else:
            return "12"
    elif (typ == "den"):
        if (cislo > 0 and cislo < 32):
            return cislo
        else:
            return "2"
    else:
        return None

def main():
    temperature_analytics = TemperatureAnalytics(temperature_data)
    vybrano = vyber()
    if vybrano == "1":
        year = input("Zadej Rok:")
        average_temp = temperature_analytics.get_average_temperature(validacniFunkce("rok", year))
        print(f"Průměrná teplota v roce {year}: {average_temp:.1f}°C")
    elif vybrano =="2":
        year = input("Zadej Rok:")
        max_temp, date_of_max_temp = temperature_analytics.get_max_temperature(validacniFunkce("rok", year))
        print(f"Maximální teplota v roce {year}: {max_temp:}°C, datum: {date_of_max_temp['den']}.{date_of_max_temp['měsíc']}.{date_of_max_temp['rok']}")
    elif vybrano =="3":
        year = input("Zadej Rok:")
        monthly_averages = temperature_analytics.get_monthly_averages(validacniFunkce("rok", year))
        print(f"Mesicni prumer pro rok {year} jsou:")
        print(f"{monthly_averages}")
    elif vybrano =="4":
        start_year = input("Zadej Zacatecni Rok: ")
        end_year = input("Zadej Koncovy Rok: ")
        trends = temperature_analytics.analyze_temperature_trends(validacniFunkce("rok", start_year), validacniFunkce("rok", end_year))
        print(trends)
    elif vybrano == "5":
        start_year = input("Startovní rok:")
        end_year = input("Koncový rok rok:")
        temperature_analytics.plot_anual_temperature_averages(validacniFunkce("rok", start_year),validacniFunkce("rok", end_year))
    elif vybrano == "6":
        start_year = input("Zadej první rok:")
        end_year = input("Zadej poslední rok:")
        temperature_analytics.plot_daily_temperature_trends(validacniFunkce("rok", start_year), validacniFunkce("rok", end_year))
    elif vybrano == "7":
        day = input("den:")
        month = input("měsíc:")
        year = input("rok:")
        temperature_analytics.plot_day(validacniFunkce("den", day), validacniFunkce("mesic", month), validacniFunkce("rok", year))
    elif vybrano == "0":
        print("0")
    else:
        print("ERROR")

if __name__ == '__main__':
    main()