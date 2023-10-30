from  .  import views
from django.urls import path

urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('logout/',views.logout,name='logout')

]
# def login(request):
#     if request.method =='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(user=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,"Invalid credentials ")
#             return redirect('login')
#     return render(request,"login.html")
