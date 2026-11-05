import pandas as pd 

class CovidDataAnalyzer:
    
    def __init__(self, file_path: str) -> None :
        self.file_path = file_path
        self.data = self.load_data()
        self.filtered_data = None

    def load_data(self) -> pd.DataFrame:
        df = pd.read_csv(self.file_path)
        return df

    def describe_data(self) -> None :
        print(self.data.columns)
        print(self.data.shape)
        print(self.data.describe())




analyzer = CovidDataAnalyzer("covid_19_data.csv")

print(analyzer.data.head(10))

analyzer.describe_data()

