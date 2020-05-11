from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request , 'Home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordcount= fulltext.split()
    sentence = "there are about " + str(len(wordcount)) + " words in your textbox"
    words = dict()
    for each in wordcount:
        if each not in words:
            words[each] = 1
        else:
            words[each] += 1
    sortedWords = sorted(words.items(),key=operator.itemgetter(1),reverse=True)
    return render(request, "count.html",{'sentence':sentence,"words":sortedWords})

def about(request):
    return render(request, "about.html")
