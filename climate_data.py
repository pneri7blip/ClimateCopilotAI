class ClimateData:
    def __init__(self):
        self.city = ""
        self.temperature = 0
        self.rainfall = 0

    def load_sample_data(self):
        self.city = "Rome"
        self.temperature = 34
        self.rainfall = 5

    def show_data(self):
        print("City:", self.city)
        print("Temperature:", self.temperature, "°C")
        print("Rainfall:", self.rainfall, "mm")
