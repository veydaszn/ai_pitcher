from flask import Flask, request, render_template
import openai, os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        idea = request.form["idea"]
        prompt = f"""
        Analyze this startup idea: "{idea}"
        Give me:
        1. Summary
        2. Market demand
        3. Monetization
        4. SWOT
        5. Competitors
        6. Success score (1–10)
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content.strip()
    return render_template("index.html", output=result)

if __name__ == "__main__":
    app.run(debug=True)
