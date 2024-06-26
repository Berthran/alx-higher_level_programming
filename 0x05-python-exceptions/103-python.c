/* CODE to implement printing basic information about Python lists */
/* and Python bytes object */

#include <Python.h>
#include <string.h>

void print_python_bytes(PyObject *p);

void print_python_float(PyObject *p);

/**
 * print_python_list - print basic information about the Python list
 * @p: a pointer to a Python object
 *
 * Return: nothing
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i = 0;
	PyListObject *list = (PyListObject *)p;
	const char *itemObjType;

	printf("[*] Python list info\n");

	if (strcmp(p->ob_type->tp_name, "list") != 0)
		printf("  [ERROR] Invalid List Object\n");
	else
	{
		size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", size);
		allocated = list->allocated;
		printf("[*] Allocated = %ld\n", allocated);
		for (i = 0; i < size; i++)
		{
			itemObjType = list->ob_item[i]->ob_type->tp_name;

			printf("Element %ld: %s\n", i, itemObjType);
			if (strcmp(itemObjType, "float") == 0)
				print_python_float(list->ob_item[i]);
			if (strcmp(itemObjType, "bytes") == 0)
				print_python_bytes(list->ob_item[i]);
			fflush(stdout);
		}
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

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p) == 1)
	{

		/* Size information */
		size = byte->ob_base.ob_size;
		printf("  size: %ld\n", size);

		/* String printing */
		printf("  trying string: %s\n", byte->ob_sval);

		/* Printing bytes */
		str = byte->ob_sval;
		if (size < 10)
			size = size + 1;
		else
			size = 10;

		printf("  first %ld bytes: ", size);

		for (i = 0; i < size - 1; i++)
			printf("%02x ", (unsigned char)str[i]);
		if (str[i] == '\0')
			printf("00\n");
		else
			printf("%02x\n", (unsigned char)str[i]);
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}


/**
 * print_python_float - print basic information about Python float
 * @p: a pointer to a Python object
 *
 * Return: nothing
 */

void print_python_float(PyObject *p)
{
	/*PyFloatObject *f = (PyFloatObject *)p;*/

	printf("[.] float object info\n");

	if (PyFloat_Check(p))
	{
		printf("  value: %f\n", PyFloat_AsDouble(p));
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}

