#Import the things
from struct import *
import sys
import math
#from IPython.core.debugger import Tracer
import pdb #; pdb.set_trace()
#%debug
#D://2360//Scripting_data//Python_trail//Stdffiles/20180607130537_CSC_NEG40C_001_S11E_N_T08-V93K_C2222B01SXX135P4.std
##class reader:
#Reading STDF file
#Input_file=Inputfile
#@staticmethod
def ReadFile(Inputfile):
    STDF_File=open(Inputfile,'rb')
    global STDF_Data
    STDF_Data=STDF_File.read()
#Creating the Dict for Records

All_Record_Names={}
All_Record_Names[0,10]=['FAR']
All_Record_Names[0,20]=['ATR']
All_Record_Names[0,30]=['VUR']
All_Record_Names[1,10]=['MIR']
All_Record_Names[1,20]=['MRR']
All_Record_Names[1,30]=['PCR']
All_Record_Names[1,40]=['HBR']
All_Record_Names[1,50]=['SBR']
All_Record_Names[1,60]=['PMR']
All_Record_Names[1,62]=['PGR']
All_Record_Names[1,63]=['PLR']
All_Record_Names[1,70]=['RDR']
All_Record_Names[1,80]=['SDR']
All_Record_Names[1,90]=['PSR']
All_Record_Names[1,91]=['NMR']
All_Record_Names[1,92]=['CNR']
All_Record_Names[1,93]=['SSR']
All_Record_Names[1,94]=['SCR']
All_Record_Names[2,10]=['WIR']
All_Record_Names[2,20]=['WRR']
All_Record_Names[2,30]=['WCR']
All_Record_Names[5,10]=['PIR']
All_Record_Names[5,20]=['PRR']
All_Record_Names[10,30]=['TSR']
All_Record_Names[15,10]=['PTR']
All_Record_Names[15,15]=['MPR']
All_Record_Names[15,20]=['FTR']
All_Record_Names[15,20]=['STR']
All_Record_Names[20,10]=['BPS']
All_Record_Names[20,20]=['EPS']
All_Record_Names[50,10]=['GDR']
All_Record_Names[50,30]=['DTR']
#Declaring some variables for further use age
global Starting_byte
#global Next_Reading_Byte,Record_lenght,Record_Name,End_Record_Byte,Number_Of_Sites,Record_name
Next_Reading_Byte=0
Starting_byte=0

Record_lenght=0
Record_Name='Null'
End_Record_Byte=0
Number_Of_Sites=0
Record_name="DontKnow"
#global Test_Details,Test_Flag_Details,TestNumbers,FullTestDetails,PartFullInfo
#global TestSummary_Report,Hbin_sumary,Sbin_sumary,PCR_Rec_Summary,GDR_Summary
Test_Details={'000':'TestNumber ,TestName ,LowLimit ,High Limit, Unit'}
Test_Flag_Details={'000':'OptFlag,TestResult Scaling Expo,Low Limit Scaling expo,High Limit Scaling expo,Low limit,High Lim,Test Unit,C Result Fmt String,C low lim fmt string,C High Lim Fmt string,Low spec,High Spec'}
TestNumbers=['Test Numbers']
FullTestDetails=['TestFull details']
PartFullInfo=[[['Part_Number'," "," "," "," "]],[['TestHeadNumber'," "," "," "," "]],[['SiteNumber'," "," "," "," "]],[['PartFlag'," "," "," "," "]],[['NumberofTestesExcicuted'," "," "," "," "]],[['HardBin'," "," "," "," "]],[['Softbin'," "," "," "," "]],[['X co'," "," "," "," "]],[['Y co'," "," "," "," "]]]
TestSummary_Report=[['Test Head number '],['Site number'],['Test type'],['test num'],['Exec cnt'],['Fail cnt'],['alaram cnt'],['test name'],['Seq name'],['Test lbl'],['opt flag'],
                    ['test tim'],['test min'],['test max'],['test sums'],['test sqares']]
