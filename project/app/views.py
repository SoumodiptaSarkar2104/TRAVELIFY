from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import userdata
from django.shortcuts import redirect
from .form import ImageForm
from .models import Image
import os
from .models import picfile


# Create your views here.

import requests
from django.shortcuts import render
from django.http import JsonResponse

def hotel_search(request):
    if request.method == 'GET':
        # Render the initial search page
        return render(request, 'hotel_search.html')

import requests
from django.shortcuts import render
from django.http import JsonResponse

# View to render the hotel search page (hotel.html)
def hotel_search(request):
    if request.method == 'GET':
        # Render the hotel.html template
        return render(request, 'hotel.html')

# View to fetch hotel data from SerpApi
def fetch_hotels(request):
    if request.method == 'GET':
        # Get the search parameters from the request (e.g., from the URL)
        search_query = request.GET.get('q', '')
        check_in_date = request.GET.get('check_in_date', '')
        check_out_date = request.GET.get('check_out_date', '')
        adults = request.GET.get('adults', '2')
        currency = request.GET.get('currency', 'USD')

        # SerpAPI URL and API Key (replace 'YOUR_API_KEY' with your actual key)
        api_key = '09049a6d636459450583a07aef71ce427f69a6e72fc83b1e9bd81da428292ba1'
        url = f'https://serpapi.com/search?engine=google_hotels&q={search_query}&check_in_date={check_in_date}&check_out_date={check_out_date}&adults={adults}&currency={currency}&gl=us&hl=en&api_key={api_key}'

        try:
            # Send a GET request to the SerpAPI endpoint
            response = requests.get(url)
            data = response.json()  # Parse the JSON response
            return JsonResponse(data)  # Return data as JSON response
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)


def home(request):
  return render(request,'home.html')
def list(request):
  return render(request,'list.html')
def form(request):
  return render(request,'form.html')

def reg(request):
  u=userdata()
  u.Name=request.POST.get('Name')
  u.DOB=request.POST.get('a2')
  u.Email=request.POST.get('a3')
  u.Contact=request.POST.get('a4')
  u.Place=request.POST.get('a5')
  u.Gender=request.POST.get('a6')
  u.Country=request.POST.get('a7')
  u.Password=request.POST.get('a8')
  u.save()
  return render(request,'form.html')
def login(request):
    return render(request,'login.html')
def log(request):
    a= request.POST.get('b1')
    b=request.POST.get('b2')
    if userdata.objects.filter(Email=a,password=b):
        return render(request,'index.html')
    else:
        return redirect('../login.html')
def index(request):
    return render(request,'index.html')
def hotel(request):
    return render(request,'hotel.html')
def display(request):
    a=userdata.objects.all()
    return render(request,'display.html',{'x':a})
def editdata(request,id):
    d=userdata.objects.get(id=id)
    return render(request,'editdata.html',{'x':d})
def edit(request,id):
    d=userdata.objects.get(id=id)
    d.Name=request.POST.get('Name')
    d.DOB=request.POST.get('a2')
    d.Email=request.POST.get('a3')
    d.Contact=request.POST.get('a4')
    d.Place=request.POST.get('a5')
    d.Gender=request.POST.get('a6')
    d.Country=request.POST.get('a7')
    d.Password=request.POST.get('a8')
    d.save()
    return redirect('../display')
def miniproject(request):
    return render(request,'miniproject.html')
def home(request):
 
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 return render(request, 'miniproject.html', {'img':img,'form':form})
def handle_upd(file,filename):
    if not os.path.exists('app/static/imageupload/'):
        os.mkdir('app/static/imageupload/')
    with open('app/static/imageupload/'+filename,'wb+') as dest:
        for c in file.chunks():
            dest.write(c)
def upd(request):
    if request.method=='POST':
        handle_upd(request.FILES['a1'],str(request.FILES['a1']))
        url="imageupload/"+str(request.FILES['a1'])
        u=picfile()
        u.pname=request.POST['b1']
        u.purl=url
        u.save()
        return redirect("../imageupload")

def imageupload(request):
    return render (request,'imageupload.html')
def delete(request, id):
    e = userdata.objects.get(id=id)
    e.delete()
    return redirect('../display')

import requests
from django.shortcuts import render
from django.http import JsonResponse

import requests
from django.shortcuts import render
from django.http import JsonResponse

