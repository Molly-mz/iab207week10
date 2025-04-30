'''
(Part 2 of exercise: Run the application in VSC)

Your directory should look like this after new file main.py added:
project (folder)
 ├── main.py
 ├── travel (folder)
      ├── __init__.py

the code below should be placed into main.py
'''

from travel import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)