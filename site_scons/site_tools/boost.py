###
#This file is a part of the NVDA project.
#URL: http://www.nvda-project.org/
#Copyright 2006-2010 NVDA contributers.
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License version 2.0, as published by
#the Free Software Foundation.
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#This license can be found at:
#http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
###

import _winreg

_boostRoot=None

def findBoostRoot():
	global _boostRoot
	if _boostRoot is None:
		try:
			k=_winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r'Software\boostpro.com')
		except:
			print "boost tool: can't find bostpro.com registry key"
			return None
		kLen=_winreg.QueryInfoKey(k)[0]
		if kLen<1:
			print "boost tool: no subkeys in boostpro.com registry key"
			return None
		subkeyString=_winreg.EnumKey(k,kLen-1)
		try:
			k=_winreg.OpenKey(k,subkeyString)
		except:
			print "boost tool: failed to open %s subkey of boostpro.com registry key"%subkeyString
			return None
		try:
			boostRoot=_winreg.QueryValueEx(k,"InstallRoot")
		except:
			print "no InstallRoot value in %s subkey of boostpro.com registry key"%subkeyString
			return None
		_boostRoot=boostRoot
	return _boostRoot

def exists():
	return True if findBoostRoot() is not None else False

def generate(env):
	boostRoot=findBoostRoot()
	env.Append(CPPPATH=boostRoot)