def hotel_search(request):
    # Get query parameters from the form
    location = request.GET.get("location", "")
    check_in = request.GET.get("check_in", "")
    check_out = request.GET.get("check_out", "")
    adults = request.GET.get("adults", "2")
    rooms = request.GET.get("rooms", "1")
    currency = request.GET.get("currency", "USD")
    
    # Default page number
    page = int(request.GET.get("page", "0"))
    
    # Your Makcorps API Key (replace with your actual key)
    api_key = "67cbcd164e06c884d76a82c0"
    
    # Define the API URL template
    url_template = 'https://api.makcorps.com/citysearch/{cityname}/{page}/{currency}/{num_of_rooms}/{num_of_adults}/{check_in_date}/{check_out_date}'
    
    # Format the URL with actual parameters
    url = url_template.format(
        cityname=location,
        page=page,
        currency=currency,
        num_of_rooms=rooms,
        num_of_adults=adults,
        check_in_date=check_in,
        check_out_date=check_out
    )
    
    # Append the API key to the URL
    url_with_api_key = f"{url}?api_key={api_key}"
    
    # Make the API request
    response = requests.get(url_with_api_key)
    
    # Check the status code of the response
    if response.status_code == 200:
        try:
            # Parse the response as JSON
            data = response.json()
            
            hotels = []
            total_pages = 0
            if data.get("status") == "success":
                hotels = data.get("hotels", [])
                total_pages = data.get("total_pages", 0)
            else:
                # If the status is not success, log the error
                print("API Response Status is not 'success'.")
                print("Response Data:", data)
        except ValueError as e:
            # Handle JSON decoding error
            print(f"JSONDecodeError: {e}")
            print(f"Response content: {response.content.decode('utf-8')}")
            hotels = []
            total_pages = 0
    else:
        # If the API request failed, log the status code and message
        print(f"Error: Received a {response.status_code} status code from the API.")
        print("Error Message:", response.text)
        hotels = []
        total_pages = 0
    
    # Pass the data to the template for rendering
    return render(request, "hotel_search.html", {
        "hotels": hotels,
        "page": page,
        "total_pages": total_pages,
        "location": location,
        "check_in": check_in,
        "check_out": check_out,
        "adults": adults,
        "rooms": rooms,
        "currency": currency
    })
# restaurant_search/views.py
from django.shortcuts import render
import requests

def search_restaurants(request):
    if request.method == "POST":
        query = request.POST.get("location", "")
        if query:
            # Use HERE API for geocoding
            api_key = "M23fwn7Q4vKjieSrBYbOB_u2gIUwImAwCkw7-ybDxFY"
            url = f"https://geocode.search.hereapi.com/v1/geocode?q={query}&apiKey={api_key}"
            response = requests.get(url)
            data = response.json()

            if 'items' in data and len(data['items']) > 0:
                lat = data['items'][0]['position']['lat']
                lng = data['items'][0]['position']['lng']

                # Call a restaurant API using the lat/lng (e.g., Yelp, Google Places, etc.)
                # Placeholder API endpoint for restaurants (you should replace this)
                restaurant_url = f"https://api.yelp.com/v3/businesses/search?latitude={lat}&longitude={lng}&categories=restaurants"
                headers = {'Authorization': 'Bearer YOUR_YELP_API_KEY'}
                restaurant_response = requests.get(restaurant_url, headers=headers)
                restaurant_data = restaurant_response.json()
                
                return render(request, 'restaurant_search/results.html', {'restaurants': restaurant_data['businesses'], 'query': query})
            else:
                return render(request, 'restaurant_search/results.html', {'error': 'No results found for your location.'})
    
    return render(request, 'restaurant_search/search.html')

import openai
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

openai.api_key = settings.OPENAI_API_KEY  # Set the OpenAI API key from settings
def generate_itinerary(request):
    if request.method == 'POST':
        # Get user inputs (destination, duration, budget)
        destination = request.POST.get('destination')
        duration = request.POST.get('duration')
        budget = request.POST.get('budget')

        # Form the prompt based on the user input
        prompt = f"Create a tour itinerary for {destination} for {duration} days with a budget of {budget}. List activities, attractions, and any special recommendations."

        try:
            # Use the OpenAI API with the correct Completion method
            response = openai.Completion.create(
                model="gpt-3.5-turbo",  # You can use "gpt-4" if available for your account
                prompt=prompt,  # Direct prompt for itinerary generation
                max_tokens=500,  # Adjust for detailed responses
                temperature=0.7  # Control randomness (0.7 is a good balance)
            )

            # Extract the generated itinerary
            itinerary = response.choices[0].text.strip()

            # Return the generated itinerary as JSON
            return JsonResponse({"itinerary": itinerary})
        except Exception as e:
            return JsonResponse({"error": str(e)})

    # For GET request, render the input form page
    return render(request, 'generate_itinerary.html')
# views.py
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def reviews_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # Save the review to the database
            return redirect('reviews')  # Redirect to the same page to see the new review

    # Fetch all reviews to display them
    reviews = Review.objects.all().order_by('-created_at')
    form = ReviewForm()  # Initialize an empty form

    return render(request, 'reviews.html', {'reviews': reviews, 'form': form})


import json
import requests
from django.shortcuts import render
from django.http import JsonResponse

