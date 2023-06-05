from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer
from .models import Person
import fasttext
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import schedule
import time
import threading

import requests

words = []
model1 = fasttext.load_model(r"C:\Users\LENOVO\Desktop\Using AI to prevent mental"
                            r" illness\Psybot1.1\backend\auth_sys\api\models\depression-model.bin")

model2 = fasttext.load_model(r"C:\Users\LENOVO\Desktop\Using AI to prevent mental"
                            r" illness\Psybot1.1\backend\auth_sys\api\models\suicide-model.bin")

model3 = fasttext.load_model(r"C:\Users\LENOVO\Desktop\Using AI to prevent mental"
                            r" illness\Psybot1.1\backend\auth_sys\api\models\cyberbullying-model.bin")


def graph_task(person):
    import ast

    def graph():
        graph_home = ast.literal_eval(
            person.graph_home) if person.graph_home else []  # Convert the string to a list or initialize an empty list
        graph_home.append((((person.depressive + person.suicide + person.cyberbullying) / 3) * 100) / person.total)
        person.graph_home = str(graph_home)  # Convert the list back to a string representation with proper formatting

        graph_dep = ast.literal_eval(person.graph_dep) if person.graph_dep else []
        graph_dep.append((person.depressive * 100) / person.total)
        person.graph_dep = str(graph_dep)

        graph_sui = ast.literal_eval(person.graph_sui) if person.graph_sui else []
        graph_sui.append((person.suicide * 100) / person.total)
        person.graph_sui = str(graph_sui)

        graph_cyb = ast.literal_eval(person.graph_cyb) if person.graph_cyb else []
        graph_cyb.append((person.cyberbullying * 100) / person.total)
        person.graph_cyb = str(graph_cyb)

        person.save()
        print("done")

    # Schedule the graph function to run every 3 seconds
    schedule.every(5).minutes.do(graph)

    # Continuously run the schedule
    while True:
        schedule.run_pending()
        time.sleep(1)


@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_person(request):
    name = request.data.get('name')
    texts = request.data.get('texts')
    time = request.data.get('time')

    # Try to get the person with the given name
    try:
        if name != '':
            person = Person.objects.get(name=name)

    except Person.DoesNotExist:
        # If the person does not exist, create a new one
        person = Person(name=name)
        person.save()

    # Iterate through the texts and update the prediction fields
    for text in texts:
        label1, prediction1 = model1.predict(text)[0][0], model1.predict(text)[1][0]
        label2, prediction2 = model2.predict(text)[0][0], model2.predict(text)[1][0]
        label3, prediction3 = model3.predict(text)[0][0], model3.predict(text)[1][0]

        if label1 == '__label__depression':
            person.depressive += prediction1

        if label2 == '__label__suicide':
            person.suicide += prediction2

        if label3 != '__label__not_cyberbullying':
            person.cyberbullying += prediction3

        person.total += 1

    person.time += (time / 3600)

    # Save the person to the database
    person.save()
    threading.Thread(target=graph_task, args=(person,), daemon=True).start()
    print("done 222222")

    # Return the serialized person
    serializer = PersonSerializer(person)
    return Response(serializer.data, status=201)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_person_data(request, name):
    # Query the database for the person with the given name
    person = get_object_or_404(Person, name=name)

    # Serialize the person data
    serializer = PersonSerializer(person)

    # Return the serialized data in the response
    return Response(serializer.data)


