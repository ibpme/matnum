import numpy as np

matrix = [[2, 1, -2, 3], [1, -1, -1, 0], [1, 1, 3, 12]]
matrix_np = np.mat(matrix)
row, col = matrix_np.shape
solution = [None for i in range(row)]
determinant = None


def eliminate(matrix):
    """
    Fungsi ini mengeliminasi matrix dengan Algorithma Gauss dan membuat matrix baru 

    Note: 
    * Gunakan ini hanya pada matrix yang belum di eliminasi
    * Gunakan ini atau eliminate_pivot()
    """
    for k in range(row-1):
        if abs(matrix[k][k]) < 10**-15:
            print("NotValidValue", (k, k))
            raise Exception("Proses Gagal")
        for i in range(k+1, row):
            p = matrix[i][k]/matrix[k][k]
            for j in range(k+1, col):
                matrix[i][j] = matrix[i][j] - p*matrix[k][j]
            matrix[i][k] = 0

    matrix_np = np.mat(matrix)
    return matrix_np


def eliminate_pivot(matrix):
    """
    Fungsi ini mengeliminasi matrix dengan Algorithma Gauss 
    dengan Penumpuan Parsial dan membuat matrix baru 

    Note: 
    * Gunakan ini hanya pada matrix yang belum di eliminasi
    * Gunakan ini atau eliminate()
    """
    for k in range(row-1):  # Iterate from first row to the second last row
        # Begin pivoting
        m = k
        for i in range(k+1, row):  # Iterate from next kth row to the last row

            if abs(matrix[i][k]) > abs(matrix[m][k]):
                m = i

        if m != k:
            for j in range(k, col):  # Iterate from kth collumn to the last collumn
                s = matrix[k][j]
                matrix[k][j] = matrix[m][j]
                matrix[m][j] = s

        if abs(matrix[k][k]) < 10**-15:
            print("NotValidValue", (k, k))
            raise Exception("Proses Gagal")

        # Gauss Elimination
        for i in range(k+1, row):  # Iterate from first row to the second last row

            p = matrix[i][k]/matrix[k][k]

            for j in range(k+1, col):  # Iterate from next to kth collumn to the last collumn
                matrix[i][j] = matrix[i][j] - p*matrix[k][j]
            matrix[i][k] = 0
    matrix_np = np.mat(matrix)
    return matrix_np


def backwards(matrix):
    """
    Fungsi ini melakukan penyulihan mundur pada matrix yang telah dieliminasi 
    dan akan menghasilan solusi 

    Note: 
    * Gunakan ini hanya pada matrix sudah di eliminasi
    """
    dim = row - 1  # n kalau di buku modul
    if abs(matrix[dim][dim]) < 10**-15:
        print("NotValidValue", (dim, dim))
        raise Exception("Proses Gagal")

    solution[dim] = matrix[dim][dim+1]/matrix[dim][dim]

    for k in range(dim-1, -1, -1):
        s = 0
        for i in range(k+1, dim):
            s += matrix[k][i]*solution[i]

        solution[k] = matrix[k][dim+1]/matrix[k][k]

    if None in solution:
        raise Exception("Tidak ada Solusi")
    return solution


def find_determinant(matrix, pivot=False):
    """
    Fungsi ini mencari determinan pada matrix yang belum di eliminasi

    Note: 
    * Gunakan ini hanya pada matrix belum di eliminasi
    * Tambahkan argumen True di argumen kedua untuk mengunakan metode pivot contoh solve(matrix,True)
    """
    if pivot:
        eliminate()
    else:
        eliminate_pivot()
    det = 1
    for i in range(row):
        det = det*matrix[i][i]

    determinant = det

    return det


def solve(matrix, pivot=False):
    """
    Fungsi ini mencari solusi pada matrix yang belum di eliminasi
    dengan menjalankan fungsi eliminate kemudian penyulihan mundur

    Akan menghasilkan solusi 

    Note: 
    * Gunakan ini hanya pada matrix belum di eliminasi
    * Tambahkan argumen True di argumen kedua untuk mengunakan metode pivot contoh solve(matrix,True)
    """
    if pivot:
        eliminate_pivot(matrix)
    else:
        eliminate(matrix)
    return backwards(matrix)


print(solve(matrix))

for i in range(len(solution)):
    print(f"x{i}=", solution[i])
