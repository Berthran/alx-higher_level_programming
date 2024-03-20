#include <Python.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i = 0;

	PyListObject *list = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	while(i < size)
	{
		printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		++i;
	}
}

