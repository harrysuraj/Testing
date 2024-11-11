
from my_math import square

def test_square():
    # Arrange
    number = 5
    
    # Act
    result = square(number)
    
    # Assert
    assert result == 25, f"Expected 25 but got {result}"
