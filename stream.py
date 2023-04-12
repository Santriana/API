def dataScience(stream):
    
    if stream == 'Data Analyst' :
        CO11 = 20/100
        CO21 = 0
        CO12 = 40/100
        CO22 = 0
        CO13 = 40/100
        CO23 = 0
        CO14 = 0
        CO24 = 70/100
        CO15 = 0
        CO25 = 30/100
    elif stream == 'Data Scientist' :
        CO11 = 40/100
        CO21 = 0
        CO12 = 60/100
        CO22 = 0
        CO13 = 0
        CO23 = 50/100
        CO14 = 0
        CO24 = 50/100
        CO15 = 0
        CO25 = 0
    elif stream == 'Data Engineer' :
        CO11 = 30/100
        CO21 = 0
        CO12 = 30/100
        CO22 = 0
        CO13 = 40/100
        CO23 = 0
        CO14 = 0
        CO24 = 100/100
        CO15 = 0
        CO25 = 0
    elif stream == 'Artificial Intellegence' :
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 50/100
        CO14 = 0
        CO24 = 50/100
        CO15 = 0
        CO25 = 0
    
    return CO11, CO21, CO12, CO22, CO13, CO23, CO14, CO24, CO15, CO25

def engineer (stream):

    if stream == 'Firmware Engineer':
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 40/100
        CO14 = 0
        CO24 = 40/100
        CO15 = 0
        CO25 = 20/100
    elif stream == 'Hardware Engineer':
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 30/100
        CO14 = 0
        CO24 = 30/100
        CO15 = 0
        CO25 = 40/100
    
    return CO11, CO21, CO12, CO22, CO13, CO23, CO14, CO24, CO15, CO25

def developer (stream):

    if stream == 'Mobile Developer - Android':
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 100/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    elif stream == 'Mobile Developer - iOS':
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 100/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    elif stream == 'Back End Developer' :
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 100/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    elif stream == 'Front End Developer':
        CO11 = 600/100
        CO21 = 0
        CO12 = 40/100
        CO22 = 0
        CO13 = 0
        CO23 = 100/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    elif stream == 'System Documentation':
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 100/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    elif stream == 'Software Quality Assurance':
        CO11 = 60/100
        CO21 = 0
        CO12 = 40/100
        CO22 = 0
        CO13 = 0
        CO23 = 100/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    elif stream == 'DevOps Engineer':
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 100/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0

    return CO11, CO21, CO12, CO22, CO13, CO23, CO14, CO24, CO15, CO25

def designer (stream):

    if stream == 'UX Designer':
        CO11 = 100/100
        CO21 = 0
        CO12 = 0
        CO22 = 50/100
        CO13 = 0
        CO23 = 50/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    elif stream == 'UI Designer':
        CO11 = 100/100
        CO21 = 0
        CO12 = 0
        CO22 = 50/100
        CO13 = 0
        CO23 = 50/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    elif stream == 'UX Writer':
        CO11 = 100/100
        CO21 = 0
        CO12 = 0
        CO22 = 100/100
        CO13 = 0
        CO23 = 0
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    elif stream == 'Graphic Designer':
        CO11 = 100/100
        CO21 = 0
        CO12 = 0
        CO22 = 60/100
        CO13 = 0
        CO23 = 40/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0

    return CO11, CO21, CO12, CO22, CO13, CO23, CO14, CO24, CO15, CO25

def researcher(stream):
    
    if stream == 'UX Researcher':
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 30/100
        CO14 = 0
        CO24 = 40/100
        CO15 = 0
        CO25 = 30/100
    elif stream == 'Business Analyst':
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 40/100
        CO14 = 0
        CO24 = 30/100
        CO15 = 0
        CO25 = 30/100
    elif stream == 'Business Development':
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 40/100
        CO14 = 0
        CO24 = 20/100
        CO15 = 0
        CO25 = 40/100
    
    return CO11, CO21, CO12, CO22, CO13, CO23, CO14, CO24, CO15, CO25

def general (stream):

    if stream == 'Project Integration': #LO A1
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 100/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    if stream == 'Reporting Project': #LO A2
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 40/100
        CO14 = 0
        CO24 = 20/100
        CO15 = 0
        CO25 = 40/100
    
    return CO11, CO21, CO12, CO22, CO13, CO23, CO14, CO24, CO15, CO25

def marketing(stream):

    if stream == 'Marketing Planning': #LO A1
        CO11 = 30/100
        CO21 = 0
        CO12 = 40/100
        CO22 = 0
        CO13 = 30/100
        CO23 = 0
        CO14 = 0
        CO24 = 50/100
        CO15 = 0
        CO25 = 50/100
    elif stream == 'Marketing Analyzing': #LO 
        CO11 = 100/100
        CO21 = 0
        CO12 = 0
        CO22 = 100/100
        CO13 = 0
        CO23 = 0
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    
    return CO11, CO21, CO12, CO22, CO13, CO23, CO14, CO24, CO15, CO25

def productManagement(stream):

    if stream == 'Project Management': #LO A1
        CO11 = 50/100
        CO21 = 0
        CO12 = 50/100
        CO22 = 0
        CO13 = 0
        CO23 = 100/100
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    elif stream == 'IT Management': #LO A2
        CO11 = 100/100
        CO21 = 0
        CO12 = 0
        CO22 = 100/100
        CO13 = 0
        CO23 = 0
        CO14 = 0
        CO24 = 0
        CO15 = 0
        CO25 = 0
    
    return CO11, CO21, CO12, CO22, CO13, CO23, CO14, CO24, CO15, CO25
