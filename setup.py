from setuptools import setup, Extension
from subprocess import call
swig = "h:\\Python\\swigwin-3.0.2\\swig.exe"
temp = input("Where is swig?[%s]:" % swig)
if len(temp) > 0:
    swig = temp
call([swig, "-python", "-c++", "pytinyxml2.i"])


files = ["tinyxml2.cpp", "pytinyxml2_wrap.cxx"]

setup(name="pytinyxml2",
      description="Python wrapper for tinyxml2",
      version="2.1.0",
      author="Wiadufa Chen",
      author_email="wiadufachen@gmail.com",
      url="https://github.com/wiadufachen/pytinyxml2",
      py_modules=['pytinyxml2'],
      ext_modules=[
                    Extension("_pytinyxml2", files),
                    ],
      classifiers=["Programming Language :: Python",
             "Programming Language :: Python :: 3",
             "License :: OSI Approved :: Apache Software License",
             "Development Status :: 4 - Beta",
             "Operating System :: OS Independent",
             ]
)