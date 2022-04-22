
#utk cari waiting time for each process
def WaitingTime(proc, n, bt, wt) :

    #utk first process
    wt[0] = 0

    #for other process
    for i in range(1,n):
        wt[i] = bt[i-1] + wt[i-1]

#utk calc turn around time for every process
def TurnAroundTime(proc, n, bt, wt,tat):


    #formula turn around time ni dapat dekat website
    for i in range(n):
        tat[i] = bt[i] + wt[i]

#utk kira most of the calc yg kena buat
def AvgTime(proc, n ,bt):

    wt =[0]*n
    tat = [0]*n
    total_wt=0
    total_tat=0

    WaitingTime(proc,n,bt,wt)


    TurnAroundTime(proc, n, bt, wt, tat)


    print("Process\tBurst Time\tWaiting Time\tTurn Around Time")

    #calc total waiting time
    #calc total turn around time
    for i in range(n):
        total_wt += wt[i]
        total_tat+= tat[i]

        print(""+ str(i+1) + "\t\t\t"+str(bt[i])+ "\t\t\t" + str(wt[i])+"\t\t\t" + str(tat[i]))

    print("Average waiting time = " + str(total_wt / n))
    print("Average turn around time = " + str(total_tat / n))


#main code
process = [1,2,3]
n =len(process)

burst_time = [10,5,8]

AvgTime(process,n,burst_time)




