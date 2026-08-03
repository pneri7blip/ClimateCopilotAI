from climate_data import ClimateData

print("===================================")
print("       ClimateCopilot AI")
print(" Decision Support for Governments")
print("===================================")

print()

climate = ClimateData()

climate.load_sample_data()

climate.show_data()
