from graphviz import Digraph

dot = Digraph('Use Case Diagram')

dot.attr(size='12', dpi='300', rankdir='LR')

dot.node('Rider', label='Rider', shape='plaintext')
dot.node('Driver', label='Driver', shape='plaintext')
dot.node('Admin', label='Admin', shape='plaintext')

dot.node('UC1', 'Sign up / Login', shape='ellipse')
dot.node('UC2', 'Request a Ride', shape='ellipse')
dot.node('UC3', 'Choose Wafa Core / Diamond', shape='ellipse')
dot.node('UC4', 'Track Ride in Real-Time', shape='ellipse')
dot.node('UC5', 'Use Panic Button', shape='ellipse')
dot.node('UC6', 'Rate & Review Driver', shape='ellipse')
dot.node('UC7', 'Accept Ride Requests', shape='ellipse')
dot.node('UC8', 'View Trust Ranking', shape='ellipse')
dot.node('UC9', 'Complete Ride & Receive Payment', shape='ellipse')
dot.node('UC10', 'Upgrade Trust Level', shape='ellipse')
dot.node('UC11', 'Verify Driver Profiles', shape='ellipse')
dot.node('UC12', 'Manage Safety Features', shape='ellipse')
dot.node('UC13', 'Handle Customer Support', shape='ellipse')
dot.node('UC14', 'Collaborate with Safety Organizations', shape='ellipse')

dot.edge('Rider', 'UC1')
dot.edge('Rider', 'UC2')
dot.edge('Rider', 'UC3')
dot.edge('Rider', 'UC4')
dot.edge('Rider', 'UC5')
dot.edge('Rider', 'UC6')

dot.edge('Driver', 'UC1')
dot.edge('Driver', 'UC7')
dot.edge('Driver', 'UC8')
dot.edge('Driver', 'UC9')
dot.edge('Driver', 'UC10')

dot.edge('Admin', 'UC11')
dot.edge('Admin', 'UC12')
dot.edge('Admin', 'UC13')
dot.edge('Admin', 'UC14')

dot.render('Wafa_Use_Case_Diagram', format='png')
