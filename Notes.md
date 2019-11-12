https://github.com/ravijaya/python3_materials  
https://pymotw.com/3/  
https://projecteuler.net/archives  
#Day1
##What is Python?
Pure oop and general purpose scripting language & supports functional programming (JS)

##Why Python?
Alternative to Perl, dynamically typed

#Applications using Python?
https://awesome-python.com/

##Python virtual machine
Memory manager+Garbage collector (M&S)

##Python syntax
https://www.python.org/dev/peps/pep-0008/

##Data types
    scalar/simple
        numeric (int,float,complex)
        strings (unicode), immutable objects
            regular
            raw
            doc
            bytes
        boolean
        none-type
    collections
        list (array), ordered collections
        tuple (readonly-list), divmod(8,5)
        dictionary (hash, hasp-maps) (key,value)pair,lookup database
        set (hashed-list)

##Sequences type/object (str, list, tuple)
    operations
        indexing
        slicing
        iteration

##Operators
    arithmetic
        +,-,*,/,**,%
        //floor division, 5.8/2=2.9, 5.8//2=2.0
    relational
        >,>=,<.<=,==,!=
    logical
        and,or,not
    bitwise
        &,|,^,~,>>,<<
    conditional
        if else (?:)
        //syntax: true-part-expression if test-condition else false-part-expression
    membership test
        in,not in
    lamda (lamda function)
    
Try 1: Python program to guess me, accepts number between 1 to 1000 and predict in 10 chances

###To recap for Day2: OOPS
    class
    object
        attributes
        methods
    static variables
    static methods
    constructor
    destructor
    features
        inheritance
        data encapsulation
        polymorphism
        abstract

#Day2     
##Regular expressions
###Operations
    pattern matching
    find&replacement
    split
###Syntax
    case sensitive
    match only once in a line
    sub strings
    greedy in nature
##Functions
Named sub program defined to solve a particular problems
##Context manager
What? 
    Programming construct  
Why? 
    Used for IO effectively  
How?  
    code block  
    handles events  
         - entry (allocate)  
         - exit (deallocate)  
Try2: Write a program for making tar file
##OOP  
class (template)  
object (instances)  
attributes (state)  
methods (behave)  
constructor  
desctructor  
###Features
Inheritance (reusable)  
    
Polymorphism   
encapsulation/abstraction  (hiding low level/complex implementation details)  
#####Neither method nor constructor overriding is not possible & only overloading is possible
this is not there in Python and have self  
##SSH with Python
https://pypi.org/project/paramiko/  
python -m pip install paramiko  
netmiko for network automation  

#Day3
##static variables & methods  
shared across all the objects  
@classmethod used as decorator  
use cases - database access  
__ refers to private  

##Logger  
what to log? formatter  
where to log? handler  
#####Log rollover (based on time and size)
##Multi-processing (chrome) & multi-threading (light weight)  (mozilla)
https://reqres.in/  
##SQL connection
https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15  
https://pynative.com/python-postgresql-tutorial/  
http://mvsourcecode.com/python-how-to-connect-to-microsoft-database-using-odbc-driver-pycharm/  
https://datatofish.com/python-script-windows-scheduler/  
```python
import pyodbc

connString = 'Trusted_Connection=yes;DRIVER={ODBC Driver 13 for SQL Server};SERVER=localhost;PORT=1433;DATABASE=Test;'

try:
    cn = pyodbc.connect(connString)
    print('You are connected to db ')
    cursor = cn.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    while row:
        print(row[0])
        row = cursor.fetchone()

except Exception as e:
    print('Error connecting to database: ', str(e))

finally:
    cn.close()
    print('Connection closed')

```
##Subprocess
##keyword arguments - optional
##lamda used in functional programming