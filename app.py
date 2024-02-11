import csv
import sys
import matplotlib.pyplot as plt
from jinja2 import Template
file='data.csv'
with open(file,newline='') as csv_file:
    read=list(csv.DictReader(csv_file))
def student_detail(id):
    sum=0
    c=0
    s=''
    for i in read:
        if id==i['Student id']:
            sum=sum+int(i[' Marks'])
            c=1
    if c==0:
        s="Something went wrong"
            
            
            
    html="""<!DOCTYPE html>
        <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
    {%if c!=0 %}
        <h1>Student Details</h1>
        
        <table border="1">
        <tr>
        <th>Student ID</th>
        <th>Course ID</th>
        <th>Marks</th>
        </tr>
        
        {% for i in read %}
       
            {% if i['Student id'] == (id) %}
                    
                <tr>
                    <td>{{ i['Student id'] }}</td>
                    <td>{{ i[' Course id'] }}</td>
                    <td>{{ i[' Marks'] }}</td>
                </tr>
            {%endif%}
    
        {% endfor %}
        <tr>
                    <td colspan="2">Total Marks</td>
                    <td>{{ sum }}</td>
            </tr>
            
        </table>
        {% else %}
        <h1>Wrong Inputs</h1>
        {{s}}
        
        {% endif %}
        
        
    </body>
    </html>
    """
    out=Template(html)
    final=out.render(read=read, id=id,sum=sum,s=s,c=c)
    
    file1=open('output.html','w')
    file1.write(final)
    file1.close()
def course_detail(id):
    sum=0
    avg=0
    c=0
    s=0
    s1=''
    max=-254545444444
    for i in read:
        if int(id) ==int(i[' Course id']):
            sum=sum+int(i[' Marks'])
            c=c+1
            s=1;
    if c>0:
        avg=sum/c
    for i in read:
        if int(id) ==int(i[' Course id']):
            if int(i[' Marks'])>max:
                max=int(i[' Marks'])
    if s==0:
        s1="Something went wrong"
    marks = [float(row[" Marks"]) for row in read]
    plt.hist(marks, bins=10, edgecolor="black")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.title(f"Histogram of Marks for Course {id}")
    plt.savefig("histogram.png")
    html1="""<!DOCTYPE html>
        <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
    {%if s!=0 %}
        <h1>Course Details</h1>
        <table border=1>
        <tr>
        <th>Average Marks</th>
        <th>Maximum Marks</th>
        
        </tr>
        
        
             
        
                <tr>
                    <td>{{ avg }}</td>
                    <td>{{ max}}</td>
                   
                </tr>
            
    
        
        </table>
         <img src="histogram.png" alt="Histogram of Marks">
         {% else %}
        <h1>Wrong Inputs</h1>
        {{s1}}
        {% endif %}
    </body>
    </html>
    """
    out=Template(html1)
    final=out.render(read=read,avg=avg,max=max,s1=s1,s=s)
    file1=open('output.html','w')
    file1.write(final)
    file1.close()
    
def main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments. Usage: python app.py [-s|-c] <id>")
        return
    id=str(sys.argv[2])
    a=sys.argv[1]
    if a=='-s':
        student_detail(id)
    elif a=='-c':
        course_detail(id)
    # else:
    #     print("Provide Correct Arguments")

    # out=Template(html)
    # final=out.render(read=read)
    # file1=open('output.html','w')
    # file1.write(final)
    # file1.close()
if __name__=="__main__":
    main()
    
    
    
     