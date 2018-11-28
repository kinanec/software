import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import final

#==========================================
#       Visualisation #1
#    Bar graphs for 3 different users
#==========================================

users, stars = zip(*final.followerList)
#print(users)
#print(stars)
#data = [go.Bar(
#            x=users,
#            y=stars
#    )]

#py.iplot(data, filename='basic-bar')


x = users
y = stars

data = [go.Bar(
            x=x,
            y=y,
            text=y,
            textposition = 'auto',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )]

py.plot(data, filename='bar-direct-labels v4')

# https://plot.ly/~kinanec/6/#/
