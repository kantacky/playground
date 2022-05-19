class Profile:
  def __init__(self, name, sex):
    self.name = name
    self.sex = sex

  def getName(self):
    print(self.name)

  def getSex(self):
    print(self.sex)

  def setName(self, name):
    self.name = name


kantacky = Profile('Kanta Oikawa', 'M')

print(kantacky.getName())
kantacky.setName('Kenta Oikawa')
print(kantacky.getName())