Hbin_sumary=[['Head number'],['Site Number'],['Hbin Num'],['Hbin cnt'],['Hbin PF'],['Hbin name']]
Sbin_sumary=[['Head number'],['Site Number'],['Sbin Num'],['Sbin cnt'],['Sbin PF'],['Sbin name']]
PCR_Rec_Summary=[['Head number'],['Site Number'],['Part count'],['RTst_Cnt'],['Numb of abort during testing'],['Number of passed'],['Number of Functional']]
GDR_Summary=[]     

#Supporting functions

def Read_Variable_lenght_Char_Data(Starting_byte,Length_of_char):
    x,Starting_byte=One_Byte_Unsigned_int(Starting_byte,1)
    Byte_length_of_field=x[0]    
    if Byte_length_of_field>0:
        dumy=unpack( str(Byte_length_of_field) +'s',STDF_Data[Starting_byte:Starting_byte+Byte_length_of_field])
        return dumy, Starting_byte+Byte_length_of_field        
    elif Byte_length_of_field==0:
        Field='';return Field,Starting_byte+Byte_length_of_field;print('Field Empty :',Field)
def One_Byte_Unsigned_int(Starting_byte,Length_of_char): return unpack(str(Length_of_char)+'B',STDF_Data[Starting_byte:Starting_byte+Length_of_char]), Starting_byte+Length_of_char
def One_Byte_Signed_int(Starting_byte,Length_of_char):return unpack(str(Length_of_char)+'b',STDF_Data[Starting_byte:Starting_byte+Length_of_char]), Starting_byte+Length_of_char
def KX_One_Byte_Unsingned_int(Starting_byte,K_values):
    K=K_values[0];return unpack(str(K)+'B',STDF_Data[Starting_byte:Starting_byte+int(K)]), Starting_byte+int(K)
def Two_Byte_Unsigned_int(Starting_byte,Length_of_char): return unpack(str(Length_of_char)+'H',STDF_Data[Starting_byte:Starting_byte+(2*Length_of_char)]),Starting_byte+(2*Length_of_char)
def Two_Byte_Signed_int(Starting_byte,Length_of_char): return unpack(str(Length_of_char)+'h',STDF_Data[Starting_byte:Starting_byte+(2*Length_of_char)]), Starting_byte+(2*Length_of_char)
def Fourbyte_Floating_point(Starting_byte,Length_of_char): return unpack(str(Length_of_char)+'f',STDF_Data[Starting_byte:Starting_byte+(4*Length_of_char)]), Starting_byte+(4*Length_of_char)
def Four_Byte_Unsigned_int(Starting_byte,Length_of_char):return unpack(str(Length_of_char)+'I',STDF_Data[Starting_byte:Starting_byte+(4*Length_of_char)]), Starting_byte+(4*Length_of_char)
def Four_Byte_signed_int(Starting_byte,Length_of_char):return unpack(str(Length_of_char)+'i',STDF_Data[Starting_byte:Starting_byte+(4*Length_of_char)]), Starting_byte+(4*Length_of_char)
def Eightbyte_Floating_point(Starting_byte,Length_of_char): return unpack(str(Length_of_char)+'d',STDF_Data[Starting_byte:Starting_byte+(8*Length_of_char)]), Starting_byte+(8*Length_of_char)
def Fixed_lengh_Char(Starting_byte,Length_of_char):return unpack(str(Length_of_char)+'c',STDF_Data[Starting_byte:Starting_byte+Length_of_char]), Starting_byte+Length_of_char
def Fixed_Lenght_BitEncoded_data(Starting_byte,Bytelenght): return unpack(str(Bytelenght)+'s',STDF_Data[Starting_byte:Starting_byte+1]),Starting_byte+1
def Variable_len_BitencodedData(Starting_byte,Length_of_char):    
    x,Starting_byte=Two_Byte_Unsigned_int(Starting_byte,1)#;print(x[0])
    x=math.ceil(x[0]/8)
    if x>0:
        x,Starting_byte=One_Byte_Signed_int(Starting_byte,x);y=str(x[0]);x=' '.join(format(ord(i), 'b') for i in y)#print(y);x=format(ord(y),'b');lth=len(x)-1;x=x[lth:]#x=''.join(format(ord(i),'b') for i in y)#
        return x,Starting_byte  
    else:
        return x,Starting_byte
