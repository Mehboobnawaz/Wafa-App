from graphviz import Digraph

dot = Digraph('Process Flow Diagram')

dot.attr(size='10', dpi='300', rankdir='TB')

dot.node('Start', 'Start', shape='oval')
dot.node('SignUp', 'User Signs Up / Logs In', shape='parallelogram')
dot.node('RideRequest', 'User Requests a Ride', shape='diamond')
dot.node('DriverMatch', 'Match with Available Driver', shape='box')
dot.node('RideTracking', 'Track Ride in Real-Time', shape='box')
dot.node('CompleteRide', 'Complete Ride & Payment', shape='box')
dot.node('Review', 'Rate & Review', shape='parallelogram')
dot.node('End', 'End', shape='oval')

dot.edge('Start', 'SignUp')
dot.edge('SignUp', 'RideRequest')
dot.edge('RideRequest', 'DriverMatch')
dot.edge('DriverMatch', 'RideTracking')
dot.edge('RideTracking', 'CompleteRide')
dot.edge('CompleteRide', 'Review')
dot.edge('Review', 'End')

dot.render('Wafa_Process_Flow_Diagram', format='png')
