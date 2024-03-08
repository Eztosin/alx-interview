#!/usr/bin/python3

def pascal_triangle(n):
    """implementing Pascal’s Triangle in Python"""
    if n <= 0:
        return []

    pas_tri = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = pas_tri[i - 1]
                prev_val_l = prev_row[j - 1] if j - 1 < len(prev_row) else 0
                prev_val_r = prev_row[j] if j < len(prev_row) else 0
                row.append(prev_val_l + prev_val_r)
        pas_tri.append(row)
    return pas_tri
