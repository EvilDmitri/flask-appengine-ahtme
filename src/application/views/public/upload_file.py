# -*- coding: utf-8 -*-

import logging
from flask.views import View

from flask import flash, redirect, url_for, request, jsonify
from werkzeug.utils import secure_filename

from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from models import ExampleModel

from decorators import login_required

import cloudstorage as gcs


class UploadFile(View):

    def dispatch_request(self):
        if request.method == "POST":
            # upload_files = self.get_uploads('file')
            # blob_info = upload_files[0]
            # user = users.get_current_user()
            # print 'user - ', user
            # print 'blob_info', dir(blob_info)

            collective = request.args.get('collective')
            print collective
            file = request.files.get('file')
            print secure_filename(file.filename).rsplit('.', 1)
            extension = secure_filename(file.filename).rsplit('.', 1)[1]
            filename = file.filename
            file.filename = filename.encode('utf-8')
            print '------------------------------------------'
            print 'file.filename - ', file.filename
            print '---------------------'
            print 'extension - ', extension
            print 'file - ', file
            print '------------------------------------------'

            options = {}
            options['retry_params'] = gcs.RetryParams(backoff_factor=1.1)
            options['content_type'] = 'audio/' + extension
            # options['metadata'] = {'x-goog-meta-file_name': filename.encode('utf-8')}

            bucket_name = "ahtme-music"
            path = '/' + bucket_name + '/' + collective + '/' + str(secure_filename(file.filename))
            if file:
                try:
                    with gcs.open(path, 'w', **options) as f:
                        f.write(file.stream.read())# instead of f.write(str(file))
                        print jsonify({"success": True})
                    flash(u'Файл %s загружен.' % file.filename, 'success')
                    # return jsonify({"success": True})
                    return redirect(url_for(collective ))
                except Exception as e:
                    logging.exception(e)
                    flash(u'Файл %s не загружен!' % file.filename, 'info')
                    return redirect(url_for(collective ))
            # flash(u'Файл %s загружен.' % file.filename, 'success')
            # return redirect(url_for('list_examples'))
