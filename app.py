from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Initialize the Gemini model with API key and model ID
API_KEY = ""  # Replace with your actual API key
MODEL_ID = "tunedModels/xdata-32hdxri8pmum"  

# Set the API key for the Generative AI library
genai.configure(api_key=API_KEY) 
model = genai.GenerativeModel(MODEL_ID)

# Route to render the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Route for inference, accepts form data from POST request
@app.route('/inference', methods=['POST'])
def run_inference():
    input_text = request.form.get("input_text")

    # Generate content using the Gemini model
    try:
        response = model.generate_content(input_text)
        model_output = response.text
    except Exception as e:
        # Handle any exceptions that occur during content generation
        return jsonify({"error": f"Failed to generate content: {e}"}), 500

    # Render the form with the model response
    return render_template('index.html', model_response=model_output)

if __name__ == '__main__':
    app.run(debug=True)