# IBM Watson Assistant credentials
WATSON_API_KEY = 'ygEAP1gccWhJx-S7vYIdLeokmLo_MbtjbnQKadkqykFG'
WATSON_URL = 'https://api.au-syd.assistant.watson.cloud.ibm.com/instances/de168c10-e86f-4244-bba0-c3a079cf0934'
WATSON_ASSISTENT_ID = 'f751300f-0b7f-4c1b-ad43-5cc5d2780caa'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {WATSON_API_KEY}'
}

# Create the Watson Assistant session
def create_watson_session():
    response = requests.post(WATSON_URL, headers=HEADERS)
    return response.json()['session_id']

# Send user input to Watson Assistant
def send_to_watson(session_id, user_input):
    watson_input = {
        'input': {'text': user_input}
    }
    response = requests.post(f"{WATSON_URL}/{session_id}/message", headers=HEADERS, json=watson_input)
    return response.json()

def index2(request):
    return render(request, 'index2.html')

def plan_itinerary(request):
    if request.method == 'POST':
        destination = request.POST['destination']
        duration = request.POST['duration']
        budget = request.POST['budget']

        # Create Watson session
        session_id = create_watson_session()

        # Send the input to Watson Assistant
        user_input = f"I am planning a trip to {destination} for {duration} days with a budget of {budget}."
        watson_response = send_to_watson(session_id, user_input)

        # Get Watson's response (the generated itinerary or plan)
        itinerary = watson_response['output']['text'][0]

        return render(request, 'planner/itinerary.html', {'itinerary': itinerary})

    return JsonResponse({'error': 'Invalid request'}, status=400)



from django.http import JsonResponse
from django.shortcuts import render
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from django.conf import settings

# Set up Watson Assistant client
authenticator = IAMAuthenticator(WATSON_API_KEY)
assistant = AssistantV2(
    version='2021-06-14',
    authenticator=authenticator
)
assistant.set_service_url(WATSON_URL)

def plan_itinerary(request):
    # Check if session_id exists in the session
    if 'session_id' not in request.session:
        # Create a new session if it doesn't exist
        response = assistant.create_session(
            assistant_id=WATSON_ASSISTENT_ID
        ).get_result()
        # Store the session_id in the Django session
        request.session['session_id'] = response['session_id']

    session_id = request.session['session_id']
    user_input = request.POST.get('input')

    # Send user input to Watson Assistant
    response = assistant.message(
        assistant_id=WATSON_ASSISTENT_ID,
        session_id=session_id,
        input={'text': user_input}
    ).get_result()

    return JsonResponse(response)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Reply

def comment_view(request):
    if request.method == 'POST' and 'description' in request.POST:
        description = request.POST.get('description')
        if description:
            Comment.objects.create(description=description)
            return redirect('comments')  # Redirect to avoid resubmission

    comments = Comment.objects.prefetch_related('replies').all().order_by('-timestamp')
    return render(request, 'comments.html', {'comments': comments})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('comments')

def reply_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST' and 'reply_description' in request.POST:
        description = request.POST.get('reply_description')
        if description:
            Reply.objects.create(comment=comment, description=description)
            return redirect('comments')

    return render(request, 'reply_form.html', {'comment': comment})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Message

def chat_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', 'Anonymous')  # Default to 'Anonymous' if no name is provided
        text = request.POST.get('text')
        if text:
            Message.objects.create(user_name=user_name, text=text)
            return redirect('chat')  # Redirect to avoid resubmission

    messages = Message.objects.all().order_by('-timestamp')  # Fetch messages in reverse chronological order
    return render(request, 'chat.html', {'messages': messages})

def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.method == 'POST':
        message.delete()
        return redirect('chat')

# Other views (comment_view, delete_comment, reply_comment) remain unchanged.
from django.shortcuts import render
from django.http import HttpResponse

def rental_form(request):
    if request.method == 'POST':
        duration = request.POST.get('duration')
        license = request.POST.get('license')
        budget = request.POST.get('budget')
        persons = request.POST.get('persons')
        driver_needed = request.POST.get('driver_needed')

        response = f"""
            <h1>Rental Details</h1>
            <p>Duration: {duration} days</p>
            <p>License: {license}</p>
            <p>Budget: {budget} INR</p>
            <p>Number of Persons: {persons}</p>
            <p>Driver Needed: {driver_needed}</p>
        """
        return HttpResponse(response)
    return render(request, 'rental_form.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import RentalSubmission

def rental_form(request):
    if request.method == 'POST':
        duration = request.POST.get('duration')
        license = request.POST.get('license')
        budget = request.POST.get('budget')
        persons = request.POST.get('persons')
        driver_needed = request.POST.get('driver_needed')

        # Save to database
        submission = RentalSubmission(
            duration=duration,
            license=license,
            budget=budget,
            persons=persons,
            driver_needed=driver_needed
        )
        submission.save()

        # Pass data to the template
        context = {
            'duration': duration,
            'license': license,
            'budget': budget,
            'persons': persons,
            'driver_needed': driver_needed
        }
        return render(request, 'submit_form.html', context)
    return render(request, 'rental_form.html')
