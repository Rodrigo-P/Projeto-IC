# -*- coding: UTF-8 -*-

from unidecode import unidecode

ex="Hi⁰ this¹ needs² to³ be⁴ fixed⁵ ...⁶ asd⁷ weq⁸ 23rfr⁹"

fix=ex

for ch in ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']:
	fix=fix.replace(ch,"")

print(fix)
print(ex)