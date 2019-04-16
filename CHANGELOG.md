Version 0.5.3
=============
*  Fix for `BleachField` set to allow `blank` or `null`. (Thanks denisroldan)

Version 0.5.2
=============
*  Fix for `BleachField` receiving a `None` value. (Thanks MrkGrgsn)

Version 0.5.1
=============
*  100% coverage achieved
*  Changelog updated with `0.5.0` changes. (Thanks dyve)

Version 0.5.0
=============
*  Added support for bleach's `allowed_protocols` kwarg. (Thanks blag)
*  Bleach dependency is now `>=1.5.0`

Version 0.4.1
=============
*  Option to pass *allowed tags* to the `bleach` template filter added by Rafał Selewońko.
*  Moved project to Github.

Version 0.4.0
=============
*  Added support for django>=1.9
*  Ensure that the `model_instance` field gets updated with the clean value

Version 0.3.0
=============
*  The `BleachField` model field now does its own sanitisation,
   and does *not* specify a default form field or widget.
   Developers are expected to provide their own widget as needed.

Version 0.2.1
=============
*  Make the package python3 compatible.

Version 0.2.0
=============
*  Add `bleach_linkify` template filter from whitehat2k13

Version 0.1.3
=============
*  Add missing `templatetags` package, by using `find_packages()`
*  Correct templatetag name: ``bleach.py`` -> ``bleach_tags.py``

Version 0.1.2
=============
*  Fix south migration bug

Version 0.1.1
=============
*  add south_triple_field for south integration
*  clean up files to meet pep8 compliance

Version 0.1.0
=============
*  Initial release