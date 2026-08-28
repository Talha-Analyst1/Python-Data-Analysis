#project movie
movies=[
    {'Title':'Jack', 'Year':2010, 'Rating':8.9},
    {'Title':'Black Adam', 'Year':2011, 'Rating':9},
    {'Title':'Batman', 'Year':2012, 'Rating':9.1}
]
for movie in movies:
    print(movie['Title'], '-', movie['Year'])
    if movie['Rating'] >=8:
        print('Must watch')
    else:
        print('Good movie')


#project (about student list)

students=[
    {'Name':'Talha', 'Age':22, 'Marks': 90},
    {'Name':'Uzair', 'Age':23, 'Marks': 70},
    {'Name':'Ahmed', 'Age':24,'Marks':50}
]
for student in students:
    print(student['Name'], student['Marks'])
    if student['Marks']>=87:
        print('high')
    else:
        print('Good')