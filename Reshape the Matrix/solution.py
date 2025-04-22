class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        flatten = []
        for row in mat:
            for num in row:
                flatten.append(num)
        
        res = []
        for i in range(r):
            row = flatten[i * c: i * c + c]
            res.append(row)

        return res