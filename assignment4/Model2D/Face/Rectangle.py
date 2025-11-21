from .Face import Face
from ..Line import Line

class Rectangle(Face):
    def __init__(self, id: int, lines: list[Line]):
        super().__init__(id, lines)

        # Ensure there are exactly 4 lines in the list
        if len(lines) != 4:
            raise RuntimeError('Rectangle must have exactly 4 lines')

        # Check if all 4 lines are connected (i.e., the end of each line connects to the next)
        if not self._are_lines_connected():
            raise RuntimeError('All lines must be connected')
        
        # Validate that opposite lines are parallel
        if not self._are_opposite_lines_parallel():
            raise RuntimeError('Opposite lines of the rectangle must be parallel')

        # Validate that two consecutive lines are perpendicular
        if not self._are_consecutive_lines_perpendicular():
            raise RuntimeError('Consecutive lines of the rectangle must be perpendicular')
        
        # Ensure the last line connects back to the first line
        if not self._is_last_line_connected_to_first():
            raise RuntimeError('Last line must connect back to the first line')

    def __str__(self) -> str:
        return f"Rectangle(id={self.id}, lines={self.lines})"

    def area(self):
        # The area of a rectangle is length * width
        length = self.lines[0].length()  # Assuming lines[0] and lines[2] are parallel
        width = self.lines[1].length()   # Assuming lines[1] and lines[3] are parallel
        return length * width

    def _are_lines_connected(self):
        # Check if each line is connected to the next one
        for i in range(4):
            p1 = self.lines[i].points[1]  # End of current line
            p2 = self.lines[(i + 1) % 4].points[0]  # Start of next line
            if p1 != p2:
                return False
        return True

    def _are_opposite_lines_parallel(self):
        # Check if opposite lines (0-2 and 1-3) are parallel
        line1_dir = self.lines[0].direction()
        line2_dir = self.lines[2].direction()
        # Compare direction vectors with tolerance for floating point precision
        tolerance = 1e-6
        return (abs(line1_dir[0] - line2_dir[0]) < tolerance and
                abs(line1_dir[1] - line2_dir[1]) < tolerance)

    def _are_consecutive_lines_perpendicular(self):
        # Check if consecutive lines are perpendicular (dot product == 0)
        for i in range(4):
            line1_dir = self.lines[i].direction()
            line2_dir = self.lines[(i + 1) % 4].direction()
            dot_product = line1_dir[0] * line2_dir[0] + line1_dir[1] * line2_dir[1]
            # If the dot product is close to 0, the lines are perpendicular
            if abs(dot_product) > 1e-6:
                return False
        return True

    def _is_last_line_connected_to_first(self):
        # Ensure the last line connects back to the first line
        p1 = self.lines[3].points[1]  # End of last line
        p2 = self.lines[0].points[0]  # Start of first line
        return p1 == p2
