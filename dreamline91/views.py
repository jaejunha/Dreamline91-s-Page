# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import subprocess

def index(request):
	return render(request,'index.html')

def home_frame(request):
	return render(request,'home/frame.html')

def home_intro(request):
	return render(request,'home/intro.html')

def home_favorite(request):
	return render(request,'home/favorite.html')

def home_activity(request):
	return render(request,'home/activity.html')

def about(request):
	f = open('static/personal/txt/history.txt','r')
	data = []
	while True:
		line = f.readline()
		data.append(line)
		if not line:
			break
	f.close()
	return render(request,'about/about.html', {'data': data})

def education(request):
	f = open('static/personal/txt/education.txt','r')
	data = []
	while True:
		line = f.readline()
		data.append(line)
		if not line:
			break
	f.close()
	return render(request,'education/education.html', {'data': data})

def local(request):
	p = subprocess.Popen('C:\\Windows\\EXPLORER.EXE /n /cwd="D:\\GitHub"')
	p.wait()
	return null