def Variable_len_BitEncoded_B(Starting_byte,Lenght_of_Char):    
    Nextbyte,Starting_byte=One_Byte_Unsigned_int(Starting_byte,1)
    #print(Starting_byte)
    if Nextbyte[0]>0:
        x,Starting_byte=One_Byte_Signed_int(Starting_byte, Nextbyte[0]);return x,Starting_byte
    elif Nextbyte[0]==0:
        return Nextbyte[0],Starting_byte
def __B0(Starting_byte):
    print('B0 not defined')


B0=__B0
U1=One_Byte_Unsigned_int
U2=Two_Byte_Unsigned_int
U4=Four_Byte_Unsigned_int
I1=One_Byte_Signed_int
I2=Two_Byte_Signed_int
I4=Four_Byte_signed_int
R4=Fourbyte_Floating_point
R8=Eightbyte_Floating_point
CN=Read_Variable_lenght_Char_Data
BN=Variable_len_BitEncoded_B
DN=Variable_len_BitencodedData
N1=KX_One_Byte_Unsingned_int
VN_MAP={'0':B0,'1':U1,'2':U2,'3':U4,'4':I1,'5':I2,'6':I4,'7':R4,'8':R8,'10':CN,'11':BN,'12':DN,'13':N1}

#Type record


    
#reading the data
#@staticmethod
def Encodethedata(Starting_byte):  
    Starting_byte=Starting_byte    
    while Starting_byte<len(STDF_Data):        
        Starting_byte=Record_header(Starting_byte) 
        prgrs=math.ceil((Starting_byte/len(STDF_Data))*100)
        try:                
            #if prgrs>=1:progress['value']=prgrs;print("%s of 100 is complted"%prgrs)
            if Record_name==['FAR']:
                Starting_byte=FAR(Starting_byte)
            elif Record_name==['ATR']:
                Starting_byte=ATR(Starting_byte)
            elif Record_name==['MIR']:
                Starting_byte=MIR(Starting_byte)
                Starting_byte=End_Record_Byte
            elif Record_name==['SDR']:
                Starting_byte=SDR(Starting_byte)
            elif Record_name==['PMR']:
                Starting_byte=PMR(Starting_byte)
            elif Record_name==['WCR']:
                Starting_byte=WCR(Starting_byte)
            elif Record_name==['WIR']:
                Starting_byte=WIR(Starting_byte)
            elif Record_name==['PIR']:
                Starting_byte=PIR(Starting_byte)
            elif Record_name==['PTR']:
                Starting_byte=PTR(Starting_byte)
            elif Record_name==['FTR']:
                Starting_byte=FTR(Starting_byte)
            elif Record_name==['PRR']:
                Starting_byte=PRR(Starting_byte)
            elif Record_name==['WRR']:
                Starting_byte=WRR(Starting_byte)
            elif Record_name==['TSR']:
                Starting_byte=TSR(Starting_byte)
            elif Record_name==['HBR']:
                Starting_byte=HBR(Starting_byte)
            elif Record_name==['SBR']:
                Starting_byte=SBR(Starting_byte)
            elif Record_name==['PCR']:
                Starting_byte=PCR(Starting_byte)  
            elif Record_name==['MRR']:
                Starting_byte=MRR(Starting_byte)
            elif Record_name==['BPS']:
                Starting_byte=BPS(Starting_byte)
            elif Record_name==['DTR']:
                Starting_byte=DTR(Starting_byte)
            elif Record_name==['EPS']:
                Starting_byte=EPS(Starting_byte)
            elif Record_name==['GDR']:
                Starting_byte=GDR(Starting_byte)
            elif Record_name==['PGR']:
                Starting_byte=PGR(Starting_byte)
            elif Record_name==['PLR']:
                Starting_byte=PLR(Starting_byte)
            elif Record_name==['RDR']:
                Starting_byte=RDR(Starting_byte)
            elif Record_name==['MPR']:
                Starting_byte=MPR(Starting_byte)
            elif Record_name==['VUR']:
                #Starting_byte=VUR(Starting_byte)
                Starting_byte=End_Record_Byte;print('VUR RECORD USED')                
            elif Record_name==['NMR']:
                #Starting_byte=NMR(Starting_byte)
                Starting_byte=End_Record_Byte;print('NMR RECORD USED')
            elif Record_name==['PSR']:
                #Starting_byte=PSR(Starting_byte)
                Starting_byte=End_Record_Byte;print('PSR RECORD USED')
            elif Record_name==['CNR']:
                #Starting_byte=CNR(Starting_byte)
                Starting_byte=End_Record_Byte;print('CNR RECORD USED')
            elif Record_name==['SSR']:
                #Starting_byte=SSR(Starting_byte)
                Starting_byte=End_Record_Byte;print('SSR RECORD USED')
            elif Record_name==['SCR']:
                #Starting_byte=SCR(Starting_byte)
                Starting_byte=End_Record_Byte;print('SCR RECORD USED')
            elif Record_name==['STR']:
                #Starting_byte=STR(Starting_byte)  
                Starting_byte=End_Record_Byte;print('STR RECORD USED')                  
            else:
                print(Record_name,Starting_byte)#;break
        except:
            print(Record_name,Starting_byte)
    Starting_byte>=len(STDF_Data)
    print('File reading complted');return
