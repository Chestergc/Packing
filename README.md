# Packing
Learning how to package a python app

So, It's a pretty simple thing to do, nice to know how to do it finally, after the directories are in place everything is pretty self explanatory, there is even the Package index to upload the app to once it's been properly packaged.

Once the package is ready, you can just go to the root of the aplication and run:

	python setup.py sdist

That will create a tar.gz of the aplication as you are using it, and name it something like "MyApplication-0.1.0.tar.gz", which you can then register in the index and distribute, to install the application you just run it through:

	python setup.py install

For a simple installation, or:

	python setup.py develop

So that the requirements are also installed and you can actually work on it.

	python setup.py register

Gets your app in the index, and if you have a login:

	python setup.py sdist upload

You can just upload it.

This was just a simple tutorial on the concepts of packaging and distributing an app, now this repo is going ot be inactive, and kept for future reference.