class India():
    def Capital(self):
        print("Delhi is the capital of India")

    def Language(self):
        print("Hindi is the most spoken language of India")

    def Type(self):
        print(" India is a developing country")

class USA():
    def Capital(self):
        print("Washinton,DC is the capital of USA")

    def Language(self):
        print("English is the most spoken language of USA")

    def Type(self):
        print(" IUSA is a developed country")

obj_ind = India()
obj_usa = USA()


for country in (obj_ind,obj_usa):
      country.Capital()
      country.Language()
      country.Type()

      print("-------------------")
