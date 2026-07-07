class Engine:
    def start(self):
        print("Engine Started")
    def stop(self):
        print("Engine Stopped")
class Car:
    def __init__(self):
        self.engine=Engine()
    def start(self):
        self.engine.start()
    def stop(self):
        self.engine.stop()
Car1=Car()
Car1.start()
Car1.stop()