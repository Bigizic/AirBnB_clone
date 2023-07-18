# AirBnB_clone

## Welcome to the AirBnB clone project!

## First Step:

	Write a command interpreter to manage your AirBnB objects.

## Second Step:

	Python Scripts

## Third Step:

	Python Unit Tests

## Exection:

Your shell should work like this in interactive mode:

	$ ./console.py
	(hbnb) help
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	
	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$

But also in non-interactive mode:

	$ echo "help" | ./console.py
	(hbnb)
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

## Tasks:

### README.md:

Readme must contain:

	description of the project
	desctiption of the command interpreter

### AUTHORS:

All individuals having contributed to this project is listed in this file


### BaseModel:

Write a class BaseModel that defines all common attributes/methods for other classes:

1. models/base_model.py

2. Public instance attributes:

	id: string - assign with an uuid when an instance is created:

	you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string

	the goal is to have unique id for each BaseModel

	created_at: datetime - assign with the current datetime when an instance is created

	updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object

3. __str__: should print: [<class name>] (<self.id>) <self.__dict__>

4. Public instance methods:

	save(self): updates the public instance attribute updated_at with the current datetime

	to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:

	by using self.__dict__, only instance attributes set will be returned

	a key __class__ must be added to this dictionary with the class name of the object

	created_at and updated_at must be converted to string object in ISO format:

	format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)

	you can use isoformat() of datetime object

	This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel

