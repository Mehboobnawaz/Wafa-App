from graphviz import Digraph

dot = Digraph('Architecture Diagram')

dot.attr(size='10', dpi='300', rankdir='TB')

dot.node('UserApp', 'User Mobile App', shape='box')
dot.node('DriverApp', 'Driver Mobile App', shape='box')
dot.node('Backend', 'Backend Server', shape='cylinder')
dot.node('Database', 'Database (User, Ride, Payment Info)', shape='cylinder')
dot.node('Payment', 'Payment Gateway', shape='box')
dot.node('Maps', 'Maps & Navigation API', shape='box')

dot.edge('UserApp', 'Backend')
dot.edge('DriverApp', 'Backend')
dot.edge('Backend', 'Database')
dot.edge('Backend', 'Payment')
dot.edge('Backend', 'Maps')

dot.render('Wafa_Architecture_Diagram', format='png')
