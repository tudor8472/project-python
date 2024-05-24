from django.shortcuts import render, HttpResponse, HttpResponseRedirect,redirect
from .models import ToDoList, Item,JournalEntry
from .forms import CreateNewList
from .forms import JournalEntryForm

def index(response, id):
    ls = ToDoList.objects.get(id = id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text = txt, complete = False)
            else:
                print("Invalid")


    return render(response, "main/list.html", {"ls" : ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()
            response.user.todolist.add(t)
            
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form" : form})

def default(response):
    return render(response, "main/default.html")

def view(response):
    return render(response, "main/view.html", {})

def entry_list(request):
    entries = JournalEntry.objects.filter(user=request.user)
    return render(request, 'main/entry_list.html', {'entries': entries})

def add_entry(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('entry_list')
    else:
        form = JournalEntryForm()
    return render(request, 'main/add_entry.html', {'form': form})


def info_dozare(request):
    return render(request, 'main/info_dozare.html')

def resurse_medicale(request):
    return render(request, 'main/resurse_medicale.html') 
