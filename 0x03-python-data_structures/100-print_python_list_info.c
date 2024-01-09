#include <Python.h>

void print_python_list_info(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Object is not a list\n");
		return;
	}

	int size = PyList_Size(p);
	PyObject *element;

	printf("List size: %d\n", size);
	printf("Elements:\n");

	for (int i = 0; i < size; i++) {
		element = PyList_GetItem(p, i);

		if (PyLong_Check(element))
		{
			printf("- %ld (integer)\n", PyLong_AsLong(element));
		}
		else if (PyFloat_Check(element))
		{
			printf("- %f (float)\n", PyFloat_AsDouble(element));
		}
		else if (PyUnicode_Check(element))
		{
			printf("- %s (string)\n", PyUnicode_AsUTF8(element));
		}
		else
		{
			printf("- %s (unknown type)\n", Py_TYPE(element)->tp_name);
		}
	}
}
