from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    wordsdictionary = {}

    for word in wordlist:
        if word in wordsdictionary:
            wordsdictionary[word] += 1
        else:
            wordsdictionary[word] = 1

    sorteddict = sorted(wordsdictionary.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'count.html', {'fulltext':fulltext, 'words':len(wordlist), 'dictionaries':sorteddict})

def about(request):
    return render(request, 'about.html')