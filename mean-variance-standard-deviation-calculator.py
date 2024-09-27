import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("A lista deve conter exatamente 9 números.")
    
    # Converter a lista em uma matriz 3x3
    matrix = np.array(lst).reshape(3, 3)
    
    # Calcular estatísticas para as linhas, colunas e toda a matriz
    calculations = {
        'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()],
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()],
        'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()],
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()],
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]
    }
    
    return calculations
