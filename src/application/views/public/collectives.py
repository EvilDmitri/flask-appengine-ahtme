# -*- coding: utf-8 -*-

from flask.views import View

from flask import flash, redirect, url_for, render_template

from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from forms import ExampleForm
from models import ExampleModel

from decorators import login_required


class Antares(View):
    def dispatch_request(self):
        examples = ExampleModel.query()
        collective = {'name': 'Антарес'}
        return render_template('collectives/collective.html', examples=examples, collective=collective)


class Arlekin(View):
    def dispatch_request(self):
        examples = ExampleModel.query()
        collective = {'name': 'Арлекин'}
        return render_template('collectives/collective.html', examples=examples, collective=collective)


class Step(View):
    def dispatch_request(self):
        examples = ExampleModel.query()
        collective = {'name': 'Степ студия'}
        return render_template('collectives/collective.html', examples=examples, collective=collective)


class Viva(View):
    def dispatch_request(self):
        examples = ExampleModel.query()
        collective = {'name': 'Viva Dance'}
        return render_template('collectives/collective.html', examples=examples, collective=collective)


class Smirnov(View):
    def dispatch_request(self):
        examples = ExampleModel.query()
        collective = {'name': 'Павел Смирнов'}
        return render_template('collectives/collective.html', examples=examples, collective=collective)