def Convert_to_CSV(input):
    output=input
    output=output[0:len(output)-5]+'.csv'
    with open(output,'w') as F:
        for i in range(0 , len(PartFullInfo)):
             print(PartFullInfo[i],file=F)
        for i in range(1 , len(FullTestDetails)):
             print(FullTestDetails[i],file=F)
        progress['value']=100
        
        #print('CSV file created with file name %s'%output)
        
    
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter, tkinter.filedialog, tkinter.constants 
from tkinter.filedialog import askopenfilename
#from Stdf_Reader import *

def _Browse_File():
    filename = tkinter.filedialog.askopenfilename(parent=Stdf_Parser_Form,title='Choose a file')
    yourName.insert(0,filename)
    clicked=True   
    
def Start_process():
    Input_file=yourName.get()
    if Input_file!="":
        ReadFile(Input_file)
        Encodethedata(0)
        Convert_to_CSV(Input_file)
        messagebox.showinfo("Successful", "STDF to CSV Convertion is completed")
        Stdf_Parser_Form.destroy()
    else:
        messagebox.showinfo("Error", "Please Browse a File")

Stdf_Parser_Form=Tk()
Stdf_Parser_Form.geometry("510x90")
Stdf_Parser_Form.wm_iconbitmap('C:/Users/2360/Desktop/Tes_logo.ico')
Stdf_Parser_Form.title("Stdf_to_CSV")
l=LabelFrame(Stdf_Parser_Form,text="Browse the file",width=500,height=80)
l.pack( expand="yes")
l.place(x=7,y=3)
#Browse Button
custName = StringVar(None)
yourName = Entry(l, textvariable=custName)
yourName.pack(padx = 20, pady = 20,anchor='n')
yourName.place(y = 0, x = 70, width = 350, height = 20)
browsebutton = Button(l, text="Browse", command=_Browse_File,width=7)
browsebutton.pack(side=RIGHT)   
browsebutton.place(y = -2, x = 430)

global Input_file
Input_file=yourName.get()#input("Enter the file name & path")#main_Lot_1_Oct_12_17h06m09s
#Okay button
ok=Button(l,text="OK",command=Start_process,width=5)
ok.pack()
ok.place(x=370,y=30)
#Quit Button
quit=Button(l,text="Quit",width=5,command=Stdf_Parser_Form.destroy)
quit.pack()
quit.place(x=420,y=30)
#Lable
label2=Label(l, text="Select File:")
label2.pack()
label2.place(y = -2, x = 5)
#Progress Bar
progress = ttk.Progressbar(l, orient="horizontal",length=350, mode="determinate")
progress.pack()
progress.place(x=8,y=30)
Stdf_Parser_Form.mainloop()
