/* CODE to implement printing basic information about Python lists */
/* and Python bytes object */

#include <Python.h>

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

	if (PyBytes_Check(p) == 1)
	{
		printf("[.] bytes object info\n");

		/* Size information */
		size = PyBytes_Size(p);
		printf("\tsize: %ld\n", size);
		/**
		 * Other alternatives to displaying the size information
		 * printf("\tsize: %ld\n", byte->ob_base.ob_size);
		 */

		/* String printing */
		printf("\ttrying string: %s\n", byte->ob_sval);
		/**
		 * other alternatives to attempting to print a string
		 * printf("\ttrying string: %s\n", PyBytes_AS_STRING(p));
		 * printf("\ttrying string: %s\n", PyBytes_AsString(p));
		 */

		/* Printing bytes */
		str = byte->ob_sval;
		if (size < 10)
			size = size + 1;
		else
			size = size - ((size / 10) - 1) * 10;

		printf("\tfirst %ld bytes: ", size);

		for (i = 0; i < size - 1; i++)
			printf("%02x ", (unsigned char)str[i]);
		if (str[i] == '\0')
			printf("00\n");
		else
			printf("%02x\n", (unsigned char)str[i]);
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("\t[ERROR] Invalid Bytes Object\n");
	}
}

