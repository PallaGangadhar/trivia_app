from django.shortcuts import render, HttpResponse
from trivia_app.models import *
from django.shortcuts import redirect

# Create your views here.

def homepage(request):
    """ Store player name """
    if request.method == 'POST':
        
        name_saved = Person.objects.create(name=request.POST['name'])
        name_saved.save()
        return redirect('select_cricketer', pk=name_saved.id)
    return render(request, 'trivia_app/index.html',{}, status=200)

def select_cricketers(request,pk):
    """ Save crcketers name  """
    players = FavPlayer.objects.all()
    if not players:
        return redirect('homepage')
    
    else:
        if request.method == 'POST':
            try:
                person_object = Person.objects.get(id=pk)
                player_obj = FavPlayer.objects.get(id=request.POST['cricketers'])
                cricketers_name = BestCrickter.objects.create(fav_player=player_obj,person=person_object)
                cricketers_name.save()
                return redirect('select_flag_colors', pk=pk)
            except:
                return render(request, 'trivia_app/select_cricketer.html',{'msg':'Please select cricketrs','players_list':players})
    return render(request, 'trivia_app/select_cricketer.html', {'players_list':players})

def select_flag_colors(request,pk):
    """ Save Flag Colors  """
    error_msg = ''
    colors = Color.objects.all()
    try:
        if request.method == 'POST':
            person_object = Person.objects.get(id=pk)
            colors = request.POST.getlist('colors[]')
            if len(colors) == 0:
                error_msg = 'Please select one or more colors'
            else:
                for color in colors:
                    flag_object = Color.objects.get(id=color)
                    flag_color = IndianFlagcolor.objects.create(color=flag_object, person=person_object)
                    flag_color.save()
            return redirect('summary', pk=pk)
    except:
        return render(request, 'trivia_app/select_flag_color.html',{'error_msg':error_msg, 'colors':colors}, status=500)

    return render(request, 'trivia_app/select_flag_color.html',{'error_msg':error_msg, 'colors':colors})

def summary(request,pk):
    """ Show selected answer details for a person """
    try:
        person_object = Person.objects.get(id=pk)
        best_cricketer = BestCrickter.objects.get(person_id=pk)
        colors = IndianFlagcolor.objects.filter(person_id=pk)
    except:
        return render(request, 'trivia_app/summary.html',{'msg','No summary for the player'}, status=404)

    return render(request, 'trivia_app/summary.html',{'answer_details':person_object,'best_cricketer':best_cricketer,'colors':colors})

def history(request):
    """ Show all details of each person related data """
    
    persons_details = Person.objects.all()
    
    if not persons_details:
        return render(request, 'trivia_app/history.html',{'msg':'No History Found'},status=404)
    return render(request, 'trivia_app/history.html',{'persons_details':persons_details})

# def players_list(request):
    