from bokeh.plotting import figure, show
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure()
p.line(x, y)
p.circle(x, y,size=10)

p.text(1, 6, text=["Point 1"])

show(p)
