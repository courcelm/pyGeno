import sys, os, time, cPickle
#from tools import io
#from exceptions import *

class PythonVersionError(Exception) :
	pass

pyGeno_SETTINGS_PATH = os.path.expanduser('~/.pyGeno/')
pyGeno_SETTINGS_FILENAME = '%s/pyGeno_settings.pkl' % pyGeno_SETTINGS_PATH

pyGeno_FACE = "~-~-:>"
pyGeno_BRANCH = "Medusa"

pyGeno_VERSION_NAME = 'Lean Viper!'
pyGeno_VERSION_RELEASE_LEVEL = 'Beta'
pyGeno_VERSION_NUMBER = 14.02
pyGeno_VERSION_BUILD_TIME = time.ctime(os.path.getmtime(__file__))

pyGeno_RABA_NAMESPACE = 'pyGenoRaba'
pyGeno_RABA_DBFILE = '%s/pyGenoRaba.db' % pyGeno_SETTINGS_PATH

pyGeno_SETTINGS = {'DATA_PATH' : '%s/data' % pyGeno_SETTINGS_PATH}

def version() :
	"""returns a tuple describing pyGeno's current version"""
	return (pyGeno_FACE, pyGeno_BRANCH, pyGeno_VERSION_NAME, pyGeno_VERSION_RELEASE_LEVEL, pyGeno_VERSION_NUMBER, pyGeno_VERSION_BUILD_TIME )

def prettyVersion() :
	"""returns pyGeno's current version in a pretty human redable way"""
	return "pyGeno %s Branch: %s, Name: %s, Release Level: %s, Version: %s, Build time: %s" % version()

def checkPythonVersion() :
	if sys.version_info[0] < 2 or (sys.version_info[0] > 2  and sys.version_info[1] < 7) :
		return False
	return True

def checkSettingsPath() :
	if not os.path.exists(pyGeno_SETTINGS_PATH) :
		return False
	return True

def checkDataPath() :
	if not os.path.exists(pyGeno_SETTINGS['DATA_PATH']) :
		return False
	return True

#def checkReferenceGenome(self, specie) :
#	if specie not in pyGeno_SETTINGS['REFERENCE_GENOMES'] :
#		return False
#	return True

#def setReferenceGenome(specie, newRef) :
#	pyGeno_SETTINGS['REFERENCE_GENOMES'][specie] = newRef
#	cPickle.dump(pyGeno_SETTINGS, open(pyGeno_SETTINGS_FILENAME, 'w'))
#	return True

#def getReferenceGenome(specie) :
#	"returns the reference genome of the specie if one is set. If not prompt"
#	try :
#		return pyGeno_SETTINGS['REFERENCE_GENOMES'][specie]
#	except KeyError:
#		KeyError('specie %s has no defined reference genome, use setReference to manualy set one' % specie)

def getGenomeSequencePath(specie, name) :
	return os.path.normpath(pyGeno_SETTINGS['DATA_PATH']+'/%s/%s' % (specie.lower(), name))

def getReferenceGenomeSequencePath(specie) :
	return os.path.normpath(conf.pyGeno_SETTINGS['DATA_PATH']+'/%s/%s' % (specie.lower(), pyGeno_SETTINGS['REFERENCE_GENOMES'][specie.lower()]))

def pyGeno_init() :
	"This function is automaticly called at launch"
	global pyGeno_SETTINGS

	if not checkPythonVersion() :
		raise PythonVersionError("==> FATAL: pyGeno only works with python 2.7 and above, please upgrade your python version")

	if not checkSettingsPath() :
		os.makedirs(pyGeno_SETTINGS_PATH)

	if not checkDataPath() :
		os.makedirs(pyGeno_SETTINGS['DATA_PATH'])

	try :
		pyGeno_SETTINGS = cPickle.load(open(pyGeno_SETTINGS_FILENAME))

	except :
		cPickle.dump(pyGeno_SETTINGS, open(pyGeno_SETTINGS_FILENAME, 'w'))

pyGeno_init()
