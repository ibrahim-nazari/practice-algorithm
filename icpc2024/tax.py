
t=int(input())
def taxCalc(salary):
    pay=salary
    
    if salary > 100000:
        fivep= 7000 * 5 / 100
        tenp= 88000 * 10 / 100
        twenty= (salary - 100000) * 20/100
        totaltax=fivep + twenty+tenp
        pay=salary- totaltax
    elif salary > 12000:
        fivep= 7000 * 5 / 100
        tenp= (salary - 12000) * 10/100
        totaltax=fivep + tenp
        pay=salary-totaltax
    elif salary > 5000:
        fivep=(salary -5000) * 5/100
        pay=salary-fivep
    return pay


    return tax
def findTax(salaries):
    payes=[]
    for salary in salaries:
        pay=taxCalc(salary)
        if pay==int(pay):
            pay=int(pay)
        payes.append(pay)
    return payes
         
for _ in range(t):
    n=int(input())
    salaries=[int(input()) for _ in range(n)]
    res= findTax(salaries)
    print(res)