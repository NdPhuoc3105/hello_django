from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# tasks = ['foo', 'bar', 'baz']

# New Task Django Form:
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):

    # Check if there already exists a 'tasks' key in our session

    if 'tasks' not in request.session:

        # if not, create a new list
        request.session['tasks'] = []

    return render(request, 'tasks/index.html', {
        'tasks': request.session['tasks']
    })

def add(request):

    # Check if method is POST
    if request.method == 'POST':

        # take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)

        # check if form data is valid (server-side)
        if form.is_valid():

            # isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data['task']

            # add the new task to our list of tasks
            request.session['tasks'] += [task]

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse('tasks:index'))
        
        else:
            # if the form is invalid, re-render the page with existing information
            return render(request, 'tasks/add.html', {
                'form': form
            })

    return render(request, 'tasks/add.html', {
        'form': NewTaskForm()
    })