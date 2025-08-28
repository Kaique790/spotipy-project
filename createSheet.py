import pandas as pd

data = {
    'artistas': ['Linkin Park', 'System of a Down', 'Guns and Roses', 'Radiohead', 'Eminem']
}

df = pd.DataFrame(data)

df.to_excel('artistas.xlsx', index=False)