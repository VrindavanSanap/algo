class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        original_color = image[sr][sc]
        if original_color == color:
            return image

        self._flood_fill(image, sr, sc, color, original_color)
        return image

    def _flood_fill(self, image, r, c, color, original_color):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color:
            return

        image[r][c] = color
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            self._flood_fill(image, r + dr, c + dc, color, original_color)


image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
sr = 1
sc = 1
color = 2

s = Solution()
s.floodFill(image, sr, sc, color)
print(np.matrix(image))