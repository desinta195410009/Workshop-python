
import pandas as pd

url = "https://data.jakarta.go.id/read-resource/json/rekapitulasi-kejadian-banjir-pertahun/8ab1b8ccbed6e2555e577bc487f0981b"
df = pd.read_csv(url)

print(df)
print(df.head(3))