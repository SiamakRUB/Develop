


# Litkey
 Litkey is short for “Literacy as the key to social participation: Psycholinguistic perspectives on orthography instruction and literacy acquisition”, a collaborative research project funded by the Volkswagen Foundation as part of the research initiative “Key Issues for Research and Society”. On these pages, we present the project as a whole and each of a total of four project strands for all those who might be interested in what we do:

    interested colleagues and fellow scientists,
    preschool and primary school teachers who are interested in our research or might want to contribute to it, and, of course,
    parents whose children might participate in one of our studies and who want to know more about what we do.

# Installation
##  Usage
- Mysql
- Python
- Django

##  Database File 
	
Restore database LITKEY from

    '\litkey_db.sql'
 on server Database

##  Database Configuration
in path

       '\RubLitkeyCorpusWeb\settings.py' 
replace your database server configuration  
	
	DATABASES = {
    		'default': {
    		    	'ENGINE': 'django.db.backends.mysql',
        		'NAME': 'litkey',
		        'USER': 'root',
		        'PASSWORD': '',
		        'HOST': 'localhost',
		        'PORT': '3306',
    				}
		}

 
 
# Credits

 - Prof. Dr. Eva Belke
 - Prof. Dr. Stefanie Dipper
 - Siamak Abbasi
 - Sepehr Banani 
 
	

# License
 - Ruhr University Bochum
 
 