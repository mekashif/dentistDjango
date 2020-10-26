from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		
		#Sending Email

		send_mail(
			message_name,#subject
			message,#message
			message_email,#from email
			['mekashifk@gmail.com'],#to email
			)	
		return render(request, 'contact.html', {'message_name': message_name})

	else:	
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {})

def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone'] 
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_scheldule = request.POST['your-scheldule']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message']
		
		
		#Sending Email
		appointment = "Your Name" + your_name + " Your Phone Number"  + your_phone + " Your Email " + your_email + " Your Address " + your_address + " Your Schedule " + your_scheldule + " Your Time " + your_time + "Your Message " +  your_message


		send_mail(
			'Appintment Message',#subject
			appointment,#message
			your_email,#from email
			['mekashifk@gmail.com'],#to email
			)	
			
		return render(request, 'appointment.html',{
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_scheldule': your_scheldule,
			'your_time': your_time,
			'your_message': your_message
			})

	else:	
		return render(request, 'contact.html', {})