from django.shortcuts import render
from .models import QueryLog
from .serializers import RequestSerializer, ResponseSerializer, QuerySerializer
import os
import json
from dotenv import load_dotenv
from google import genai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=GOOGLE_API_KEY)


ACTIONS = {
    "ORDER_FOOD": "Order food online",
    "FIND_RECIPE": "Find food recipes",
    "ASK_HELP": "Ask for assistance",
}

def suggest_actions(tone, intent):
    suggestions = []

    if intent.lower() == "order food":
        suggestions.append({"action_code":"ORDER_FOOD", "display_text":ACTIONS["ORDER_FOOD"]})
        suggestions.append({"action_code":"FIND_RECIPE", "display_text":ACTIONS["FIND_RECIPE"]})
    elif intent.lower() == "receive assistance":
        suggestions.append({"action_code":"ASK_HELP", "display_text":ACTIONS["ASK_HELP"]})
    else:
        suggestions.append({"action_code":"ASK_HELP", "display_text":ACTIONS["ASK_HELP"]})
    
    return suggestions[:3]



class AnalyzeView(APIView):
    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data['query']
            prompt = f"Analyze this message '{query}'. What is the tone (e.g., Happy, Urgent)? What is the intent like Order Food, or Receive Assistance etc like if the message is 'i am hungry' or 'i want any food' give intent as 'Order Food'? Reply as JSON. "
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=[prompt]
                )
                data = response.text  

                json_str = data.split('```json')[1].split('```')[0].strip()
                content = json.loads(json_str)
                tone = content["tone"]
                intent = content["intent"]
                suggestions = suggest_actions(tone, intent)

                QueryLog.objects.create(
                    query=query,
                    tone=tone,
                    intent=intent,
                    suggestions=suggestions
                )

                return Response({
                    "query": query,
                    "analysis": {
                        "tone": tone,
                        "intent": intent
                    },
                    "suggestions": suggestions
                })

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



