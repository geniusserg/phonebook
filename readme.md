# ![](http://www.mgp.go.cr/images/Plantilla/Portada/Destacados/destacado_directorio.png) Phonebook

<span style="color:blue">*"Put information here if you have anybody to call!"*</span>
- It is console application, based to SQLite, which allows you to save information about friends colleagues in one place
- You may call evrybody without using paper phonebook
- May be you have troubles with remebering birthday dates? With this phonebook it will be just a funding memory
- Thanks to docker it can be launched from every PC without installing any packages or utils
- Databases can be easily imported or exported

> "Notice! Docker.io should be installed on the machine to import the container" [Download docker here](https://www.docker.com/)。or for Linux
`$ sudo apt upgrade; sudo apt install docker.io`

>Also you need to install git to clone this repository on your PC
[Git download](https://git-scm.com/) or for Linux
`$ sudo apt upgrade; sudo apt install git`


## Requirements:

- Ubuntu v. 16+ or another Linux
- Git and Docker installed
- 200+ MB of RAM
- 10+ MB of free space

## How to use?

##### To launch clone this repository
`$ git clone https://github.com/HSE-NN-SE/devops-18pi-geniusserg `

##### Build docker image
`$ docker build -t app .  `

##### And run built image
`$ docker run -v 'pwd'/databases:/databases -i app `

You can just copy this in terminal:
`$ git clone https://github.com/HSE-NN-SE/devops-18pi-geniusserg; docker build -t app . ;  docker run -v ${PWD}/databases:/databases -i app`

### First steps　
You should enter name of database or leave it empty to create new database.
> You can also attach your database, creating dir databases and putting databse file here before launch

![alt launch](https://user-images.githubusercontent.com/50704370/75451837-4535dd80-5982-11ea-8d99-5ad850515b2b.png)

Feel free to add new record in the phonebook!!!

` >>>  append name=Serega surname=Danilich phone=88005553535`

Congratulations! You put new record in db! :stuck_out_tongue_winking_eye: Now see table you've filled!

` >>> output`

![](https://sun9-44.userapi.com/c857220/v857220411/129397/cI6q7eGS-UA.jpg)

Now lets update your created record:

` >>> update  name=Serega surname=Danilich`

And now put your changes: 

` phone=98987879074`

![](https://sun9-68.userapi.com/c857220/v857220411/1293a8/ERIyYsK-gyE.jpg)

And search field with, for example, phone 9898787907:

` >>> search  phone=9898787907`

![](https://sun9-28.userapi.com/c857220/v857220411/1293ca/9xbP-bsEo9U.jpg)

Now lets learn how to delete records:

` >>> delete  name=Serega surname=Danilich`

![](https://sun9-41.userapi.com/c857220/v857220411/1293d1/ZooD1wmn_-c.jpg)

For more information you can check <a href="https://github.com/HSE-NN-SE/devops-18pi-geniusserg/blob/master/help.txt">official documebtation</a>

## Project structure:

|

| _ database.py - wrapper under SQLite functions

| _ core.py - framework (connetction between cLI and database)

| _ main.py - entrypoint of application

| _ databases - directory with databases

|           | _ name.db 
  
|           | _ another_name.db
  
| _ help .txt - documentation about abilities

| _ Dockerfile - configuration for docker image

| _ .travis.yml - configuration for Travis CI


### Link on used technologies

[Python oficial site](https://www.python.org/)

[SQLite official site](https://www.sqlite.org/index.html)

[Docker](https://www.docker.com/)

## Future planes of the projext:

- this system needs *testing system* for appropriate quality 
- this project can be a framework for *GUI* application
- *web interface* also could be implemented in future...

## Testing report

:disappointed_relieved: :disappointed_relieved: :disappointed_relieved: Sorry, it is not ready yet. Here you will see result of latest test. :disappointed_relieved: :disappointed_relieved: :disappointed_relieved:

Be later when tesing will be implemented (about the end of March). We are going to  use Python Test Framework and implement unit testing for core module and manual User Interface test.  

## Information about the releases

- v 0.1 alpha - wrapper under SQLite
- v 0.5 alpha - beta command line interface with low
- v 1.0 beta - availbale now for download. <<< WE HERE
- v 1.0.1 beta - tesing will be implemented, come soon 
- v 1.1 gold - CLI interface ready
- v 1.1.1 beta - gui interface test
- v 1.2 gold - GUI interface ready
- v 1.2.1 beta - internal database
- v 1.2.2 beta - web interface beta
- v 1.3 - Web interface
- v 1.3.1 - Mobile application for Android
- v 1.3.2 - Mobile application for IOS
- v 1.4 - Mobile interface ready

## Information about author

Author: Danilov Sergey

Organization: HSE NN SE

Data Created: 31 december, 2019

Contacts to report bugs: <a href="http://www.vk.com/sergeysergey123">Sergey Danilov in VK</a> or issue page in current repo.
> Notice! send snapshot and full description.

Copyright: Do all what you want with it, i dont care...
