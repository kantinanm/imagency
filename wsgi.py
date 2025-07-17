#import factory 
from factory import create_app

#App = factory.create_app()  # Create the Flask app using the factory function
app=create_app()  # Create the Flask app using the factory function

if __name__ == "__main__":
    app.run()