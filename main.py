import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Načtení dat z Excel souboru
data_path = 'data/klementinum.xlsx'  # Upravte cestu k vašemu souboru
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




def test():


# Vytvoření instance třídy a provedení analýzy

    """
    temperature_analytics = TemperatureAnalytics(temperature_data)
    rok = 2022
    average_temp = temperature_analytics.get_average_temperature(rok)
    max_temp, date_of_max_temp = temperature_analytics.get_max_temperature(rok)
    min_temp, date_of_min_temp = temperature_analytics.get_min_temperature(rok)
    temperature_analytics.plot_anual_temperature_averages(rok,rok)


    print(f"Průměrná teplota v roce 2022: {average_temp}°C")
    print(f"Maximální teplota v roce 2022: {max_temp}°C, datum: {date_of_max_temp['den']}.{date_of_max_temp['měsíc']}.{date_of_max_temp['rok']}")
    print(f"Minimální teplota v roce 2022: {min_temp}°C, datum: {date_of_min_temp['den']}.{date_of_min_temp['měsíc']}.{date_of_min_temp['rok']}")
    """
# Příklad použití



def main():
    temperature_analytics = TemperatureAnalytics(temperature_data)
    vybrano = vyber()
    if vybrano == "1":
        rok = input("Zadej Rok:")
        average_temp = temperature_analytics.get_average_temperature(int(rok))
        print(f"Průměrná teplota v roce {rok}: {average_temp:.1f}°C")
    elif vybrano =="2":
        rok = input("Zadej Rok:")
        max_temp, date_of_max_temp = temperature_analytics.get_max_temperature(int(rok))
        print(f"Maximální teplota v roce {rok}: {max_temp:}°C, datum: {date_of_max_temp['den']}.{date_of_max_temp['měsíc']}.{date_of_max_temp['rok']}")
    elif vybrano =="3":
        rok = input("Zadej Rok:")
        monthly_averages = temperature_analytics.get_monthly_averages(int(rok))
        print(f"Mesicni prumer pro rok {rok} jsou:")
        print(f"{monthly_averages}")
    elif vybrano =="4":
        print("4")
    elif vybrano == "5":
        print("5")
    elif vybrano == "6":
        print("6")
    elif vybrano == "7":
        print("7")
    elif vybrano == "8":
        print("8")
    elif vybrano == "9":
        print("9")
    elif vybrano == "0":
        print("0")
    else:
        print("ERROR")



    #max_temp, date_of_max_temp = temperature_analytics.get_max_temperature(2022)
    #min_temp, date_of_min_temp = temperature_analytics.get_min_temperature(2022)
    #temperature_analytics.plot_anual_temperature_averages(2005, 2010)



def vyber():
        
    print("1 - Zobrazit průměrnou teplotu pro zadaný rok")
    print("2 - Zobrazit minimální a maximální teplotu pro zadaný rok")
    print("3 - Zobrazit měsíční průměry pro zadaný rok")
    print("4 - Analyzovat teplotní trendy")
    print("5 - Analyzovat sezónní změny")
    print("6 - Detekovat teplotní anomálie")
    print("7 - Vykreslit průměrné roční teploty")
    print("8 - Vykreslit denní teplotní trendy")
    print("9 - Vykreslit minimální a maximální teploty pro konkrétní den")
    print("0 - Konec")
    vybrano = input("Zvolte akci:")
    return vybrano

if __name__ == '__main__':
    main()