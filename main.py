from collections import Counter


def questionOne(file_name):
    with open(file_name, "rt") as filestream:
        sum_of_orders = 0
	for line in filestream:
            sum_of_orders +=1
    print("Site received %d orders" %(sum_of_orders-2))


def questionTwo(file_name):
    stocks = open(file_name).read().splitlines()
    total_amount = 0
    for line in stocks:
        x = line.split(', ')
        try:
            total_amount += int(x[3])
        except ValueError:
            pass
        except IndexError:
            pass
    print("Total amount of the orders is %d" %(total_amount))


def questionThree(file_name):
    list_of_customers = []
    final_customers = []
    c = 0
    stocks = open(file_name).read().splitlines()
    total_no = 0
    for line in stocks:
        x = line.split(', ')
        try:
            list_of_customers.append(x[2])
        except ValueError:
            pass
        except IndexError:
            pass
    list_of_customers = list(list_of_customers)
    c =  dict(Counter(list_of_customers))
    for key, value in c.iteritems():
        if(value==1):
            final_customers.append(key)
    final_customers.remove("Name")
    print("The customers who ordered once are :")
    for i in final_customers:
        print(i)


def questionFour(file_name):
    list_of_customers = []
    count_1 = count_2 = count_3 =count_4 = count_more = 0
    c = 0
    stocks = open(file_name).read().splitlines()
    total_no = 0
    for line in stocks:
        x = line.split(', ')
        try:
            list_of_customers.append(x[2])
        except ValueError:
            pass
        except IndexError:
            pass
    list_of_customers = list(list_of_customers)
    c =  dict(Counter(list_of_customers))
    del(c["Name"])
    for key, value in c.iteritems():
        if(value==1):
            count_1 +=1
        elif(value==2):
            count_2 +=1 
        elif(value==3):
            count_3 +=1
        elif(value==4):
            count_4 +=1  
        elif(value>=5):
            count_more +=1 
        else:
            continue 
    print("Order | Count of customers :")
    print("1     | %d" %(count_1))
    print("2     | %d" %(count_2))
    print("3     | %d" %(count_3))
    print("4     | %d" %(count_4))
    print("5+    | %d" %(count_more))


if __name__=='__main__':
    print("Enter a value from 1 to 4: ")
    value = input()
    if value==1:
        questionOne("customerdata.txt")  
    elif value==2:
        questionTwo("customerdata.txt")
    elif value==3:
        questionThree("customerdata.txt")
    elif value==4:
        questionFour("customerdata.txt")
