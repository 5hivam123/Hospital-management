from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
       self.root=root 
       self.root.title("HOSPITAL MANAGEMENT SYSTEM")
       self.root.geometry("1540x800+0+0")


      
       self.Nameoftablets=StringVar()
       self.ref=StringVar()
       self.NumberofTablets=StringVar()
       self.Lot=StringVar()
       self.Issuedate=StringVar()
       self.Expdate=StringVar()
       self.dailyDose=StringVar()
       self.sideEfects=StringVar()
       self.FurtherInformation=StringVar()
       self.StorageAdvice=StringVar()
       self.DrivingUsingMachine=StringVar()
       self.HowToUseMedication=StringVar()
       self.PatientID=StringVar()
       self.nhsNumber=StringVar()
       self.PatientName=StringVar()
       self.DateOfBirth=StringVar()
       self.patientAddress=StringVar()


       lbltitle=Label(self.root,bd=20,
                      relief= RIDGE,
                      text="HOSPITAL MANAGEMENT SYSTEM",
                      fg="red",
                      bg="white",
                      font=("times new roman",50,"bold"))
       lbltitle.pack(side=TOP,fill=X)

       #=====================DATA FRAME============================#
       Dataframe=Frame(self.root,bd=20,relief=RIDGE)
       Dataframe.place(x=0,y=130,width=1530,height=350)


       DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                font=("arial",12,"bold"),text="PATIENT INFORMATION")
       DataframeLeft.place(x=0,y=5,width=980,height=350)


       dataFrameRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                font=("arial",12,"bold"),text="Prescription")
       dataFrameRight.place(x=990,y=5,width=460,height=350)
       
       #=============================BUTTON Frame=======================#
       Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
       Buttonframe.place(x=0,y=530,width=1530,height=70)

        #=============================Details Frame Frame=======================#
       Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
       Detailsframe.place(x=0,y=600,width=1530,height=190)

       #==================DataFrame left=======================#

       lblNameTablet=Label(DataframeLeft,text="Names of tablet"
                          ,font=("arial",12,"bold"),padx=2,pady=6)
       lblNameTablet.grid(row=0,column=0)
       comNametablet=ttk.Combobox(DataframeLeft,textvariablr=self.Nameoftablets,state="readonly",
                                  font=("arial",12,"bold"),
                                                                     width=33)
       comNametablet["values"]=("nice","corona vaccine","Pain Relievers","Diuretics","Insulin")
       comNametablet.current(0)
       comNametablet.grid(row=0,column=1)


       lblref = Label(DataframeLeft, font=("arial",12,"bold"), text="Reference No.", padx=2)
       lblref.grid(row=1, column=0, sticky=W)
       txtref = Entry(DataframeLeft, font=("arial",13,"bold"),textvariable=self.ref, width=35)
       txtref.grid(row=1, column=1)

       lblDose = Label(DataframeLeft, font=("arial",12,"bold"), text="Dose", padx=2, pady=4)
       lblDose.grid(row=2, column=0, sticky=W)
       txtDose = Entry(DataframeLeft, font=("arial",13,"bold"),textvariable=self.Dose, width=35)
       txtDose.grid(row=2, column=1)


       lblNoOftablets = Label(DataframeLeft, font=("arial",12,"bold"), text="No.Of Tablets", padx=2,pady=6)
       lblNoOftablets .grid(row=3, column=0, sticky=W)
       txtNoOftablets  = Entry(DataframeLeft, font=("arial",13,"bold"),textvariable=self.NumberofTablets, width=35)
       txtNoOftablets.grid(row=3, column=1)

       lblLot = Label(DataframeLeft, font=("arial",12,"bold"), text="Lot", padx=2, pady=6)
       lblLot.grid(row=4, column=0, sticky=W)
       txtLot = Entry(DataframeLeft, font=("arial",13,"bold"),textvariable=self.Lot, width=35)
       txtLot.grid(row=4, column=1)


       lblissueDate = Label(DataframeLeft, font=("arial",12,"bold"), text="Issue Date.", padx=2,pady=6)
       lblissueDate .grid(row=5, column=0, sticky=W)
       txtissueDate  = Entry(DataframeLeft, font=("arial",13,"bold"),textvariable=self.Issuedate, width=35)
       txtissueDate.grid(row=5, column=1)

       lblExpDate = Label(DataframeLeft, font=("arial",12,"bold"), text="Exp.Date", padx=2, pady=6)
       lblExpDate.grid(row=6, column=0, sticky=W)
       txtExpDate = Entry(DataframeLeft, font=("arial",13,"bold"),textvariable=self.Expdate ,width=35)
       txtExpDate.grid(row=6, column=1)

       lblDailyDose = Label(DataframeLeft, font=("arial",12,"bold"), text="Daily.Dose.", padx=2,pady=4)
       lblDailyDose .grid(row=7, column=0, sticky=W)
       txtDailyDose  = Entry(DataframeLeft, font=("arial",13,"bold"),textvariable=self.dailyDose, width=35)
       txtDailyDose.grid(row=7, column=1)

       lblSideEffect = Label(DataframeLeft, font=("arial",12,"bold"), text="Side Effect", padx=2, pady=6)
       lblSideEffect.grid(row=8, column=0, sticky=W)
       txtSideEffect= Entry(DataframeLeft, font=("arial",13,"bold"),textvariable=self.sideEfects, width=35)
       txtSideEffect.grid(row=8, column=1)

       
       lblFurtherinfo = Label(DataframeLeft, font=("arial",12,"bold"), text="Further Info.", padx=2)
       lblFurtherinfo  .grid(row=0, column=2, sticky=W)
       txtFurtherinfo  = Entry(DataframeLeft, font=("arial",12,"bold"),textvariable=self.FurtherInformation, width=35)
       txtFurtherinfo.grid(row=0, column=3)

       lblBloodPressure = Label(DataframeLeft, font=("arial",12,"bold"), text="Blood Pressu", padx=2,pady=6)
       lblBloodPressure  .grid(row=1, column=2, sticky=W)
       txtBloodPressure  = Entry(DataframeLeft, font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine, width=35)
       txtBloodPressure.grid(row=1, column=3)

       
       lblStorage = Label(DataframeLeft, font=("arial",12,"bold"), text="Storage", padx=2,pady=6)
       lblStorage  .grid(row=2, column=2, sticky=W)
       txtStorage  = Entry(DataframeLeft, font=("arial",12,"bold"),textvariable=self.StorageAdvice, width=35)
       txtStorage.grid(row=2, column=3)

       lblMedicine= Label(DataframeLeft, font=("arial",12,"bold"), text="Medication", padx=2,pady=6)
       lblMedicine .grid(row=3, column=2, sticky=W)
       txtMedicine  = Entry(DataframeLeft, font=("arial",12,"bold"),textvariable=self.HowToUseMedication, width=35)
       txtMedicine.grid(row=3, column=3,sticky=W)

       
       lblpatientID= Label(DataframeLeft, font=("arial",12,"bold"), text="PatientID", padx=2,pady=6)
       lblpatientID .grid(row=4, column=2, sticky=W)
       txtpatientID  = Entry(DataframeLeft, font=("arial",12,"bold"),textvariable=self.PatientID, width=35)
       txtpatientID.grid(row=4, column=3)

       lblNHSNo= Label(DataframeLeft, font=("arial",12,"bold"), text="NHS No.", padx=2,pady=6)
       lblNHSNo .grid(row=5, column=2, sticky=W)
       txtNHSNo  = Entry(DataframeLeft, font=("arial",12,"bold"),textvariable=self.nhsNumber, width=35)
       txtNHSNo.grid(row=5, column=3)

       
       lblName= Label(DataframeLeft, font=("arial",12,"bold"), text="Name", padx=2,pady=6)
       lblName .grid(row=6, column=2, sticky=W)
       txtName  = Entry(DataframeLeft, font=("arial",12,"bold"),textvariable=self.PatientName, width=35)
       txtName.grid(row=6, column=3)

       lblDOB= Label(DataframeLeft, font=("arial",12,"bold"), text="DOB", padx=2,pady=6)
       lblDOB .grid(row=7, column=2, sticky=W)
       txtDOB  = Entry(DataframeLeft, font=("arial",12,"bold"),textvariable=self.DateOfBirth, width=35)
       txtDOB.grid(row=7, column=3)

       lblPatientAddress = Label(DataframeLeft, font=("arial",12,"bold"), text="Patient add.", padx=2, pady=6)
       lblPatientAddress.grid(row=8, column=2, sticky=W)
       txtPatientAddress= Entry(DataframeLeft, font=("arial",12,"bold"),textvariable=self.patientAddress, width=35)
       txtPatientAddress.grid(row=8, column=3)



        #=====================data frame right===================#


       self.txtprescription = Text(dataFrameRight,font=("arial",12,"bold"), width=45, height=16, padx=2, pady=6)
       self.txtprescription.grid(row=0, column=0)

       #==================button=================#


       btnPrescription=Button(Buttonframe,text="Prescription",bg="Green",fg="White", font=("arial",12,"bold"), 
                              width=23, height=2, padx=2, pady=6)
       btnPrescription.grid(row=0,column=0)

       
       btnPrescriptionData=Button(Buttonframe,text="Prescription Data",bg="Green",fg="White", font=("arial",12,"bold"), 
                              width=23, height=2, padx=2, pady=6)
       btnPrescriptionData.grid(row=0,column=1)

       
       btnupdates=Button(Buttonframe,text="Updates",bg="Green",fg="White", font=("arial",12,"bold"), 
                              width=23, height=2, padx=2, pady=6)
       btnupdates.grid(row=0,column=2)

       
       btnDelete=Button(Buttonframe,text="Delete",bg="Green",fg="White", font=("arial",12,"bold"), 
                              width=23, height=2, padx=2, pady=6)
       btnDelete.grid(row=0,column=3)


       
       btnClear=Button(Buttonframe,text="Clear",bg="Green",fg="White", font=("arial",12,"bold"), 
                              width=23, height=2, padx=2, pady=6)
       btnClear.grid(row=0,column=4)


       
       btnExit=Button(Buttonframe,text="EXIT",bg="Green",fg="White", font=("arial",12,"bold"), 
                              width=23, height=2, padx=2, pady=6)
       btnExit.grid(row=0,column=5)

       #=====================================TABLE


       scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
       self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expdate","dailydose",
                                                             "storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set
                                                             ,yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
       scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

       self.hospital_table.heading("nameoftablets",text="Name Of Tablets")
       self.hospital_table.heading("ref",text="Reference no.")
       self.hospital_table.heading("dose",text="Dose")
       self.hospital_table.heading("nooftablets",text="Number of tablets")
       self.hospital_table.heading("lot",text="LOT")
       self.hospital_table.heading("issuedate",text="Issue Date")
       self.hospital_table.heading("expdate",text="expdate")
       self.hospital_table.heading("dailydose",text="daily dose")
       self.hospital_table.heading("storage",text="Storage")
       self.hospital_table.heading("nhsnumber",text="NHS Number")
       self.hospital_table.heading("pname",text="Patient NAME")
       self.hospital_table.heading("dob",text="DOB")
       self.hospital_table.heading("address",text="Address")

       self.hospital_table["show"]="headings"
       self.hospital_table.pack(fill=BOTH,expand=1)

       self.hospital_table.column("nameoftablets",width=100)
       self.hospital_table.column("ref",width=100)
       self.hospital_table.column("dose",width=100)
       self.hospital_table.column("nooftablets",width=100)
       self.hospital_table.column("lot",width=100)
       self.hospital_table.column("issuedate",width=100)
       self.hospital_table.column("expdate",width=100)
       self.hospital_table.column("dailydose",width=100)
       self.hospital_table.column("storage",width=100)
       self.hospital_table.column("nhsnumber",width=100)
       self.hospital_table.column("pname",width=100)
       self.hospital_table.column("dob",width=100)
       self.hospital_table.column("address",width=100)
       
       self.hospital_table.pack(fill=BOTH,expand=1)






       #============================functionality Declaration===================

       def iPrescriptionData(self):
           if self.Nameoftablets.get()==""or self.ref.get()=="":
               messagebox.showerror("Error","all fields are required")
           else:
               conn=mysql.connector.connect(host="local",username="root",password="Test@123",database="My data")
               my_cursor=conn.cursor()
               my_cursor=conn.cursor()

             




       


                                  




       





       






    


if __name__ == "__main__":
    root=Tk()
    ob=Hospital(root)
    root.mainloop()
