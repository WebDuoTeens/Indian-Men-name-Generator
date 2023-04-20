import random

fn = ["Abhirup", 'Priyanshu' ,'Aniket', 'Ankit', 'Rupesh', 'Sumanta', 'Subhransu', 'Dibyanshu', 'Piyush', 'Aditya', "Soham", 'Soumarya', 'Rakesh', 'Manish', 'Kunal', 'Gyan', 'Debashish', 'Riddhish', 'Gautam', 'Virat', 'Yuvraj', 'Bahubali', 'Ashok', 'Parsuram', 'Susanta']

mn = ["Kumar", '', '', '']

ln = ['Goswami', 'Patra', "Teri ma ki", "Sahoo", "Sahu", "Yadav", "Choudhry", "Singh", "Prasad", "Paul", "Kumar", "Adhek", "Kundu", "Panda", "Pal", "Sanyal", "Ranjan", "Ghosh", "Dhawan", "Reddy", "Rawat", "Mallick", "Negi", "Upadhyaya", "Kapoor", "Mahapatra", "Nautiyal", "Saha", "Kohli"]

f = fn[random.randrange(0, 24)]
m = mn[random.randrange(0, 3)]
l = ln[random.randrange(0, 28)]

print(f,m,l)