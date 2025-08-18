Student_data  = {
    'id1' : {
        'Name':'Arunav',
        'Age': 23,
        'Course':['English','math'],
        'numbers':['89','76']
    },
    'id2' : {
        'Name':'Tabi',
        'Age': 25,
        'Course':['Social sceince','math'],
        'numbers':['99','90']
    },
    'id2' : {
        'Name':'Tabi',
        'Age': 25,
        'Course':['Social sceince','math'],
        'numbers':['99','90']
    },
        'id2' : {
        'Name':'Marko',
        'Age': 22,
        'Course':['sceince','math'],
        'numbers':['56','60']
    },


}
print("Orignal student data",Student_data)
result = {}
for key,value in Student_data.items():
    if value not in result.values():
        result[key] = value

print("Student data after removing duplicates:",result)
print("The unique numbers are:",len(result))