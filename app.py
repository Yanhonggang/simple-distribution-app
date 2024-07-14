from flask import Flask, request, render_template, jsonify
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    mean = data.get('num1')
    std_dev = data.get('num2')

    # Generate x values
    x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 100)
    # Calculate the normal distribution
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

    # Create a plot with a specified size
    plt.figure(figsize=(8, 4))  # Set the size of the plot
    plt.plot(x, y, label='Normal Distribution')
    plt.title('Normal Distribution (mean={}, std dev={})'.format(mean, std_dev))
    plt.xlabel('X-axis')
    plt.ylabel('Probability Density')
    plt.legend()

    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close()

    # Encode the image in base64
    plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
    
    return jsonify({'plot_url': plot_url})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
