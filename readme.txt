1. Problem Set 1 REGEX Solustion is in find regex in orange highlighter python file uploaded in repository project root folder.


2. Problem set 2 A Functioning Web App With API

	1. I have Developed a custom Admin Interface, didn't used any in built aur 3rd party package for it.
	
	2. All the Admin related Views are in Views.py file and i have used function based views for it.

	3. There are two model in Admin face componente AdminUser & Apps, AdminUser has one to many relationship with Apps.

	4. I have used Django.contrib.auth app for User facing interface.

	5. I have Used default Login & Logout view with redirection and every other User facing views are in userviews.py file.

	6. User facing Component has two models auth_user and AppsDownloaded.

	7. auth_user and Apps models have many to many relationship with Appsdownloaded model.

	8. All the Apps model related Api views are in apiviews.py file and only registered admin users are allow to perform Create, update and delete operations on it.
	
	9. A python script to review Api functioning is given in app api.py python file uploaded in git repository inside project root folder.


3. Problem set 3

	A. Write and share a small note about your choice of system to schedule periodic
	   tasks (such as downloading a list of ISINs every 24 hours). Why did you choose it? Is it
	   reliable enough; Or will it scale? If not, what are the problems with it? And, what else
	   would you recommend to fix this problem at scale in production?


	Ans: I think celery beat is best for sheduling periodic tasks.
	     
	     As you build and scale a Django app you'll inevitably need to run certain tasks periodically and automatically in the background.

	     some examples:

	     Generating periodic reports
           Clearing cache
           Sending batch e-mail notifications
           Running nightly maintenance jobs
           This is one of the few pieces of functionality required for building and scaling a web app that isn't part of the Django core. 
	     Fortunately, Celery provides a powerful solution, which is fairly easy to implement called Celery Beat.
	     
	    Celery beat is a python task scheduling module. It performs specified tasks at regular intervals irrespective of any other process/event occurring. 
          Celery is compatible with Django since it provides many predefined methods for executing asynchronously as well as synchronously tasks on schedule as well as periodically.	     

	    I chose it because Celery modules Periodic Task functionality allows developers to automate repetitive tasks from within a Django project.
	     Once you integrate Celery into your app, you can send time-intensive tasks to Celery’s task queue. That way, your web app can continue to respond quickly to users while Celery completes expensive operations asynchronously in the background.

	    There are multiple ways to schedule tasks in your Django app, but there are some advantages to using Celery. It’s supported, scales well, and works nicely with Django.


	B. In what circumstances would you use Flask instead of Django and vice versa?

	Ans: Django and Flask are the web frameworks of Python. As we know, Python is the most versatile programming language which provides a wide range of web framework. 
	     A web developer has the option to choose from these frameworks. 
	     A programmer has the flexibility to take advantage of the full-stack Python web frameworks. 
	     It enhances the development of complex web applications. 
	     Python also provides an option to choose for micro and lightweight Python web frameworks to build simple web applications without putting extra time and effort.

	     You should prefers flask if you want the granular level of control while a Django developer relies on an extensive community to create unique website.
	     Django combined with the REST Framework helps you to build powerful APIs, whereas Flask requires more work, so there are high chances to make a mistake.
	     It is also depends on project requirements and it's dependencies to chose which framework is better for that specific application.
	     we should use flask if we want to use third party packages to develeop an custom interface with our own choice of vast available python libraries or packages.
	     if we need to develop a Complicated application which need lots of internal implemaintation then Django is best as it includes most of the pre installed apps which a developer might need to develop an application.
	     I think the best way to decide is to build a prototype project with both frameworks and decide which framework fits your project style better.


