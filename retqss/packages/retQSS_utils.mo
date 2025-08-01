package retQSS_utils

import retQSS;

/*
  Useful constant for comparing to zero or triggering immediate events (ie time + EPS())
*/
function EPS
	output Real eps;
algorithm
	eps := 1e-5;
end EPS;

/*
  PI constant
*/
function PI
	output Real pi;
algorithm
	pi := 3.1415926536;
end PI;

/*
  Useful placeholder as unused arguments values
*/
function EMPTY
	output Real _;
algorithm
	_ := 0;
end EMPTY;

/*
  INFO logging level constante value (0)
*/
function INFO
	output Integer level;
algorithm
	level := 0;
end INFO;

/*
  DEBUG logging level constante value (1)
*/
function DEBUG
	output Integer level;
algorithm
	level := 1;
end DEBUG;

/*
  Sets the debug level
*/
function setDebugLevel
	input Integer level;
	output Boolean status;
	external "C" status=utils_setDebugLevel(level) annotation(
	    Library="utils",
	    Include="#include \"retqss_utils.hh\"");
end debug;

/*
  Logs a debug message. This function is implemented in C because it writes a log file.
  Accepts C-like message formmating (ie: %f %s %d)
*/
function debug
	input Integer level;
	input Real time;
	input String format;
	input Integer int1;
	input Integer int2;
	input Real real1;
	input Real real2;
	output Boolean status;
	external "C" status=utils_debug(level, time, format, int1, int2, real1, real2) annotation(
	    Library="utils",
	    Include="#include \"retqss_utils.hh\"");
end debug;

/*
  Gets an element of discrete array. Only way to access arrays outside main module (?)
*/
function arrayGet
	input Real array[1];
	input Integer index;
	output Real value;
	external "C" value=utils_arrayGet(array, index) annotation(
	    Library="utils",
	    Include="#include \"retqss_utils.hh\"");
end arrayGet;

/*
  Gets an element of normal non-discrete array used in equations section. Only way to access arrays outside main module (?)
*/
function equationArrayGet
	input Real array[1];
	input Integer index;
	output Real value;
algorithm
	value := arrayGet(array, (index-1)*3+1);
end equationArrayGet;

/*
  Util function for retrieving an array of integers from parameters.config file
*/
function isInArrayParameter
	input String name;
	input Integer value;
	output Boolean result;
external "C" result=utils_isInArrayParameter(name, value) annotation(
	    Library="utils",
	    Include="#include \"retqss_utils.hh\"");
end isInArrayParameter;

/*
  Util function for retrieving an integer value from parameters.config file
*/
function getIntegerModelParameter
	input String name;
	input Integer defaultValue;
	output Integer value;
	external "C" value=utils_getIntegerModelParameter(name, defaultValue) annotation(
	    Library="utils",
	    Include="#include \"retqss_utils.hh\"");

end getIntegerModelParameter;

/*
  Util function for retrieving a real value from parameters.config file
*/
function getRealModelParameter
	input String name;
	input Real defaultValue;
	output Real value;
	external "C" value=utils_getRealModelParameter(name, defaultValue) annotation(
	    Library="utils",
	    Include="#include \"retqss_utils.hh\"");
end getRealModelParameter;


end retQSS_utils;
