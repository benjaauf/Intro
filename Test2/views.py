from django.shortcuts import render
from .forms import Test2


def test2(request):
	f = Test2()
	return render(request,'test2.html',{'form': f})
