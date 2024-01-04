#include "Python.h"

/**
 * print_python_string - prints info about python strings
 * @p: pointer to PyObject
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	wchar_t *str;

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	len = ((PyASCIIObject *)(p))->length;
	str = PyUnicode_AsWideCharString(p, &len);
	printf("  type: %s\n", p->ob_type->tp_name);
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", str);
}
