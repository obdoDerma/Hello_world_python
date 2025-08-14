from flask import Flask
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/plot')
def plot():
    # Generate the plot
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.title("A Simple Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # Save the plot to a temporary in-memory buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    
    # Encode the image to base64
    plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # Return the image embedded in an HTML tag
    return f"""
    <html>
        <body>
            <h1>Your Python Sketch</h1>
            <img src="data:image/png;base64,{plot_data}" />
        </body>
    </html>
    """

if __name__ == '__main__':
    # This line starts the web server
    app.run(debug=True, host='0.0.0.0', port=5000)
