h:\Python\swigwin-3.0.2\swig -python -c++ pytinyxml2.i
g++ -c pytinyxml2_wrap.cxx tinyxml2.cpp -Ih:\Python\Python34\include\
g++ -shared pytinyxml2_wrap.o tinyxml2.o -o _pytinyxml2.pyd -lpython34 -Lh:\Python\Python34\libs\
pause