

def cargar_dataset(archivo):  #La entrada es un archivo
    import pandas as pd
    import os
    
    extension = os.path.splitext(archivo)[1].lower()
# Cargar el archivo según su extensión
    if extension == '.csv':
        df= pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df= pd.read_excel(archivo)
        return (df)
    elif extension == '.json':
        df= pd.read_json(archivo)
        return (df)
    elif extension == '.html':
        df= pd.read_html(archivo)
        return (df)
    else:
            raise ValueError(f"Formato de archivo no soportado: {extension}")



#Sustitución de valores nulos con el método de “ffill” (Para todas las variables).
def ffill_df(df):
    import pandas as pd
    return df.fillna(method="ffill")


#Sustitución de valores nulos con el método de “bfill” (Para todas las variables).
def bfill_df(df):
     return df.fillna(method="bfill")


# Sustitución de valores nulos con el método por un “string concreto” (Solo para variables String).
def fillna_string(df, string_value="Sin Dato"):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include=["object"]).columns:
        df_copy[col] = df_copy[col].fillna(string_value)
    return df_copy


# Sustitución de valores nulos con el método de “promedio” (Solo para variables Numéricas).
def fillna_mean(df):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include=["number"]).columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].mean())
    return df_copy


# Sustitución de valores nulos con el método de “mediana” (Solo para variables Numéricas).
def fillna_median(df):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include=["number"]).columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy


# Sustitución de valores nulos con el método de “constante” (Solo para variables Numéricas).
def fillna_constant(df, constant_value=0):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include=["number"]).columns:
        df_copy[col] = df_copy[col].fillna(constant_value)
    return df_copy


# Identificación de valores nulos por columna y por dataframe” (Para todas las variables).
def resumen_nulos(df):
    nulos_columna = df.isnull().sum()
    total_nulos = df.isnull().sum().sum()
    porcentaje_nulos = (df.isnull().mean() * 100).round(2)
    
    import pandas as pd
    resumen = pd.DataFrame({
        "Nulos": nulos_columna,
        "Porcentaje (%)": porcentaje_nulos
    })
    
    return resumen, f"Total de valores nulos en el DataFrame: {total_nulos}"


