from django.shortcuts import render, redirect

# Create your views here.


def start(request, exception=None):
  return redirect('/dashboard')


def page_not_found_view(request, exception=None):
  return redirect('/dashboard')


def error_view(request, exception=None):
  return redirect('/dashboard')


def permission_denied_view(request, exception=None):
  return redirect('/dashboard')


def ad_request_view(request, exception=None):
  return redirect('/dashboard')
