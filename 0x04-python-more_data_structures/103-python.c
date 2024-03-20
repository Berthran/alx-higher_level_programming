/* CODE to implement printing basic information about Python lists */
/* and Python bytes object */

#include <Python.h>
#include <string.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - print basic information about the Python list
 * @p: a pointer to a Python object
 *
 * Return: nothing
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i = 0;
	const char *obj_type;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", list->allocated);

	while (i < size)
	{
		obj_type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		if (strcmp(obj_type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		++i;
	}
}

/**
 * print_python_bytes - print basic information about Python bytes
 * @p: a pointer to a Python object
 *
 * Return: nothing
 */

void print_python_bytes(PyObject *p)
{
	char *str;
	PyBytesObject *byte = (PyBytesObject *)p;
	Py_ssize_t size, i;
	(void)byte, (void)p, (void)str, (void)size, (void)i;
}

