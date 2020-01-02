'''
Add this to `requirements.txt`:

```
libsass
django-compressor
django-sass-processor
```

Add `libsass` to your Alpine `Dockerfile` `runbase` `apk add` command and `libsass-dev` to your Alpine `Dockerfile` `buildbase` `apk add` command.

Run `docker-compose build`.

Then copy this file into your settings as `base_07_sass.py` and add this to the top:

```
from .base_06_timezone import *
```

Then change `dev.py` and `production_01_bucket.py` to import from `.base_07_sass` instead of `.base_06_timezone`.

Write your SCSS in `teratree/css/mystyle.scss`.

Then use like this in your Django templates:

```
{% load sass_tags %}

<link href="{% sass_src 'teratree/css/mystyle.scss' %}" rel="stylesheet" type="text/css" />
```

Which renders as:

```
<link href="/static/teratree/css/mystyle.css" rel="stylesheet" type="text/css" />
```

If you don't want to expose the SASS/SCSS files in a production environment, change the `collectstatic` command in `run.sh.local` to:

```
manage.py collectstatic --ignore=*.scss
```

You can compile offline instead of dynamically with:

```
manage.py compilescss
```

See https://github.com/jrief/django-sass-processor for the full information.
'''

from .base_06_timezone import *

# DISABLE FOR NOW # for finder in [
# DISABLE FOR NOW #     'django.contrib.staticfiles.finders.FileSystemFinder',
# DISABLE FOR NOW #     # 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# DISABLE FOR NOW #     'sass_processor.finders.CssFinder',
# DISABLE FOR NOW # ]:
# DISABLE FOR NOW #     if finder not in STATICFILES_FINDERS:
# DISABLE FOR NOW #         STATICFILES_FINDERS.append(finder)
# DISABLE FOR NOW # 
# DISABLE FOR NOW # for app in [
# DISABLE FOR NOW #     'sass_processor',
# DISABLE FOR NOW # ]:
# DISABLE FOR NOW #     if app not in INSTALLED_APPS:
# DISABLE FOR NOW #         INSTALLED_APPS.append(app)
# DISABLE FOR NOW # 
# DISABLE FOR NOW # # Optionally, add a list of additional search paths, the SASS compiler may examine when using the @import "..."; statement in SASS/SCSS files:
# DISABLE FOR NOW # #
# DISABLE FOR NOW # # import os
# DISABLE FOR NOW # # 
# DISABLE FOR NOW # # SASS_PROCESSOR_INCLUDE_DIRS = [
# DISABLE FOR NOW # #     os.path.join(PROJECT_PATH, 'extra-styles/scss'),
# DISABLE FOR NOW # #     os.path.join(PROJECT_PATH, 'node_modules'),
# DISABLE FOR NOW # # ]
# DISABLE FOR NOW # # 
# DISABLE FOR NOW # # Other settings you can set:
# DISABLE FOR NOW # # 
# DISABLE FOR NOW # # SASS_PROCESSOR_AUTO_INCLUDE = False
# DISABLE FOR NOW # # SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'
# DISABLE FOR NOW # # SASS_PRECISION = 8
# DISABLE FOR NOW # # SASS_OUTPUT_STYLE = 'compact'
