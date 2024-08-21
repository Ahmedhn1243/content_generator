from django.shortcuts import render
from .models import Content
import pdfkit
import openai
from django.conf import settings





openai.api_key = settings.OPENAI_API_KEY

def generate_content(request):
    if request.method == 'POST':
        topic = request.POST['topic']
        tone = request.POST['tone']

        # Generate the prompt using the topic and tone
        prompt = f"Write a haiku about {topic} in a {tone} tone."

        # Use the correct model name 'gpt-4'
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt},
            ]
        )

        # Extract the generated content from the response
        content = response['choices'][0]['message']['content']
        
        return render(request, 'result.html', {'content': content})
    
    return render(request, 'home.html')





def export_to_pdf(content):
    pdf = pdfkit.from_string(content.body, False)
    return pdf

# Create your views here.
