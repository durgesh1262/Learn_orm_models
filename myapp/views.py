from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q
from datetime import date , time
from django.db.models import Avg, Sum, Min, Max, Count

def orm(request):
    # student_data = Student.objects.all()

    #student_data = Student.objects.exclude(marks=70)

    # student_data = Student.objects.order_by('name')
    # student_data = Student.objects.order_by('-name')
    # student_data = Student.objects.order_by('?') ? for randam data
    # student_data = Student.objects.order_by('marks').reverse()[ :3] its use slicing also

    # student_data = Student.objects.views()
    # student_data = Student.objects.values('name', 'marks')

    # student_data = Student.objects.values_list()
    #student_data = Student.objects.values_list('name', 'marks', named = True , flat=False) both parameter not give together

    # student_data = Student.objects.using('defult') we can use multipal datadases

    # student_data = Student.objects.dates('month')
    # student_data = Student.objects.datetimes('month')

    # student_data = Student.objects.none() it will give no objects, no data will appears in table [empty quaryset]

 ###########################################################################################################################
    #  qs1 = Student.objects.values_list('name', named = True)
    #  qs2 = Teacher.objects.values_list('name', named = True)
    #  student_data = qs2.union(qs1, all= True) it will give both tables data but  not redundent data 
    # if do all=true so give redendet data


    #  qs1 = Student.objects.values_list('name', named = True)
    #  qs2 = Teacher.objects.values_list('name', named = True)
    #  student_data = qs1.intersection(qs2) display data will same in both table

    #  qs1 = Student.objects.values_list('name', named = True)
    #  qs2 = Teacher.objects.values_list('name', named = True)
    #  student_data = qs1.intersection(qs2) display data will not same in both table

#########################################################operators##################################
    # AND(&)-> combine to quary set using the  sql AND opater. sign &

    # student_data =  Student.objects.filter(id=2) & Student.objects.filter(name = 'durgesh')
    # student_data = Student.objects.filter(Q(id=2) & Q(name= 'durgesh'))
    # student_data = Student.objects.filter(Q(id=2) | Q(name= 'durgesh')) or opertor

################################################### FIELF LOOKUP(WHERE CLOUSE) ######################################  

    # student_data = Student.objects.filter(name__exact='durgesh') its case sensitive
    # student_data = Student.objects.filter(name__iexact='DURGESH')its not case sensitive
    # student_data = Student.objects.filter(name__contains='u') u containt all the names are show in the table and case sencitive
    # student_data = Student.objects.filter(id__in=[2,3,4]) it gives the data in this id
    # student_data = Student.objects.filter(marks__in=[60,70]) it gives the data in these marks
    # student_data = Student.objects.filter(marks__gt=60) gt -> grater then
    # student_data = Student.objects.filter(marks__gte=60) gte -> grater then and equal
    # student_data = Student.objects.filter(marks__lt=60) lt -> less then
    # student_data = Student.objects.filter(marks__lte=60) lte -> less then and equal 
    # student_data = Student.objects.filter(name__startswith = 'S') case sensitive
    # student_data = Student.objects.filter(name__istartswith = 's') not case sensitive but dipend on database
    # student_data = Student.objects.filter(name__endswith = 'A') case sensitive
    # student_data = Student.objects.filter(name__iendswith = 'A') not case sensitive but dipend on database
    # student_data = Student.objects.filter(marks__range=('50', '80')) it shows marks between 50 to 80

    # student_data = Student.objects.filter(pass_date__range=('2020-04-01', '2020-05-05')) only work on date time field need to import date time 
    # in date time lookup fielsd we use multiple lookup field like
    #student_data = Student.objects.filter(marks__range__gt=('50', '80'))
    # student_data = Student.objects.filter(marks__isnull=False)  if its true no data apiar on the table

########################################### AGGREGATION FUNTIONS ##############################################    

   student_data = Student.objects.all()
   average = student_data.aggregate(Avg('marks'))
   addition = student_data.aggregate(Sum('marks'))
   minimum = student_data.aggregate(Min('marks'))
   maximum = student_data.aggregate(Max('marks'))
   totalcount = student_data.aggregate(Count('marks'))
   context = {'student':student_data,'average':average, 'addition': addition,
   'minimum':minimum, 'maximum':maximum, 'totalcount':totalcount }
#    print(avg)
#    print('Return:', student_data)
#    print('SQL Query:', student_data.Query)


    


   return render(request, 'home.html', context)


