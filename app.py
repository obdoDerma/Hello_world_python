import base64

def generate_simple_diagram():
    """Generates a simple black and white pixel image as a base64 string."""
    # A simple 8x8 pixel image (8 rows, 8 columns)
    # 0 = black, 1 = white
    # This represents a simple diagonal line
    pixels = [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1]
    ]

    # Simple PGM header for a black-and-white image
    header = "P2\n8 8\n1\n"
    pixel_data = " ".join([str(p) for row in pixels for p in row])
    
    image_data = f"{header}{pixel_data}".encode('utf-8')
    return base64.b64encode(image_data).decode('utf-8')

if __name__ == '__main__':
    # Print the base64-encoded image data
    print(generate_simple_diagram())
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
