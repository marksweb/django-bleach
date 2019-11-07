Version 0.6.1
=============
###### 07-11-2019
*  Handle `None` as an input value of template tags (Thanks [pegler](https://github.com/pegler))

Version 0.6.0
=============
###### 18-10-2019
*  Introduced testing against Python 3.8
*  Drop support for Django <1.11
*  Test coverage at 100%

Version 0.5.3
=============
###### 16-04-2019
*  Fix for `BleachField` set to allow `blank` or `null`. (Thanks [denisroldan](https://github.com/denisroldan))

Version 0.5.2
=============
###### 15-03-2019
*  Fix for `BleachField` receiving a `None` value. (Thanks [MrkGrgsn](https://github.com/MrkGrgsn))

Version 0.5.1
=============
###### 12-02-2019
*  100% coverage achieved
*  Changelog updated with `0.5.0` changes. (Thanks [dyve](https://github.com/dyve))

Version 0.5.0
=============
###### 02-02-2019
*  Added support for bleach's `allowed_protocols` kwarg. (Thanks [blag](https://github.com/blag))
*  Bleach dependency is now `>=1.5.0`

Version 0.4.1
=============
###### 24-01-2019
*  Option to pass *allowed tags* to the `bleach` template filter added by [Rafał Selewońko](https://github.com/seler).
*  Moved project to Github.

Version 0.4.0
=============
###### 18-12-2018
*  Added support for django>=1.9
*  Ensure that the `model_instance` field gets updated with the clean value

Version 0.3.0
=============
###### 20-09-2014
*  The `BleachField` model field now does its own sanitisation,
   and does *not* specify a default form field or widget.
   Developers are expected to provide their own widget as needed.

Version 0.2.1
=============
###### 02-09-2014
*  Make the package python3 compatible.

Version 0.2.0
=============
###### 14-02-2014
*  Add `bleach_linkify` template filter from [whitehat2k13](https://bitbucket.org/%7B66836148-7eee-4894-acec-e073b30499ee%7D/)

Version 0.1.5
=============
###### 25-09-2013

Version 0.1.4
=============
###### 03-06-2013

Version 0.1.3
=============
###### 22-08-2012
*  Add missing `templatetags` package, by using `find_packages()`
*  Correct templatetag name: ``bleach.py`` -> ``bleach_tags.py``

Version 0.1.2
=============
###### 13-08-2012
*  Fix south migration bug

Version 0.1.1
=============
###### 13-08-2012
*  add south_triple_field for south integration
*  clean up files to meet pep8 compliance

Version 0.1.0
=============
###### 13-08-2012
*  Initial release