# -*- coding: utf-8 -*-

from flask.views import View

from flask import flash, redirect, url_for, render_template

from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from forms import ExampleForm
from models import ExampleModel

from decorators import login_required

from google.appengine.ext import blobstore
import cloudstorage as gcs


def list_bucket(collective):
    """Create several files and paginate through them.

    Production apps should set page_size to a practical value.

    Args:
    bucket: bucket.
    """
    bucket = '/ahtme-music/' + collective

    page_size = 10
    stats = gcs.listbucket(bucket, max_keys=page_size)
    print '---------------------- stats'

    while True:
        count = 0
        for stat in stats:
            count += 1
            print repr(stat)
            # self.response.write(repr(stat))
            # self.response.write('\n')

        if count != page_size or count == 0:
            break
        stats = gcs.listbucket(bucket, max_keys=page_size,
                               marker=stat.filename)
    print stats
    return stats


class Antares(View):
    def dispatch_request(self):
        list_bucket()
        # examples = ExampleModel.query()

        collective = {'name': 'Антарес', 'bucket': 'antares'}
        print collective['bucket']
        return render_template('collectives/collective.html', stats=list_bucket(collective['bucket']),
                               collective=collective)


class Arlekin(View):
    def dispatch_request(self):
        examples = ExampleModel.query()
        collective = {'name': 'Арлекин', 'bucket': 'arlekin'}
        return render_template('collectives/collective.html', examples=examples, collective=collective)


class Step(View):
    def dispatch_request(self):
        examples = ExampleModel.query()
        collective = {'name': 'Степ студия', 'bucket': 'step'}
        return render_template('collectives/collective.html', examples=examples, collective=collective)


class Viva(View):
    def dispatch_request(self):
        examples = ExampleModel.query()
        collective = {'name': 'Viva Dance', 'bucket': 'viva'}
        return render_template('collectives/collective.html', examples=examples, collective=collective)


class Smirnov(View):
    def dispatch_request(self):
        examples = ExampleModel.query()
        collective = {'name': 'Павел Смирнов', 'bucket': 'smirnov'}
        return render_template('collectives/collective.html', examples=examples, collective=collective)
