import pandas as pd

# 1. Carregando os dados
basics = pd.read_csv('../data/raw/title.basics.tsv', sep='\t', na_values='\\N', dtype=str)

ratings = pd.read_csv('../data/raw/title.ratings.tsv', sep='\t', na_values='\\N', dtype=str)

# 2. Filtrar apenas filmes (titleType = movie) e que sejam do gênero Terror

filmes_terror = basics[
    (basics["titleType"] == "movie") & 
    (basics["genres"].notna()) &
    (basics["genres"].str.contains("Horror"))]

# 3. Juntar com os dados de nota

filmes_com_notas = filmes_terror.merge(ratings, on="tconst")

# 4. Convertendo valores

filmes_com_notas['averageRating'] = filmes_com_notas['averageRating'].astype(float)

filmes_com_notas['numVotes'] = filmes_com_notas['numVotes'].astype(int)

# 5. Filtrando filmes com mais de 1000 votos
filmes_filtrados = filmes_com_notas[filmes_com_notas['numVotes'] > 1000]
filmes_filtrados

# 6. Ordenando do mais bem avaliado para o menos bem avaliado

filmes_ordenados = filmes_filtrados.sort_values(by='averageRating', ascending=False)

print(filmes_ordenados[["primaryTitle", "startYear", "averageRating", "numVotes"]].head(10))

# 7. Salvando arquivo CSV

filmes_ordenados.to_csv('filmes_terror_filtrados.csv', index=False)