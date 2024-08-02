def count_right_triangles(grid):
    rows = len(grid)
    cols = len(grid[0])
    row_counts = [sum(row) for row in grid]
    col_counts = [sum(grid[row][col] for row in range(rows)) for col in range(cols)]
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # 计算以 (i, j) 为直角点的直角三角形数量
                # 可以选择的行数 * 可以选择的列数
                # 减去当前行和当前列中已经选择的 1（即 row_counts[i] - 1 和 col_counts[j] - 1）
                # 再减去当前元素本身
                count += (row_counts[i] - 1) * (col_counts[j] - 1)

    return count

# 示例
grid = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]

print(count_right_triangles(grid))  # 输出: 3
