
books = {
    "9780135171879": {
        "title": "Operating System Concepts",
        "author": "Abraham Silberschatz, Greg Gagne, Peter B. Galvin",
        "publisher": "Wiley",
        "year": 2020,
        "genre": "Operating Systems"
    },
    "9780134743356": {
        "title": "Modern Operating Systems",
        "author": "Andrew S. Tanenbaum, Herbert Bos",
        "publisher": "Pearson",
        "year": 2021,
        "genre": "Operating Systems"
    },
    "9781492052203": {
        "title": "Data Structures and Algorithms in Python",
        "author": "Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser",
        "publisher": "Wiley",
        "year": 2021,
        "genre": "Data Structures"
    },
    "9780262043649": {
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
        "publisher": "MIT Press",
        "year": 2020,
        "genre": "Data Structures"
    },
    "9780134093413": {
        "title": "Operating Systems: Internals and Design Principles",
        "author": "William Stallings",
        "publisher": "Pearson",
        "year": 2020,
        "genre": "Operating Systems"
    },
    "9781789807303": {
        "title": "Hands-On Data Structures and Algorithms with Python",
        "author": "Dr. Basant Agarwal, Benjamin Baka",
        "publisher": "Packt Publishing",
        "year": 2020,
        "genre": "Data Structures"
    },
    "9780134687477": {
        "title": "Machine Learning with Python",
        "author": "Andreas C. Müller, Sarah Guido",
        "publisher": "O'Reilly Media",
        "year": 2021,
        "genre": "Machine Learning"
    },
    "9781492052647": {
        "title": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow",
        "author": "Aurélien Géron",
        "publisher": "O'Reilly Media",
        "year": 2020,
        "genre": "Machine Learning"
    },
    "9780262043601": {
        "title": "Pattern Recognition and Machine Learning",
        "author": "Christopher M. Bishop",
        "publisher": "Springer",
        "year": 2020,
        "genre": "Machine Learning"
    },
    "9780128145940": {
        "title": "Python Machine Learning By Example",
        "author": "Yuxi (Hayden) Liu",
        "publisher": "Packt Publishing",
        "year": 2022,
        "genre": "Machine Learning"
    },
    "9781492032649": {
        "title": "Python for Data Analysis",
        "author": "Wes McKinney",
        "publisher": "O'Reilly Media",
        "year": 2022,
        "genre": "Machine Learning"
    },
    "9780135166308": {
        "title": "Data Structures and Algorithms in Python",
        "author": "Robert Lafore",
        "publisher": "Pearson",
        "year": 2022,
        "genre": "Data Structures"
    },
    "9780134686034": {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "year": 2020,
        "genre": "Python Programming"
    },
    "9780134093414": {
        "title": "Algorithms and Data Structures",
        "author": "David Harel, Yishai Feldman",
        "publisher": "Pearson",
        "year": 2020,
        "genre": "Data Structures"
    },
    "9781119556844": {
        "title": "Introduction to Machine Learning with Python",
        "author": "Andreas C. Müller, Sarah Guido",
        "publisher": "O'Reilly Media",
        "year": 2021,
        "genre": "Machine Learning"
    },
    "9781491962299": {
        "title": "Machine Learning Engineering",
        "author": "Andriy Burkov",
        "publisher": "True Positive Inc.",
        "year": 2020,
        "genre": "Machine Learning"
    },
    "9781789136601": {
        "title": "Data Structures and Algorithms with Python",
        "author": "Kent D. Lee, Steve Hubbard",
        "publisher": "Springer",
        "year": 2021,
        "genre": "Data Structures"
    },
    "9781492054993": {
        "title": "Python Machine Learning Projects",
        "author": "Lisa Tagliaferri",
        "publisher": "DigitalOcean",
        "year": 2020,
        "genre": "Machine Learning"
    },
    "9781492037964": {
        "title": "Practical Machine Learning with Python",
        "author": "Dipanjan Sarkar",
        "publisher": "Apress",
        "year": 2020,
        "genre": "Machine Learning"
    },
    "9780134845623": {
        "title": "Mastering Machine Learning with Python",
        "author": "James D. Miller",
        "publisher": "Packt Publishing",
        "year": 2021,
        "genre": "Machine Learning"
    },
    "9780135164722": {
        "title": "The Art of Machine Learning with Python",
        "author": "John Hearty",
        "publisher": "O'Reilly Media",
        "year": 2022,
        "genre": "Machine Learning"
    },
    "9781484261428": {
        "title": "Deep Learning with Python",
        "author": "Francois Chollet",
        "publisher": "Manning Publications",
        "year": 2022,
        "genre": "Machine Learning"
    },
    "9780134494166": {
        "title": "Machine Learning for Absolute Beginners",
        "author": "Oliver Theobald",
        "publisher": "CreateSpace Independent Publishing Platform",
        "year": 2023,
        "genre": "Machine Learning"
    },
    "9781119467768": {
        "title": "Programming Machine Learning",
        "author": "Paolo Perrotta",
        "publisher": "Pragmatic Bookshelf",
        "year": 2021,
        "genre": "Machine Learning"
    },
    "9780134685990": {
        "title": "Machine Learning with Python Cookbook",
        "author": "Chris Albon",
        "publisher": "O'Reilly Media",
        "year": 2022,
        "genre": "Machine Learning"
    }
}

for isbn, details in books.items():
    print(f"ISBN: {isbn}")
    for key, value in details.items():
        print(f"  {key}: {value}")
    print("\n")
