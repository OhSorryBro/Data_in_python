from die import Die
import plotly.express as px

die1 = Die()
die2 = Die(6)
#die3 = Die(6)

results = []
for roll_num in range(10000):
    result = die1.roll() + die2.roll() #+ die3.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides #+ die2.num_sides
poss_results = range(1, max_result +1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title ="Result of trowing 10000 times D6x3"
labels ={'x': 'Result', 'y':'Frequency of value'}
fig = px.bar(x=poss_results, y=frequencies, title=title,labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

print(frequencies)