import pandas as pd


def obter_particulas_dataframe(particulas):
    df_particulas = pd.DataFrame(particulas)
    df_particulas.index = [f"Partícula {i + 1}" for i in range(len(particulas))]
    return df_particulas