Terminal:


	guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
	#!/usr/bin/python3
	from models.base_model import BaseModel
	
	my_model = BaseModel()
	my_model.name = "My First Model"
	my_model.my_number = 89
	print(my_model)
	my_model.save()
	print(my_model)
	my_model_json = my_model.to_dict()
	print(my_model_json)
	print("JSON of my_model:")
	for key in my_model_json.keys():
	    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
	
	guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
	[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
	[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
	{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
	JSON of my_model:
	    my_number: (<class 'int'>) - 89
	    name: (<class 'str'>) - My First Model
	    __class__: (<class 'str'>) - BaseModel
	    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
	    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
	    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427
	
	guillaume@ubuntu:~/AirBnB$ 

-----------------------------------------------------------------------------------------------------------------------------------------------------


### Create BaseModel from dictionary:

Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.

	<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>

1. Update models/base_model.py:

	__init__(self, *args, **kwargs):

	you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)

	*args won’t be used

	if kwargs is not empty:

	each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)

	each value of this dictionary is the value of this attribute name

	Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime

	otherwise:

	create id and created_at as you did previously (new instance)

Terminal:

	guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
	#!/usr/bin/python3
	from models.base_model import BaseModel
	
	my_model = BaseModel()
	my_model.name = "My_First_Model"
	my_model.my_number = 89
	print(my_model.id)
	print(my_model)
	print(type(my_model.created_at))
	print("--")
	my_model_json = my_model.to_dict()
	print(my_model_json)
	print("JSON of my_model:")
	for key in my_model_json.keys():
	    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
	
	print("--")
	my_new_model = BaseModel(**my_model_json)
	print(my_new_model.id)
	print(my_new_model)
	print(type(my_new_model.created_at))
	
	print("--")
	print(my_model is my_new_model)
	
	guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
	56d43177-cc5f-4d6c-a0c1-e167f8c27337
	[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
	<class 'datetime.datetime'>
	--
	{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
	JSON of my_model:
	    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
	    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
	    __class__: (<class 'str'>) - BaseModel
	    my_number: (<class 'int'>) - 89
	    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
	    name: (<class 'str'>) - My_First_Model
	--
	56d43177-cc5f-4d6c-a0c1-e167f8c27337
	[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
	<class 'datetime.datetime'>
	--
	False
	guillaume@ubuntu:~/AirBnB$ 

-----------------------------------------------------------------------------------------------------------------------------------------------------


### Store first object:

Now we can recreate a BaseModel from another one by using a dictionary representation:

	<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>

It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:

Python doesn’t know how to convert a string to a dictionary (easily)

It’s not human readable

Using this file with another program in Python or other language will be hard.

So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:

	<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>

Magic right?

Terms:
	simple Python data structure: Dictionaries, arrays, number and string. ex: { '12': { 'numbers': [1, 2, 3], 'name': "John" } }

	JSON string representation: String representing a simple data structure in JSON format. ex: '{ "12": { "numbers": [1, 2, 3], "name": "John" } }'

Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances

-----------------------------------------------------------------------------------------------------------------------------------------------------


### Console 0.0.1:

Write a program called console.py that contains the entry point of the command interpreter:

	1. You must use the module cmd
	2. Your class definition must be: class HBNBCommand(cmd.Cmd):
	3. Your command interpreter should implement:
		quit and EOF to exit the program
		help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
		a custom prompt: (hbnb)
		an empty line + ENTER shouldn’t execute anything

	4. Your code should not be executed when imported

Warning:

You should end your file with:

	if __name__ == '__main__':
	    HBNBCommand().cmdloop()

Terminal:

	guillaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) help
		
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	
	(hbnb) 
	(hbnb) help quit
	Quit command to exit the program
	
	(hbnb) 
	(hbnb) 
	(hbnb) quit 
	guillaume@ubuntu:~/AirBnB$ 


----------------------------------------------------------------------------------------------------------------------------------------------------


### Console 0.1:

command interpreter (console.py) should have these commands:

	1. create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel

	2. show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.

	3. destroy: Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.

	4. all: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.

	5. update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".


-----------------------------------------------------------------------------------------------------------------------------------------------------


### First User:

Write a class User that inherits from BaseModel:

	1. models/user.py
	2. Public class attributes:
		email: string - empty string
		password: string - empty string
		first_name: string - empty string
		last_name: string - empty string
Update FileStorage to manage correctly serialization and deserialization of User.

Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User.

Terminal:

	guillaume@ubuntu:~/AirBnB$ cat test_save_reload_user.py
	#!/usr/bin/python3
	from models import storage
	from models.base_model import BaseModel
	from models.user import User
	
	all_objs = storage.all()
	print("-- Reloaded objects --")
	for obj_id in all_objs.keys():
	    obj = all_objs[obj_id]
	    print(obj)
	
	print("-- Create a new User --")
	my_user = User()
	my_user.first_name = "Betty"
	my_user.last_name = "Bar"
	my_user.email = "airbnb@mail.com"
	my_user.password = "root"
	my_user.save()
	print(my_user)
	
	print("-- Create a new User 2 --")
	my_user2 = User()
	my_user2.first_name = "John"
	my_user2.email = "airbnb2@mail.com"
	my_user2.password = "root"
	my_user2.save()
	print(my_user2)
	
	guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
	{"BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049"}}
	guillaume@ubuntu:~/AirBnB$
	guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
	-- Reloaded objects --
	[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
	[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
	[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
	[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
	[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
	-- Create a new User --
	[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@mail.com', 'first_name': 'Betty', 'last_name': 'Bar', 'password': 'root'}
	-- Create a new User 2 --
	[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'email': 'airbnb2@mail.com', 'first_name': 'John', 'password': 'root'}
	guillaume@ubuntu:~/AirBnB$
	guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
	{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at": "2017-09-28T21:11:42.848279", "updated_at": "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", "first_name": "Betty", "__class__": "User", "last_name": "Bar", "password": "root"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"id": "d0ef8146-4664-4de5-8e89-096d667b728e", "created_at": "2017-09-28T21:11:42.848280", "updated_at": "2017-09-28T21:11:42.848294", "email": "airbnb_2@mail.com", "first_name": "John", "__class__": "User", "password": "root"}}
	guillaume@ubuntu:~/AirBnB$ 
	guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
	-- Reloaded objects --
	[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544), 'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521)}
	[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862), 'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852)}
	[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058), 'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049)}
	[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296), 'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287)}
	[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347), 'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337)}
	[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'last_name': 'Bar', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'first_name': 'Betty'}
	[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'first_name': 'John'}
	-- Create a new User --
	[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'last_name': 'Bar', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'first_name': 'Betty'}
	-- Create a new User 2 --
	[User] (fce12f8a-fdb6-439a-afe8-2881754de71c) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611354), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611368), 'id': 'fce12f8a-fdb6-439a-afe8-2881754de71c', 'first_name': 'John'}
	guillaume@ubuntu:~/AirBnB$
	guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
	{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"updated_at": "2017-09-28T21:11:12.971544", "__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "created_at": "2017-09-28T21:11:12.971521"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848279", "email": "airbnb@mail.com", "id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "last_name": "Bar", "updated_at": "2017-09-28T21:11:42.848291", "first_name": "Betty", "__class__": "User"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848280", "email": "airbnb_2@mail.com", "id": "d0ef8146-4664-4de5-8e89-096d667b728e", "updated_at": "2017-09-28T21:11:42.848294", "first_name": "John", "__class__": "User"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"updated_at": "2017-09-28T21:11:14.963058", "__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "created_at": "2017-09-28T21:11:14.963049"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"updated_at": "2017-09-28T21:11:15.504296", "__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"updated_at": "2017-09-28T21:11:13.753347", "__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"updated_at": "2017-09-28T21:11:14.333862", "__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "created_at": "2017-09-28T21:11:14.333852"}, "User.246c227a-d5c1-403d-9bc7-6a47bb9f0f68": {"password": "root", "created_at": "2017-09-28T21:12:19.611352", "email": "airbnb@mail.com", "id": "246c227a-d5c1-403d-9bc7-6a47bb9f0f68", "last_name": "Bar", "updated_at": "2017-09-28T21:12:19.611363", "first_name": "Betty", "__class__": "User"}, "User.fce12f8a-fdb6-439a-afe8-2881754de71c": {"password": "root", "created_at": "2017-09-28T21:12:19.611354", "email": "airbnb_2@mail.com", "id": "fce12f8a-fdb6-439a-afe8-2881754de71c", "updated_at": "2017-09-28T21:12:19.611368", "first_name": "John", "__class__": "User"}}
	guillaume@ubuntu:~/AirBnB$ 


-----------------------------------------------------------------------------------------------------------------------------------------------------


### More classes!:

Write all those classes that inherit from BaseModel:

	1. State (models/state.py):
		Public class attributes:
			name: string - empty string
	2. City (models/city.py):
		Public class attributes:
			state_id: string - empty string: it will be the State.id
			name: string - empty string
	3. Amenity (models/amenity.py):
		Public class attributes:
			name: string - empty string
	4. Place (models/place.py):
		Public class attributes:
			city_id: string - empty string: it will be the City.id
			user_id: string - empty string: it will be the User.id
			name: string - empty string
			description: string - empty string
			number_rooms: integer - 0
			number_bathrooms: integer - 0
			max_guest: integer - 0
			price_by_night: integer - 0
			latitude: float - 0.0
			longitude: float - 0.0
			amenity_ids: list of string - empty list: it will be the list of Amenity.id later
	5. Review (models/review.py):
		Public class attributes:
			place_id: string - empty string: it will be the Place.id
			user_id: string - empty string: it will be the User.id
			text: string - empty string


-----------------------------------------------------------------------------------------------------------------------------------------------------


### 10. Console 1.0:

Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

Enjoy your first console!

No unittests needed for the console


# ADVANCED TASKS:


## 11. All instances by class name:

Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().

terminal:

	guillaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) User.all()
	[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
(hbnb) 


---------------------------------------------------------------------------------------------------------------------------------------------------


## 12. Count instances:

Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().

terminal:

	guillaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) User.count()
	2
	(hbnb) 


---------------------------------------------------------------------------------------------------------------------------------------------------


## 13. Show:

Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).

Errors management must be the same as previously.

	guillaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
	[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
	(hbnb) User.show("Bar")
	** no instance found **
	(hbnb)


----------------------------------------------------------------------------------------------------------------------------------------------------



## 14. Destroy:

Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).

Errors management must be the same as previously.

	guillaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) User.count()
	2
	(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
	(hbnb) User.count()
	1
	(hbnb) User.destroy("Bar")
	** no instance found **
	(hbnb) 


----------------------------------------------------------------------------------------------------------------------------------------------------



## 15. Update:

Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).

Errors management must be the same as previously.

	guillaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
	[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
	(hbnb)
	(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
	(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
	(hbnb)
	(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
	[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
	(hbnb) 


---------------------------------------------------------------------------------------------------------------------------------------------------


## 16. Update from dictionary:


Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).

Errors management must be the same as previously.

	guillaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
	[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 23, 'first_name': 'Bob', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
	(hbnb) 
	(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
	(hbnb) 
	(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
	[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
	(hbnb) 
	

---------------------------------------------------------------------------------------------------------------------------------------------------


## 17. Unittests for the Console!

Write all unittests for console.py, all features!

For testing the console, you should “intercept” STDOUT of it, we highly recommend you to use:

	with patch('sys.stdout', new=StringIO()) as f:
	    HBNBCommand().onecmd("help show")
